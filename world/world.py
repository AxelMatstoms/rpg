class World:
    def __init__(self, stdscr, keys, lock):
        self.stdscr = stdscr
        self.entities = []
        self.keys = keys
        self.lock = lock

    def update(self):
        for entity in self.entities:
            entity.update()

    def draw(self):
        self.stdscr.clear()
        
        for entity in self.entities:
            entity.draw()

    def width(self):
        _, width = self.stdscr.getmaxyx()
        return width

    def height(self):
        height, _ = self.stdscr.getmaxyx()

    def dim(self):
        height, width = self.stdscr.getmaxyx()
        return (width, height)

    def add_entity(self, entity):
        self.entities.append(entity)

    def remove_entity(self, entity):
        self.entities.remove(entity)

