#!/usr/bin/env python3
"""styles/render_starter.py — 用 styles.json 里某套风格画多面板示例图（可复用模板）。

用法:
    python styles/render_starter.py nature-journal   # 指定风格名；不填则用 styles.json 的 default
依赖: numpy, matplotlib
"""
import json
import os
import sys

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))


def load_styles(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def apply_style(style):
    plt.rcParams.update({
        "font.family": style.get("font", "DejaVu Sans"),
        "font.size": 9,
        "axes.titlesize": 11,
        "axes.labelsize": 10,
        "figure.dpi": style.get("dpi", 200),
        "savefig.dpi": style.get("dpi", 200),
        "axes.spines.top": False,
        "axes.spines.right": False,
        "grid.color": "#DDDDDD",
        "grid.linewidth": 0.6,
    })
    return style["palette"]


def main(name=None):
    styles_cfg = load_styles(os.path.join(HERE, "styles.json"))
    if name is None:
        name = styles_cfg.get("default", "nature-journal")
    style = next((s for s in styles_cfg["styles"] if s["name"] == name), styles_cfg["styles"][0])
    pal = apply_style(style)

    fig, axes = plt.subplots(2, 2, figsize=(9, 7))
    x = np.linspace(0, 10, 200)
    for i, ax in enumerate(axes.flat, start=1):
        c = pal[(i - 1) % len(pal)]
        ax.plot(x, np.sin(x) * i, color=c, lw=1.6, label=f"series {i}")
        ax.set_title(f"{style['name']} · panel {i}")
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        if style.get("grid", False):
            ax.grid(True)
        ax.legend(fontsize=7)
    fig.suptitle(f"Style: {name} (tool={style['tool']})", fontsize=12)
    fig.tight_layout()

    out_dir = os.getcwd()
    out_pdf = os.path.join(out_dir, "fig_example.pdf")
    out_png = os.path.join(out_dir, "fig_example.png")
    fig.savefig(out_pdf, format="pdf")
    fig.savefig(out_png, format="png")
    print("saved:", out_pdf, "and", out_png)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else None)