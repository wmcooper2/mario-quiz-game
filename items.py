import pyglet

class Item(pyglet.sprite.Sprite):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class BlueBall(Item):
    """English vocabulary word."""    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        
