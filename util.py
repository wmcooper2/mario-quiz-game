import pyglet
import random

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

class Line():

    player_spots = [] #filled by Line.line_up() 
    item_spots = []

    def __init__(self, num_players = 0, screen_w = 0, num_items = 0, *args, **kwargs):
        self.num_players = num_players
        self.screen_w = screen_w
        self.num_items = num_items

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
                next_spot = (self.screen_w // 2) - 216 - (24 * item) #problem with width math
                self.item_spots.append(next_spot)
        print("item_spots = ", Line.item_spots)
