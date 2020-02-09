#########################################

# definitions
UIFILES = $(wildcard src/*.ui)
DESTOBJ = $(UIFILES:src/%.ui=src/%_ui.py)

generate:: $(UIFILES)
	pyuic4 -x $(UIFILES) -o $(DESTOBJ)

run:: $(DESTOBJ)
	python3 src/UI_800x480_ui.py

