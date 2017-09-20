import curses

BLACK = 0
RED = 1
GREEN = 2
YELLOW = 3
BLUE = 4
MAGENTA = 5
CYAN = 6
WHITE = 7

def init_colors():
    for fg in range(8):
        for bg in range(8):
            curses.init_pair(fg + 8 * bg + 1, fg, bg)

def color_pair(bg, fg, bright=0):
    color_pair = curses.color_pair(fg + 8 * bg + 1)
    if bright == 1:
        color_pair |= curses.A_BOLD
    elif bright == 2:
        color_pair |= curses.A_DIM
    return color_pair

def _test(stdscr):
    stdscr.clear()
    curses.start_color()
    init_colors()

    for brightness in range(3):
        for fg in range(8):
            for bg in range(8):
                stdscr.addstr(bg, fg + 8 * brightness, "A", color_pair(bg, fg, bright=brightness))


    stdscr.getkey()

if __name__ == "__main__":
    curses.wrapper(_test)
            
