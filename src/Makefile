PYTHONPATH ?= :$(shell git rev-parse --top-level)/src
WILD_TYPE := $(shell which gtrue)

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

wild_type: $(WILD_TYPE)
	cp $(WILD_TYPE) wild_type


.PHONY: clean lint test
.SILENT:                             # don't echo commands
