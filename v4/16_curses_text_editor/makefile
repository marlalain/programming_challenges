##
# Spacer
#
# @file spacer.c
# @version 0.1

CC=tcc
CFLAGS=ltermbox
FILES=spacer.c
EXE=spacer

build: $(FILES)
	$(CC) -o $(EXE) $(FILES) -$(CFLAGS)

clean:
	rm -f *.o $(FILES)

run: $(FILES)
	$(CC) -o $(EXE) $(FILES) -$(CFLAGS) && ./$(EXE)

dev: $(FILES)
	clear && $(CC) -o $(EXE) $(FILES) -$(CFLAGS) && ./$(EXE)

# end
