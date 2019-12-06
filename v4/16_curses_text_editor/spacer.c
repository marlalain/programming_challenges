// Spacer - Terminal-focused Text Editor
// Made by Paulo Elienay II (github.com/paulo-e)
// Compile with gcc -lncurses spacer.c

#include <ncurses.h>

int main ()  {
  // initializes the screen
  // sets up memory and clears the screen
  initscr();
  printw("Hello World!");
  // print to screen
  refresh();
  // wait for user input
  getch();
  // deallocates memory and ends ncurses
  //endwin();
  return 0;
}
