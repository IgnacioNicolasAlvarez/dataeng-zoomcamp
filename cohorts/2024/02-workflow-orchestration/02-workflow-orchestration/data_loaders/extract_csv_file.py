import subprocess
import os
import pandas as pd
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data(*args, **kwargs):
    """
    Template code for loading data from any source.

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    dataframes = []
    urls_list = kwargs["url_raw_data"].split("**")

    for url in urls_list:
        df = pd.read_csv(url, compression='gzip')
        dataframes.append(df)

    df = pd.concat(dataframes, ignore_index=True)
    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
