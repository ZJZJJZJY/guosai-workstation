# latex_quickstart — 三竞赛 LaTeX 编译速查

| 竞赛 | 引擎 | 模板 | 编译命令 |
|---|---|---|---|
| CUMCM | xelatex | `<mm>/templates/latex/cumcm/cumcmthesis/` | `xelatex -synctex=1 -interaction=nonstopmode main.tex`（两遍） |
| MCM/ICM | pdflatex | `<mm>/templates/latex/mcm/main.tex` | `pdflatex main.tex`（两遍；有引用则 `bibtex main`） |
| 电工杯 | xelatex | `<mm>/templates/latex/diangong/main.tex` | `xelatex -synctex=1 -interaction=nonstopmode main.tex`（两遍） |

## 检查
- `xelatex --version` / `pdflatex --version` 可用；Windows 用 TeX Live（`tlmgr` 装缺失宏包）或 MiKTeX（自动安装）。
- 中文乱码 → 用 xelatex + `\usepackage{ctex}`（cumcmthesis 已内置排版）。
- 参考文献：GB/T 7714 用 `gbt7714` 宏包；美赛用 natbib + plain。
- 图：PDF/SVG 矢量；`\includegraphics[width=0.9\textwidth]{fig.pdf}`。

## 常见错误
- 找不到 .cls → 在模板目录内编译或 `-output-directory` 指定。
- 图片路径中文 → 避免中文路径；文件名 ASCII。