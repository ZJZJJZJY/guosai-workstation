# env_setup — Python/环境就绪

## 一键安装（推荐）
```powershell
python -m pip install -r "~.claude\skills\mathmodel-skill\templates\shared\requirements.txt"
```
含 numpy/scipy/pandas/matplotlib/seaborn/cvxpy/pulp/scikit-learn/xgboost/lightgbm/statsmodels/deap/pyswarms/SALib/simpy/mesa/pdfplumber/pypdf/unidiff。

## 可选
- Gurobi（商用求解器，有学生 license）：`pip install gurobipy`。
- LaTeX：装 TeX Live 或 MiKTeX（见 latex_quickstart.md）。
- 多AI：`python tests/test_multi_ai.py` 自测（详见 `../multi_ai/README.md`）。

## 方案缺口补齐库（国赛计算需要）
```powershell
python -m pip install networkx sympy pymoo openpyxl
```
networkx=图论/网络流；sympy=符号推导；pymoo=多目标优化；openpyxl=xlsx 读写。

## 检查
```powershell
python -c "import numpy, pandas, scipy, matplotlib; print('core ok')"
```