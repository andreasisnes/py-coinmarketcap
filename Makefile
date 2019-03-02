.PHONY: init test clean

init:
	pip install -r requirements.txt

test:
	py.test tests

clean:
	@find . -name '__pycache__' -exec rm -r "{}" \;
	@find . -name '__*.pyc' -delete
