from unittest import mock

import pytest

from lib.what_year_is_now import what_is_year_now, API_URL


@pytest.mark.parametrize(
    'given',
    ['2021_04-18T20:21Z']
)
def test_raises_value_error(given):
    data = {"currentDateTime": given}

    with mock.patch('urllib.request.urlopen'), \
            mock.patch('json.load', return_value=data), \
            pytest.raises(ValueError):
        what_is_year_now()


@pytest.mark.parametrize(
    'given, expected',
    [
        ('2021-04-18T20:21Z', 2021),
        ('18.04.2021', 2021),
    ]
)
def test_date_time_format(given, expected):
    data = {"currentDateTime": given}

    with mock.patch('urllib.request.urlopen'), \
            mock.patch('json.load', return_value=data):
        assert expected == what_is_year_now()


def test_foo():
    assert API_URL == 'http://worldclockapi.com/api/json/utc/now'
