import pytest
import pandas as pd


from src.analysis import unload


data = pd.read_csv("tests/test.csv")

data_unload = pd.DataFrame({
    "nr_labels":[0.0, 1.0],
    "nr_examples":[2.0, 4.0]})
data_unload = data_unload.set_index("nr_labels")

def test_unload(data=data, dataset_name="movies"):
    """Need to figure out how to test a tuple with a DF inside it
    """
    # pd.testing.assert_frame_equal(unload(data, dataset_name), data_unload)
    # unload(data, dataset_name) == (2.0, 3.0, data_unload)