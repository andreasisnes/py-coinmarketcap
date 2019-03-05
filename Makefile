.PHONY: init test clean pypi_test pypi_prod egg egg_check

init:
	pip install -r requirements.txt

test:
	py.test tests

egg:
	python setup.py sdist bdist_wheel

egg_check:
	@twine check dist/*

pypi_test:
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

pipi_prod:
	twine upload dist/*

clean:
	@find . -type f -name ".mypy_cache" -print0 | xargs -r0 -- rm -r
	@find . -type d -name ".pytest_cache" -print0 | xargs -r0 -- rm -r
	@find . -type d -name "__pycache__" -print0 | xargs -r0 -- rm -r
	@find . -type d -name "*.pyc" -print0 | xargs -r0 -- rm -r
	@rm -rf *.egg-info build dist
