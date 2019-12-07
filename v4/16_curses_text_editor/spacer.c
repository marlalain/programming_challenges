// Spacer - Terminal-focused Text Editor
// Made by Paulo Elienay II (github.com/paulo-e)
// This program uses by default tcc (tiny c compiler)
//  if you don't want to use it, change the first line of
//  the makefile from 'tcc' to 'gcc' (gnu c compiler)
// Compile using make and run using ./spacer

#include <ncurses.h>
#include <string.h>
#include <stdlib.h>

void main_loop() {
  char str[80];
  while (true) {
    getstr(str);
    refresh();
  }
}

void welcome_message() {
  // Welcome message like in vim
  // Triggered when the program is opened without a file to write
  FILE *fp;
  fp = fopen("/tmp/spacer_temp_file", "w+");
  int row, col;
  char welcome[] = "Welcome to Spacer!";
  char prompt[] = "Press any key.";
  getmaxyx(stdscr, row, col);
  mvprintw(row/2, (col-strlen(welcome))/2, "%s", welcome);
  mvprintw((row/2)-1, (col-strlen(prompt))/2, "%s", prompt);
  getch();
  clear();
  move(0, 0);
}

void config() {
  // here using cbreak() instead of raw() so we can ^C the program
  cbreak();
  // echoing what the user types, temporary
  echo();
  // F1-12 and other things
  keypad(stdscr, TRUE);
  // activating colors
  start_color();
}

int main (int argc, char *argv[])  {
  int row, col, x, y, ch;
  FILE *fp;
  if (argc != 2) {
    welcome_message();
  }
  fp = fopen(argv[1], "r+");
  if (fp == NULL) {
    perror("Cannot open input file");
    exit(1);
  }
  initscr();
  config();
  getmaxyx(stdscr, row, col);
  while ((ch = fgetc(fp)) != EOF) {
    getyx(stdscr, y, x);
    if (y == (row - 1)) {
      printw("<=Press Any  Key=>");
      getch();
      clear();
      move(0, 0);
    }
    printw("%c", ch);
    refresh();
  }
  main_loop();
  getch();
  endwin();
  fclose(fp);
  return 0;
}
