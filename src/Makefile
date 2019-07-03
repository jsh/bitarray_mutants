all: lint test

causes_of_death:
	cp ../causes_of_death .

clean:
	git clean -dfx

lint:
	isort *.py
	pylama *.py
	pylama -l radon *.py

test: causes_of_death
	pytest


.PHONY: clean lint test
.SILENT:                             # don't echo commands
