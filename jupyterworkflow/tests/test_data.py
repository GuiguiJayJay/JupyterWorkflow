import pandas as pd
import numpy as np
from jupyterworkflow.data import get_freemont_data

data = get_freemont_data()

def test_freemont_data():
    data = get_freemont_data()
    assert all(data.columns == ['West','East','Total'])
    assert isinstance(data.index, pd.DatetimeIndex)
    assert len(np.unique(data.index.time)) == 24
