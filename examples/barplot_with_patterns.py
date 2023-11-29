
import matplotlib.pyplot as plt
import numpy as np
import mpl_visual_context.patheffects as pe
from mpl_pe_pattern_monster import PatternMonster

species = ("Adelie", "Chinstrap", "Gentoo")
penguin_means = {
    'Bill Depth': (18.35, 18.43, 14.98),
    'Bill Length': (38.79, 48.83, 47.50),
    'Flipper Length': (189.95, 195.82, 217.19),
}

x = np.arange(len(species))  # the label locations
width = 0.25  # the width of the bars
multiplier = 0

fig, ax = plt.subplots(num=1, clear=True, figsize=(8, 6))

for attribute, measurement in penguin_means.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width*0.8, label=attribute)
    ax.bar_label(rects, padding=3)
    multiplier += 1

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Length (mm)')
ax.set_title('Penguin attributes by species')
ax.set_xticks(x + width, species)
ax.set_ylim(0, 250)

import itertools
color_cycle = itertools.cycle(["#805AD5", "#E91E63", "#03A9F4", "#ECC94B"])

pm = PatternMonster()

for bars, slug in zip(ax.containers, ["circles-5", "circles-6", "concentric-circles-2"]):
    pattern = pm.get(slug, scale=2)
    pattern_fill = pattern.fill(ax, color_cycle)
    for patch in bars:
        patch.set_path_effects([
            pe.GCModify(alpha=0.1) | pe.FillOnly(),
            pattern_fill,
            pe.GCModify(linewidth=1) | pe.StrokeColorFromFillColor() | pe.StrokeOnly()
        ])

ax.legend(loc='upper left', ncols=3)
plt.show()

