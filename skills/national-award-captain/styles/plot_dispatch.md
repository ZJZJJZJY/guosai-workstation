# 高级绘图派发器 — 一句话出图（期刊调色板版）

## 选风格（先定家族）
| 你要 | 风格名 | 家族 | 工具 |
|---|---|---|---|
| 数学建模论文正文（默认） | `nature-journal` | Nature(NPG) | nature-figure |
| Science 调性 | `science-aaas` | Science(AAAS) | nature-figure |
| 医学/临床 | `nejm-clinical` / `lancet` | NEJM / Lancet | nature-figure |
| 肿瘤/多指标 | `jco` | JCO | nature-figure |
| 审稿向黑白 | `minimal-bw` | 灰度GS | nature-figure |
| 答辩/海报高对比 | `infographic` / `vibrant-poster` | 展示 | matplotlib / figura |
| 高级渐变感 | `gradient-smooth` | 展示 | matplotlib |
| 夜间/科技感 | `dark-paper` | 展示 | matplotlib |

## 一句话出图流程
1. 用户给调性（"Nature 期刊级多面板"/"答辩海报风"/"极简黑白"）→ 从 `styles.json` 取该风格：`palette / font / dpi / despine / grid`。
2. 期刊家族（nature/aaas/nejm/lancet/jco/gs）走 `nature-figure`：**多面板 + 矢量输出（PDF/SVG）+ 300dpi + 色盲安全**。
3. 展示家族走 `matplotlib`（快速）或 `figura`（渲染→回看→修复循环）。
4. 出图：论文正文 → PDF/SVG 300dpi；答辩 → PNG 150-200dpi。

## 快速落地（可运行模板）
```powershell
python styles/render_starter.py nature-journal   # 用某套风格画 2×2 示例图
# 输出：fig_example.pdf（矢量）+ fig_example.png；自机渲染
```
模板 `styles/render_starter.py` 读 `styles.json`、应用该风格的 palette/font/dpi/despine/grid，画多面板示例；
复用时把画图逻辑替换成你的真实数据即可。

## 多个真实调色板速查（ggsci）
| 家族 | 前 3 色 | 说明 |
|---|---|---|
| npg(Nature) | #E64B35 #4DBBD5 #00A087 | Nature 出版集团默认 |
| aaas(Science) | #3B4992 #EE0000 #008B45 | Science 期刊 |
| nejm | #BC3C29 #0072B5 #E18727 | NEJM 医学 |
| lancet | #00468B #ED0000 #42B540 | Lancet 医学 |
| jco | #0073C2 #EFC000 #868686 | JCO 肿瘤 |
| gs | #000000 #666666 #CCCCCC | 灰度/黑白 |

## 铁律
- 每个子问 ≥1 流程图 + ≥1 结果图；结果图实测中位数 8 张，含流程图全文 18-25 图为目标。
- 字号 ≥9pt；不套 Excel 默认配色；期刊家族一律矢量+300dpi。
- 调色板按"首色主、末色辅"取用；数据 ≥5 类再取第 6-7 色，别只用前两色。