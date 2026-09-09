# 底层数模技能总结（Top-math-group 集成对象清单）

本文是对你已安装的两个数模技能 + 一个新装语言编辑技能的完整总结，供 Top-math-group 编排时查阅。

---

## 一、mathmodel-skill（过程引擎）— 三竞赛通用 v5.0

**一句话**：把"3–4 天打 1 篇竞赛论文"工程化，10 阶段 + 4 反馈层，全程问答式。

### 1. 三竞赛支持
| 竞赛 | 时长 | 语言 | LaTeX | 子问数 IQR | 数据状态 |
|---|---|---|---|---|---|
| cumcm 国赛 | 72h | 中文 | xelatex / cumcmthesis | [3,5] | stable（91 篇 2023–2025） |
| mcm 美赛 | 96h | English | pdflatex / article | [3,6] | seed v0.1 |
| diangong 电工杯 | 72h | 中文 | xelatex / ctex | [6,8] | seed v0.1 |

### 2. 三模式
| 模式 | Token | 反馈层 | 用途 |
|---|---|---|---|
| fast | ≤50k | L1 | 选题试跑 / sanity check |
| standard | ≤200k | L1+L2 | 默认主流程 |
| championship | ≤500k | L1+L2+L3+L4 + red-team | 提交前最后冲刺 |

### 3. 10 阶段索引
0 启动 → 1 选题 → 2 问题解析 → 3 模型选型 → 4 Foundation → 5 递归子问题循环（per-Qi 加权）→ 6 稳健性 → 7 模型评价 → 8 论文写作 → 9 终审+Panel。

### 4. 4 层反馈
- **L1 critic**：rubric 单次自评（JSON 强制输出，~500 token/次）
- **L2 backtrack**：跨阶段一致性回检，触发定向回滚（只改冲突点，不重做整阶段）
- **L3 panel**：终局多视角评委团（persona 各异）
- **L4 calibration**：实测分位锚定打分校准

### 5. 核心机制
- **问答式交互**：用户只答编号问题（竞赛/题号/分工/截止/PDF 路径），agent 自动读写 state
- **state 持久化**：`cwd/state/decision_log.json`（v3.0 schema），跨阶段、跨 harness（Claude Code / Codex CLI）互通
- **verdict 收敛准则**：block / pass_early / pass / refine / refine_partial / carryover，weighted_mean 由 `config/dim_weights.json[<comp>][<task_type>]` 决定
- **per-Qi 差异化降级**（stage 5）：某子问 min<7 时只 refine 该子问
- **token 纪律**：懒加载、section-level patch（`scripts/extract_diff.py`）、超预算 30% 自动降级
- **竞赛特化资源**：`competitions/<comp>/{winning_patterns, phrase_bank, abstract_template, paper_skeleton, anti_patterns, empirical, topic_specs, rubric_overlay, distilled_*}.md`
- **模型目录**：`references/model_catalog.md`（60+ 方法，按"问题类型 → 候选族"映射，含 Python 实现）
- **LaTeX 模板**：`templates/latex/{cumcm/cumcmthesis, mcm, diangong}`
- **脚本**：`scripts/{download_cumcm_papers, ingest_papers, render_paper, score_artifact, extract_diff}.py`

---

## 二、math-modeling（内容/资源引擎）— 三阶段内容工作流

**一句话**：建模分析 → 代码实现 → 论文撰写（+ 答辩），配套算法库、角色说明、模板与优秀论文。

### 1. 三阶段工作流
- **第一阶段 建模分析**：读「建模手说明」→ 产出 `题目分析报告.md` + `术语表格.md`（不写代码）
- **第二阶段 代码实现**：读「编程手说明」→ 按题分开写代码 → 结果写表 → `nature-figure` 出图 → `README.md`
- **第三阶段 论文撰写**：读「论文手说明」→ `nature-writing` 搭结构 + `nature-polishing` 润色 + `nature-citation` 引用 → docx 出稿
- **第四阶段（可选）答辩**：`nature-paper2ppt` 出学术 PPT

### 2. 算法资源库（assets/，7 大类）
| 文件 | 覆盖 |
|---|---|
| 01-优化 | 线性规划、整数规划、动态规划、GA、PSO、模拟退火、蚁群、差分进化、禁忌搜索、灰狼、免疫、鲸鱼、麻雀、多目标、鲁棒优化 |
| 02-预测 | 灰色预测、插值拟合、线性回归、神经网络、SVM、ARIMA、指数平滑、Prophet、LSTM、XGBoost/LightGBM、时空预测 |
| 03-评价 | AHP、Fuzzy-AHP、熵权、TOPSIS、灰色关联、秩和比、变异系数、主观赋权、DEA、区间数评价、改进 TOPSIS |
| 04-图论网络 | 最短路径、最小生成树、网络流、关键路径、欧拉/哈密顿、匹配 |
| 05-统计处理 | 数据预处理、聚类(K-Means/层次/DBSCAN)、假设检验、PCA、因子分析、典型相关、非负矩阵分解 |
| 06-综合 | 蒙特卡洛、排队论、博弈论、元胞自动机、马尔科夫链、微分方程建模 |
| 07-机器学习 | 随机森林、AdaBoost、孤立森林 |

### 3. 角色说明（references/roles/）
建模手说明 / 编程手说明 / 论文手说明 —— 各阶段工作细则、规范、注意事项。

### 4. 论文模板
- docx：`references/论文模板.docx`（标准数模论文）+ `references/默认论文模板.md`
- 使用 `docx` skill 或 `<mmd>/tools/docx` 生成

### 5. 优秀论文库（references/Outstanding Thesis/）
- CUMCM：RGV 动态调度、汽车总装线、会员画像、高温作业服等 9 篇
- MCM/ICM 2017：A–F 六类共 27 篇 O 奖
- 读 PDF 用 `<mmd>/tools/pdf`

### 6. 文档处理子技能（tools/）
- `tools/docx`：Word 处理（创建/读取/编辑/生成规范论文）
- `tools/pdf`：PDF 读取/提取/合并/拆分/填表
- `tools/xlsx`：Excel 读取/编辑/公式输出
- `tools/paper_search`：OpenAlex 学术搜索，自动生成参考文献

### 7. nature-* 联动
nature-figure（多面板科研图）/ nature-writing（结构）/ nature-polishing（润色）/ nature-citation（引用）/ nature-paper2ppt（PPT）。

---

## 三、anti-defensive-writing（语言编辑）— 去 AI 味

**一句话**：删除防御式写作（多余 caveat / disclaimer / hedge / apology 框架），让文风直接、自信、claim-forward，同时保留必要 scope 与方法学限制。

- **核心规则**：直接推进论点，写"本文研究/证明/说明了什么"，不默认解释"本文不主张/不证明/不涵盖什么"。
- **检测清单**：多余 disclaimer、反复声明不主张、过度 hedge、段落以 limitations 开头、负向框架、多余 "not X but Y"、"however/nevertheless/although" 冗余转折。
- **改写流程**：识别功能 → 删多余 disclaimer → 把防御式限制转成正向 scope → 用精确代替 hedge → 按主旨重建段落。
- **保留原则**：限制若影响结论效度/证据解释/适用范围/研究设计/读者正确使用，则保留（集中放方法/讨论/limitations 一节）。
- **推荐句式**：This paper examines/shows / The analysis focuses on / The evidence indicates / The central contribution is。
- **忌讳句式**：This paper does not claim / We do not attempt to / This is not to say / The goal is not X but Y / It is worth noting that / To be clear。

---

## 四、三者关系与分工

```
        ┌─────────────────────────────────────────────┐
        │              Top-math-group                  │
        │          (统一流水线 / 专家团队编排)          │
        └─────────────────────────────────────────────┘
              │                    │              │
   ┌──────────▼──────────┐  ┌──────▼──────────┐  ┌▼──────────────────┐
   │ mathmodel-skill     │  │ math-modeling    │  │ anti-defensive-    │
   │ 过程引擎(怎么走)     │  │ 内容引擎(写什么) │  │ writing(改文风)    │
   └─────────────────────┘  └─────────────────┘  └───────────────────┘
```
