all: lint battleship.html

battleship.html: wild_type
	battleship.py

lint:
	@ isort *.py
	@ pylama *.py

wild_type: /usr/bin/true
	@ cp /usr/bin/true wild_type

.PHONY: all lint

