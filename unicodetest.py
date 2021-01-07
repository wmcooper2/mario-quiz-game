import pyglet
window = pyglet.window.Window()
label = pyglet.text.Label(text = "none", font_size = 36, x = window.width // 2, y = window.height // 2 - 64, anchor_x = 'center', anchor_y = 'center')

# print("pyglet version", pyglet.version)

@window.event
def on_draw():
    window.clear()
    label.draw()
   

pyglet.app.run()
