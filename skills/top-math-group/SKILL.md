---
name: top-math-group
description: 数学建模专家团队集成技能（Top 数学组），专门解决数学建模竞赛与项目。整合 mathmodel-skill（10 阶段过程引擎 + 三竞赛 CUMCM/MCM/电工杯 + 三模式 fast/standard/championship + 4 层反馈 + 问答式 + state 持久化）与 math-modeling（三阶段内容工作流 + 7 大类算法库 + 建模/编程/论文三角色说明 + 论文模板 + 优秀论文库 + docx/pdf/xlsx/paper_search 子技能 + nature-* 联动），并在论文终稿阶段联动 anti-defensive-writing 去除 AI 写作味（防御式写作/多余 hedge/caveat）。触发：用户提到"数学建模、数模、CUMCM、国赛、MCM、ICM、美赛、电工杯、建模求解、建模分析、数模论文、数模答辩、去 AI 味、防御式写作"或要求"用 Top 数学组/专家团队做建模"。
---

# Top-math-group — 数学建模专家团队（集成技能）

专门解决数学建模。把你已安装的两个数模技能整合为一支**专家团队**端到端流水线，并在论文终稿阶段联动 `anti-defensive-writing` 去除 AI 写作味。

## 底层技能能力地图（集成对象）

| 底层技能 | 团队角色 | 提供什么 |
|---|---|---|
| `mathmodel-skill` | **过程引擎** | 10 阶段端到端工作流；三竞赛（CUMCM 国赛 / MCM 美赛 / 电工杯）；三模式（fast/standard/championship）；4 层反馈（L1 critic / L2 backtrack / L3 panel / L4 calibration）；全程问答式（用户只答编号问题）；`state/decision_log.json` 状态持久化；verdict 收敛准则；题型 dim 加权打分 + 实测分位锚定 |
| `math-modeling` | **内容/资源引擎** | 三阶段内容工作流（建模分析→代码实现→论文撰写）+ 答辩；7 大类算法说明库（assets/）；建模手/编程手/论文手角色说明；论文模板（docx + LaTeX）；优秀论文库（CUMCM + MCM/ICM）；文档处理子技能（docx/pdf/xlsx/paper_search）；nature-* 系列联动（figure/writing/polishing/citation/paper2ppt） |
| `anti-defensive-writing` | **语言编辑** | 论文终稿去 AI 味：删除防御式写作、多余 disclaimers/hedges/caveats、apology 框架、"not X but Y" 结构，让文风直接、自信、claim-forward，同时保留必要的 scope / 方法学限制 |

**路径约定**（本技能内统一使用）：
- `<mm>` = mathmodel-skill 目录 = `~/.claude/skills/mathmodel-skill`
- `<mmd>` = math-modeling 目录 = `~/.claude/skills/math-modeling`（等于 `~/.agents/skills/math-modeling`）
- `<adw>` = anti-defensive-writing 目录 = `~/.claude/skills/anti-defensive-writing`
- `<cwd>` = 用户工作目录；`<comp>` = 当前竞赛（cumcm | mcm | diangong）

---

## 团队角色（Top 数学组）

| 角色 | 职责 | 主要阶段 | 依赖资源 |
|---|---|---|---|
| **建模手** (Modeler) | 选题、问题解析、模型选型、假设与符号 | 0–4 | `<mm>/references/stage_00..04` + `<mm>/references/model_catalog.md` + `<mmd>/assets/01..07` + `<mmd>/references/roles/建模手说明.md` |
| **编程手** (Coder) | 求解、敏感性分析、可视化 | 5–7 | `<mm>/references/stage_05..07` + `<mmd>/references/roles/编程手说明.md` + `nature-figure` 画图 |
| **论文手** (Writer) | 装配论文、摘要、润色、引用 | 8 | `<mm>/references/stage_08` + `<mmd>/references/roles/论文手说明.md` + `nature-writing`/`nature-polishing`/`nature-citation` |
| **语言编辑** (Editor) | 去 AI 味 / 去防御式写作 | 8 末 + 9 | `anti-defensive-writing` |
| **评委团** (Review Panel) | L1–L4 反馈、终审、anti-patterns 对照 | 各阶段末 + 9 | `<mm>/references/feedback_layer1..4.md` + `rubrics.md` + `<mm>/competitions/<comp>/anti_patterns.md` |

---

## 分诊 / 路由规则

进入本技能后，先判断用户意图：

| 用户要什么 | 怎么走 |
|---|---|
| **完整建模**（从选题到成稿） | 走下面「统一流水线」，主干用 `<mm>` 的 10 阶段，阶段内按需注入 `<mmd>` 资源 |
| 只要**模型选型 / 算法推荐** | 直接读 `<mm>/references/model_catalog.md`（60+ 模型速查）或 `<mmd>/assets/README.md`（算法索引），不必跑全流程 |
| 只要**写论文 / 润色 / 引用** | 跳到阶段 8，用 `<mmd>` 第三阶段 + `nature-writing`/`nature-polishing`/`nature-citation` |
| 只要**去 AI 味 / 改防御式写作** | 单独调用 `anti-defensive-writing`（不跑建模流程） |
| **答辩 PPT** | 用 `nature-paper2ppt` 从论文生成（阶段 9 可选） |

---

## 统一流水线（10 阶段主干 + 内容注入）

主干沿用 `mathmodel-skill` 的 10 阶段（过程引擎），在对应阶段注入 `math-modeling` 的内容与资源。**只读当前阶段所需文件，严禁一次全读。**

| # | 阶段 | 主干（`<mm>`） | 内容注入（`<mmd>` + 联动） | 关键产出 |
|---|---|---|---|---|
| 0 | 团队启动 + 资料预扫 | `references/stage_00_kickoff.md` | 先读三角色说明（`references/roles/建模手/编程手/论文手说明.md`） | `decision_log.json` 初始化 |
| 1 | 选题（多题对比 → 1） | `references/stage_01_problem_selection.md` | — | `task_type` 写入 |
| 2 | 问题深度解析与分解 | `references/stage_02_analysis.md` | 建模手说明 → 写题目分析报告 + 术语表格 | `题目分析报告.md`、`术语表格.md` |
| 3 | 模型选型（≥3 候选） | `references/stage_03_model_selection.md` + `references/model_catalog.md` | `assets/01..07` 算法库查详细原理/代码 | 候选模型 ≥3 |
| 4 | Foundation（假设+符号+术语） | `references/stage_04_foundation.md` | 术语表与阶段 2 对齐 | 假设 + 符号 + 术语 |
| 5 | **递归子问题循环** Q1..Qn | `references/stage_05_subproblem_loop.md` | 编程手说明（代码规范/可视化）+ `nature-figure` 出图 | `问题X_求解.py` + 结果表 + 图 |
| 6 | 全局灵敏度 / 稳健性 | `references/stage_06_robustness.md` | — | 灵敏度结论 |
| 7 | 模型评价 + 推广 | `references/stage_07_evaluation.md` | — | 评价 + 推广 |
| 8 | 论文写作 | `references/stage_08_writing.md` | 论文手说明 + `<mmd>` 模板 + `nature-writing`/`nature-polishing`/`nature-citation` | `paper.tex` / `论文.docx` |
| 8.5 | **去 AI 味** | — | 调用 `anti-defensive-writing` 对全文做防御式写作清除 | 终稿（claim-forward） |
| 9 | 终稿审核 + Panel | `references/stage_09_review.md` | `<mmd>` 优秀论文对照 + `nature-paper2ppt` 出答辩 PPT | 终稿 + `答辩.pptx` |

> 阶段 8.5 是本技能对 `mathmodel-skill` 的关键增强：stage 8 成稿后、stage 9 终审前，用 `anti-defensive-writing` 通读全文，删除防御式写作与 AI 味表达，再交给评委团。

---

## 加载协议（省 token 关键）

- **只在进入阶段 N 时加载** `<mm>/references/stage_NN_*.md`；**切勿一次全读**。
- 每阶段开头读 `<cwd>/state/decision_log.json`，结尾写回（核心决策 + 5 维评分 + `current_stage += 1`）。
- 每阶段末尾跑 L1 自评（`<mm>/references/rubrics.md` 对应章节）。
- 触发反馈时读对应 `<mm>/references/feedback_layer*.md`。
- stage 8 额外读 `<mm>/competitions/<comp>/{winning_patterns, phrase_bank, abstract_template, paper_skeleton, anti_patterns}.md` + `empirical.json`。
- `<mmd>` 的资源（算法库/角色说明/模板/优秀论文）按需读，不必随主干全载。

---

## 收敛准则（verdict，三处一致）

| verdict | 触发 | 行为 |
|---|---|---|
| `block` | issues 含 ≥1 high-severity | 暂停，用户介入 |
| `pass_early` | raw_min ≥ 9 AND weighted_mean ≥ 9 | iter-1 早退 |
| `pass` | raw_min ≥ 7 AND weighted_mean ≥ 8 | 进下一阶段 |
| `refine` | 其他 | section-patch 精修，iter+=1（cap 3） |
| `carryover` | iter==3 仍 refine | 进下一阶段，标记由 L2 处理 |

`weighted_mean = Σ(s_i×w_i)/Σ(w_i)`，权重来自 `<mm>/config/dim_weights.json[<comp>][<task_type>]`。此定义与 `<mm>/references/feedback_layer1_critic.md`、`<mm>/references/rubrics.md`、`<mm>/scripts/score_artifact.py` 完全一致。

---

## 模式与竞赛（正交组合）

- **竞赛**（决定时长/语言/模板/子问数）：cumcm 72h 中文 xelatex / mcm 96h English pdflatex / diangong 72h 中文 xelatex。
- **模式**（决定 token 预算/反馈深度）：fast ≤50k L1 / standard ≤200k L1+L2（默认）/ championship ≤500k L1+L2+L3+L4+red-team。
- 模式自动推荐：>60h standard；24–60h standard；6–24h fast 关键阶段 + championship 终审；<6h 直接 stage 9。

---

## 去 AI 味流程（anti-defensive-writing 集成）

论文终稿前必做，与 `anti-defensive-writing` 的核心规则一致：

1. **先审查**：让编辑列出所有防御式写作实例（disclaimers、反复声明"本文不主张"、过度 hedge、段落以 limitations 开头、负向框架、"not X but Y"、"to be clear"、"It is worth noting that"）。
2. **逐条判断**：区分「必要限制」（影响结论效度/方法学透明/scope 的保留）与「多余防御」（纯粹怕被误解而加的）。
3. **改写**：claim 前置、正向 scope、用证据而非道歉支撑；必要时把限制集中放到方法/讨论/limitations 一节，不散落摘要/引言/结论。
4. 保留必要限制，删除不增加准确性的 hedge。

---

## 快捷指令

- "开始建模" / "Top 数学组 做这道题" → 进入统一流水线 stage 0（先 5 问：竞赛/题号/队员分工/截止时间/题目 PDF 路径）
- "进入 stage N" / "重做 stage N" → 跳转
- "切到 mcm / cumcm / diangong" → 改 `decision_log.competition`
- "升级 championship" / "切到 fast" → 改模式
- "去 AI 味" → 单独跑 `anti-defensive-writing`
- "出答辩 PPT" → `nature-paper2ppt`
- "看进度" → 输出 decision_log 摘要 + 当前评分

---

## 资源索引速查

- **模型选型速查**（问题类型 → 模型族，进入 stage 3 第一步必查）：
  - 求最优/分配/约束下最大 → 优化类（LP/IP/NLP/启发式）
  - 预测/未来/时间序列 → 预测类（回归/ARIMA/灰色/LSTM）
  - 评价/排名/综合得分 → 评价类（AHP/TOPSIS/熵权/模糊）
  - 判断/归类/识别 → 分类类（Logistic/SVM/决策树/NN）
  - 模拟/随机/如果会怎样 → 仿真类（蒙特卡罗/系统动力学/ABM）
  - 网络/路径/流量 → 图论类（最短路/最大流/最小生成树）
  - 概率/分布/假设检验 → 统计类（描述统计/检验/方差分析）
  - 动态/随时间 → 动力系统类（ODE/PDE/差分方程）
- **算法库**：`<mmd>/assets/01-优化 02-预测 03-评价 04-图论 05-统计 06-综合 07-机器学习`（每类含原理/适用/代码/文献）。
- **模型目录**：`<mm>/references/model_catalog.md`（60+ 模型，含 Python 实现与国赛常见用法）。
- **优秀论文**：`<mmd>/references/Outstanding Thesis/{CUMCM, 2017MCM ICM}/`（读 PDF 用 `<mmd>/tools/pdf`）。
- **模板**：docx `<mmd>/references/论文模板.docx`；LaTeX `<mm>/templates/latex/<comp>/`。
- **文档处理**：`<mmd>/tools/{docx,pdf,xlsx,paper_search}`。

## 数据来源声明

- `<mm>/competitions/cumcm/`：91 篇真国赛 2023–2025 PDF 烘焙（empirical.json 11 维 p25/p50/p75）；mcm / diangong 为 SEED v0.1。
- 本技能不复制底层技能内容，运行时按需读取；若底层技能被移除，请按路径重新安装。
