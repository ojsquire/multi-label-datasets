---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.12
    jupytext_version: 1.6.0
kernelspec:
  display_name: multi-label-datasets
  language: python
  name: multi-label-datasets
---

# Explore multi-label datasets
In the document I explore the suitability of datasets for training a multi-label classifier.

## Datasets
1. [CMU Movie Summary Corpus](http://www.cs.cmu.edu/~ark/personas/) as used on [this blog](https://towardsdatascience.com/multi-label-text-classification-5c505fdedca8).
2. [Toxic Comment Classification Challenge](https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge) (but very few datapoint with multiple labels).
3. [Mulan](http://mulan.sourceforge.net/datasets-mlc.html) (under "text" category).
4. RCV1 - agreement clauses needs to be checked
5. Reuters - agreement clauses needs to be checked

```{code-cell} ipython
from src.load_datasets import *
import matplotlib as mpl
import pickle

%matplotlib inline
%load_ext autoreload
%autoreload 2
```

## CMU movie summary dataset
```{code-cell} ipython
meta = get_movies()
meta = clean_up_genre(meta)
class_dists = data_to_plot(meta)

nr_genres = meta["genre"].explode().unique()

print(f"Overall number of unique classes: {nr_genres.shape[0]}")
print(f"Average labels per example: {round(meta['nr_classes'].mean(), 3)}")
plot_class_dists(class_dists, "Label distribution, CMU dataset")
```

## Toxic comments dataset
```{code-cell} ipython
toxic_comments = get_toxic_comments()
toxic_comments = get_toxic_label_counts(toxic_comments)

categories = ["toxic", "severe_toxic", "obscene", "threat", "insult", "identity_hate"]
class_dists = data_to_plot(toxic_comments)

print(f"Overall number of unique classes: {len(categories)}")
print(f"Average labels per example: {round(toxic_comments['nr_classes'].mean(), 3)}")
plot_class_dists(class_dists, "Label distribution, toxic comments dataset")
```

## RCV1 dataset
```{code-cell} ipython

with open("datasets/rcv1.multilabel/rcv1.multilabel.labels.pkl", "rb") as pickle_file:
    rcv1 = pickle.load(pickle_file)

nr_labels = []

unique_classes = set()

for sample in rcv1:
    nr_labels.append(len(sample))
    for category in sample:
        if category not in unique_classes:
            unique_classes.add(category)

nr_labels_per_example = pd.DataFrame({"nr_classes": nr_labels})
class_dists = nr_labels_per_example.value_counts().sort_index()

print(f"Overall number of unique classes: {len(unique_classes)}")
print(f"Average labels per example: {round(nr_labels_per_example['nr_classes'].mean(), 3)}")
plot_class_dists(class_dists, "Label distribution, miniRCV1 dataset")
```