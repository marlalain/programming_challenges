#include "termbox.h"
#include <math.h>
#include <openssl/rand.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <unistd.h>
//#include <wchar.h>

// TODO Add Resize

struct room {
  int center_x;
  int center_y;
} room;

int initialize_map(int w, int h) {
  for (int i = 0; i < w; i++) {
    for (int j = 0; j < h; j++) {
      tb_change_cell(i, j, ' ', TB_WHITE, TB_DEFAULT);
    }
  }
  return 0;
}

int main() {
  tb_init();
  tb_clear();
  srand((unsigned)time(NULL));

  int w, h;
  w = tb_width();
  h = tb_height();
  struct tb_event env;

  initialize_map(w, h);

  // 1. Generate first cell
  struct room first_room;
  first_room.center_x = (rand() % w) + 1;
  first_room.center_y = (rand() % h) + 1;
  tb_change_cell(first_room.center_x, first_room.center_y, '#', TB_WHITE,
                 TB_DEFAULT);

  tb_present();
  tb_poll_event(&env);

  tb_shutdown();
  return 0;
}
