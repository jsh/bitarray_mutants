all: lint test

clean:
	@ git clean -dfx

lint: wild_type
	@ isort *.py
	@ pylama *.py
	@ pylama -l radon *.py

test: wild_type
	@ pytest test*.py

wild_type: /usr/bin/true
	@ cp /usr/bin/true wild_type

.PHONY: clean lint test

