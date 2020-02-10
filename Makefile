#########################################

# definitions
UIFILES = $(wildcard src/*.ui)
DESTOBJ = $(UIFILES:src/%.ui=src/%_ui.py)

default: run

generate:: $(UIFILES)
	pyuic4 -x $(UIFILES) -o $(DESTOBJ)

run: generate
#	python3 src/UI_640x480_ui.py
	python3 src/main.py
