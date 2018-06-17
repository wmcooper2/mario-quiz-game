import math
import pyglet
from pyglet.window import key


class Character(pyglet.sprite.Sprite):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.keys = dict(left=False, right=False, up=False, down=False)
        self.key_handler = key.KeyStateHandler()
        
    def update(self, dt):
        if self.key_handler[key.LEFT]:
            self.x -= 1
        if self.key_handler[key.RIGHT]:
            self.x += 1
        if self.key_handler[key.UP]:
            self.y += 1
        if self.key_handler[key.DOWN]:
            self.y -= 1
        else:
            pass

class FloatingChar(Character):
    
    float_height = 0
    float_deg = 0

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def floating(self):
        """Makes the character float up and down in place.
            Returns None."""
        radians = math.radians(FloatingChar.float_deg)
        FloatingChar.float_height = math.sin(radians)
        if FloatingChar.float_deg == 360:
            FloatingChar.float_deg = 0
            FloatingChar.float_height = 0
        FloatingChar.float_deg += 1
        print("float_height = ", FloatingChar.float_height)
        print("float_deg = ", FloatingChar.float_deg)

    def update(self, dt):
        self.floating()
        self.y = self.y + (FloatingChar.float_height / 2) #?
        if self.key_handler[key.LEFT]:
            self.x -= 1
        if self.key_handler[key.RIGHT]:
            self.x += 1
        if self.key_handler[key.UP]:
            self.y += 1
        if self.key_handler[key.DOWN]:
            self.y -= 1
        else:
            pass
