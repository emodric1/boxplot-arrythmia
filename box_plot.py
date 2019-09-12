import matplotlib.pyplot as plt
import numpy as np

def box_plot(data, col, group, title, klase, ylab, plt_show = False):
    fig, ax = plt.subplots(nrows=1, ncols=1, sharey=False, figsize=(10,100))
    data.boxplot(column=[col], by=[group], ax=ax)
    ax.set_title(col)
    fig.suptitle(title)
    ax.set_xticklabels(klase,rotation=45, fontsize=8)
    ax.set_ylabel(ylab)

    if plt_show:
        plt.show()
