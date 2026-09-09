# national-award-captain — 国奖冲刺总指挥

数学建模竞赛统一入口。主攻 CUMCM 国赛（国一/国二），兼容 MCM/ICM 与电工杯。

## 架构
```
[用户] → national-award-captain（入口路由）
  ├── top-math-group（专家团队编排）
  │     ├── mathmodel-skill（10阶段引擎 + state/decision_log.json）
  │     ├── math-modeling（算法库/优秀论文库/三角色说明）
  │     └── anti-defensive-writing（去AI味，stage 8 子步骤 8B）
  ├── cumcm-award-playbook（获奖知识：横向对比/省一→国奖差距）
  ├── multi_ai/  VSCode 本地多AI（DeepSeek/Claude/GPT：数据、编排、评审）
  ├── search/    文献检索入口（找相关论文）
  ├── ai-flavor/ 去AI味入口（轻度/深度）
  ├── styles/    高级绘图风格库（期刊+展示 10 风格 + 派发器 + 出图模板）
  ├── diagnostics/ 赛前检查清单 + 赛后复盘
  └── addons/    资源扩充（真题索引/模型笔记/LaTeX速查/环境/三年国一精华+落选教训）
```

## 安装自检
- 底层引擎路径（见 SKILL.md 目录约定）全部存在；
- Python 依赖：`python -m pip install -r ~.claude\skills\mathmodel-skill\templates\shared\requirements.txt`（或见 addons/env_setup.md）；
- LaTeX：xelatex（国赛/电工杯）/ pdflatex（美赛），见 addons/latex_quickstart.md；
- 多AI（可选）：复制 `multi_ai/config.example.json` → `config.json`；三个 VSCode 插件分别管理认证，调用器使用本地 CLI。

## 三分钟上手
1. 说"冲刺国奖，做这道题"（或任意触发词，如"数学建模""国赛"）。
2. 回答 5 问 → 自动走 `<tmg>` 流水线。
3. 各阶段自动加载：获奖点、三年国一精华、反模式、多AI评审（如有 key）。
4. 详情：`SKILL.md`。
