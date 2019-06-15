TRUE := $(shell which true)

all: appends graphs

graphs: battleship.html causes_of_death.html plus_and_minus_frameshifts.html battleship_with_frameshifts.html

export PYTHONPATH := ..

%: %.py wild_type
	./$<

%: %.sh
	./$<

%.html: %.py wild_type  # if the graph is newer than the python program, don't regenerate
	./$<

clean:
	rm -rf *.{mutants,results,html}

distclean:
	git clean -dfx

lint:
	isort *.py
	pylama *.py

wild_type: $(TRUE)
	cp $(TRUE) wild_type

.PHONY: all clean distclean lint
.SILENT:                              # don't echo any commands
