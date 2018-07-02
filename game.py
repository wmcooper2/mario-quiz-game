import util
import pyglet
import random
import objects
import problems
import items #must come after objects (resource mod is defined in objects... move to main?)
from pyglet.window import key
from pyglet import clock

#game_window
game_window = pyglet.window.Window(1000,563) #16:9 screen

#key_handler
key_handler = key.KeyStateHandler()
#keys = dict(left=False)
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

#setup item containers
game_items = []
falling_item = []
item_choices = [    "green mushroom", 
                    "red mushroom", 
                    "pow button", 
                    "yoshi coin", 
                    "spiny beetle", 
                    "pirahna plant",]

def new_item():
    """Adds new item to game_items. Returns None."""
    item = random.choice(item_choices)
    if item == "green mushroom": 
        item = (items.GreenMushroom(img = items.GreenMushroom.stand_right_anim, x = OFF_SCREEN_L, y = ITEM_PLATFORM_H, batch = main_batch))
    if item == "red mushroom": 
        item = (items.RedMushroom(img = items.RedMushroom.stand_right_anim, x = OFF_SCREEN_L, y = ITEM_PLATFORM_H, batch = main_batch))
    if item == "pow button": 
        item = (items.PowButton(img = items.PowButton.stand_right_anim, x = OFF_SCREEN_L, y = ITEM_PLATFORM_H, batch = main_batch))
    if item == "yoshi coin": 
        item = (items.YoshiCoin(img = items.YoshiCoin.stand_right_anim, x = OFF_SCREEN_L, y = ITEM_PLATFORM_H, batch = main_batch))
    if item == "spiny beetle": 
        item = (items.SpinyBeetle(img = items.SpinyBeetle.walk_right_anim, x = OFF_SCREEN_L, y = ITEM_PLATFORM_H, batch = main_batch))
    if item == "pirahna plant":
        item = (items.PirahnaPlant(img = items.PirahnaPlant.stand_right_anim, x = OFF_SCREEN_L, y = ITEM_PLATFORM_H, batch = main_batch))
    item.scale = 1.5
    game_items.append(item)

#initial loading of items to game_items
for item in range(NUM_ITEMS):
    new_item()

#line up the items
item_spots = util.Line(screen_w = SCREEN_W, num_items = NUM_ITEMS)
item_spots.item_line_up(game_items)

@game_window.event
def on_draw():
    game_window.clear()
    main_batch.draw()
    
    #show the problem
    if game_objects[0].item and game_objects[0].inventory[0].problem.showing_black_box:
        problems.Problem.vocab_black_box.draw()
        game_objects[0].inventory[0].problem.question.draw()

def update(dt):
    """Game update loop. Returns None."""
    for player in game_objects:         #update players 
        player.spot = util.Line.player_spots[game_objects.index(player)]
        player.update(dt)

        #player automatically uses item
        if player.has_item() and game_objects[0].inventory[0].problem.showing_black_box == False: 
            player.use_item()           #Player.item = True, Problem.showing_black_box = True
    for player in floating_players:
        player.float()
    for item in game_items:             #update items 
        item.spot_x = util.Line.item_spots[game_items.index(item)]
        item.update(dt)
    yammy.update()                      #animate yammy, give items automatically 
    if yammy.inventory:                 #only if len() > 0
        for obj in yammy.inventory:
            obj.update(dt)
            obj.transition() 

    #fade yammy in and out
    if key_handler[key.F] and not player_movement() and not yammy.transitioning:
        yammy.transitioning = True
        yammy.toggle_transition_direction()
    
    #player gets one item
    if key_handler[key._1] and not any_movement(): 
        yammys_item = game_items[0]
        yammy.wave_wand()
        yammy.take_item(yammys_item)
        game_items.remove(yammys_item)
        yammys_item.spot_y = 400            #make the item rise
        yammys_item.transitioning = True    #make item disappear
        new_item()                          #add new item to lineup

        #player in the ready position is set up to receive the item
        #item automatically given, part of Yammy.update()
        yammy.victim = game_objects[0] #victim is player in ready position

    #manually rotate the players left
    if key_handler[key.LEFT] and not player_movement():
        #rotate players left one
        rotate_players_left()

    if key_handler[key.RIGHT] and not player_movement():
        rotate_players_right()

    if key_handler[key.UP] and not player_movement():
        #randomly mix players
        mix_players()

    if key_handler[key.O] and game_objects[0].item and game_objects[0].inventory[0].problem.showing_black_box:
        #right answer, one point given
        right_answer()
        item_sequence()

    if key_handler[key.X] and game_objects[0].item and game_objects[0].inventory[0].problem.showing_black_box:
        #wrong answer, no points given, no points taken
        item_sequence()

    if key_handler[key.A] and not item_movement():
        #rotates the items left (screen)
        rotate_items_left()

    if key_handler[key.D] and not item_movement():
        #rotates the items right (screen)
        rotate_items_right()

    if key_handler[key.S] and not item_movement():
        #randomly mix the items (screen)
        mix_items()

def right_answer():
    """Gives the player in the ready position a point. Returns None."""
    game_objects[0].points += 1

def item_sequence():
    players_item = game_objects[0].inventory[0]
    problems.Problem.showing_black_box = False              #reset flag, stop showing box
    game_objects[0].item = False
    game_objects[0].inventory.remove(players_item)
    players_item.delete()
    for player in game_objects:
        print(player.__class__, " has ", player.points, " points.")

def yammy_take_item(obj):
    """Item is taken by Yammy from the platform. Returns None."""
    yammys_item = game_items[0]
    yammy.inventory.append(yammys_item)
    game_items.remove(yammys_item)
    yammy.inventory[0].spot_y = ITEM_DISAPPEAR_H
    yammy.inventory[0].toggle_transition_direction()

def any_movement():
    """Checks if anything is moving. Returns Boolean."""
    movement = []
    for obj in game_objects: 
        movement.append(obj.moving)
    for obj in game_items: 
        movement.append(obj.moving)
    if yammy.inventory:
        for obj in yammy.inventory: 
            movement.append(obj.moving)
    return any(movement)

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

def rotate_items_left():
    """Rotates contents of items list to the right by one. Returns None."""         #reverse order from what appears on screen
    temp_item = game_items[-1]
    game_items.remove(temp_item)
    game_items.insert(0, temp_item)

def rotate_items_right():
    """Rotates contents of the items list to left the by one. Returns None."""      #reverse order from what appears on screen
    temp_item = game_items[0]
    game_items.remove(temp_item)
    game_items.append(temp_item) 

def mix_items():
    """Randomly mixes the items in the line. Returns None."""
    global game_items
    mixed_items = []
    copy = game_items[:]
    for x in game_items:
        item_choice = random.choice(copy)
        mixed_items.append(item_choice)
        copy.remove(item_choice)
    game_items = mixed_items[:]
    
def rotate_players_left(): 
    """Rotates contents of players list to the left by one. Returns None."""
    temp_player = game_objects[0]
    game_objects.remove(temp_player)
    game_objects.append(temp_player)

def rotate_players_right():
    """Rotates contents of players list to the right by one. Returns None."""
    temp_player = game_objects[-1]
    game_objects.remove(temp_player)
    game_objects.insert(0, temp_player)

def reverse_rotate_player_list():
    """Rotates contents of players list to the right by one. Returns None."""
    temp_player = game_objects[-1]
    game_objects.remove(temp_player)
    game_objects.insert(0, temp_player)
    
def mix_players():
    """Randomly mixes the players in the line. Returns None."""
    global game_objects
    mixed_players = []
    copy = game_objects[:]
    for x in game_objects:
        player_choice = random.choice(copy)
        mixed_players.append(player_choice)
        copy.remove(player_choice)
    game_objects = mixed_players[:]

if __name__ == "__main__":
    pyglet.clock.schedule_interval(update, 1/120)
    pyglet.app.run()

