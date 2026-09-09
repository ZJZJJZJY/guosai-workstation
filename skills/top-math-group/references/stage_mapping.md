# 阶段映射与文件加载表（Top-math-group 执行细则）

本文件把 `mathmodel-skill`（过程引擎）的 10 阶段与 `math-modeling`（内容引擎）的产出对齐，并列出每阶段**必读文件**。遵循「只读当前阶段所需文件，一次一阶段」的懒加载原则。

路径约定：`<mm>` = mathmodel-skill，`<mmd>` = math-modeling，`<adw>` = anti-defensive-writing，`<comp>` = 当前竞赛。

---

## 阶段 0 — 团队启动 + 资料预扫

| 来源 | 文件 | 用途 |
|---|---|---|
| `<mm>` | `references/stage_00_kickoff.md` | 启动流程、竞赛/题号/分工/截止/PDF 五问 |
| `<mmd>` | `references/roles/建模手说明.md` | 建模手角色职责（预读建立基线） |
| `<mmd>` | `references/roles/编程手说明.md` | 编程手角色职责 |
| `<mmd>` | `references/roles/论文手说明.md` | 论文手角色职责 |
| state | `<cwd>/state/decision_log.json` | 不存在则 cp `<mm>/templates/shared/decision_log.json` |

**产出**：decision_log 初始化（competition / mode / 分工 / 截止）。

---

## 阶段 1 — 选题

| 来源 | 文件 | 用途 |
|---|---|---|
| `<mm>` | `references/stage_01_problem_selection.md` | 多题对比 → 选 1 |
| `<mm>` | `competitions/<comp>/topic_specs.json` | 题号 → task_type 映射 |
| `<mm>` | `competitions/<comp>/winning_patterns.md` | 建立基线（整个 skill 只读一次） |

**产出**：`task_type` 写入 decision_log。

---

## 阶段 2 — 问题深度解析与分解

| 来源 | 文件 | 用途 |
|---|---|---|
| `<mm>` | `references/stage_02_analysis.md` | 解析流程 |
| `<mmd>` | `references/roles/建模手说明.md` | 分析工作流、模型选择原则 |

**产出**：`题目分析报告.md`、`术语表格.md`（中英文术语对照，供后续阶段复用）。

---

## 阶段 3 — 模型选型（≥3 候选）

| 来源 | 文件 | 用途 |
|---|---|---|
| `<mm>` | `references/stage_03_model_selection.md` | 选型流程 + 反事实对比 |
| `<mm>` | `references/model_catalog.md` | 60+ 模型目录（问题类型 → 候选族） |
| `<mmd>` | `assets/README.md` | 算法快速索引 |
| `<mmd>` | `assets/01..07-*.md` | 按候选族读对应算法详述（原理/代码/文献） |

**产出**：候选模型 ≥3 + 选择理由 + 命名变体（避免 vanilla 名）。

---

## 阶段 4 — Foundation（假设 + 符号 + 术语）

| 来源 | 文件 | 用途 |
|---|---|---|
| `<mm>` | `references/stage_04_foundation.md` | 假设/符号/术语规范 |
| `<mm>` | `templates/shared/assumption_table.md`、`notation_table.md` | 假设表/符号表模板 |

**产出**：假设表 + 符号表 + 术语表（与阶段 2 对齐）。

---

## 阶段 5 — 递归子问题循环 Q1..Qn（核心，时长最长）

| 来源 | 文件 | 用途 |
|---|---|---|
| `<mm>` | `references/stage_05_subproblem_loop.md` | 子问题循环、per-Qi 加权聚合 |
| `<mm>` | `references/model_catalog.md` | 各子问选型复核 |
| `<mmd>` | `references/roles/编程手说明.md` | 代码规范、可视化要求 |
| `<mm>` | `templates/shared/code_starter/{optimization,prediction,evaluation,classification,simulation}.py` | 代码骨架 |
| 联动 | `nature-figure`（Skill 工具） | 出多面板科研图（SVG/PDF，300+dpi） |
| `<mm>` | `scripts/score_artifact.py --mode aggregate_qi` | per-Qi 评分聚合 |

**产出**：`问题X_求解.py`、`结果表格.csv`、`figures/`、README。

---

## 阶段 6 — 全局灵敏度 / 稳健性

| 来源 | 文件 | 用途 |
|---|---|---|
| `<mm>` | `references/stage_06_robustness.md` | 灵敏度分析（工程参数 diangong vs 数学参数 cumcm/mcm） |
| `<mm>` | `templates/shared/sensitivity_table.md` | 灵敏度表模板 |

---

## 阶段 7 — 模型评价 + 推广

| 来源 | 文件 | 用途 |
|---|---|---|
| `<mm>` | `references/stage_07_evaluation.md` | 评价 + 推广 |

---

## 阶段 8 — 论文写作（摘要最后写）

| 来源 | 文件 | 用途 |
|---|---|---|
| `<mm>` | `references/stage_08_writing.md` | 写作顺序、装配流程 |
| `<mm>` | `competitions/<comp>/paper_skeleton.md` | 论文骨架 |
| `<mm>` | `competitions/<comp>/abstract_template.md` | 摘要模板（cumcm 5 段 / mcm 1-page+Letter / diangong 4 段） |
| `<mm>` | `competitions/<comp>/winning_patterns.md`、`phrase_bank.md` | 写作 anchor |
| `<mm>` | `competitions/<comp>/anti_patterns.md` | 回避清单 |
| `<mm>` | `competitions/<comp>/empirical.json` | 硬阈值打分锚定 |
| `<mm>` | `templates/latex/<comp>/` | LaTeX 模板 |
| `<mmd>` | `references/roles/论文手说明.md` | 撰写规范 |
| `<mmd>` | `references/论文模板.docx` / `默认论文模板.md` | docx 模板 |
| 联动 | `nature-writing` / `nature-polishing` / `nature-citation`（Skill 工具） | 结构 / 润色 / 引用 |

**产出**：`paper.tex` 或 `论文.docx`。

---

## 阶段 8.5 — 去 AI 味（Top-math-group 增强）

| 来源 | 文件 | 用途 |
|---|---|---|
| 联动 | `anti-defensive-writing`（Skill 工具） | 全文审查防御式写作 → 逐条判断 → 改写（claim 前置、正向 scope、删多余 hedge） |

**产出**：终稿（direct / confident / claim-forward，保留必要限制）。

---

## 阶段 9 — 终稿审核 + Panel（+ 答辩，可选）

| 来源 | 文件 | 用途 |
|---|---|---|
| `<mm>` | `references/stage_09_review.md` | 终审流程 |
| `<mm>` | `competitions/<comp>/anti_patterns.md` | 逐条对照 |
| `<mm>` | `competitions/<comp>/rubric_overlay.json` | panel_personas |
| `<mm>` | `references/feedback_layer3_panel.md`、`feedback_layer4_calibration.md` | 多视角 panel + 校准 |
| `<mmd>` | `references/Outstanding Thesis/<comp 对应目录>/` | 优秀论文对照（读 PDF 用 `<mmd>/tools/pdf`） |
| 联动 | `nature-paper2ppt`（Skill 工具） | 答辩 PPT（可选） |

**产出**：终稿 PDF + `答辩.pptx`（可选）。

---

## 每阶段通用纪律

1. 开头读 `<cwd>/state/decision_log.json`，核对 `current_stage`。
2. 结尾写回（核心决策 + 摒弃方案 + 5 维评分 + `current_stage += 1`）。
3. 跑 L1 自评（`<mm>/references/rubrics.md` 对应章节）；verdict 未达 `pass` 则 section-patch 精修（`<mm>/scripts/extract_diff.py`），iter cap 3。
4. 触发反馈时读 `<mm>/references/feedback_layer*.md`。
5. 超 token 预算 30% 自动降级（championship → standard → fast）。
