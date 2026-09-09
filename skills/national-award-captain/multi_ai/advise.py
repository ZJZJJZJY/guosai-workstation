"""advise.py — 三方协作统一入口（阶段感知 · 并行 · 优雅降级）。

分工（见 role_division.md）：
    Claude Code = 编排/拍板（就是跑这个脚本的人，不自评）
    DeepSeek    = 数据与数值顾问
    GPT/Codex   = 内容与呈现顾问 + 严谨复核

用法:
    python advise.py --stage 3 --text "方案：机理建模+梯度优化（Q3 x=12.34）"
    python advise.py --stage 9 --file paper/draft.md --json out.json
    echo "内容" | python advise.py --stage 5

输出：合并后的 JSON。任一顾问失败自动跳过，不中断。
"""
import argparse
import concurrent.futures as futures
import io
import json
import os
import re
import sys

import multi_ai

HERE = os.path.dirname(os.path.abspath(__file__))

JSON_CONTRACT = (
    '只输出严格 JSON，不要 markdown 代码块、不要客套话：'
    '{"recommendation":"一句话明确推荐","enhancements":["<=3条"],"risk":"<=1条最可能导致降档的风险"}'
)

DATA_ADVISOR = (
    "你是数学建模国赛数据与数值顾问。针对给定内容给出【一条明确推荐】；"
    "再给【<=3 条增强点】集中在：数据清洗与异常处理、基线实验是否充分、"
    "求解器/算法选择与收敛性、灵敏度是否多变量联合扰动（LHS/Sobol，禁 OAT）、"
    "结果可复现性（随机种子/复现命令）；最后给【<=1 条单点风险】。"
    "方向与我一致，只补强不抬杠。" + JSON_CONTRACT
)

CONTENT_ADVISOR = (
    "你是数学建模国赛内容与呈现顾问。针对给定内容给出【一条明确推荐】；"
    "再给【<=3 条增强点】集中在：摘要 5 段式、>=3 条定量结果、图表密度与可读性、"
    "模型复合命名与创新点、行文学术化（去 AI 味）；最后给【<=1 条单点风险】。"
    "方向与我一致，只补强不抬杠。" + JSON_CONTRACT
)

RIGOR_ADVISOR = (
    "你是数学建模国赛严谨顾问（红队复核）。针对给定内容给出【一条明确推荐】；"
    "再给【<=3 条增强点】集中在：关键小问数值与官方答案对标、假设合理性（3-7 条且带依据）、"
    "灵敏度是否 >=3 参数联合扰动 + 稳健区间、模型与实现一致性、附录代码完整可运行（缺失=取消资格）；"
    "最后给【<=1 条单点风险】。方向与我一致，只补强不抬杠。" + JSON_CONTRACT
)

# 阶段 → 该派谁上。key 为 stage 号，value 为 [(provider, persona名, system prompt)]
STAGE_ROUTING = {
    0: [("deepseek", "data", DATA_ADVISOR)],
    1: [("deepseek", "data", DATA_ADVISOR)],
    2: [("gpt", "content", CONTENT_ADVISOR)],
    3: [("deepseek", "data", DATA_ADVISOR), ("gpt", "content", CONTENT_ADVISOR), ("gpt", "rigor", RIGOR_ADVISOR)],
    4: [("deepseek", "data", DATA_ADVISOR)],
    5: [("deepseek", "data", DATA_ADVISOR), ("gpt", "rigor", RIGOR_ADVISOR)],
    6: [("deepseek", "data", DATA_ADVISOR)],
    7: [("gpt", "content", CONTENT_ADVISOR)],
    8: [("gpt", "content", CONTENT_ADVISOR)],
    9: [("gpt", "rigor", RIGOR_ADVISOR), ("deepseek", "data", DATA_ADVISOR)],
}


def parse_advice(text):
    """从模型输出里抽出 JSON 三件套；失败则退化为纯文本包装。"""
    if not text:
        return None
    body = text.strip()
    # 剥 markdown 代码块围栏
    body = re.sub(r"^```(?:json)?\s*", "", body)
    body = re.sub(r"\s*```$", "", body).strip()
    match = re.search(r"\{.*\}", body, re.S)
    if match:
        try:
            data = json.loads(match.group(0))
            enhancements = data.get("enhancements") or []
            if isinstance(enhancements, str):
                enhancements = [enhancements]
            return {
                "recommendation": str(data.get("recommendation", "")).strip(),
                "enhancements": [str(x).strip() for x in enhancements][:3],
                "risk": str(data.get("risk", "")).strip(),
            }
        except (ValueError, AttributeError):
            pass
    return {"recommendation": body[:400], "enhancements": [], "risk": "",
            "_note": "未返回合规 JSON，已降级为文本"}


def ask_one(cfg, provider_name, persona, system_prompt, payload, timeout):
    """调一个顾问。返回 (provider, persona, advice or None)。"""
    provider = multi_ai.resolve_provider(cfg, provider_name)
    if not provider:
        return provider_name, persona, None
    raw = multi_ai.call_llm(provider, system_prompt, payload, timeout=timeout)
    return provider_name, persona, parse_advice(raw)


def main():
    ap = argparse.ArgumentParser(description="三方协作顾问入口（阶段感知）")
    ap.add_argument("--stage", type=int, required=True, help="阶段号 0-9")
    ap.add_argument("--text", help="直接给内容")
    ap.add_argument("--file", help="从文件读内容")
    ap.add_argument("--json", dest="out_json", help="把结果写入该 JSON 文件")
    ap.add_argument("--timeout", type=float, default=600.0)
    ap.add_argument("--only", help="只问某个 provider（deepseek/gpt）")
    args = ap.parse_args()

    if args.file:
        with io.open(args.file, "r", encoding="utf-8", errors="replace") as f:
            payload = f.read()
    elif args.text:
        payload = args.text
    else:
        payload = sys.stdin.read()
    payload = (payload or "").strip()
    if not payload:
        print("ERROR: 没有输入内容（--text / --file / stdin 三者选一）", file=sys.stderr)
        return 2

    routing = STAGE_ROUTING.get(args.stage)
    if not routing:
        print(f"ERROR: 未知阶段 {args.stage}（有效 0-9）", file=sys.stderr)
        return 2
    if args.only:
        routing = [r for r in routing if r[0] == args.only]
        if not routing:
            print(f"ERROR: 阶段 {args.stage} 不涉及 {args.only}", file=sys.stderr)
            return 2

    cfg = multi_ai.load_config(os.path.join(HERE, "config.json"))
    tagged = f"[阶段 stage{args.stage}]\n\n{payload}"

    results, skipped = [], []
    with futures.ThreadPoolExecutor(max_workers=len(routing)) as pool:
        jobs = [pool.submit(ask_one, cfg, name, persona, sys_prompt, tagged, args.timeout)
                for name, persona, sys_prompt in routing]
        for job in futures.as_completed(jobs):
            name, persona, advice = job.result()
            if advice:
                results.append({"provider": name, "persona": persona, **advice})
            else:
                skipped.append({"provider": name, "persona": persona})

    merged = {
        "stage": args.stage,
        "advisors": results,
        "skipped": skipped,
        "degraded": bool(skipped),
        "all_enhancements": [e for r in results for e in r.get("enhancements", [])],
        "all_risks": [r["risk"] for r in results if r.get("risk")],
    }

    out = json.dumps(merged, ensure_ascii=False, indent=2)
    if args.out_json:
        with io.open(args.out_json, "w", encoding="utf-8") as f:
            f.write(out + "\n")
        print(f"written: {args.out_json}  (advisors={len(results)}, skipped={len(skipped)})")
    else:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        print(out)
    return 0 if results else 1


if __name__ == "__main__":
    raise SystemExit(main())
