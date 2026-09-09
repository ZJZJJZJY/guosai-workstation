"""multi_ai.py — 多AI API 调用器（零第三方依赖，OpenAI 兼容 chat/completions）。

说明：优先通过 VSCode 插件安装的本地 CLI 调用；旧的 OpenAI 兼容接口仅作为可选回退。

用法:
    from multi_ai import load_config, resolve_provider, call_llm
    cfg = load_config("config.json")
    p = resolve_provider(cfg, "gpt")      # 无 key 时返回 None
    text = call_llm(p, system_prompt, user_prompt)  # 失败返回 None（优雅降级）
"""
import json
import os
import shutil
import subprocess
import urllib.request
from pathlib import Path

DEFAULT_TIMEOUT = 30.0
LOCAL_TIMEOUT = 900.0


def load_config(path):
    """读取 JSON 配置；文件不存在或损坏返回 {}（不抛异常）。"""
    try:
        # 兼容 Windows 编辑器保存的 UTF-8 BOM 配置文件。
        with open(path, "r", encoding="utf-8-sig") as f:
            return json.load(f)
    except Exception:
        return {}


def resolve_provider(config, name):
    """按名称解析 provider；配置缺失或环境变量无 key 时返回 None。"""
    p = (config or {}).get(name)
    if not p:
        return None
    if p.get("transport") == "cli":
        out = dict(p)
        out["transport"] = "cli"
        return out
    key_env = p.get("api_key_env")
    key = os.environ.get(key_env, "") if key_env else ""
    if not key:
        return None
    out = dict(p)
    out["api_key"] = key
    return out


def call_llm(provider, system_prompt, user_prompt, timeout=DEFAULT_TIMEOUT):
    """调用本地 VS Code/CLI 适配器或 OpenAI 兼容接口；失败返回 None。"""
    if not provider:
        return None
    if provider.get("transport") == "cli":
        return call_local_cli(provider, system_prompt, user_prompt, timeout=timeout)
    payload = {
        "model": provider.get("model", ""),
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        "temperature": provider.get("temperature", 0.4),
        "max_tokens": provider.get("max_tokens", 2048),
    }
    req = urllib.request.Request(
        provider["endpoint"],
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer " + provider["api_key"],
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            body = json.loads(resp.read().decode("utf-8"))
        return body.get("choices", [{}])[0].get("message", {}).get("content")
    except Exception:
        return None


def _which(name):
    """Windows 下同时寻找裸命令、.cmd 和 .exe。"""
    for candidate in (name, f"{name}.cmd", f"{name}.exe"):
        found = shutil.which(candidate)
        if found:
            return found
    return None


def _local_command(provider):
    """构造不依赖 CCSwitch 数据库的本地 CLI 命令。"""
    kind = provider.get("kind", "")
    configured = provider.get("executable")
    if configured and Path(configured).exists():
        return [configured]

    if kind == "dsh":
        # dsh.ps1 受 Windows ExecutionPolicy 影响，直接调用 node + bin.js。
        script = Path(os.environ.get("APPDATA", "")) / "npm" / "node_modules" / "@deepseek-ai" / "dsh" / "lib" / "bin.js"
        node = _which("node")
        if node and script.exists():
            return [node, str(script)]
        return [_which("dsh") or _which("dsh.cmd") or "dsh"]
    if kind == "claude":
        npm_root = Path(os.environ.get("APPDATA", "")) / "npm" / "node_modules" / "@anthropic-ai" / "claude-code" / "bin" / "claude.exe"
        if npm_root.exists():
            return [str(npm_root)]
        return [_which("claude") or _which("claude.cmd") or "claude"]
    if kind == "codex":
        found = _which("codex")
        if found:
            return [found]
        extension_root = Path(os.environ.get("USERPROFILE", "")) / ".vscode" / "extensions"
        matches = sorted(extension_root.glob("openai.chatgpt-*/bin/windows-x86_64/codex.exe"))
        if matches:
            return [str(matches[-1])]
        return ["codex"]
    return [provider.get("command", "")]


CAPACITY_MARKERS = ("at capacity", "rate limit", "overloaded", "try a different model")


def call_local_cli(provider, system_prompt, user_prompt, timeout=LOCAL_TIMEOUT):
    """通过本地 CLI 调用模型；遇到上游容量故障自动沿 fallback_models 降级。

    provider["fallback_models"] 给出备用模型列表；主模型返回 "at capacity"
    一类的瞬时错误时依次重试，全部失败才返回 None（优雅降级）。
    """
    candidates = [provider.get("model")]
    candidates += list(provider.get("fallback_models", []))
    seen, ordered = set(), []
    for model in candidates:
        marker = model or ""
        if marker not in seen:
            seen.add(marker)
            ordered.append(model)

    for model in ordered:
        attempt = dict(provider)
        if model:
            attempt["model"] = model
        else:
            attempt.pop("model", None)
        text, transient = _run_local_cli(attempt, system_prompt, user_prompt, timeout)
        if text:
            return text
        if not transient:
            return None
    return None


def _run_local_cli(provider, system_prompt, user_prompt, timeout):
    """跑一次 CLI。返回 (输出, 是否为可重试的瞬时故障)。"""
    try:
        command = _local_command(provider)
        kind = provider.get("kind", "")
        prompt = f"{system_prompt}\n\n严格遵守以上角色定义。\n\n用户任务：\n{user_prompt}"
        args = list(provider.get("args", []))
        if kind == "dsh":
            args = ["--profile", provider.get("profile", "headless"), prompt]
        elif kind == "claude":
            args = ["--print", "--output-format", "text", "--no-session-persistence"]
            if provider.get("model"):
                args += ["--model", provider["model"]]
            args += ["--system-prompt", system_prompt, prompt]
        elif kind == "codex":
            # 注意：codex exec 无 --ask-for-approval（那是顶层 flag）；
            # --ephemeral 已隐含 approval=never，多传会导致参数错误退出。
            args = ["exec", "--ephemeral", "--skip-git-repo-check", "--sandbox", "read-only"]
            if provider.get("model"):
                args += ["--model", provider["model"]]
            args += [prompt]
        else:
            args += [prompt]

        # 抓原始字节自行解码：Windows 中文环境下 CLI 可能输出 GBK，
        # 硬指定 utf-8 + errors="replace" 会把中文静默烧成 U+FFFD。
        proc = subprocess.run(
            command + args,
            cwd=provider.get("cwd") or None,
            capture_output=True,
            timeout=float(provider.get("timeout", timeout)),
            check=False,
        )
        stdout = _decode_bytes(proc.stdout)
        stderr = _decode_bytes(proc.stderr)
        proc_stdout = stdout
        combined = (stdout + "\n" + stderr).lower()
        transient = any(marker in combined for marker in CAPACITY_MARKERS)
        if proc.returncode != 0:
            return None, transient
        output = proc_stdout.strip()
        if not output:
            return None, transient
        return _strip_cli_noise(output, kind), False
    except subprocess.TimeoutExpired:
        return None, True
    except Exception:
        return None, False


def _decode_bytes(raw):
    """按 utf-8 → gbk → utf-8(replace) 顺序解码 CLI 输出，尽量不丢中文。"""
    if not raw:
        return ""
    if isinstance(raw, str):
        return raw
    for enc in ("utf-8", "gbk", "cp936"):
        try:
            return raw.decode(enc)
        except UnicodeDecodeError:
            continue
    return raw.decode("utf-8", errors="replace")


def _strip_cli_noise(text, kind):
    """剥掉 CLI 包装噪音（codex 的 session banner / token 统计等）。"""
    if kind != "codex":
        return text
    lines = text.splitlines()
    # codex exec 把回答放在最后一个 "codex" 标记行之后、"tokens used" 之前。
    start = 0
    for i, line in enumerate(lines):
        if line.strip() == "codex":
            start = i + 1
    body = []
    for line in lines[start:]:
        stripped = line.strip()
        if stripped.startswith("tokens used"):
            break
        body.append(line)
    cleaned = "\n".join(body).strip()
    return cleaned or text


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    cfg = load_config(os.path.join(here, "config.example.json"))
    print("providers:", list(cfg.keys()))
    for name in ("deepseek", "claude", "gpt"):
        provider = resolve_provider(cfg, name)
        print(f"{name} local CLI resolved:", provider is not None)
