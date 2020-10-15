# multi-label-datasets
Exploratory analysis of publicly available datasets suitable for training multi-label language models

# Requirements
* node.js & npm (for Jupyterlab extensions)
* Python >=3.8.5
* pip
* pyenv
* virtualenv

# Setup
1. Install node & npm:
```
brew install node
```
2. If you want to use a git user that is different from the global one for your computer, first set
these locally:
```
git config user.name "Your Name Here"
git config user.email your@email.com
```
3. Create a virtual environment
```
# Example path: ~/.pyenv/versions/3.8.5/bin/python
virtualenv --python=/path/to/python/version .venv
```
4. Activate the virtual environment
```
source .venv/bin/activate
```
5. Update pip
```
pip install --upgrade pip
```
6. Install dependencies from `requirements.txt`
```
pip install -r requirements.txt
```
7. Set Jupyter notebook kernel to use Python from your virtual environment ([more info](https://janakiev.com/blog/jupyter-virtual-envs/)).
    * Add your virtual environment to Jupyter by running:
    ```
    python -m ipykernel install --name=multi-label-datasets
    ```
    * Note: to remove kernel from Jupyter:
    ```
    jupyter kernelspec uninstall multi-label-datasets
    ```

# Datasets
The following datasets are used here:
1. [CMU Movie Summary Corpus](http://www.cs.cmu.edu/~ark/personas/) as used on [this blog](https://towardsdatascience.com/multi-label-text-classification-5c505fdedca8).
2. [Toxic Comment Classification Challenge](https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge) (but very few datapoint with multiple labels).
3. [Mulan](http://mulan.sourceforge.net/datasets-mlc.html) (under "text" category).
4. RCV1 - agreement clauses needs to be checked
5. Reuters - agreement clauses needs to be checked

Note: to generate the report, you don't need the raw data, since the minimal data to generate the report is saved to git in `data_report/data_report.csv` (a very small file). If you want to regenerate this file, do the following:
1. Download the datasets above (Mulan and Reuters not currently supported) into `data_raw`.
2. Run:
```
python data_report.py
```
This will transform the raw data into `data_report/data_report.csv`.

# Generating the full report
This repository does not come with a jupyter notebook, and so you cannot see any of the plots in the report. However, this can easily be generated from the `analysis.md` file, which is written in MyST markdown. You just need to run:
```
jupytext analysis.md --to ipynb
```

# Extending the analysis
If you want to extend this analysis and see the results at the same time, the easiest way is to pair the markdown file with the jupyter notebook you generated in the last step. To pair the md and ipynb:

1. Start jupyter lab:
```
jupyter lab
```
2. Open `analysis.ipynb` and use `jupytext` to pair it with `analysis.md`. See instructions [here](https://jupytext.readthedocs.io/en/latest/paired-notebooks.html).
