```shell
$ pipenv run make coverage
'python3' -m pytest --cov=lib --cov-config=setup.cfg tests
========================================================================= test session starts ==========================================================================
platform darwin -- Python 3.8.2, pytest-6.2.2, py-1.10.0, pluggy-0.13.1 -- /Users/nvzhiga/.local/share/virtualenvs/avito-hw-3-tests-8eV7mvol/bin/python3
cachedir: .pytest_cache
rootdir: /Users/nvzhiga/code/python/avito-hw-3-tests, configfile: setup.cfg
plugins: flake8-1.0.7, cov-2.11.1
collected 21 items

tests/__init__.py::FLAKE8 SKIPPED (file(s) previously passed FLAKE8 checks)                                                                                      [  4%]
tests/test_issue01.py::FLAKE8 SKIPPED (file(s) previously passed FLAKE8 checks)                                                                                  [  9%]
tests/test_issue01.py::tests.test_issue01.encode PASSED                                                                                                          [ 14%]
tests/test_issue02.py::FLAKE8 SKIPPED (file(s) previously passed FLAKE8 checks)                                                                                  [ 19%]
tests/test_issue02.py::test_decode[... --- ...-SOS] PASSED                                                                                                       [ 23%]
tests/test_issue02.py::test_decode[..-. --- ----FOO] PASSED                                                                                                      [ 28%]
tests/test_issue02.py::test_decode[-... .- -... .- -... --- ..-BABABOI] PASSED                                                                                   [ 33%]
tests/test_issue03.py::FLAKE8 SKIPPED (file(s) previously passed FLAKE8 checks)                                                                                  [ 38%]
tests/test_issue03.py::TestIssue03::test_fit_transform PASSED                                                                                                    [ 42%]
tests/test_issue03.py::TestIssue03::test_fit_transform_exception PASSED                                                                                          [ 47%]
tests/test_issue04.py::FLAKE8 SKIPPED (file(s) previously passed FLAKE8 checks)                                                                                  [ 52%]
tests/test_issue04.py::test_fit_transform[given0-expect0] PASSED                                                                                                 [ 57%]
tests/test_issue04.py::test_fit_transform[given1-expect1] PASSED                                                                                                 [ 61%]
tests/test_issue04.py::test_fit_transform[given2-expect2] PASSED                                                                                                 [ 66%]
tests/test_issue04.py::test_fit_transform[given3-expect3] PASSED                                                                                                 [ 71%]
tests/test_issue04.py::test_fit_transform_exception PASSED                                                                                                       [ 76%]
tests/test_issue05.py::FLAKE8 SKIPPED (file(s) previously passed FLAKE8 checks)                                                                                  [ 80%]
tests/test_issue05.py::test_raises_value_error[2021_04-18T20:21Z] PASSED                                                                                         [ 85%]
tests/test_issue05.py::test_date_time_format[2021-04-18T20:21Z-2021] PASSED                                                                                      [ 90%]
tests/test_issue05.py::test_date_time_format[18.04.2021-2021] PASSED                                                                                             [ 95%]
tests/test_issue05.py::test_foo PASSED                                                                                                                           [100%]

---------- coverage: platform darwin, python 3.8.2-final-0 -----------
Name                      Stmts   Miss  Cover
---------------------------------------------
lib/what_year_is_now.py      19      0   100%
---------------------------------------------
TOTAL                        19      0   100%


==================================================================== 15 passed, 6 skipped in 0.16s =====================================================================
```
