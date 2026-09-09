# multi_ai — VSCode 插件本地协作层（DeepSeek / Claude / GPT）

## 接入步骤

1. `config.json` 使用本地 CLI 适配器：DeepSeek 走 DSH headless，Claude 走 Claude Code CLI，GPT 走 VSCode Codex CLI。
2. CCSwitch 只负责中转和切换；调用器不读取 CCSwitch 数据库，也不把 `api.new.bi` 当作模型入口。
3. 三个插件必须已登录并可在本机 CLI 工作；密钥由各自插件/CLI 的配置管理，不写入本目录。
4. 自测：`python tests/test_multi_ai.py`，输出 `ALL TESTS PASSED` 即完成。

## 调用时机与分工

- stage 3（模型选型）：Claude 组织候选模型，DeepSeek 快速跑基线，GPT 选择主线和呈现方式。
- stage 5（子问）：DeepSeek 执行数值求解和现实/官方对标，Claude 解释，GPT 抽检结果链。
- stage 8（论文）：Claude 写作，GPT 检查摘要、图表、创新点和定量结果密度。
- stage 9（终审）：DeepSeek 全量复算，Claude 修订，GPT 做终审把关。

## 本地适配器

- DeepSeek：`dsh --profile headless`，由 DSH 负责模型选择、工具调用和会话编排。
- Claude：`claude --print --output-format text --no-session-persistence`，适合论文写作与项目编排。
- GPT：`codex exec --ephemeral --sandbox read-only`，适合独立审校、代码检查和呈现质量把关。

适配器实现：`multi_ai.py` 的 `call_local_cli`。传统 OpenAI 兼容 API 仍保留为可选回退路径。

## 优雅降级

- 本地 CLI 不存在、插件未登录或请求失败时，`call_llm` 返回 `None`，跳过该 AI，不中断主流程。
- 调用方应在 `state/decision_log.json` 记录降级警告，并使用可用模型继续 L1 评审。
- 所有评审要求输出 JSON；解析失败视为降级。
