run:
	python3 src/main.py

install:
	pip3 install -r requirements.txt

requirements:
	pip3 freeze > requirements.txt

run_tests:
	python3 -m pytest tests
