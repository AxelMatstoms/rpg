from world.entities.entity import Entity
from world.entities.components.flicker import Flicker
from world.entities.components.drawable import Drawable
from world.entities.components.position import Position
from colors import colors

class Campfire(Entity):
    def __init__(self, world, x, y):
        super().__init__(world)

        self.add_component("appearance", Flicker(self, ["A"], [1],
                                                 [colors.color_pair(colors.BLACK, colors.RED, 2),
                                                  colors.color_pair(colors.BLACK, colors.RED, 0),
                                                  colors.color_pair(colors.BLACK , colors.RED, 1),
                                                  colors.color_pair(colors.BLACK, colors.YELLOW, 2),
                                                  colors.color_pair(colors.BLACK, colors.YELLOW, 0),
                                                  colors.color_pair(colors.BLACK, colors.YELLOW, 1),
                                                  colors.color_pair(colors.BLACK, colors.YELLOW, 2),
                                                  colors.color_pair(colors.BLACK, colors.RED, 1),
                                                  colors.color_pair(colors.BLACK, colors.YELLOW, 0),
                                                  colors.color_pair(colors.BLACK, colors.YELLOW, 1),
                                                  colors.color_pair(colors.BLACK, colors.RED, 1),
                                                  colors.color_pair(colors.BLACK, colors.RED, 0)],
                                                 [6, 4, 2, 2, 2, 6, 4, 2, 4, 4, 6]))
        self.add_component("drawable", Drawable(self))
        self.add_component("position", Position(self, x, y))
        
