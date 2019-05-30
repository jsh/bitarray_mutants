all: lint test experiment

clean:
	@ git clean -dfx

graph-mutants.html: graph-mutants.py
	@ ./graph-mutants.py

result.experiment: result.empty result.frameshift result.point
	@ ./experiment.py
	@ touch result.experiment

lint: wild_type
	@ isort *.py
	@ pylama *.py
	@ pylama -l radon *.py

test: wild_type
	@ touch empty
	@ pytest test*.py experiment.py
	@ rm empty

wild_type: /usr/bin/true
	@ cp /usr/bin/true wild_type

.PHONY: clean lint test experiment

