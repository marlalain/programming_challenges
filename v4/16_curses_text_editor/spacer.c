#include "termbox.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
  tb_init();  // init termbox
  tb_clear(); // clear the screen

  int w, h, x, y; // height, width and cursors x and y
  w = tb_width();
  h = tb_height();
  struct tb_event env;

  tb_change_cell(0, 0, 'H', TB_WHITE, TB_DEFAULT); // Hello
  tb_change_cell(0, 1, 'W', TB_WHITE, TB_DEFAULT); // World
  tb_change_cell(0, 2, '!', TB_WHITE, TB_DEFAULT); // !

  tb_present();        // sync internal buffer with termina
  tb_poll_event(&env); // wait for input

  tb_shutdown(); // shutting termbox down
  return 0;      // no errors
}
