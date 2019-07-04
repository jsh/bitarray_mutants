TRUE := $(shell which true)
PYTHONPATH ?= :${PWD}/src

all: lint test

clean:
	git clean -dfx

distclean: clean
	$(MAKE) -C experiments distclean

lint: wild_type
	isort *.py
	pylama *.py
	pylama -l radon *.py

test: wild_type
	pytest

wild_type: $(TRUE)
	cp $(TRUE) wild_type

.PHONY: clean distclean lint test
.SILENT:                             # don't echo commands
