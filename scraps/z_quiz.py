import util
import items
import pyglet
import random
import players

#game_window
game_window = pyglet.window.Window(1000,563) #16:9 screen
SCREEN_W = game_window.width
SCREEN_H = game_window.height
OFF_SCREEN_R = 1100
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

#fire_light
fire_light_img = pyglet.resource.image("fire_light1.png")
util.center_floating_player(fire_light_img)
fire_light = players.FloatingPlayer(img = fire_light_img, x = OFF_SCREEN_R, y = FLOAT_H, batch = main_batch)
fire_light.scale = 2
#game_objects.append(fire_light)
game_window.push_handlers(fire_light)
game_window.push_handlers(fire_light.key_handler)

#dragon
dragon_img = pyglet.resource.image("dragon_walk1.png")
util.center_walking_player(dragon_img)
dragon = players.WalkingPlayer(img = dragon_img, x = OFF_SCREEN_R, y = WALK_H, batch = main_batch)
dragon.scale = 2
#game_objects.append(dragon)
game_window.push_handlers(dragon)
#game_window.push_handlers(dragon.key_handler)

#big_boo
big_boo_img = pyglet.resource.image("big_boo1_left.png")
util.center_floating_player(big_boo_img)
big_boo = players.FloatingPlayer(img = big_boo_img, x = OFF_SCREEN_R, y = FLOAT_H, batch = main_batch)
#no scale
#game_objects.append(big_boo)
game_window.push_handlers(big_boo) 
#no handler push yet

#green_koopa
green_koopa_img = pyglet.resource.image("green_koopa1_left.png")
util.center_walking_player(green_koopa_img)
green_koopa = players.WalkingPlayer(img = green_koopa_img, x = OFF_SCREEN_R, y = WALK_H, batch = main_batch) 
green_koopa.scale = 2
#game_objects.append(green_koopa)
game_window.push_handlers(green_koopa)

#big_mole
big_mole_img = pyglet.resource.image("big_mole1_left.png")
util.center_walking_player(big_mole_img)
big_mole = players.WalkingPlayer(img = big_mole_img, x = OFF_SCREEN_R, y = WALK_H, batch = main_batch)
big_mole.scale = 2
#game_objects.append(big_mole)
game_window.push_handlers(big_mole)

#mario
mario_img = pyglet.resource.image("mario_big_left_1.png")
util.center_walking_player(mario_img)
mario = players.WalkingPlayer(img = mario_img, x = OFF_SCREEN_R, y = WALK_H)#, batch = main_batch)
mario.scale = 2
mario.batch = main_batch
#game_objects.append(mario)
game_window.push_handlers(mario)





#def sprite_type(type_ = "standing"):
#    if type_ == "moving-forward":
#        moving_forward_image_list = [pyglet.image.load('assassin2.png'), pyglet.image.load('assassin3.png')]
#        moving_forward_animation = pyglet.image.Animation.from_image_sequence(moving_forward_image_list, 0.3) 
#        return moving_forward_animation
#    if type_ == "standing":
#        standing_animation = pyglet.image.load("assassin1.png")
#        return standing_animation






#add lakitu, mario, luigi, peach, toad
#move character image creation to its own class and return the image if its chosen. use generic names for player variables (player1 , player2, etc).


##########
##randomize player selection... use the objects, not the names of images
player_list = [big_boo, green_koopa, big_mole, fire_light, dragon, mario]
def randomize_players():
    if players.Player.randomized == False:
        players.Player.randomized = True
        random_players = []
        copy = player_list[:]
        for x in range(num_players):
            player_choice = random.choice(copy)
            random_players.append(player_choice)
            copy.remove(player_choice)
        for player in random_players:
            game_objects.append(player) #need to assign varnames to be able to call on them later.
########
randomize_players()

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
