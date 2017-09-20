from world.entities.components.component import Component

class KeyboardController(Component):
    def __init__(self, entity, keys, lock):
        super().__init__(entity)
        self.keys = keys
        self.lock = lock

    def update(self):
        if "position" in self.entity:
            position = self.entity["position"]
            if "KEY_LEFT" in self.keys:
                position.x -= 1
                with self.lock:
                    self.keys.remove("KEY_LEFT")
            if "KEY_RIGHT" in self.keys:
                position.x += 1
                with self.lock:
                    self.keys.remove("KEY_RIGHT")
            if "KEY_UP" in self.keys:
                position.y -= 1
                with self.lock:
                    self.keys.remove("KEY_UP")
            if "KEY_DOWN" in self.keys:
                position.y += 1
                with self.lock:
                    self.keys.remove("KEY_DOWN")
