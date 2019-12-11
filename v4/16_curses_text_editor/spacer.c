// Spacer (Spacemacs and SpaceVim based text editor)
// Made in C and compiled with tcc by Paulo Elienay II
// If you wish to use gcc, change the CC param in the
// makefile.

#include <ncurses.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/ioctl.h>

int setup() {
  initscr();
  raw();
  keypad(stdscr, TRUE);
  noecho();
}

int kbd_handler() {
  int ch, row, col, x, y;
  char str[80];

  getmaxyx(stdscr, row, col);
  while (true) {
    ch = getch();
    if (ch == 'q') {
      exit(0);
    } else if (ch == KEY_LEFT) {
      getyx(stdscr, y, x);
      move(y, x - 1);
    }else if (ch == KEY_RIGHT) {
      getyx(stdscr, y, x);
      move(y, x + 1);
    }else if (ch == KEY_UP) {
      getyx(stdscr, y, x);
      move(y - 1, x);
    }else if (ch == KEY_DOWN) {
      getyx(stdscr, y, x);
      move(y + 1, x);
    }
  }
}

int main(int argc, char **argv) {
  int ch, row, col;
  setup();

  kbd_handler();

  getch();
  endwin();

  return 0;
}
