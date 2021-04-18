import pytest

from lib.morse import decode


@pytest.mark.parametrize(
    'given, expect',
    [
        ('... --- ...', 'SOS'),
        ('..-. --- ---', 'FOO'),
        ('-... .- -... .- -... --- ..', 'BABABOI')
    ]
)
def test_decode(given: str, expect: str):
    assert decode(given) == expect
