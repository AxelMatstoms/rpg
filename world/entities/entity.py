class Entity:
    def __init__(self, world):
        self.components = {}
        self.world = world

    def update(self):
        for component in self.components.values():
            component.update()

    def draw(self):
        for component in self.components.values():
            component.draw()

    def add_component(self, name, component):
        self.components[name] = component

    def __contains__(self, item):
        return item in self.components

    def __getitem__(self, key):
        return self.components[key]
    
