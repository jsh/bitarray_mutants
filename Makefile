TRUE := $(shell which true)

all: lint test experiment

clean:
	git clean -dfx

distclean: clean
	$(MAKE) -C experiments distclean

graph-mutants.html: graph-mutants.py
	./graph-mutants.py

result.experiment: result.empty result.frameshift result.point
	./experiment.py
	touch result.experiment

lint: wild_type
	isort *.py
	pylama *.py
	pylama -l radon *.py

test: wild_type
	touch empty
	pytest test*.py
	pytest util.py
	rm empty

wild_type: $(TRUE)
	cp $(TRUE) wild_type

.PHONY: clean lint test experiment
.SILENT:                             # don't echo commands
