from world.entities.components.appearance import Appearance
from world.entities.components.drawable import Drawable
from world.entities.components.keyboardcontroller import KeyboardController
from world.entities.components.position import Position
from world.entities.entity import Entity
from colors import colors

class Player(Entity):
    def __init__(self, world, x, y):
        super().__init__(world)
        
        self.add_component("appearance", Appearance(self, "Y", colors.color_pair(0, 6, 1)))
        self.add_component("drawable", Drawable(self))
        self.add_component("controller", KeyboardController(self, world.keys, world.lock))
        self.add_component("position", Position(self, x, y))
