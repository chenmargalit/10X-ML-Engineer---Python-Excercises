from pytest import fixture
import pandas as pd


@fixture()
def return_airbnb_df():

    airbnb_df = pd.read_csv('AB_NYC_2019.csv')
    return airbnb_df
