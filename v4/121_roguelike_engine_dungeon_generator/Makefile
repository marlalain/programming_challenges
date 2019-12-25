##
# Dungeon Crawler Engine
#
# @file main.c
# @version 0.1

CC=tcc
CFLAGS=ltermbox
FILES=main.c
EXE=main

build: $(FILES)
	$(CC) -o $(EXE) $(FILES) -$(CFLAGS)

clean:
	rm -f *.o $(FILES)

run: $(FILES)
	$(CC) -o $(EXE) $(FILES) -$(CFLAGS) && ./$(EXE)

dev: $(FILES)
	clear && $(CC) -o $(EXE) $(FILES) -$(CFLAGS) && ./$(EXE)

# end
