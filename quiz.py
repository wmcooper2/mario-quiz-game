import util
import pyglet
import players

#game_window
game_window = pyglet.window.Window(1000,563) #16:9 screen
SCREEN_W = game_window.width
SCREEN_H = game_window.height
OFF_SCREEN_R = 100
FLOAT_H = 100
WALK_H = 63

#determine number of players
num_players = 6

#create the spots for player positions on the screen
spots = util.Line(screen_w = SCREEN_W, num_players=num_players)
spots.line_up()





#setup resource dirs
resource_dir = "./resources"
pyglet.resource.path = [resource_dir]
pyglet.resource.reindex()

#setup images
game_objects = []
main_batch = pyglet.graphics.Batch()
background_img = pyglet.resource.image("quiz1.png")
background = pyglet.sprite.Sprite(img = background_img, batch = main_batch)

#load players

#fire_light
fire_light_img = pyglet.resource.image("fire_light1.png")
util.center_floating_player(fire_light_img)
fire_light = players.FloatingPlayer(img = fire_light_img, x = OFF_SCREEN_R, y = FLOAT_H, batch = main_batch)
fire_light.scale = 2
game_objects.append(fire_light)
game_window.push_handlers(fire_light)
game_window.push_handlers(fire_light.key_handler)

#dragon
dragon_img = pyglet.resource.image("dragon_walk1.png")
util.center_walking_player(dragon_img)
dragon = players.WalkingPlayer(img = dragon_img, x = OFF_SCREEN_R, y = WALK_H, batch = main_batch)
dragon.scale = 2
game_objects.append(dragon)
game_window.push_handlers(dragon)
#game_window.push_handlers(dragon.key_handler)

#big_boo
big_boo_img = pyglet.resource.image("big_boo1_left.png")
util.center_floating_player(big_boo_img)
big_boo = players.FloatingPlayer(img = big_boo_img, x = OFF_SCREEN_R, y = FLOAT_H, batch = main_batch)
#no scale
game_objects.append(big_boo)
game_window.push_handlers(big_boo) 
#no handler push yet

#green_koopa
green_koopa_img = pyglet.resource.image("green_koopa1_left.png")
util.center_walking_player(green_koopa_img)
green_koopa = players.WalkingPlayer(img = green_koopa_img, x = OFF_SCREEN_R, y = WALK_H, batch = main_batch) 
green_koopa.scale = 2
game_objects.append(green_koopa)
game_window.push_handlers(green_koopa)

#big_mole
big_mole_img = pyglet.resource.image("big_mole1_left.png")
util.center_walking_player(big_mole_img)
big_mole = players.WalkingPlayer(img = big_mole_img, x = OFF_SCREEN_R, y = WALK_H, batch = main_batch)
big_mole.scale = 2
game_objects.append(big_mole)
game_window.push_handlers(big_mole)


#add big_mole, lakitu, mario, luigi, peach, toad
#move character image creation to its own class and return the image if its chosen. use generic names for player variables (player1 , player2, etc).



@game_window.event
def on_draw():
    game_window.clear()
    main_batch.draw()

def update(dt):
    for obj in game_objects:
        obj.update(dt)
    fire_light.floating()
    big_boo.floating()

if __name__ == "__main__":
    pyglet.clock.schedule_interval(update, 1/120)
    pyglet.app.run()
