PYTHON='python3'

test:
	${PYTHON} -m pytest tests

coverage:
	${PYTHON} -m pytest --cov=lib --cov-config=setup.cfg tests
