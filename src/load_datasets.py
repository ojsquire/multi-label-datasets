import pandas as pd
from ast import literal_eval


def get_movies():
    meta = pd.read_csv(
        "datasets/cmu_movies/movie.metadata.tsv",
        usecols=[0, 2, 8],
        sep="\t",
        header=None)

    meta.columns = ["movie_id", "movie_name", "genre"]

    return meta


def clean_up_genre(meta):

    meta["genre"] = meta["genre"].apply(literal_eval)

    def _get_items(x):
        return [v for k,v in x.items()]

    meta["genre"] = meta["genre"].apply(_get_items)
    meta["nr_classes"] = meta["genre"].apply(len)

    return meta


def data_to_plot(data):

    class_dist = data["nr_classes"].value_counts().sort_index()

    return class_dist


def get_toxic_comments():
    meta = pd.read_csv(
        "datasets/toxic_comment/train.csv")
#        usecols=[0, 2, 8],
#        sep="\t",
#        header=None)
    return meta


def get_toxic_label_counts(data):

    return (
        data
        .assign(nr_classes=lambda x: (
            x["toxic"] + x["severe_toxic"] +
            x["obscene"] + x["threat"] +
            x["insult"] + x["identity_hate"])))


def plot_class_dists(class_dists, title=""):
    ax = class_dists.plot(
        kind="bar",
        title=title,
        figsize=(10, 5))

    ax.set_ylabel("Number of examples")
    ax.set_xlabel("Number of labels")

    