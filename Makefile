install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	#python -m pytest test_gcli.py
	python -m pytest -vv --cov=hello test_cli.py
	#python -m pytest --nbval notebook.ipynb

format:
	black hello.py

lint:
	pylint --disable=R,C hello.py

all: install format lint test