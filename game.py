import util
import pyglet
import random
import objects
import items #must come after objects (resource mod is defined in objects... move to main?)
from pyglet.window import key
from pyglet import clock

DEBUG = False
if DEBUG == True:
    #set debug in all classes to True
    objects.Player.debug = True
    items.Item.debug = True

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
OFF_SCREEN_L = -100
FLOAT_H = 100
WALK_H = 63
ITEM_PLATFORM_H = 264
ITEM_PLATFORM_W = 300
ITEM_DISAPPEAR_H = 350
#determine number of players (replace with return val from menu screen)
NUM_PLAYERS = 6
NUM_ITEMS = 6

#create the spots for player positions on the screen
player_spots = util.Line(screen_w = SCREEN_W, num_players=NUM_PLAYERS)
player_spots.line_up()

#setup player containers 
game_objects = [] #all players are added in randomize_players()
floating_players = []
walking_players = []
players = [] #for now, contents are similar to game_objects
main_batch = pyglet.graphics.Batch()

#background
background = objects.Background(img = objects.Background.background_img, batch = main_batch)

#yammy (not a playing character)
yammy = objects.Yammy(img = objects.Yammy.stand_right, x = 30, y = ITEM_PLATFORM_H, batch = main_batch)
yammy.scale = 2
yammy.opacity = 0

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

#setup item containers
game_items = []
falling_item = []

#setup item sprites
green_mushroom = items.GreenMushroom(img = items.GreenMushroom.stand_right_anim, x = OFF_SCREEN_L, y = ITEM_PLATFORM_H, batch = main_batch)
green_mushroom.scale = 1.5
game_items.append(green_mushroom)

red_mushroom = items.RedMushroom(img = items.RedMushroom.stand_right_anim, x = OFF_SCREEN_L, y = ITEM_PLATFORM_H, batch = main_batch)
red_mushroom.scale = 1.5
game_items.append(red_mushroom)

pow_button = items.PowButton(img = items.PowButton.stand_right_anim, x = OFF_SCREEN_L, y = ITEM_PLATFORM_H, batch = main_batch)
pow_button.scale = 1.5
game_items.append(pow_button) 

yoshi_coin = items.YoshiCoin(img = items.YoshiCoin.stand_right_anim, x = OFF_SCREEN_L, y = ITEM_PLATFORM_H, batch = main_batch)
yoshi_coin.scale = 1.5
game_items.append(yoshi_coin) 

spiny_beetle = items.SpinyBeetle(img = items.SpinyBeetle.walk_right_anim, x = OFF_SCREEN_L, y = ITEM_PLATFORM_H, batch = main_batch)
spiny_beetle.scale = 1.5
game_items.append(spiny_beetle) 

pirahna_plant = items.PirahnaPlant(img = items.PirahnaPlant.stand_right_anim, x = OFF_SCREEN_L, y = ITEM_PLATFORM_H, batch = main_batch)
pirahna_plant.scale = 1.5
game_items.append(pirahna_plant) 

#line up the items
item_spots = util.Line(screen_w = SCREEN_W, num_items = NUM_ITEMS)
item_spots.item_line_up(game_items)

print(game_items)
print(players)

@game_window.event
def on_draw():
    game_window.clear()
    main_batch.draw()
    if DEBUG == True:
        for obj in game_objects:
            obj.debug_xpos.draw()

def update(dt):
    """Game update loop. Returns None."""

    #players update
    for obj in game_objects:
        #give the players a spot
        obj.spot = util.Line.player_spots[game_objects.index(obj)]
        obj.update(dt)
    for obj in floating_players:
        obj.float()
    #items update
    for obj in game_items:
        obj.spot_x = util.Line.item_spots[game_items.index(obj)]
        obj.update(dt)

    #yammy animation
    yammy.update()
    if yammy.inventory: #only if len() > 0
        for obj in yammy.inventory:
            obj.update(dt)
            obj.transition() 
    if key_handler[key.F] and not player_movement() and not yammy.transitioning:
        yammy.transitioning = True
        yammy.toggle_transition_direction()
    
    if key_handler[key._1] and not player_movement() and not item_movement():
        #player gets one item
        print("give one item")
        yammy_take_item(game_objects[0])
        yammy.inventory[0].transitioning = True
        yammy.inventory[0].toggle_transition_direction()

#    if key_handler[key._2] and not player_movement():
#        #player gets two items
#        print("give two items")
#        for x in range(2):
#            yammys_item = game_items[0]
#            yammy.inventory.append(yammys_item)
#            game_items.remove(yammys_item)
#        yammy.yammy_take_item()

    if key_handler[key.LEFT] and not player_movement():
        #rotate players left one
        next_player()
        print("next_player(), lineup = ", game_objects)

    if key_handler[key.UP] and not player_movement():
        #randomly mix players
        mix_players()
        print("mix_players(), lineup = ", game_objects)

def yammy_take_item(obj):
    """Item is taken by Yammy from the platform. Returns None."""
    print("game_items = ", game_items)
    yammys_item = game_items[0]
    yammy.inventory.append(yammys_item)
    game_items.remove(yammys_item)
    yammy.inventory[0].spot_y = ITEM_DISAPPEAR_H

def player_movement():
    """Checks if any player is moving. Returns Boolean."""
    movement = []
    for obj in game_objects: 
        movement.append(obj.moving)
    return any(movement)

def item_movement():
    """Checks if any item is moving. Return Boolean."""
    movement = []
    for obj in game_items: 
        movement.append(obj.moving)
    if yammy.inventory:
        for obj in yammy.inventory:
            movement.append(obj.moving)
    return any(movement)
    
def next_player(): 
    """Gets the next player into the ready position. Returns None."""
    player_leaving = game_objects[0]
    rotate_player_list() 

def rotate_player_list():
    """Rotates contents of players list to the left by one. Returns None."""
    temp_player = game_objects[0]
    game_objects.remove(temp_player)
    game_objects.append(temp_player)

def mix_players():
    """Mixes the players in the line. Returns None."""
    global game_objects
    mixed_players = []
    copy = game_objects[:]
    for x in game_objects:
        player_choice = random.choice(copy)
        mixed_players.append(player_choice)
        copy.remove(player_choice)
    game_objects = mixed_players[:]

def randomize_players():
    """Randomizes the starting order of the player line up. Returns None."""
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

if __name__ == "__main__":
    pyglet.clock.schedule_interval(update, 1/120)
    pyglet.app.run()

