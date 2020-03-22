# stand lib
import copy
import random
from typing import Any, List

# 3rd party
import pyglet


def randomize_players(players: List[Any]) -> List[Any]:
    """Randomizes starting order of player. Returns None."""
    new_order = []
    lineup = players.copy()
    for player in range(len(players)):
        choice = random.choice(lineup)
        new_order.append(choice)
        lineup.remove(choice)
    return new_order


def any_movement(items, players, yammy):
    """Checks if anything is moving. Returns Boolean."""
    movement = []
    [movement.append(player.delta()) for player in players]
    [movement.append(item.deltax()) for item in items]
    [movement.append(item.deltay()) for item in items]
    return any(movement)


def player_movement(players):
    """True if any player is moving. Returns Boolean."""
    movement = []
    [movement.append(player.delta()) for player in players]
    return any(movement)


def item_movement(items, yammy):
    """True if any item is moving. Return Boolean."""
    movement = []
    [movement.append(item.deltax()) for item in items]
    [movement.append(item.deltay()) for item in items]
    # syntax bug?
#    [movement.append(yammy.inventory[0].moving) if yammy.inventory]
    return any(movement)


def item_clean_up(players, black_box):
    """Performs item clean up. Returns None."""
    player = players[0]
    item = player.inventory[0]
    player.inventory.remove(item)  # remove inventory
    item.delete()  # dont need?
#    player.item     = False             #reset flag
    black_box = False  # reset flag

    # show points in terminal
    if DEBUG:
        for p in pp:
            print(p.__class__, " has ", p.points, " points.")
            print("point_index = ", p.point_index)


def rotate_items_left(items):
    """Rotates items to left by one. Returns None."""
    items.insert(0, items.pop())


def rotate_items_right(items):
    """Rotates items to right by one. Returns None."""
    items.append(items.pop(0))


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
    players.append(players.pop(0))


def rotate_players_right(players):
    """Rotates players to right by one. Returns None."""
    players.insert(0, players.pop())


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


def gravity(time):
    """Calculates y position of falling object. Returns Integer."""
    # calculates "-(1/2) * g * t^2" where g == 9.8
    # + and time is the accumulated time for falling.
    g = gravity = 5
    return math.floor(-(0.5 * g) * (time ** 2))


def score_positions():
    """Sets top row positions on screen. Returns None."""
    for spot in range(7):
        TOP_ROW_SPOTS.append((SCREEN_WIDTH // 8) * spot + 125)
    if NUM_PLAYERS >= 4:
        INVENTORY_SPOT.append(TOP_ROW_SPOTS[3])

    # quick patch
    for element in TOP_ROW_SPOTS[0:3]:
        SCORE_SPOTS.append(element)
    for element in TOP_ROW_SPOTS[4:8]:
        SCORE_SPOTS.append(element)


def calculate_player_starting_pos(players: List[Any], screen_w: int) -> List[int]:
    """Calculates available player 'x' spots on screen. Returns List of positions."""
    player_screen_positions = []
    for index in range(len(players)):
        if len(player_screen_positions) == 0:
            first_position = (screen_w // 2)-150
            player_screen_positions.append(first_position)
        else:
            next_position = (screen_w // 2)-150+(100*index)
            player_screen_positions.append(next_position)
    return player_screen_positions


def item_positions(items):
    """Sets available item spots on screen. Returns None."""
    for item in range(NUM_ITEMS):
        if len(ITEM_SPOTS) == 0:
            first_spot = (SCREEN_WIDTH // 2)-ITEM_START_LEFT
            ITEM_SPOTS.append(first_spot)
        else:
            next_spot = (SCREEN_WIDTH // 2)-ITEM_START_LEFT-(24*item)
            ITEM_SPOTS.append(next_spot)
