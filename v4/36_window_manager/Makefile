LIBS=\
	$(shell pkg-config --cflags --libs wlroots) \
	$(shell pkg-config --cflags --libs wayland-server) \
	$(shell pkg-config --cflags --libs wkbcommon)

bbwm: bbwm.c
	$(CC) $(CFLAGS) \
-g -Werror -I. \
	-DWLR_USE_UNSTABLE \
	-o $@ $< \
	$(LIBS)

clean:
	rm -f bbwm
