import util
import pyglet
import random
import objects
import problems
#import builtins
import items #must come after objects (resource mod is defined in objects... move to main?)
from pyglet.window import key
from pyglet import clock

#important stuff
game_window = pyglet.window.Window(1000,563) #16:9 screen
main_batch = pyglet.graphics.Batch()
key_handler = key.KeyStateHandler()
game_window.push_handlers(key_handler)

#constants
SCREEN_W = game_window.width
SCREEN_H = game_window.height
OFF_SCREEN_R = 1100
OFF_SCREEN_L = -100 #not used
FLOAT_H = 100
WALK_H = 63
ITEM_PLATFORM_H = 264
ITEM_PLATFORM_W = 300
ITEM_DISAPPEAR_H = 300
NUM_PLAYERS = 6 # (replace with return val from menu screen)
NUM_ITEMS = 6

#setup player containers 
all_players = [] #global #players added in randomize_players()
floating_players = []
walking_players = []
players = [] #temp holder for sprite creation

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

#add luigi, peach 

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
            all_players.append(player) 
randomize_players()

#setup item containers
all_items = [] #global
falling_item = []
item_choices = [    "green mushroom", 
                    "red mushroom", 
                    "pow button", 
                    "yoshi coin", 
                    "spiny beetle", 
                    "pirahna plant",
                    "bombomb",]

def new_item():
    """Adds new item to all_items. Returns None."""
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
    if item == "bombomb":
        item = (items.Bombomb(img = items.Bombomb.stand_right_anim, x = OFF_SCREEN_L, y = ITEM_PLATFORM_H, batch = main_batch))
    item.scale = 1.5
    all_items.append(item)

#initial loading of items to all_items
for item in range(NUM_ITEMS):
    new_item()

#create the spots for player positions on the screen
player_spots = util.Line(screen_w = SCREEN_W, num_players=NUM_PLAYERS)
player_spots.line_up()

#line up the items
item_spots = util.Line(screen_w = SCREEN_W, num_items = NUM_ITEMS)
item_spots.item_line_up(all_items)

#debug
print("player spots = ", player_spots.player_spots)
print("item spots = ", item_spots.item_spots)

@game_window.event
def on_draw():
    game_window.clear()
    main_batch.draw()
   
    player = all_players[0]

 
    #show the problem
    if problems.showing_black_box: 
        problems.Problem.vocab_black_box.draw()#mixing the different ways methods from different classes are called...           
        all_players[0].inventory[0].problem.question.draw() #change so that it doesnt go through the item instance, but goes directly to the class attribute


        #question guides
        if player.has_item() and problems.showing_black_box: 
            players_item = player.inventory[0]
            if isinstance(players_item, items.RedMushroom):
                problems.Problem.english_vocab_guide.draw()
            if isinstance(players_item, items.PirahnaPlant):
                problems.Problem.japanese_vocab_guide.draw() #same for japanese to english translation, for now.
            if isinstance(players_item, items.YoshiCoin):
                problems.Problem.pronunciation_guide.draw()

def update(dt):
    """Game update loop. Returns None."""
    #non-question effects go below this comment.
    if items.bombomb_effect:
        mix_items()
        items.bombomb_effect = False    #reset the flag
        item_clean_up()
    if items.pow_button_effect:
        for player in all_players:
            player.points -= 1
        items.pow_button_effect = False
        item_clean_up()

    for player in all_players:         #update players 
        player.spot = util.Line.player_spots[all_players.index(player)]
        player.update(dt)

        #player automatically uses item
        if player.has_item() and problems.showing_black_box == False: 
            players_item = all_players[0].inventory[0]
            player.use_item() 
                 
    for player in floating_players:
        player.float()

    for item in all_items:             #update items 
        item.spot_x = util.Line.item_spots[all_items.index(item)]
        item.update(dt)

    yammy.update()
    if yammy.inventory:                 #only if len() > 0
#        for item in yammy.inventory:
        yammy.inventory[0].update(dt)
        yammy.inventory[0].transition() 

    #fade yammy in and out
    if key_handler[key.F] and not player_movement() and not yammy.transitioning:
        yammy.transitioning = True
        yammy.toggle_transition_direction()
    
    #player gets one item
    if key_handler[key._1] and not any_movement(): 
        yammys_item = all_items[0]
        yammy.wave_wand()
        yammy.take_item(yammys_item)
        all_items.remove(yammys_item)
        yammys_item.spot_y = ITEM_DISAPPEAR_H            #make the item rise
        yammys_item.transitioning = True                 #make item disappear
        new_item()                                       #add new item to lineup
        yammy.victim = all_players[0]                    #victim player in ready position

    if key_handler[key.LEFT] and not player_movement():
        rotate_players_left()

    if key_handler[key.RIGHT] and not player_movement():
        rotate_players_right()

    if key_handler[key.UP] and not player_movement():
        mix_players()

    if key_handler[key.O] and all_players[0].item and problems.showing_black_box:
        #right answer, one point given
        right_answer()
        item_clean_up()

    if key_handler[key.X] and all_players[0].item and problems.showing_black_box:
        #wrong answer, no points given, no points taken
        item_clean_up()

    if key_handler[key.A] and not item_movement():
        rotate_items_left()

    if key_handler[key.D] and not item_movement():
        rotate_items_right()

    if key_handler[key.S] and not item_movement():
        mix_items()

def item_clean_up():
    """Performs item clean up. Returns None."""
    player = all_players[0]
    players_item = player.inventory[0]
    problems.showing_black_box = False                       #reset flag, stop showing box
    player.item = False                                      #reset flag
    player.inventory.remove(players_item)                    #remove the item from player's inventory
    players_item.delete()                                    #item's instance is deleted

    #show points in terminal (move to the update/draw blocks)
    for player in all_players:
        print(player.__class__, " has ", player.points, " points.")

def right_answer():
    """Gives the player in the ready position a point. Returns None."""
    all_players[0].points += 1

def any_movement(): #dont change this, creates a weird bug if you do.
    """Checks if anything is moving. Returns Boolean."""
    movement = []
    for player in all_players: 
        movement.append(player.moving)
    for item in all_items: 
        movement.append(item.moving)
    if yammy.inventory:
        movement.append(yammy.inventory[0].moving)
    return any(movement)

def player_movement():
    """Checks if any player is moving. Returns Boolean."""
    movement = []
    for player in all_players: 
        movement.append(player.moving)
    return any(movement)

def item_movement():
    """Checks if any item is moving. Return Boolean."""
    movement = []
    for item in all_items: 
        movement.append(item.moving)
    if yammy.inventory:
        movement.append(yammy.inventory[0].moving)
    return any(movement)

def rotate_items_left():
    """Rotates contents of items list to the right by one. Returns None."""         #reverse order from what appears on screen
    temp_item = all_items[-1]
    all_items.remove(temp_item)
    all_items.insert(0, temp_item)

def rotate_items_right():
    """Rotates contents of the items list to left the by one. Returns None."""      #reverse order from what appears on screen
    temp_item = all_items[0]
    all_items.remove(temp_item)
    all_items.append(temp_item) 

def mix_items():
    """Randomly mixes the items in the line. Returns None."""
    global all_items
    mixed_items = []
    copy = all_items[:]
    for x in all_items:
        item_choice = random.choice(copy)
        mixed_items.append(item_choice)
        copy.remove(item_choice)
    all_items = mixed_items[:]
    
def rotate_players_left(): 
    """Rotates contents of players list to the left by one. Returns None."""
    temp_player = all_players[0]
    all_players.remove(temp_player)
    all_players.append(temp_player)

def rotate_players_right():
    """Rotates contents of players list to the right by one. Returns None."""
    temp_player = all_players[-1]
    all_players.remove(temp_player)
    all_players.insert(0, temp_player)

def reverse_rotate_player_list():
    """Rotates contents of players list to the right by one. Returns None."""
    temp_player = all_players[-1]
    all_players.remove(temp_player)
    all_players.insert(0, temp_player)
    
def mix_players():
    """Randomly mixes the players in the line. Returns None."""
    global all_players
    mixed_players = []
    copy = all_players[:]
    for x in all_players:
        player_choice = random.choice(copy)
        mixed_players.append(player_choice)
        copy.remove(player_choice)
    all_players = mixed_players[:]

if __name__ == "__main__":
    pyglet.clock.schedule_interval(update, 1/120)
    pyglet.app.run()

