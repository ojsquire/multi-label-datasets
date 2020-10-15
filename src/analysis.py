import pandas as pd


def unload(data, dataset_name):
    """Unload data for report
    """

    data = data[lambda x: x["dataset"] == dataset_name]

    nr_classes = (
        data[lambda x: (
            (x["info_type"] == "stats") &
            (x["metric"] == "nr_classes"))]
            ["value"].tolist()[0])


    mean_labels_per_sample = (
        data[lambda x: (
            (x["info_type"] == "stats") &
            (x["metric"] == "mean_labels_per_sample"))]
            ["value"].tolist()[0])

    class_dists = data[lambda x: x["info_type"] == "distribution"]
    class_dists = class_dists.pivot(index=["index", "dataset", "info_type"], columns="metric", values="value")
    class_dists = class_dists.reset_index()[["nr_labels", "nr_examples"]]
    class_dists = class_dists.set_index("nr_labels")

    return (nr_classes, mean_labels_per_sample, class_dists[["nr_examples"]], )


def plot_class_distribution(class_dists, title=""):
    ax = class_dists.plot(
        kind="bar",
        title=title,
        figsize=(10, 5))

    ax.set_ylabel("Number of examples")
    ax.set_xlabel("Number of labels")


def analyse(data, dataset_name, title):
    nr_classes, mean_labels_per_sample, class_dists = unload(data, dataset_name)

    print(f"Overall number of unique classes: {nr_classes}")
    print(f"Average labels per example: {mean_labels_per_sample}")
    plot_class_distribution(class_dists, f"Label distribution, {title}")