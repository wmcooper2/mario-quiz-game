import pyglet


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

class Line():

    spots = []    
    spots_avail = []


    def __init__(self, num_players = 0, screen_w = 0, *args, **kwargs):
        self.num_players = num_players
        self.screen_w = screen_w

    def line_up(self):
        """Sets the available positions on the screen.
            Returns None."""
        for place in range(self.num_players):
            if len(self.spots) == 0:
                first_spot = (self.screen_w // 2) - 100
                self.spots.append(first_spot)
            else:
                next_spot = (self.screen_w // 2) + (90 * place)
                self.spots.append(next_spot)
        for place in self.spots:
            self.spots_avail.append(True)

        print("initial spots = ", self.spots)
        print("initial spots_avail = ", self.spots_avail)
