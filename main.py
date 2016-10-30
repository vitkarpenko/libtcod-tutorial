import libtcodpy as libtcod

def handle_keys():
    global player_x, player_y
    
    key = libtcod.console_wait_for_keypress(True)
    if key.vk == libtcod.KEY_ENTER and key.lalt:
        # Alt + Enter: Toggle full_screen
        libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())

    elif key.vk == libtcod.KEY_ESCAPE:
        return True

    if key.vk == libtcod.KEY_CHAR:
        if key.c == ord('k'):
            player_y -= 1
        elif key.c == ord('j'):
            player_y += 1
        elif key.c == ord('h'):
            player_x -= 1
        elif key.c == ord('l'):
            player_x += 1
        elif key.c == ord('y'):
            player_y -= 1
	    player_x -= 1	
        elif key.c == ord('u'):
            player_y -= 1
	    player_x += 1	
        elif key.c == ord('b'):
            player_y += 1
	    player_x -= 1	
        elif key.c == ord('n'):
            player_y += 1
	    player_x += 1	


SCREEN_WIDTH = 80
SCREEN_HEIGHT = 40
LIMIT_FPS = 30


libtcod.console_set_custom_font('dejavu16x16_gs_tc.png',
                                libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)

libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'libtcod_tutorial', False)
con = libtcod.console_new(SCREEN_WIDTH, SCREEN_HEIGHT)

player_x = SCREEN_WIDTH / 2
player_y = SCREEN_HEIGHT / 2

while not libtcod.console_is_window_closed():
    libtcod.console_set_default_foreground(con, libtcod.Color(248, 238, 97))
    libtcod.console_put_char(con, player_x, player_y, '@', libtcod.BKGND_NONE)
    libtcod.console_blit(con, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0, 0)
    libtcod.console_flush()
    libtcod.console_put_char(con, player_x, player_y, ' ', libtcod.BKGND_NONE)

    # handle keys and exit game if needed
    exit = handle_keys()
    if exit:
        break
