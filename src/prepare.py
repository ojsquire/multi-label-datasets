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

    stats["nr_classes"] = genres.shape[0]
    stats["mean_labels_per_sample"] = round(movies["nr_classes"].mean(), 3)

    return stats


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

    stats["nr_classes"] = len(categories)
    stats["mean_labels_per_sample"] = round(toxic['nr_classes'].mean(), 3)

    return stats


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

    stats["nr_classes"] = len(unique_classes)
    stats["mean_labels_per_sample"] = round(rcv1['nr_classes'].mean(), 3)

    return stats


def multi_label_distribution(data):
    """Get multi-label distribution

    How many examples are there with each number of labels?
    """

    return data["nr_classes"].value_counts().sort_index()


def write_stats(save_path, stats):
    """
    """

    stats = pd.DataFrame(stats)
    stats.to_csv(save_path, index=False)


def write_multi_label_distribution(save_path, multi_label_distribution):
    """
    """

    multi_label_distribution.to_csv(save_path, index=False)