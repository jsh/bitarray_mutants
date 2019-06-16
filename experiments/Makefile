TRUE := $(shell which true)
export PYTHONPATH := ..

all: appends graphs

graphs: battleship.html battleship_with_frameshifts.html causes_of_death.html plus_and_minus_frameshifts.html

other: neutrals random_mutants

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

.PHONY: all clean distclean graphs other lint
.SILENT:                              # don't echo any commands
