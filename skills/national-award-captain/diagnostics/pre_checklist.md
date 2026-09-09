# 赛前检查清单（开赛日/训练日执行）

- [ ] 环境：`python -m pip install -r <mm>/templates/shared/requirements.txt` 无报错（或见 addons/env_setup.md）
- [ ] LaTeX：`xelatex --version`（国赛/电工杯）与 `pdflatex --version`（美赛）可用（见 addons/latex_quickstart.md）
- [ ] 题目 PDF 已读入：题目类型、子问数（cumcm 通常 4，电工杯 7）、关键数据表
- [ ] 摘要 5 段式模板已就位（背景→任务拆解→各问方法+定量结果→灵敏度→创新推广）
- [ ] 每子问的**基线对比**计划：基线方法是什么（经典/简单启发式/历史数据）
- [ ] ≥3 个结构性不同的候选模型清单（PK 表：精度/时间/可解释性/数据需求）
- [ ] 灵敏度计划：≥3 参数多变量联合扰动（LHS/Sobol），非单变量 OAT
- [ ] 关键小问**官方对标**计划（哪个结果必须与官方答案/现实对标）
- [ ] 图表规划：每子问 ≥1 流程图 + ≥1 结果图；目标 18-25 图；字号 ≥9pt
- [ ] 论文模板：`<mmd>/references/论文模板.docx` 或 `<mm>/templates/latex/<comp>/`
- [ ] 附录代码规范：每段对应论文小节、中文注释、50-300 行、无调试残留
- [ ] 格式红线：承诺书/编号页/摘要页 3 页起；正文 ≤20 页；匿名；PDF ≤20MB；2025 新规 AI 工具使用报告
- [ ] （可选）多AI：config.json 已配置，`python tests/test_multi_ai.py` 通过