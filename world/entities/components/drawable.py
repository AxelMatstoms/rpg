from world.entities.components.component import Component

class Drawable(Component):
    def __init__(self, entity):
        super().__init__(entity)

    def draw(self):
        if "position" in self.entity and "appearance" in self.entity:
            x, y = self.entity["position"].pos()
            char = self.entity["appearance"].char
            attr = self.entity["appearance"].attr

            stdscr = self.entity.world.stdscr

            if attr:
                stdscr.addstr(y, x, char, attr)
            else:
                stdscr.addstr(y, x, char)
        
