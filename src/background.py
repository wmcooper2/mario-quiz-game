# 3rd party
import pyglet


class Background(pyglet.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.background_img = pyglet.resource.image("quiz1.png")
