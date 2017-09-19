from world.entities.components.appearance import Appearance
from world.entities.components.drawable import Drawable
from world.entities.components.keyboardcontroller import KeyboardController
from world.entities.components.position import Position
from world.entities.entity import Entity

class Player2(Entity):
    def __init__(self, world, x, y):
        super().__init__(world)
        
        self.add_component("appearance", Appearance(self, "Y"))
        self.add_component("drawable", Drawable(self, world.stdscr))
        self.add_component("controller", KeyboardController(self, world.keys, world.lock))
        self.add_component("position", Position(self, x, y))
