import util
import pyglet
import random
import players #not needed?
import problems
import items #must come after players (resource mod is defined in players... move to main?) #not needed?
import playersetup
import playerscores
from constants import *
from itemsetup import *
from pyglet import clock

#setup player containers 
#player_order determines the players' score positions at the top, fix the order based on menu screen selections.
all_players = []            #the initial order of players hard-coded below, and the order of scores at the top.
playing_players = []        #global #players added in randomize_players(), change this order to change the players on the screen
score_display = []          #initially the same as playing_players, does not change, the player sprites at the top of the screen 
walking_players = []
floating_players = []

#background
background = players.Background(img = players.Background.background_img, batch = main_batch)

#player setup
yammy = playersetup.make_yammy()
fire_light = playersetup.make_firelight()
dragon = playersetup.make_dragon()
big_boo = playersetup.make_big_boo()
green_koopa = playersetup.make_green_koopa()
big_mole = playersetup.make_big_mole()
mario = playersetup.make_mario()
luigi = playersetup.make_luigi()

all_players.append(fire_light)
all_players.append(dragon)
all_players.append(big_boo)
all_players.append(green_koopa)
all_players.append(big_mole)
all_players.append(mario)
all_players.append(luigi)

floating_players.append(fire_light)
floating_players.append(big_boo)

walking_players.append(dragon)
walking_players.append(green_koopa)
walking_players.append(big_mole)
walking_players.append(mario)
walking_players.append(luigi)

#this random player selection assumes that the players dont want to choose their characters.
def randomize_players():
    """Randomizes the starting order of the player line up. Returns None."""
    if players.Player.randomized == False:
        players.Player.randomized = True
        random_players = []
        copy = all_players[:]
        for x in range(NUM_PLAYERS):
            player_choice = random.choice(copy)
            random_players.append(player_choice)
            copy.remove(player_choice)
        for player in random_players:
            playing_players.append(player) 
randomize_players()

#setup items 
all_items = []                  #global #new items added with new_item() and the for-loop below it. 
falling_item = []
for item in range(NUM_ITEMS):
    all_items.append(new_item())

#line setups
lines = util.Line(screen_w = SCREEN_W, num_players = NUM_PLAYERS, num_items = NUM_ITEMS)
lines.line_up()                                 #player line up
lines.item_line_up(all_items)                   #item line up
lines.top_row_line_up()                         #for scores and item at top of game_window
player_spots = lines.player_spots               #at players platform
item_spots = lines.item_spots                   #at item platform
score_spots = lines.score_spots                 #at top of game_window
inventory_spot = lines.inventory_spot           #at top center of game_window

#score setup, relies on playerscores.py
for player in playing_players:
    score_x = score_spots[playing_players.index(player)]
    score_sprite = playerscores.make_sprite(player, score_x)
    score_display.append(score_sprite) 
    player.point_index = score_display.index(score_sprite) 

@game_window.event
def on_draw():
    game_window.clear()
    main_batch.draw()
    player = playing_players[0]
    
    #show the problem
    if problems.showing_black_box: 
        problems.Problem.vocab_black_box.draw()#mixing the different ways methods from different classes are called...           
        player.inventory[0].problem.question.draw() #change so that it doesnt go through the item instance, but goes directly to the class attribute

        #question guides
        if player.has_item() and problems.showing_black_box: 
            players_item = player.inventory[0]
            if isinstance(players_item, items.RedMushroom):             #simple vocab
                problems.Problem.english_vocab_guide.draw()
            if isinstance(players_item, items.GreenMushroom):           #verbs
                problems.Problem.present_verb_guide.draw()
            if isinstance(players_item, items.PirahnaPlant):            #J -> E translation
                problems.Problem.english_sentence_guide.draw() 
            if isinstance(players_item, items.YoshiCoin):               #pronunciation
                problems.Problem.pronunciation_guide.draw()
            if isinstance(players_item, items.SpinyBeetle):             #E -> J translation
                problems.Problem.japanese_sentence_guide.draw()

    for score in score_display:
        if len(score.big_score) > 0:
#            print("len(big_score) = ", len(score.big_score))
            for thing in score.big_score:
                thing.draw()
#        elif len(score.small_score) > 0:
#            print("len(small_score) = ", len(score.small_score))
        elif score.points == 0:
            score.zero.draw()

def update(dt):
    """Game update loop. Returns None."""
    #non-question effects go below this comment.
    if items.bombomb_effect:                                            #mix items
        mix_items()
        items.bombomb_effect = False                                    #reset flag
        item_clean_up()
    if items.pow_button_effect:                                         #all, minus one point
        for player in playing_players:
            player.points -= 1
        items.pow_button_effect = False                                 #reset flag
        item_clean_up()

    ready_player = playing_players[0]
    for player in playing_players:                      #update players 
        player.spot = util.Line.player_spots[playing_players.index(player)]
        player.update(dt)

        #player automatically uses item
        if player.has_item() and problems.showing_black_box == False: 
            players_item = ready_player.inventory[0]
            player.use_item() 
   
        #update player scores 
        score_points = score_display[player.point_index].points         #the integer value
        score_object = score_display[player.point_index]                #the score object
        if player.points != score_points: 
            score_object.update(score_object, player)                   #player_score is in a different instance than player

    for player in floating_players:
        player.float()

    for item in all_items:                              #update items 
        item.spot_x = util.Line.item_spots[all_items.index(item)]
        item.update(dt)

    yammy.update()
    if yammy.inventory:                                 #only if len() > 0
        yammy.inventory[0].update(dt)
        yammy.inventory[0].transition() 

    #fade yammy in and out
    if key_handler[key.F] and not player_movement() and not yammy.transitioning:
        yammy.transitioning = True
        yammy.toggle_transition_direction()
    
    #player gets one item
    if key_handler[key._1] and not any_movement() and not problems.showing_black_box: 
        yammys_item = all_items[0]
        yammy.wave_wand()
        yammy.take_item(yammys_item)
        all_items.remove(yammys_item)
        yammys_item.spot_y = ITEM_DISAPPEAR_H            #make the item rise
        yammys_item.transitioning = True                 #make item disappear
        all_items.append(new_item())                     #add new item to lineup
        yammy.victim = ready_player                      #victim player in ready position

    if key_handler[key.LEFT] and not player_movement() and not problems.showing_black_box:
        rotate_players_left()

    if key_handler[key.RIGHT] and not player_movement() and not problems.showing_black_box:
        rotate_players_right()

    if key_handler[key.UP] and not player_movement() and not problems.showing_black_box:
        mix_players()

    if key_handler[key.O] and ready_player.item and problems.showing_black_box:
        right_answer()                                  #plus one point
        item_clean_up()

    if key_handler[key.X] and ready_player.item and problems.showing_black_box:
        wrong_answer()                                  #minus one point
        item_clean_up()

    if key_handler[key.A] and not item_movement():
        rotate_items_left()

    if key_handler[key.D] and not item_movement():
        rotate_items_right()

    if key_handler[key.S] and not item_movement():
        mix_items()

def item_clean_up():
    """Performs item clean up. Returns None."""
    player = playing_players[0]
    players_item = player.inventory[0]
    problems.showing_black_box = False                   #reset flag, stop showing box
    player.item = False                                  #reset flag
    player.inventory.remove(players_item)                #remove the item from player's inventory
    players_item.delete()                                #item's instance is deleted

    #show points in terminal (move to the update/draw blocks)
    for player in playing_players:
        print(player.__class__, " has ", player.points, " points.")
        print("point_index = ", player.point_index)

def right_answer():
    """Gives a point to the player in the ready position. Returns None."""
    playing_players[0].points += 1

def wrong_answer():
    """Takes away a point from the player in the ready position. Returns None."""
    playing_players[0].points -= 1

def any_movement(): #dont change this, creates a weird bug if you do.
    """Checks if anything is moving. Returns Boolean."""
    movement = []
    for player in playing_players: 
        movement.append(player.moving)
    for item in all_items: 
        movement.append(item.moving)
    if yammy.inventory:
        movement.append(yammy.inventory[0].moving)
    return any(movement)

def player_movement():
    """Checks if any player is moving. Returns Boolean."""
    movement = []
    for player in playing_players: 
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
    temp_player = playing_players[0]
    playing_players.remove(temp_player)
    playing_players.append(temp_player)

def rotate_players_right():
    """Rotates contents of players list to the right by one. Returns None."""
    temp_player = playing_players[-1]
    playing_players.remove(temp_player)
    playing_players.insert(0, temp_player)

def reverse_rotate_player_list():
    """Rotates contents of players list to the right by one. Returns None."""
    temp_player = playing_players[-1]
    playing_players.remove(temp_player)
    playing_players.insert(0, temp_player)
    
def mix_players():
    """Randomly mixes the players in the line. Returns None."""
    global playing_players
    mixed_players = []
    copy = playing_players[:]
    for x in playing_players:
        player_choice = random.choice(copy)
        mixed_players.append(player_choice)
        copy.remove(player_choice)
    playing_players = mixed_players[:]

if DEBUG == True:
    print("player spots = ", player_spots)
    print("item spots = ", item_spots)
    print("score_spots = ", score_spots)
    print("inventory_spot = ", inventory_spot)

if __name__ == "__main__":
    pyglet.clock.schedule_interval(update, 1/90)
    pyglet.app.run()

