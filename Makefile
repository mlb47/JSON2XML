all: main

test:
	python3 test.py

main:
	python3 main.py

clean:
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.xml' -delete