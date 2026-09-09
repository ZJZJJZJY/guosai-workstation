# 国赛工作站（national-award-captain）· 一键使用

围绕 CUMCM 国赛（国一/国二）的三方协作系统：**Claude 编排写作 × DeepSeek 数据计算 × GPT 顾问评审**。所有技能、多AI 调用、知识模块（近三年国一精华 + 落选教训）都在这一个仓库里，队友 clone 后跑一条 `setup.ps1` 即用。

## 仓库结构
```
国赛工作站/
├── README.md                  ← 本文件
├── docs/安装与下载指南.md      ← ★ 必读：每个东西从哪来、放哪、必须指令
├── setup.ps1                  ← ★ 一键安装器（落位 skills + 装依赖 + 生成配置）
├── LICENSE / .gitignore
└── skills/                    ← 已捆绑的 22 个技能（源码见指南）
```

## 三步开工
```powershell
# 1) 拿到本仓库（或直接下 zip 解压）
git clone <你的仓库URL> 国赛工作站
cd 国赛工作站

# 2) 一键安装（落位技能 + 装 Python 依赖 + 生成 config.json）
powershell -ExecutionPolicy Bypass -File .\setup.ps1

# 3) 新开会话，说触发词即可
"冲刺国奖/开始建模"
```

> 在 Claude Code 里也能用：skills 会一并落到 `~/.claude/skills`，同一句触发词即可。

## 已捆绑的技能（22 个，详见 `docs/安装与下载指南.md`）
- **总指挥**：`national-award-captain`
- **引擎**：`mathmodel-skill`（10 阶段）/ `math-modeling`（内容库）/ `top-math-group`（团队）/ `cumcm-award-playbook`（获奖知识）/ `anti-defensive-writing`（去AI味）
- **7 个数据/计算技能**：`xlsx` `pdf` `scikit-learn` `sympy` `networkx` `pymoo` `exploratory-data-analysis`
- **nature-* 学术技能 9 个**：`nature-writing/polishing/reader/figure/citation/response/data/paper2ppt/academic-search`

## 多AI（可选）
默认走**本地 CLI**（DSH `dsh` / Claude `claude` / GPT `codex`），无需 API key，用各 VSCode 插件自带认证；详见指南 §4。任一 CLI 未登录会自动降级，不阻塞。

## 说明
- 仓库 **不含**获奖论文 PDF（38 篇，53MB，版权+体积）；如何在官方渠道自行补充见指南 §3.4；知识模块（蒸馏成果）已包含，**不影响核心流程**。
- 配置文件 `multi_ai/config.json` 已 `.gitignore`（setup 时从示例生成），不含任何路径/密钥。
