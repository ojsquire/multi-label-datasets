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
from src.load_datasets import (
  get_movies,
  clean_up_genre,
  data_to_plot)

import matplotlib as mpl

%matplotlib inline
%load_ext autoreload
%autoreload 2



meta = get_movies()

meta = clean_up_genre(meta)

class_dists = data_to_plot(meta)

class_dists.plot(kind="bar")
```
