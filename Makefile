.PHONY: init test clean pypi_test pypi_prod egg egg_check test_unit test_integration

init:
	pip install -r requirements.txt

test:
	py.test tests

test_unit:
	python tests/test_integration.py

test_integration:
	python tests/test_integration.py

egg:
	python setup.py sdist bdist_wheel

egg_check:
	@twine check dist/*

pypi_test:
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

pypi_prod:
	twine upload dist/*

coverage:
	py.test --cov=coinmarketcap tests/

clean:
	@find . -type f -name ".mypy_cache" -print0 | xargs -r0 -- rm -r
	@find . -type d -name ".pytest_cache" -print0 | xargs -r0 -- rm -r
	@find . -type d -name "__pycache__" -print0 | xargs -r0 -- rm -r
	@find . -type d -name "*.pyc" -print0 | xargs -r0 -- rm -r
	@rm -rf *.egg-info build dist
