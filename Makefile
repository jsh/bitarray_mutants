all: lint test

lint:
	@ isort *.py
	@ pylama *.py
	@ pylama -l radon *.py

test:
	@ pytest

.PHONY: lint test

