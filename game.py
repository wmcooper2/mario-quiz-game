import util
import pyglet
import random
import objects
import items #must come after objects (resource mod is defined in objects... move to main?)
from pyglet.window import key
from pyglet import clock

#game_window
game_window = pyglet.window.Window(1000,563) #16:9 screen

#key_handler
key_handler = key.KeyStateHandler()
keys = dict(left=False)
game_window.push_handlers(key_handler)

#constants
SCREEN_W = game_window.width
SCREEN_H = game_window.height
OFF_SCREEN_R = 1100
FLOAT_H = 100
WALK_H = 63
ITEM_PLATFORM_H = 264
ITEM_PLATFORM_W = 300
#determine number of players (replace with return val from menu screen)
NUM_PLAYERS = 6
NUM_ITEMS = 1

#create the spots for player positions on the screen
player_spots = util.Line(screen_w = SCREEN_W, num_players=NUM_PLAYERS)
player_spots.line_up()

#setup images
game_objects = [] #all players are added in randomize_players()
floating_players = []
walking_players = []
players = [] #for now, contents are similar to game_objects
main_batch = pyglet.graphics.Batch()

#background
background = objects.Background(img = objects.Background.background_img, batch = main_batch)

#fire_light
fire_light = objects.FireLight(img = objects.FireLight.stand_left, x = OFF_SCREEN_R, y = FLOAT_H, batch = main_batch)
players.append(fire_light)
floating_players.append(fire_light)

#dragon
dragon = objects.Dragon(img = objects.Dragon.stand_left, x = OFF_SCREEN_R, y = WALK_H, batch = main_batch)
dragon.scale = 2
players.append(dragon)
walking_players.append(dragon)

#big_boo
big_boo = objects.BigBoo(img = objects.BigBoo.stand_left, x = OFF_SCREEN_R, y = FLOAT_H, batch = main_batch)
players.append(big_boo)
floating_players.append(big_boo)

#green_koopa
green_koopa = objects.GreenKoopa(img = objects.GreenKoopa.stand_left, x = OFF_SCREEN_R, y = WALK_H, batch = main_batch) 
green_koopa.scale = 2
players.append(green_koopa)
walking_players.append(green_koopa)

#big_mole
big_mole = objects.BigMole(img = objects.BigMole.stand_left, x = OFF_SCREEN_R, y = WALK_H, batch = main_batch)
big_mole.scale = 1.5 
players.append(big_mole)
walking_players.append(big_mole)

#mario
mario = objects.Mario(img = objects.Mario.stand_left, x = OFF_SCREEN_R, y = WALK_H, batch = main_batch)
mario.scale = 2
players.append(mario)
walking_players.append(mario)

#add lakitu, luigi, peach, toad

##randomize player selection
def randomize_players():
    if objects.Player.randomized == False:
        objects.Player.randomized = True
        random_players = []
        copy = players[:]
        for x in range(NUM_PLAYERS):
            player_choice = random.choice(copy)
            random_players.append(player_choice)
            copy.remove(player_choice)
        for player in random_players:
            game_objects.append(player) 
randomize_players()






#setup item sprites
green_mushroom = items.GreenMushroom(img = items.GreenMushroom.stop, x = ITEM_PLATFORM_W, y = ITEM_PLATFORM_H, batch = main_batch)
green_mushroom.scale = 1.5
game_items = []

game_items.append(green_mushroom)

#line up the items
item_spots = util.Line(screen_w = SCREEN_W, num_items = NUM_ITEMS)
item_spots.item_line_up(game_items)

print(game_items)

@game_window.event
def on_draw():
    game_window.clear()
    main_batch.draw()

def update(dt):
    for obj in game_objects:
        obj.update(dt)
    for obj in floating_players:
        obj.float()
    if key_handler[key.LEFT]:
#        clock.schedule_once(next_player, 1)
        next_player()
        for obj in game_objects:
            print("player and spot = ", obj.__class__, obj.spot)

def next_player(): #pass 'dt' if using a clock method
    """Next player's turn. Returns None."""
    player_leaving = game_objects[0]
    rotate_player_list() #works
    leave_ready_position(player_leaving) #works
    move_player_lineup()

def rotate_player_list():
    """Rotates contents of players list to the left by one. Returns None."""
    print("game_objects = ", game_objects)
    temp_player = game_objects[0]
    game_objects.remove(temp_player)
    game_objects.append(temp_player)
    print("game_objects = ", game_objects)

def leave_ready_position(player_leaving):
    """Moves the player from the ready position. Returns None."""
    objects.Player.leave_ready_position(player_leaving)
    print("player_spots_occupied = ", util.Line.player_spots_occupied)

def move_player_lineup():
    """Every player moves up one in the lineup. Returns None."""
    print("move_player_lineup()")

if __name__ == "__main__":
    pyglet.clock.schedule_interval(update, 1/30)
    pyglet.app.run()
