import pyglet
from math import sin, radians
from player import Player


class FloatingPlayer(Player):
    def __init__(self, img, go_right_img, go_left_img, *args, **kwargs):
        # super().__init__(*args, **kwargs)
        super().__init__(img, go_right_img, go_left_img, *args, **kwargs)
        self.float_deg = 0
        self.float_height = 0
        self.float_speed = 3

    def _center_floater(self, image):
        """Centers the anchor point in the image."""
        image.anchor_x = image.width // 2
        image.anchor_y = image.height // 2

    def _float(self):
        """Updates the character's float data. Returns None."""
        degrees = self.float_deg
        self.float_height = sin(radians(degrees))
        if degrees >= 359:  # reset float cycle
            self.float_deg = 0
            self.float_height = 0
        self.float_deg += 1
        self.y = self.y+(self.float_height/self.float_speed)

    def update(self):
        self._float()
        super().update()
