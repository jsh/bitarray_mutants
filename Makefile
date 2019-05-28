all: lint test experiment

clean:
	@ git clean -dfx

grouped-bar.html: grouped-bar.py
	@ ./grouped-bar.py

result.experiment: result.empty result.frameshift result.point
	@ ./experiment.py
	@ touch result.experiment

lint: wild_type
	@ isort *.py
	@ pylama *.py
	@ pylama -l radon *.py

test: wild_type
	@ pytest test*.py experiment.py

wild_type: /usr/bin/true
	@ cp /usr/bin/true wild_type

.PHONY: clean lint test experiment

