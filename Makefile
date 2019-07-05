PYTHONPATH ?= :$(shell git rev-parse --top-level)/src
WILD_TYPE := $(shell which gtrue)

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

wild_type: $(WILD_TYPE)
	cp $(WILD_TYPE) wild_type

.PHONY: clean distclean lint test
.SILENT:                             # don't echo commands
