from world.entities.components.component import Component

class Appearance(Component):
    def __init__(self, entity, char, attr=None):
        super().__init__(entity)
        self.char = char
        self.attr = attr
