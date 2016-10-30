import libtcodpy as libtcod
import random


SCREEN_WIDTH = 80
SCREEN_HEIGHT = 40
MAP_WIDTH = 80
MAP_HEIGHT = 35
color_dark_wall = libtcod.Color(170, 170, 170)


class Tile:
    def __init__(self, blocked, block_sight=None):
        self.blocked = blocked

        if block_sight is None: block_sight = blocked
        self.block_sight = block_sight


class Object:
    def __init__(self, x, y, char, color):
        self.x = x
        self.y = y
        self.char = char
        self.color = color

    def move(self, dx, dy):
        if not map[self.x + dx][self.y + dy].blocked:
            self.x += dx
            self.y += dy

    def draw(self):
        libtcod.console_set_default_foreground(con, self.color)
        libtcod.console_put_char(con, self.x, self.y, self.char, libtcod.BKGND_NONE)

    def clear (self):
        libtcod.console_put_char(con, self.x, self.y, ' ', libtcod.BKGND_NONE)


def make_map():
    global map
 
    map = [[ Tile(False)
        for y in range(MAP_HEIGHT) ]
            for x in range(MAP_WIDTH) ]
    map[30][22].blocked = True
    map[30][22].block_sight = True
    map[50][22].blocked = True
    map[50][22].block_sight = True



def render_all():
    for object in objects:
        object.draw()
    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
            wall = map[x][y].block_sight
            if wall:
                libtcod.console_put_char_ex(con, x, y, '#', color_dark_wall, libtcod.Color(20, 20, 20))
            else:
                libtcod.console_set_char_background(con, x, y, libtcod.Color(20, 20, 20), libtcod.BKGND_SET)
    libtcod.console_blit(con, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0, 0)


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
            player.move(0, -1)
        elif key.c == ord('j'):
            player.move(0, 1)
        elif key.c == ord('h'):
            player.move(-1, 0)
        elif key.c == ord('l'):
            player.move(1, 0)
        elif key.c == ord('y'):
            player.move(-1, -1)
        elif key.c == ord('u'):
            player.move(-1, 1)
        elif key.c == ord('b'):
            player.move(-1, 1)
        elif key.c == ord('n'):
            player.move(1, 1)


def color_dark_ground():
    color = random.randint(0, 22)
    return libtcod.Color(color, color, color)


libtcod.console_set_custom_font('dejavu16x16_gs_tc.png',
                                libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)

libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'libtcod_tutorial', False)
con = libtcod.console_new(SCREEN_WIDTH, SCREEN_HEIGHT)

player = Object(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, '@', libtcod.Color(248, 238, 97))
human = Object(SCREEN_WIDTH/2 - 5, SCREEN_HEIGHT/2, 'H', libtcod.Color(177, 194, 130))
objects = [human, player]

make_map()

while not libtcod.console_is_window_closed():
    render_all()
    libtcod.console_flush()
    for object in objects:
        object.clear()

    # handle keys and exit game if needed
    exit = handle_keys()
    if exit:
        break
