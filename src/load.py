import pandas as pd
import pickle


def get_movies():
    """Get movie names and genres
    
    Each genre is a class label, each movie can have multiple genres.
    """

    movies= pd.read_csv(
        "data_raw/cmu_movies/movie.metadata.tsv",
        usecols=[0, 2, 8],
        sep="\t",
        header=None)

    movies.columns = ["movie_id", "movie_name", "genre"]

    return movies


def get_toxic():
    """Get toxic comment labels
    """

    return pd.read_csv("data_raw/toxic_comment/train.csv")


def get_rcv1():
    """Get labels for mini RCV1 dataset
    """

    with open("data_raw/rcv1.multilabel/rcv1.multilabel.labels.pkl", "rb") as pickle_file:
        rcv1 = pickle.load(pickle_file)

    return rcv1