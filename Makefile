all: lint test

clean:
	@ git clean -dfx

lint:
	@ isort *.py
	@ pylama *.py
	@ pylama -l radon *.py

test: wild_type
	@ pytest

wild_type: /usr/bin/true
	@ cp /usr/bin/true wild_type

.PHONY: clean lint test

