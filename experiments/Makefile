all: lint battleship.html

%.html: %.py wild_type
	$<

clean:
	rm -rf *.{mutants,results,html}

distclean:
	git clean -dfx

lint:
	@ isort *.py
	@ pylama *.py

wild_type: /usr/bin/true
	@ cp /usr/bin/true wild_type

.PHONY: all lint

