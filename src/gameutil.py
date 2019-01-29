#stand lib
import random

#3rd party

#custom
from src.constants import *

def debug_message(str1, str2):
    """Prints a debug message to Terminal. Returns None."""
    print(str1, str2)

def image_res():
    """Gets Pyglet image resources. Returns 3 Functions."""
    pygresimg   = pyglet.resource.image
    pygrid      = pyglet.image.ImageGrid
    pyganim     = pyglet.image.Animation.from_image_sequence
    return pygresimg, pygrid, pyganim

#random player selection assumes players dont make character choices.
def randomize_players(flag, player_lineup, players_in_play, numplayers):
    """Randomizes starting order of player. Returns None."""
    if not flag:
        flag = True                             #set flag
        random_players = []
        copy = player_lineup[:]
        for x in range(numplayers):
            player_choice = random.choice(copy)
            random_players.append(player_choice)
            copy.remove(player_choice)
        for player in random_players:
            players_in_play.append(player)
        del random_players                      #clean up
        del copy                                #clean up

#dont change this, creates a weird bug if you do.
def any_movement(items, players, yammy): 
    """Checks if anything is moving. Returns Boolean."""
    movement = []
    for player in players:
        movement.append(player.moving)
    for item in items:
        movement.append(item.moving)
    if yammy.inventory:
        movement.append(yammy.inventory[0].moving)
    return any(movement)

def player_movement(players):
    """Checks if any player is moving. Returns Boolean."""
    movement = []
    for player in players:
        movement.append(player.moving)
    return any(movement)

def item_movement(items, yammy):
    """Checks if any item is moving. Return Boolean."""
    movement = []
    for item in items:
        movement.append(item.moving)
    if yammy.inventory:
        movement.append(yammy.inventory[0].moving)
    return any(movement)

def item_clean_up(players, black_box):
    """Performs item clean up. Returns None."""
    ready_p = players[0]
    p_item = ready_p.inventory[0]
    ready_p.inventory.remove(p_item)   #remove inventory
    p_item.delete()
    ready_p.item = False    #reset flag
    black_box = False       #reset flag

    #show points in terminal 
    if DEBUG:
        for p in pp:
            print(p.__class__, " has ", p.points, " points.")
            print("point_index = ", p.point_index)

def rotate_items_left(items):
    """Rotates items to left by one. Returns None."""
    temp_item = items[-1]
    items.remove(temp_item)
    items.insert(0, temp_item)

def rotate_items_right(items):
    """Rotates items to right by one. Returns None."""
    temp_item = items[0]
    items.remove(temp_item)
    items.append(temp_item)

def mix_items(items):
    """Randomly mixes items on screen. Returns None."""
    mixed_items = []
    copy = items[:]
    for x in items:
        item_choice = random.choice(copy)
        mixed_items.append(item_choice)
        copy.remove(item_choice)
    items = mixed_items[:]

def rotate_players_left(players):
    """Rotates players to left by one. Returns None."""
    temp_player = players[0]
    players.remove(temp_player)
    players.append(temp_player)

def rotate_players_right(players):
    """Rotates players to right by one. Returns None."""
    temp_player = players[-1]
    players.remove(temp_player)
    players.insert(0, temp_player)

def mix_players(players):
    """Randomly mixes the players in the line. Returns None."""
    mixed_players = []
    copy = players[:]
    for x in players:
        player_choice = random.choice(copy)
        mixed_players.append(player_choice)
        copy.remove(player_choice)
    players = mixed_players[:]

def center_image(image):
    """Centers the anchor point in the image."""
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2

def center_floater(image):
    """Centers the anchor point in the image."""
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2

def center_walker(image):
    """Centers the anchor point in the image."""
    image.anchor_x = image.width // 2

def falling_item(time):
    """Calculates y position of falling object. Returns Integer."""
    #calculates "-(1/2) * g * t^2" where g == 9.8 
    #+ and time is the accumulated time for falling.
    g = gravity = 5
    return math.floor(-(0.5 * g) * (time ** 2))

def top_row_line_up():
    """Sets top row positions on screen. Returns None."""
    for spot in range(7):
        TOP_ROW_SPOTS.append((SCREEN_WIDTH // 8) * spot + 125)
    if NUM_PLAYERS >= 4:
        INVENTORY_SPOT.append(TOP_ROW_SPOTS[3])

    #quick patch
    for element in TOP_ROW_SPOTS[0:3]:
        SCORE_SPOTS.append(element)
    for element in TOP_ROW_SPOTS[4:8]:
        SCORE_SPOTS.append(element)

def player_line_up():
    """Sets available player spots on screen. Returns None."""
    for place in range(NUM_PLAYERS):
        if len(PLAYER_SPOTS) == 0:
            first_spot = (SCREEN_WIDTH // 2) - 150
            PLAYER_SPOTS.append(first_spot)
        else:
            next_spot = (SCREEN_WIDTH // 2) - 150 + (100 * place)
            PLAYER_SPOTS.append(next_spot)

def item_line_up(items):
    """Sets available item spots on screen. Returns None."""
    for item in range(NUM_ITEMS):
        if len(ITEM_SPOTS) == 0:
            first_spot = (SCREEN_WIDTH // 2) - ITEM_START_LEFT
            ITEM_SPOTS.append(first_spot)
        else:
            next_spot = (SCREEN_WIDTH // 2) - ITEM_START_LEFT - (24 * item)
            ITEM_SPOTS.append(next_spot)
