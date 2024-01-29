from pandas import DataFrame
import re 

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

def to_snake_case(name):
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()


@transformer
def execute_transformer_action(df: DataFrame, *args, **kwargs) -> DataFrame:

    df = df.rename(columns=to_snake_case)
    return df


@test
def test_vendor_id_column_in_df_columns(df, *args) -> None:
    assert 'vendor_id' in df.columns, 'The vendor_id columns is in df.columns'
