# stand lib
from math import sin, radians
from typing import List

# 3rd party
import pyglet


class Player(pyglet.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.inventory = []
        self.points = 0
        self.point_index = 0
        self.spot = self.x  # starts off screen, right
        # self._pos_delta = lambda: self.x - self.spot
        self.pygresimg = pyglet.resource.image
        self.pygrid = pyglet.image.ImageGrid
        self.pyganim = pyglet.image.Animation.from_image_sequence

    def _pos_delta(self):
        """Return the difference between the players current x-pos and where it's going.
            Example:
                self.spot = 100     # where it's going.
                self.x = 50         # where it is
                return 50 - 100     # -50

            Notes:
                a negative return value means that the player is to the left of where it is going and thus will move to the right until it reaches it's spot.
        """
        return self.x - self.spot

    def _update_img(self) -> None:
        """Changes sprite's image depending on which direction it is going. Returns None.
            Example:
                if self._pos_delta() > 0: then the character will face left
                if self._pos_delta() < 0: then the character will face right
                if self._pos_delta() == 0: then the character will face left (facing yammy, the default direction)
        """
        diff = self._pos_delta()
        if diff > 0:
            self.image = self.act_anim_left
        elif diff < 0:
            self.image = self.act_anim_right
        elif diff == 0:
            if isinstance(self, FireLight):
                self.image = self.act_anim_left
            else:
                self.image = self.act_anim_left

    def _update_pos(self) -> None:
        """Shifts the player's image horizontally. Returns None.
            Example:
                if self._pos_delta() > 0: then the character will move left
                if self._pos_delta() < 0: then the character will move right
        """
        diff = self._pos_delta()
        if diff > 0 and diff > 3:
            self.x -= 3
        elif diff > 0 and diff <= 3:
            self.x -= 1
        elif diff < 0 and abs(diff) > 3:
            self.x += 3
        elif diff < 0 and abs(diff) <= 3:
            self.x += 1

    def take(self):
        """Sets player's item to player's pos. Returns None."""
        if self.inventory:
            self.inventory[0].y = self.height//2

    def update(self):
        self._update_img()
        self._update_pos()
        # self.take()


class FloatingPlayer(Player):
    def __init__(self, float_speed=3, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.float_height = 0
        self.float_deg = 0
        self.float_speed = float_speed

    def float(self):
        """Updates the character's float data. Returns None."""
        degrees = self.float_deg
        self.float_height = sin(radians(degrees))
        if degrees >= 359:  # reset float cycle
            self.float_deg = 0
            self.float_height = 0
        self.float_deg += 1
        self.y = self.y+(self.float_height/self.float_speed)

    def _center_floater(self, image):
        """Centers the anchor point in the image."""
        image.anchor_x = image.width // 2
        image.anchor_y = image.height // 2

    def update(self):
        super().update()
        self.float()
        # self.move_character()
        # self.take()


class WalkingPlayer(Player):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def center_walker(self, image):
        """Centers the anchor point in the image."""
        image.anchor_x = image.width // 2





# class GreenKoopa(WalkingPlayer):
    # face_right, act_seq_right, act_anim_right = self._sprite_setup(
    # "greenkoopagoright.png", 0.1, 2, "walk")
    # face_left, act_seq_left, act_anim_left = self._sprite_setup(
    # "greenkoopagoleft.png", 0.1, 2, "walk")
    # def __init__(self, *args, **kwargs):
    # super().__init__(*args, **kwargs)


# class Luigi(WalkingPlayer):
    # face_right, act_seq_right, act_anim_right = self._sprite_setup(
    # "bigluigigoright.png", 0.1, 2, "walk")
    # face_left, act_seq_left, act_anim_left = self._sprite_setup(
    # "bigluigigoleft.png", 0.1, 2, "walk")
    # def __init__(self, *args, **kwargs):
    # super().__init__(*args, **kwargs)


# class Mario(WalkingPlayer):
    # face_right, act_seq_right, act_anim_right = self._sprite_setup(
    # "bigmariogoright.png", 0.1, 3, "walk")
    # face_left, act_seq_left, act_anim_left = self._sprite_setup(
    # "bigmariogoleft.png", 0.1, 3, "walk")
    # def __init__(self, *args, **kwargs):
    # super().__init__(*args, **kwargs)



# def walking(char):
    # """Generic walking character constructor. Returns Player object."""
    # return char(img=char.act_anim_left, x=OFF_SCREEN_RIGHT, y=WALK_HEIGHT,
        # batch=MAIN)


def greenKoopa():
    char = walking(GreenKoopa)
    char.scale = 2
    return char



def mario():
    char = walking(Mario)
    char.scale = 2
    return char


def luigi():
    char = walking(Luigi)
    char.scale = 2
    return char
