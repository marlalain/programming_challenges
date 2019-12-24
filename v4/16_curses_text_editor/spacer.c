#include "termbox.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <wchar.h>

int tb_print(int x, int y, char *str, uint16_t fg, uint16_t bg) {
  uint32_t uni;
  while (*str) {
    str += tb_utf8_char_to_unicode(&uni, str);
    tb_change_cell(x, y, uni, fg, bg);
    x++;
  }
}

int main() {
  tb_init();  // init termbox
  tb_clear(); // clear the screen

  int w, h, x, y; // height, width and cursors x and y
  w = tb_width();
  h = tb_height();
  struct tb_event env;

  tb_print(0, 0, "Hello World!", TB_WHITE, TB_DEFAULT);

  tb_present();        // sync internal buffer with termina
  tb_poll_event(&env); // wait for input

  tb_shutdown(); // shutting termbox down
  return 0;      // no errors
}
