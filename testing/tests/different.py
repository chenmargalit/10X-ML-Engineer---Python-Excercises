from pytest import mark


@mark.changed_name
def changed_name_test():

    x = 4
    assert x == 5
