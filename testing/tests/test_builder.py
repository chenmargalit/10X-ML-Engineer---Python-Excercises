import pytest
from models.builder import PlayerBuilder


player_builder = PlayerBuilder()


@pytest.mark.dp
def test_set_shirt_number_success():

    with pytest.raises(TypeError):
        player_builder.set_shirt_number('barca').build()


@pytest.mark.dp
def test_return_shirt_number():

    player_builder_instance = player_builder.set_shirt_number(12).build()
    shirt_number = player_builder_instance.shirt_number
    assert shirt_number == 12


@pytest.mark.dp
@pytest.mark.xfail
def test_set_shirt_number_fail():
    player_builder.set_shirt_number('barca').build()