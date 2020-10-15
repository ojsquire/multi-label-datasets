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

```{code-cell} ipython3
import matplotlib as mpl
import pandas as pd

from src.analysis import analyse


%matplotlib inline
%load_ext autoreload
%autoreload 2

# Load dataset for report
data = pd.read_csv("data_report/data_report.csv")
```

## CMU movie summary dataset
```{code-cell} ipython3
analyse(data, "movies", "CMU dataset")
```

## Toxic comments dataset
```{code-cell} ipython3
analyse(data, "toxic", "toxic comments dataset")
```

## RCV1 dataset
```{code-cell} ipython3
analyse(data, "rcv1", "miniRCV1 dataset")
```