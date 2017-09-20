from world.entities.components.component import Component

class Drawable(Component):
    def __init__(self, entity, stdscr):
        super().__init__(entity)
        self.stdscr = stdscr

    def draw(self):
        if "position" in self.entity and "appearance" in self.entity:
            x, y = self.entity["position"].pos()
            char = self.entity["appearance"].char
            attr = self.entity["appearance"].attr

            if attr:
                self.stdscr.addstr(y, x, char, attr)
            else:
                self.stdscr.addstr(y, x, char)
        
