import pytest
from models import processing


@pytest.mark.regular
def test_remove_stop_words():
    text_with_stop_words = 'this is some text with stopwords'
    text_without_stop_words = processing.remove_stop_words(text_with_stop_words)

    assert text_without_stop_words == 'text stopwords'


@pytest.mark.regular
@pytest.mark.xfail
def test_remove_stop_words_fails():
    text_with_stop_words = 'this is some text with stopwords'
    text_without_stop_words = processing.remove_stop_words(text_with_stop_words)

    assert text_without_stop_words == 'some text stopwords'
