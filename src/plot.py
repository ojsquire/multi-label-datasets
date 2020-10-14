import pandas as pd


def plot_class_distribution(class_dists, title=""):
    ax = class_dists.plot(
        kind="bar",
        title=title,
        figsize=(10, 5))

    ax.set_ylabel("Number of examples")
    ax.set_xlabel("Number of labels")