run: 
	python3 sample/main.py

install:
    pip install -r requirements.txt

requirements:
	pip3 freeze > requirements.txt 