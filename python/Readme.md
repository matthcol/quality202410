# Python project illustrating test writing and usage

## Links
- https://docs.pytest.org/
- https://github.com/pytest-dev/pytest-cov
- https://github.com/pytest-dev/pytest-random-order

## Execute pytest
```
pytest (default: file beggining by test_, function begining by test_)
pytest mymodule.py (function begining by test_)
pytest package
pytest -v (verbose mode)
pytest -k pattern
pytest --cov=computing tests
pytest -v --random-order tests\computing\model
```