from mage_ai.data_cleaner.transformer_actions.base import BaseAction
from mage_ai.data_cleaner.transformer_actions.constants import ActionType, Axis
from mage_ai.data_cleaner.transformer_actions.utils import build_transformer_action
from pandas import DataFrame

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def execute_transformer_action(df: DataFrame, *args, **kwargs) -> DataFrame:
    """
    Execute Transformer Action: ActionType.FILTER

    Docs: https://docs.mage.ai/guides/transformer-blocks#filter
    """
    action = build_transformer_action(
        df,
        action_type=ActionType.FILTER,
        axis=Axis.ROW,
        action_code='passenger_count > 0 and trip_distance > 0',  # Specify your filtering code here
    )

    return BaseAction(action).execute(df)


@test
def test_trip_distance_greater_than_zero(df, *args) -> None:
    assert (df['trip_distance'] > 0).all(), 'trip_distance LOWER than zero'

@test
def test_passenger_count_greater_than_zero(df, *args) -> None:
    assert (df['passenger_count'] > 0).all(), 'passenger_count LOWER than zero'