from component import Component

class Appearance(Component):
    def __init__(self, entity, char, color_pair=None):
        super().__init__(self, entity)
        self.char = char
        self.color_pair = color_pair
