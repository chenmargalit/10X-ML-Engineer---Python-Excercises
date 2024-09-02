import time
from pytest import mark


@mark.general
def test_return_airbnb_df_success(return_airbnb_df):
    df_len = len(return_airbnb_df)
    assert df_len > 30_000


@mark.xfail(reason='expected fail')
@mark.general
def test_return_airbnb_df_fail(return_airbnb_df):
    df_len = len(return_airbnb_df)
    assert df_len < 5


@mark.general
@mark.skip(reason='dont need this now')
def test_skip_test():
    print('this test will be skipped')
    assert True


# @mark.general
# def test_takes_5_seconds():
#     time.sleep(5)
#     return True
#
#
# @mark.general
# def test_takes_3_seconds():
#     time.sleep(3)
#     return True
#
#
# @mark.general
# def test_takes_8_seconds():
#     time.sleep(8)
#     return True


