import pyglet
import util



class Item(pyglet.sprite.Sprite):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def normal(self, obj):
        """Applies the item's affect to the player. Returns None."""
        pass 
    
    def special(self, obj):
        """Applies the special affect to the player. Returns None."""
        pass

class GreenMushroom(Item):
    """Green Mushroom is a free point. Returns None."""

    stop = pyglet.resource.image("green_mushroom.png")
    util.center_ground_sprite(stop)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
#        print("GreenMushroom.x = ", self.x)
#        print("GreenMushroom.y = ", self.y)


