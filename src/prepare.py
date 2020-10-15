import pandas as pd
from ast import literal_eval


def movies_clean_up_genre(movies):

    movies["genre"] = movies["genre"].apply(literal_eval)

    def _get_items(x):
        return [v for k,v in x.items()]

    movies["genre"] = movies["genre"].apply(_get_items)

    return movies


def movies_label_counts(movies):
    """Get label counts per example for movie dataset

    Add a column to the dataframe with the number of labels per example
    """
    movies["nr_classes"] = movies["genre"].apply(len)

    return movies


def movies_summary_stats(movies):
    """Get summary statistics for movie dataset

    Return a dict containing the number of unique classes and the average number of labels
    per example.
    """

    genres = movies["genre"].explode().unique()

    stats = {}

    stats["nr_classes"] = [genres.shape[0]]
    stats["mean_labels_per_sample"] = [round(movies["nr_classes"].mean(), 3)]

    return pd.DataFrame(stats)


def toxic_label_counts(toxic):

    return (
        toxic
        .assign(nr_classes=lambda x: (
            x["toxic"] + x["severe_toxic"] +
            x["obscene"] + x["threat"] +
            x["insult"] + x["identity_hate"])))


def toxic_summary_stats(toxic):

    categories = ["toxic", "severe_toxic", "obscene", "threat", "insult", "identity_hate"]
    
    stats = {}

    stats["nr_classes"] = [len(categories)]
    stats["mean_labels_per_sample"] = [round(toxic['nr_classes'].mean(), 3)]

    return pd.DataFrame(stats)


def rcv1_clean_up(rcv1):
    """
    """

    nr_labels = []

    unique_classes = set()

    for sample in rcv1:
        nr_labels.append(len(sample))
        for category in sample:
            if category not in unique_classes:
                unique_classes.add(category)

    rcv1 = pd.DataFrame({"nr_classes": nr_labels})

    return (unique_classes, rcv1,)


def rcv1_summary_stats(rcv1, unique_classes):
    """
    """

    stats = {}

    stats["nr_classes"] = [len(unique_classes)]
    stats["mean_labels_per_sample"] = [round(rcv1['nr_classes'].mean(), 3)]

    return pd.DataFrame(stats)


def stats_transform(stats, dataset_name):

    stats["info_type"] = "stats"
    stats["dataset"] = dataset_name

    stats = pd.melt(
        stats.reset_index(),
        id_vars=["index", "info_type", "dataset"],
        value_vars=["nr_classes", "mean_labels_per_sample"],
        var_name="metric",
        value_name="value")

    return stats[["index", "dataset", "info_type", "metric", "value"]]


def multi_label_distribution(data, dataset_name):
    """Get multi-label distribution

    How many examples are there with each number of labels?
    """

    data = data["nr_classes"].value_counts().sort_index().reset_index()
    data = data.rename(columns={"nr_classes": "nr_examples", "index": "nr_labels"})
    data["info_type"] = "distribution"
    data["dataset"] = dataset_name

    data = pd.melt(
        data.reset_index(),
        id_vars=["index", "info_type", "dataset"],
        value_vars=["nr_examples", "nr_labels"],
        var_name="metric",
        value_name="value")

    return data[["index", "dataset", "info_type", "metric", "value"]]


def combine_distribution_stats(datasets):
    return (
        pd
        .concat(datasets)
        .sort_values(["dataset", "info_type", "metric", "index"]))


def write_data_report(dataset, filename):
    """
    """

    dataset.to_csv(f"data_report/{filename}.csv", index=False)