##
# Chell - the C shell!
#
# @version 0.1

CC = tcc
#CFLAGS=
FILES=chell.c
EXE=chell

build: $(FILES)
	$(CC) -o $(EXE) $(FILES)

clean:
	rm -f *.o $(FILES)

run: $(FILES)
	$(CC) -o $(EXE) $(FILES)  && ./$(EXE)

dev: $(FILES)
	clear && $(CC) -o $(EXE) $(FILES)  && ./$(EXE)

# end
