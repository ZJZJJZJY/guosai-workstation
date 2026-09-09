# tooling_route — 技能等价路由（方案引用的缺失技能 → 已有工具/库）

> 协作方案 §6 引用了 7 个当前未安装的 skill（.agents 与 .claude 均无）。此处给出等价路由：**不装技能也能干活**；确需装时再走 skill-install/find-skills。

| 方案引用（未安装） | 等价做法（无需安装） | 需要的 Python 库 |
|---|---|---|
| `scikit-learn` | ML 回归/分类/聚类：`scientific-toolkit-skill` + `<mm>/templates/shared/code_starter/{prediction,classification}.py` | scikit-learn（已在 requirements） |
| `pymoo` | 多目标优化：手写 NSGA-II/权重和+ε-约束（`<mmd>/assets/01-优化算法说明.md`）或直接 pip 装 pymoo | pymoo（需装） |
| `sympy` | 符号推导：手写推导 + 数值验证；必要时 pip 装 sympy | sympy（需装） |
| `networkx` | 图论/网络流/最短路：手写 Dijkstra/最大流或用 networkx | networkx（需装） |
| `exploratory-data-analysis` | EDA：由 DeepSeek 直接写 `code/02_eda.py` 输出 `reports/eda_report.md`（分布/相关/异常/样本量） | pandas/matplotlib/seaborn（已有） |
| `xlsx` | Excel 读写：`<mmd>/tools/xlsx`（已存在，sub-skill）+ pandas | openpyxl（需装） |
| `pdf` | PDF 提取：`<mmd>/tools/pdf`（已存在，sub-skill） | pdfplumber/pypdf（已在 requirements） |

## 建议补装（一条命令，全部国赛计算所需）
```powershell
python -m pip install networkx sympy pymoo openpyxl
```

## 备注
- `<mm>` = mathmodel-skill；`<mmd>` = math-modeling；`tools/{pdf,xlsx,paper_search}` 子技能**已有**（无缺）。
- 若后续要"技能化"（如把 networkx 包装成 skill），再经 `skill-install` 从 GitHub 安装并更新本表。
