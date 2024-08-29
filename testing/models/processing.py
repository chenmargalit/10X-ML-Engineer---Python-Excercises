import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')


def remove_stop_words(string: str) -> str:
    tokens = word_tokenize(string)
    stop_words = set(stopwords.words('english'))

    filtered_tokens = [word for word in tokens if word not in stop_words]

    filtered_text = ' '.join(filtered_tokens)

    return filtered_text






