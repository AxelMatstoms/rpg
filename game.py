import time
import threading
import curses

from keyboard.keylistener import KeyListener
from world.entities.player import Player
from world.entities.campfire import Campfire
from world.world import World
from colors import colors

#The target of how long each frame should last, that is 1 / fps
FRAME_TIME = 0.10

#main loop
def main(stdscr):
    stdscr.clear()
    curses.curs_set(0)
    curses.noecho()
    curses.start_color()

    colors.init_colors()

    height, width = stdscr.getmaxyx()

    keys = set()
    lock = threading.Lock()

    keylistener = KeyListener(stdscr, keys, lock)
    keylistener.daemon = True
    keylistener.start()

    world = World(stdscr, keys, lock)
    
    world.add_entity(Player(world, width // 2, height // 2))
    world.add_entity(Campfire(world, 10, 10))

    while True:
        if "\x1b" in keys:
            return
        
        tick = time.time()

        world.update()
        world.draw()
        
        #sleep
        tock = time.time()
        time.sleep(max(FRAME_TIME - (tock - tick), 0))

curses.wrapper(main)
    

