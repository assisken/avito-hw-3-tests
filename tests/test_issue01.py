# полный код в файле morse.py
from lib.morse import LETTER_TO_MORSE


def encode(message: str) -> str:
    """Кодирует строку в соответсвии с таблицей азбуки Морзе

    >>> encode('SOS')
    '... --- ...'
    >>> encode('foo')
    Traceback (most recent call last):
     ...
    KeyError: 'f'
    """
    encoded_signs = [
        LETTER_TO_MORSE[letter] for letter in message
    ]

    return ' '.join(encoded_signs)
