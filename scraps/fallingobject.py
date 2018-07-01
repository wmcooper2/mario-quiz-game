import pyglet
import math

game_window = pyglet.window.Window(100, 900)

@game_window.event
def on_draw():
    game_window.clear()
    luigi.draw()

def falling_y(time):
    """Calculates y_pos of a falling object. Returns Integer."""
    print(math.floor(-(0.5 * 9.8) * (time ** 2)))
    return math.floor(-(0.5 * 9.8) * (time ** 2))

main_time = 0
def update(dt):
    global main_time
    main_time += dt
    luigi.y += falling_y(main_time)
    print("main_time = ", main_time)
    if main_time > 30:
        main_time = 0

resource_dir = "./resources"
pyglet.resource.path = [resource_dir]
pyglet.resource.reindex()

luigi_img = pyglet.resource.image("luigi1.png")
luigi = pyglet.sprite.Sprite(img = luigi_img, x = game_window.width//2, y = game_window.height) 

if __name__ == "__main__":
    pyglet.clock.schedule_interval(update, 1/120)
    pyglet.app.run()
