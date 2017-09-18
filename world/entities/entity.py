class Entity:
    def __init__(self, world):
        self.components = {}

    def update(self):
        for name, component in components.items():
            component.update()

    def add_component(self, name, component):
        self.components[name] = component

    def __contains__(self, item):
        return item in self.components

    def __getitem__(self, key):
        return self.components[key]
    
