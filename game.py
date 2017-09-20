import time
import threading
import curses

from keyboard.keylistener import KeyListener
from world.entities.player import Player
from world.world import World

#The target of how long each frame should last, that is 1 / fps
FRAME_TIME = 0.10

lock = threading.Lock()

#main loop
def main(stdscr):
    global lock
    
    stdscr.clear()
    curses.curs_set(0)
    curses.noecho()

    height, width = stdscr.getmaxyx()

    #player = Player(width // 2, height // 2)

    keys = set()

    keylistener = KeyListener(stdscr, keys, lock)
    keylistener.daemon = True
    keylistener.start()

    world = World(stdscr, keys, lock)
    
    world.add_entity(Player(world, width // 2, height // 2))

    while True:
        if "\x1b" in keys:
            return
        
        tick = time.time()

        world.update()
        world.draw()
        
        #sleep
        tock = time.time()
        time.sleep(max(FRAME_TIME - (tock - tick), 0))

#try:
curses.wrapper(main)
#except Exception as e:
    #with open("errorlog", "w") as f:
        #f.write(str(e))
    

