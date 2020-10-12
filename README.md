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

7. Set Jupyter notebook kernel to use Python from your virtual environment ([more info](https://janakiev.com/blog/jupyter-virtual-envs/))

    a. Install `ipykernel` (should already be done from requirements.txt)

    b. Add your virtual environment to Jupyter
    ```
    python -m ipykernel install --name=multi-label-datasets
    ```
    c. Open JupyterLab:
    ```
    jupyter lab
    ```
    Note: to remove kernel from Jupyter:
    ```
    jupyter kernelspec uninstall multi-label-datasets
    ```

# Datasets
* Using the following links, download all the datasets and put in the `datasets/` directory:
1. [CMU Movie Summary Corpus](http://www.cs.cmu.edu/~ark/personas/) as used on [this blog](https://towardsdatascience.com/multi-label-text-classification-5c505fdedca8).
2. [Toxic Comment Classification Challenge](https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge) (but very few datapoint with multiple labels).
3. [Mulan](http://mulan.sourceforge.net/datasets-mlc.html) (under "text" category).
4. RCV1 - agreement clauses needs to be checked
5. Reuters - agreement clauses needs to be checked

