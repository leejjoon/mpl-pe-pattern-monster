"""
================================
Bar chart with Christmas pattern
================================

A bar chart with patterns, pattern colors are set explicitly.

"""

# We start from a simple barchart
# Adopted from https://matplotlib.org/stable/gallery/lines_bars_and_markers/barchart.html

import matplotlib.pyplot as plt
import numpy as np
from mpl_pe_pattern_monster import PatternMonster


species = ("Adelie", "Chinstrap", "Gentoo")
penguin_means = {
    'Bill Depth': (18.35, 18.43, 14.98),
    'Bill Length': (38.79, 48.83, 47.50),
}

x = np.arange(len(species))  # the label locations
total_width = 0.7  # total width of the group
dw = 0.2 # fraction of space between bars in the same group
width = total_width / (len(penguin_means) + dw * (len(penguin_means) - 1))

multiplier = 0

fig, ax = plt.subplots(num=1, clear=True, figsize=(8, 6))

for i, (attribute, measurement) in enumerate(penguin_means.items()):
    offset = width * (1 + dw) * i
    rects = ax.bar(x - 0.5 * total_width + offset, measurement, width,
                   label=attribute, align="edge")
    ax.bar_label(rects, padding=3)

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Length (mm)')
ax.set_title('Penguin attributes by species')
ax.set_xticks(x, species)
ax.set_ylim(0, 58)

# Now we add Christmas patterns

import mpl_visual_context.patheffects as pe

pm = PatternMonster()

# pattern names and colors
patterns = [("christmas-tree-1", ["#009688", "#E91E63", "#03A9F4", "#ECC94B"], 1),
            ("christmas-pattern-2", ["#F6AD55", "#E91E63", "#03A9F4"], 1.5)]

for bars, slug_colors_scale in zip(ax.containers, patterns):

    slug, colors, scale = slug_colors_scale
    pattern = pm.get(slug, scale=scale)
    pattern_fill = pattern.fill(ax, color_cycle=colors, alpha=0.5)

    path_effects = [
        pe.FillColor(colors[0]) | pe.GCModify(alpha=0.3),
        pe.StrokeColor(colors[0]) | pe.GCModify(linewidth=2, alpha=0.5) | pe.StrokeOnly(),
        pattern_fill
    ]

    for patch in bars:
        patch.set_path_effects(path_effects)

ax.legend(loc='upper left', ncols=1,
          handleheight=3., handlelength=3.)

plt.show()

