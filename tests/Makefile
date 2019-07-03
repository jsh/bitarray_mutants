TRUE := $(shell which true)
export PYTHONPATH ?= ${PWD}/../src

all: lint test

lint:
	isort *.py
	pylama *.py
	pylama -l radon *.py

test: wild_type
	# touch empty
	pytest test*.py
	pytest util.py
	# rm empty

wild_type: $(TRUE)
	cp $(TRUE) wild_type

.PHONY: lint test
.SILENT:                             # don't echo commands
