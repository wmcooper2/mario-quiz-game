import math
import pyglet
import random
from constants import *

def center_image(image):
    """Centers the anchor point in the image."""
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2

def center_floating_player(image):
    """Centers the anchor point in the image."""
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2

def center_walking_player(image):
    """Centers the anchor point in the image."""
    image.anchor_x = image.width // 2

def center_ground_sprite(obj):
    obj.anchor_x = obj.width // 2
    obj.anchor_y = 0

def falling_object(time):
    """Calculates y position of falling object. Returns Integer."""
    #calculates "-(1/2) * g * t^2" where g == 9.8 and time is the accumulated time for falling
    #changed gravity to 6 from 9.8
    return math.floor(-(0.5 * 6) * (time ** 2))

class Line():

    top_row_spots = []
    inventory_spot = []
    player_spots = []           #filled by Line.line_up() 
    item_spots = []             #filled by Line.item_line_up()
    score_spots = []            #the foundational x-coordinate of the score-objects
    score_spot_y = 530
#    top_row_coins = []          #relative to the score-position
#    bottom_row_coins = []       #relative to the score-position

    mixing_player_spots = False

    def __init__(self, num_players = 0, screen_w = 0, num_items = 0, *args, **kwargs):
        self.num_players = num_players
        self.screen_w = screen_w
        self.num_items = num_items

    def top_row_line_up(self):
        """Sets the positions of the top row on the screen (scores and item inventory). Returns None."""
        for spot in range(7):
            self.top_row_spots.append((self.screen_w // 8) * spot + 125) 
        if self.num_players >= 4:
            self.inventory_spot.append(self.top_row_spots[3])
        self.score_spots = self.top_row_spots[0:3] + self.top_row_spots[4:8] 

#    def coins_line_up(self):
#        """Sets the positions of the coins respresenting player score. Returns None."""

    def line_up(self):
        """Sets the available player positions on the screen.
            Returns None."""
        for place in range(self.num_players):
            if len(self.player_spots) == 0:
                first_spot = (self.screen_w // 2) - 150
                self.player_spots.append(first_spot)
            else:
                next_spot = (self.screen_w // 2) - 150 + (100 * place)
                self.player_spots.append(next_spot)

    def item_line_up(self, items):
        """Sets the available item positions on the screen.
            Returns None."""
        for item in range(self.num_items):
            if len(self.item_spots) == 0:
                first_spot = (self.screen_w // 2) - 216
                self.item_spots.append(first_spot)
            else:
                next_spot = (self.screen_w // 2) - 216 - (24 * item) 
                self.item_spots.append(next_spot)

    def falling(self):
        """Calculates y_position of falling item. Returns Integer."""
        pass
        
        time += timestep;
        position += timestep * (velocity + timestep * acceleration / 2);
        velocity += timestep * acceleration;
    
