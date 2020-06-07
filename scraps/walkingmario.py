import pyglet
from pyglet.window import key

resource_dir = "./resources"
pyglet.resource.path = [resource_dir]
pyglet.resource.reindex()

game_window = pyglet.window.Window()
main_batch = pyglet.graphics.Batch()

class Mario(pyglet.sprite.Sprite):
    
    mario_standing_img = pyglet.resource.image("big_mario_standing_left.png")
    mario_standing_seq = pyglet.image.ImageGrid(mario_standing_img, 1,1)
    mario_standing_anim = pyglet.image.Animation.from_image_sequence(mario_standing_seq, 1, True)
    mario_walking_right_img = pyglet.resource.image("mario_walking_right.png")
    mario_walking_right_seq = pyglet.image.ImageGrid(mario_walking_right_img, 1, 3)
    mario_walking_right_anim = pyglet.image.Animation.from_image_sequence(mario_walking_right_seq, 0.1, True)
    mario_walking_img = pyglet.resource.image("mario_walking_left.png")
    mario_walking_seq = pyglet.image.ImageGrid(mario_walking_img, 1, 3)
    mario_walking_anim = pyglet.image.Animation.from_image_sequence(mario_walking_seq, 0.1, True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.key_handler = key.KeyStateHandler()    

    def update(self, dt):
        if self.key_handler[key.LEFT]:
            self.image = self.mario_walking_anim
        if self.key_handler[key.UP]:
            self.image = self.mario_standing_anim
        if self.key_handler[key.RIGHT]:
            self.image = self.mario_walking_right_anim

mario_sprite = Mario(img = Mario.mario_standing_img, batch = main_batch)
game_window.push_handlers(mario_sprite.key_handler)

@game_window.event
def on_draw():
    game_window.clear()
    main_batch.draw()

def update(dt):
    mario_sprite.update(dt)

if __name__ == "__main__":
    pyglet.clock.schedule_interval(update, 1/120)
    pyglet.app.run()
