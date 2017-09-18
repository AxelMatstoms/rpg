import threading

class KeyListener(threading.Thread):
    def __init__(self, stdscr, keys, lock):
        threading.Thread.__init__(self)
        self.stdscr = stdscr
        self.keys = keys
        self.lock = lock

    def run(self):
        while True:
            key = self.stdscr.getkey()
            with self.lock:
                self.keys.add(key)
