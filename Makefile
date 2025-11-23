PYTHON := poetry run python
SRC := src/aoc2016_python

LATEST_DAY := $(shell ls $(SRC)/day*.py 2>/dev/null | sed 's/.*day//' | sed 's/\.py//' | sort -V | tail -1)
DAY ?= $(LATEST_DAY)

.PHONY: run day%
run: day$(DAY)

day%:
	$(PYTHON) $(SRC)/day$*.py
