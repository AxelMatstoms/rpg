import time
import threading

import curses
from curses import wrapper
from pynput import keyboard

pressed = set()
do_stop = False

#setup key listener
def on_press(key):
    pressed.add(key)
    
def on_release(key):
    pressed.discard(key)

    if key == keyboard.Key.esc:
        global do_stop
        do_stop = True
        return False

#main loop
def main(stdscr):
    stdscr.clear()
    curses.curs_set(0)

    height, width = stdscr.getmaxyx()
    global do_stop

    player = Player(width // 2, height // 2)

    while True:
        if do_stop:
            break
        
        tick = time.time()

        #move player
        if keyboard.Key.left in pressed:
            player.x -= 1
        if keyboard.Key.right in pressed:
            player.x += 1
        if keyboard.Key.up in pressed:
            player.y -= 1
        if keyboard.Key.down in pressed:
            player.y += 1

        #draw
        stdscr.clear()
        stdscr.addstr(player.y % height, player.x % width, "X")
        stdscr.refresh()
        
        #sleep
        tock = time.time()
        time.sleep(max(0.20 - (tock - tick), 0))

class GameThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        wrapper(main)



class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

thread = GameThread()
thread.start()

with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
    
thread.join()
