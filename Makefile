SRC_CORE=src
SRC_TEST=tests
PYTHON=python3
PIP=pip3

test: ## Test the code
	@type coverage >/dev/null 2>&1 || (echo "Run '$(PIP) install coverage' first." >&2 ; exit 1)
	@coverage run --source . -m unittest
	@coverage report
	@coverage html

test_integration: ## Test the code
	@type coverage >/dev/null 2>&1 || (echo "Run '$(PIP) install coverage' first." >&2 ; exit 1)
	@coverage run --source . -m $(SRC_TEST).integration.test_api_integration
	@coverage report

clean: ## Cleanup
	@rm -f $(SRC_CORE)/*.pyc
	@rm -rf $(SRC_CORE)/__pycache__
	@rm -f $(SRC_TEST)/*.pyc
	@rm -rf $(SRC_TEST)/__pycache__
	@rm -rf dist
	@rm -rf htmlcov
	@rm -rf $(SRC_CORE)/*.egg-info

build: ## build project
	$(PYTHON) -m pip install --upgrade build ; \
	$(PYTHON) -m build

upload:
	$(PYTHON) -m twine upload dist/*

lint:
	pylint ./

autoformat:
	autopep8 --in-place --recursive ./
