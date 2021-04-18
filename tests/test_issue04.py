import pytest

from lib.one_hot_encoder import fit_transform


@pytest.mark.parametrize(
    'given, expect',
    [
        (
            ['red', 'red', 'green'],
            [
                ('red', [0, 1]),
                ('red', [0, 1]),
                ('green', [1, 0]),
            ]
        ),
        (
            ['Moscow', 'New York', 'Moscow', 'London'],
            [
                ('Moscow', [0, 0, 1]),
                ('New York', [0, 1, 0]),
                ('Moscow', [0, 0, 1]),
                ('London', [1, 0, 0]),
            ]
        ),
        (
            ['foo'],
            [('foo', [1])]
        ),
        (
            [''],
            [('', [1])]
        )
    ]
)
def test_fit_transform(given, expect):
    assert fit_transform(*given) == expect
    for transformed in fit_transform(*given):
        assert transformed in expect


def test_fit_transform_exception():
    with pytest.raises(TypeError):
        fit_transform()
