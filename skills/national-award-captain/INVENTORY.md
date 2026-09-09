# national-award-captain — 文件清单与职责

## 入口
| 文件 | 职责 |
|---|---|
| `SKILL.md` | 技能入口。意图路由（8 条）、sprint/full 模式、5 问初始化、懒加载协议、每阶段注入、多AI统一顾问、路径断链兜底；frontmatter `name/description` 供加载触发 |
| `README.md` | 总览、架构图、安装自检、三分钟上手 |

## multi_ai/ — 多AI 统一专家顾问
| 文件 | 职责 |
|---|---|
| `config.example.json` | fable5/gpt 的 endpoint/model/环境变量名 模板（无 key 不启用） |
| `multi_ai.py` | 零依赖调用器：`load_config`/`resolve_provider`/`call_llm`，鉴权/网络失败优雅降级返回 None |
| `personas.md` | 3 个方向一致角色（首席顾问/严谨顾问/终审把关），只输出单一推荐 + ≤3 增强点 + ≤1 风险，禁止两套对立方案 |
| `role_division.md` | 分工矩阵 + 唯一方向原则 + 意见一次合并、不做无谓辩证的红线 |
| `README.md` | 接入步骤（复制 config → 填 endpoint/model → setx key → 自测） |

## styles/ — 高级绘图风格库
| 文件 | 职责 |
|---|---|
| `styles.json` | 10 套风格（6 期刊家族 NPG/AAAS/NEJM/Lancet/JCO/灰度 + 4 展示），含 palette/font/dpi/despine/grid |
| `plot_dispatch.md` | 一句话出图派发：调性 → 风格 → 工具（nature-figure/matplotlib/figura）+ 多面板模板 + 快速落地 |
| `render_starter.py` | 可运行出图模板：读 styles.json、应用风格、画 2×2 多面板、输出矢量 PDF+PNG |

## search/ — 文献检索
| 文件 | 职责 |
|---|---|
| `README.md` | 找相关论文路由：OpenAlex/CrossRef/arXiv + 本地优秀论文库 + nature-academic-search/nature-citation；GB/T 7714 或 Nature 格式；无网络降级本地 |

## ai-flavor/ — 去AI味
| 文件 | 职责 |
|---|---|
| `README.md` | 轻度（anti-defensive-writing）+ 深度（anti-slop），改写示例与入口 |

## diagnostics/ — 诊断
| 文件 | 职责 |
|---|---|
| `pre_checklist.md` | 赛前 13 项检查（环境/LaTeX/题目/摘要5段式/基线/候选/灵敏度/对标/图表/模板/代码/格式/多AI） |
| `post_review.md` | 赛后 10 条"省一→国奖"逐条自评表 |

## addons/ — 资源扩充 + 知识模块
| 文件 | 职责 |
|---|---|
| `README.md` | 四类资源索引（内容/论文绘图LaTeX/代码ML/编排评审） |
| `topic_index.md` | 2023-2025 共 15 题真题索引（题目/题型/解法/素材） |
| `model_notes.md` | 国一高频模型组合速查 |
| `latex_quickstart.md` | 三竞赛 LaTeX 编译速查 |
| `env_setup.md` | Python 依赖一键安装 |
| `cumcm-essence-2023-2025.md` | 【知识】三年国一精华：逐年逐题思路、获奖模式库 10 条、91 篇实测硬指标、三阶段落地 |
| `losing-lessons.md` | 【知识】落选教训：42 条反模式避雷卡、3 个未获奖案例、官方红线、答案精度头号门槛 |

## tests/
| 文件 | 职责 |
|---|---|
| `test_multi_ai.py` | 零依赖自测：`python tests/test_multi_ai.py` → `ALL TESTS PASSED` |

## 与外部连接
- **底层引擎**：`~/.claude/skills/{mathmodel-skill, math-modeling, top-math-group, cumcm-award-playbook, anti-defensive-writing}`
- **多AI**：`multi_ai/config.json` + 环境变量 → 连通 GPT/fable5
- **共享状态（交接点）**：`cwd/state/decision_log.json` —— DSH 与 Claude 互相接力的核心（详见 `CONNECT.md`）
