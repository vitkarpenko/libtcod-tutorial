import libtcodpy as libtcod


SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
LIMIT_FPS = 30

libtcod.console_set_custom_font('consolas12x12_gs_tc.png',
                                libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)

libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'libtcod_tutorial', False)

while not libtcod.console_is_window_closed():
    libtcod.console_set_default_foreground(0, libtcod.light_turquoise)
    libtcod.console_put_char(0, 1, 1, '@', libtcod.BKGND_NONE)
    libtcod.console_flush()

