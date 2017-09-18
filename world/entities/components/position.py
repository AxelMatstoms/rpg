from component import Component

class Position(Component):
    def __init__(self, entity, x, y):
        super().__init__(self, entity)
        self.x = x
        self.y = y

    def pos(self):
        return (self.x, self.y)
        
    def cpos(self):
        return (self.y, self.x)
