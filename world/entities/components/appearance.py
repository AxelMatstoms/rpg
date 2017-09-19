from world.entities.components.component import Component

class Appearance(Component):
    def __init__(self, entity, char, color_pair=None):
        super().__init__(entity)
        self.char = char
        self.color_pair = color_pair
