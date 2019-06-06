all: lint battleship.html causes_of_death.html frameshift_errors.html

export PYTHONPATH := ..

%: %.py wild_type
	$<

%.html: %.py wild_type  # if the graph is newer than the python program, don't regenerate
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

.PHONY: all clean distclean lint

