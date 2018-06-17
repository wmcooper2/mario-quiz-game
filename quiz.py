import pyglet
import characters
import util

def center_image(image):
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2


game_window = pyglet.window.Window(1000,563) #16:9 screen

#setup resource dirs
resource_dir = "./resources"
pyglet.resource.path = [resource_dir]
pyglet.resource.reindex()

#setup images
game_objects = []
main_batch = pyglet.graphics.Batch()
background_img = pyglet.resource.image("quiz1.png")
background = pyglet.sprite.Sprite(img = background_img, batch = main_batch)

#fire_light_char
fire_char_img = pyglet.resource.image("fire_light1.png")
util.center_image(fire_char_img)
center_image(fire_char_img)
fire_char = characters.FloatingChar(img = fire_char_img, x = 600, y = 100, batch = main_batch)
fire_char.scale = 2
game_objects.append(fire_char)
game_window.push_handlers(fire_char)
game_window.push_handlers(fire_char.key_handler)

#dragon_char
dragon_img = pyglet.resource.image("dragon_walk1.png")
util.center_image(dragon_img)
dragon_char = characters.Character(img = dragon_img, x = 700, y = 100, batch = main_batch)
dragon_char.scale = 2
game_objects.append(dragon_char)
game_window.push_handlers(dragon_char)
game_window.push_handlers(dragon_char.key_handler)


@game_window.event
def on_draw():
    game_window.clear()
    main_batch.draw()

def update(dt):
    for obj in game_objects:
        obj.update(dt)
    fire_char.floating()

if __name__ == "__main__":
    pyglet.clock.schedule_interval(update, 1/120)
    pyglet.app.run()
