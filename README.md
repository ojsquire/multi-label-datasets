# multi-label-datasets
Exploratory analysis of publicly available datasets suitable for training multi-label language models

# Requirements
* Python >=3.8.5
* pip
* pyenv
* virtualenv

# Setup
0. If you want to use a git user that is different from the global one for your computer, first set
these locally:
```
git config user.name "Your Name Here"
git config user.email your@email.com
```
1. Create a virtual environment
```
# Example path: ~/.pyenv/versions/3.8.5/bin/python
virtualenv --python=/path/to/python/version .venv
```
2. Activate the virtual environment
```
source .venv/bin/activate
```
3. Update pip
```
pip install --upgrade pip
```
4. Install dependencies from `requirements.txt`
```
pip install -r requirements.txt
```

5. Set Jupyter notebook kernel to use Python from your virtual environment ([more info](https://janakiev.com/blog/jupyter-virtual-envs/))

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