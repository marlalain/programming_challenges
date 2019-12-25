#include "termbox.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
//#include <wchar.h>

// TODO Add Resize

int initialize_map(int w, int h) {
  for (int i = 0; i < w; i++) {
    for (int j = 0; j < h; j++) {
      tb_change_cell(i, j, '.', TB_WHITE, TB_DEFAULT);
    }
  }
  return 0;
}

int main() {
  tb_init();
  tb_clear();

  int w, h;
  w = tb_width();
  h = tb_height();
  struct tb_event env;

  initialize_map(w, h);
  tb_present();
  tb_poll_event(&env);

  tb_shutdown();
  return 0;
}
