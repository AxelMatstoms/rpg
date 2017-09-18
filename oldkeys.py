"""
class GameThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        curses.wrapper(main)
"""

"""
thread = GameThread()
thread.start()

with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
    
thread.join()
"""
