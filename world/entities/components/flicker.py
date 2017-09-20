from world.entities.components.component import Component

class Flicker(Component):
    #chars is a list of characters to cycle through, should be the same length as char_pattern
    #char_pattern is a list of delays before cycling to the next char
    #attrs is a list of attributes to cycle through, should be the same length as attr_pattern
    #attr_pattern is a list of delays before cycling to the next attr
    def __init__(self, entity, chars, char_pattern, attrs, attr_pattern):
        super().__init__(entity)
        self.chars = chars
        self.char_pattern = char_pattern
        self.char_count = 0
        self.char_pattern_index = 0
        self.char = chars[0]
        
        self.attrs = attrs
        self.attr_pattern = attr_pattern
        self.attr_count = 0
        self.attr_pattern_index = 0
        self.attr = attrs[0]

    def update(self):
        self.char_count += 1
        if self.char_count >= self.char_pattern[self.char_pattern_index]:
            self.char_count = 0
            self.char_pattern_index += 1
            if self.char_pattern_index >= len(self.char_pattern):
                self.char_pattern_index = 0

        self.char = self.chars[self.char_pattern_index]

        self.attr_count += 1
        if self.attr_count >= self.attr_pattern[self.attr_pattern_index]:
            self.attr_count = 0
            self.attr_pattern_index += 1
            if self.attr_pattern_index >= len(self.attr_pattern):
                self.attr_pattern_index = 0

        self.attr = self.attrs[self.attr_pattern_index]

