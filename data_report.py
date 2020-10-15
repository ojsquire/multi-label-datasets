import pandas as pd
import src.load as mld_load
import src.prepare as mld_prep


def data_report_movies():
    """Get CMU movie data for report
    """

    movies = mld_load.get_movies()
    movies = mld_prep.movies_clean_up_genre(movies)
    movies = mld_prep.movies_label_counts(movies)

    movies_distribution = mld_prep.multi_label_distribution(movies, "movies")
    movies_stats = mld_prep.movies_summary_stats(movies)
    movies_stats = mld_prep.stats_transform(movies_stats, "movies")

    return pd.concat([movies_distribution, movies_stats])


def data_report_toxic():
    """Get toxic comments data for report
    """

    toxic = mld_load.get_toxic()
    toxic = mld_prep.toxic_label_counts(toxic)

    toxic_distribution = mld_prep.multi_label_distribution(toxic, "toxic")
    toxic_stats = mld_prep.toxic_summary_stats(toxic)
    toxic_stats = mld_prep.stats_transform(toxic_stats, "toxic")

    return pd.concat([toxic_distribution, toxic_stats])


def data_report_rcv1():
    """Get RCV1 data for report
    """

    rcv1 = mld_load.get_rcv1()
    rcv1_classes, rcv1 = mld_prep.rcv1_clean_up(rcv1)

    rcv1_distribution = mld_prep.multi_label_distribution(rcv1, "rcv1")
    rcv1_stats = mld_prep.rcv1_summary_stats(rcv1, rcv1_classes)
    rcv1_stats = mld_prep.stats_transform(rcv1_stats, "rcv1")

    return pd.concat([rcv1_distribution, rcv1_stats])    


def combine_and_write(datasets, filename):
    """
    """

    dataset = mld_prep.combine_distribution_stats(datasets)
    mld_prep.write_data_report(dataset, filename)


def main():
    """Run all data pipelines
    """

    movies = data_report_movies()
    toxic = data_report_toxic()
    rcv1 = data_report_rcv1()
    combine_and_write([movies, toxic, rcv1], "data_report")


if __name__ == "__main__":

    main()