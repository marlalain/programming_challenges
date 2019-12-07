CC = tcc
FILES = spacer.c
FLAGS = lncurses
OUT_EXE = spacer

build: $(FILES)
	$(CC) -o $(OUT_EXE) $(FILES) -$(FLAGS)

clean:
	rm -f *.o *.out spacer

rebuild: $(FILES)
	rm -f *.o *.out spacer && $(CC) -o $(OUT_EXE) $(FILES) -$(FLAGS)
