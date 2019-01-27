#stand lib
import random

#3rd party

#custom
from src.constants import *

#random player selection assumes players dont want to choose their characters.
def randomize_players(flag, player_lineup, players_in_play, numplayers):
    """Randomizes the starting order of the player line up. Returns None."""
    if not flag:
        flag = True               #set flag
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
def any_movement(): 
    """Checks if anything is moving. Returns Boolean."""
    movement = []
    for player in PLAYING_PLAYERS:
        movement.append(player.moving)
    for item in ALL_ITEMS:
        movement.append(item.moving)
    if YAMMY.inventory:
        movement.append(YAMMY.inventory[0].moving)
    return any(movement)

def player_movement():
    """Checks if any player is moving. Returns Boolean."""
    movement = []
    for player in PLAYING_PLAYERS:
        movement.append(player.moving)
    return any(movement)

def item_movement():
    """Checks if any item is moving. Return Boolean."""
    movement = []
    for item in ALL_ITEMS:
        movement.append(item.moving)
    if YAMMY.inventory:
        movement.append(YAMMY.inventory[0].moving)
    return any(movement)

def rotate_items_left():
    """Rotates items to left by one. Returns None."""
    temp_item = ALL_ITEMS[-1]
    ALL_ITEMS.remove(temp_item)
    ALL_ITEMS.insert(0, temp_item)

def rotate_items_right():
    """Rotates items to right by one. Returns None."""
    temp_item = ALL_ITEMS[0]
    ALL_ITEMS.remove(temp_item)
    ALL_ITEMS.append(temp_item)

def mix_items():
    """Randomly mixes items on screen. Returns None."""
    global ALL_ITEMS
    mixed_items = []
    copy = ALL_ITEMS[:]
    for x in ALL_ITEMS:
        item_choice = random.choice(copy)
        mixed_items.append(item_choice)
        copy.remove(item_choice)
    ALL_ITEMS = mixed_items[:]

def rotate_players_left():
    """Rotates players to left by one. Returns None."""
    temp_player = PLAYING_PLAYERS[0]
    PLAYING_PLAYERS.remove(temp_player)
    PLAYING_PLAYERS.append(temp_player)

def rotate_players_right():
    """Rotates players to right by one. Returns None."""
    temp_player = PLAYING_PLAYERS[-1]
    PLAYING_PLAYERS.remove(temp_player)
    PLAYING_PLAYERS.insert(0, temp_player)

def reverse_rotate_player_list():
    """Rotates players list to the right by one. Returns None."""
    temp_player = PLAYING_PLAYERS[-1]
    PLAYING_PLAYERS.remove(temp_player)
    PLAYING_PLAYERS.insert(0, temp_player)

def mix_players():
    """Randomly mixes the players in the line. Returns None."""
    global PLAYING_PLAYERS
    mixed_players = []
    copy = PLAYING_PLAYERS[:]
    for x in PLAYING_PLAYERS:
        player_choice = random.choice(copy)
        mixed_players.append(player_choice)
        copy.remove(player_choice)
    PLAYING_PLAYERS = mixed_players[:]
