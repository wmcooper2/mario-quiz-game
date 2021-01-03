#std lib
import math
from typing import Tuple

#3rd party
import pyglet

#custom
from constants import constants as c
import problems
import util as u

class Item(c.SPRITE):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #location
        self.dest_x = self.x
        self.dest_y = self.y
        self.dx = 0        
        self.dy = 0

        #speed
        self.y_speed = c.ITEM_Y_SPEED * 2
        self.x_speed = c.ITEM_X_SPEED
        self.gravity = 9.8

        #opacity
        self.disappear_rate = 4
        self.disappear = False
        self.disappear_limit = 100
        self.max_opacity = 255
        self.min_opacity = 0

        #problem
#         self.problem = problems.Problem()

        #flags
        self.special = False
        self.item_not_used = True

    def update(self, dt) -> None:
        """Item's main update."""
        self.dt = dt

        #self.x and self.y inherited
        self.dx = self.x - self.dest_x 
        self.dy = self.y - self.dest_y
        self.change_image()
        self.move() 
        self.disappear_animation()
        self.transfer_item()
 
    def apply_gravity(self, time) -> None:
        """Calculates y position of falling item.

            Calculates "-(1/2) * g * t^2" where g == 9.8
                and time is the accumulated time for falling.
            Changed gravity to 5 from 9.8

        """
        if time > 5:
            time = 0
        self.y += math.floor(-(0.5 * self.gravity) * (time ** 2))

    def change_image(self) -> None:
        """Changes the sprite's image."""
        dx = self.dx
        if dx != 0:
            if dx > 0 and self.image != self.walk_left_anim:
                self.image = self.walk_left_anim 
            elif dx < 0 and self.image != self.walk_right_anim:
                self.image = self.walk_right_anim 
        elif dx == 0 and self.image != self.stand_right_anim:
            self.image = self.stand_right_anim

    def disappear_animation(self) -> None:
        """Make item disappear/reappear."""
        #change opacity
        if self.disappear:
            self.opacity -= self.disappear_rate
        else:
            self.opacity += self.disappear_rate
        #keep opacity within limits
        if self.opacity >= self.max_opacity:
            self.opacity = self.max_opacity
        elif self.opacity <= self.min_opacity:
            self.opacity = self.min_opacity

    def is_at_disappear_limit(self) -> bool:
        """Is the item at or above self.disappear_limit?"""
        return self.y >= (c.ITEM_PLATFORM_H + self.disappear_limit)

    def is_left_of_p1(self) -> bool:
        """Is the item to the left of player 1?"""
        return self.x < c.P1.x

    def is_at_or_below_p1(self) -> bool:
#         """Is the item perfectly level with player 1?"""
        """Is item at or below player 1 on y-axis?"""
#         return self.y == c.P1.y
        return self.y <= c.P1.y

    def is_on_platform(self) -> bool:
        """Is the item on the platform?"""
        return self.y == c.ITEM_PLATFORM_H

    def is_over_p1(self) -> bool:
        """Is the item directly overhead player 1?"""
        return self.x == c.P1.x 

    def match_p1_coords(self) -> None:
        """Sets item x/y to player 1's x/y."""
        self.x, self.y = c.P1.x, c.P1.y

    def move(self) -> None: 
        """Moves the items closer to dest_x and dest_y."""
        dx, dy = self.dx, self.dy
        if dx > 0:                  # x_pos
            self.x -= self.x_speed
        elif dx < 0:
            self.x += self.x_speed

        if dy > 0:                  # y_pos
            self.y -= self.y_speed
        elif dy < 0:
            self.y += self.y_speed

        #if the object is within range of the speed "step", then just make delta == 0
        close_x, close_y = self.within_margin()
        if close_x:
            self.x = self.dest_x
        if close_y:
            self.y = self.dest_y

    def move_to_p1_x_axis(self) -> None:
        """Move item to same x axis."""
        self.x, self.dest_x = c.P1.x, c.P1.x

    def toggle_disappear(self) -> None:
        """Toggle self.disappear flag."""
        if self.opacity <= self.min_opacity or self.opacity >= self.max_opacity:
            self.disappear = not self.disappear

    def transfer_item(self) -> None:
        """The animation of giving the item to a player."""
        #if self is the item to transfer, perform animation sequence
        if self == c.ITEM:
            self.disappear_animation()  #always update animation

            #item rise and disappear
            if self.is_visible() and self.is_on_platform() and self.is_left_of_p1():
                self.dest_y = self.y + self.disappear_limit
                self.toggle_disappear()

            #item over player
            if not self.is_visible() and self.is_at_disappear_limit():
                self.opacity = self.min_opacity
                self.move_to_p1_x_axis()

            #item over player, much closer to it and appearing
            if self.is_over_p1() and self.is_at_disappear_limit():
                self.dest_y = c.P1.y

                # over shoot the dest_y to allow the floating players to grab the items
                self.y, self.dest_y = c.P1.y + self.disappear_limit, c.P1.y - c.SCREEN_H
                self.toggle_disappear()

            if self.is_at_or_below_p1() and self.is_over_p1():
                self.match_p1_coords()
                #TODO, the player must answer the question correctly in order to get the item.
                if c.P1.inventory:
                    c.P1.inventory.delete()             #remove item from game
                    c.P1.inventory = c.ITEM             #assign x to player's x
                else:
                    c.P1.inventory = c.ITEM             #assign x to player's x
                c.ITEM = None                           #remove item from constants

    def is_visible(self) -> bool:
        """Is the opacity even slightly above 0? Then it's visible."""
        return self.opacity > self.min_opacity

    def within_margin(self) -> Tuple[bool, bool]:
        """Checks if item within range of destination."""
        return (abs(self.dx) <= self.x_speed, abs(self.dy) <= self.y_speed)

class RedMushroom(Item):
    """Red Mushroom is a random English vocabulary question."""
    
    stand_left = c.IMG("redmushroom.png")
    u.center_ground_sprite(stand_left)
    stand_left_seq = c.GRID(stand_left, 1, 1)
    stand_left_anim = pyglet.image.Animation.from_image_sequence(stand_left_seq, 1, True)

    stand_right_anim = stand_left_anim
    walk_left_anim = stand_left_anim
    walk_right_anim = stand_left_anim

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def effect(self):
        """Presents a random English word. Returns None"""
        problems.showing_black_box = True
        self.problem.random_english_word()

class GreenMushroom(Item):
    """Green Mushroom is a random verb form question."""

    stand_left = c.IMG("greenmushroom.png")
    u.center_ground_sprite(stand_left)
    stand_left_seq = c.GRID(stand_left, 1, 1)
    stand_left_anim = c.ANIM(stand_left_seq, 1, True)

    stand_right_anim = stand_left_anim
    walk_left_anim = stand_left_anim
    walk_right_anim = stand_left_anim

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def effect(self):
        """Presents a verb form problem. Returns None"""
        problems.showing_black_box = True
        self.problem.random_present_verb()
        
class YoshiCoin(Item):
    """Yoshi Coin is a pronunciation question."""
    
    stand_right = c.IMG("yoshicoinright.png")
    u.center_ground_sprite(stand_right)
    stand_right_seq = c.GRID(stand_right, 1, 5)
    stand_right_anim = c.ANIM(stand_right_seq, 1, True)

    walk_left = c.IMG("yoshicoinleft.png")
    u.center_ground_sprite(walk_left)
    walk_left_seq = c.GRID(walk_left, 1, 5)
    walk_left_anim = c.ANIM(walk_left_seq, 0.1, True)

    walk_right = c.IMG("yoshicoinright.png")
    u.center_ground_sprite(walk_right)
    walk_right_seq = c.GRID(walk_right, 1, 5)
    walk_right_anim = c.ANIM(walk_right_seq, 0.1, True)

    stand_left_anim = walk_left_anim

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def effect(self):
        """Presents a pronunciation problem. Returns None"""
        problems.showing_black_box = True
        self.problem.random_pronunciation()

class PirahnaPlant(Item):
    """Pirahna Plant is a sentence translation problem (English to Japanese)."""

    stand_right = c.IMG("pirahnaplantsmall.png")
    u.center_ground_sprite(stand_right)
    stand_right_seq = c.GRID(stand_right, 1, 2)
    stand_right_anim = c.ANIM(stand_right_seq, 0.1, True)

    walk_left = c.IMG("pirahnaplantsmall.png")
    u.center_ground_sprite(walk_left)
    walk_left_seq = c.GRID(walk_left, 1, 2)
    walk_left_anim = c.ANIM(walk_left_seq, 0.1, True)

    walk_right = c.IMG("pirahnaplantsmall.png")
    u.center_ground_sprite(walk_right)
    walk_right_seq = c.GRID(walk_right, 1, 2)
    walk_right_anim = c.ANIM(walk_right_seq, 0.1, True)

    stand_left_anim = stand_right_anim

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def effect(self):
        """Presents a sentence translation problem (English to Japanese). Returns None"""
        problems.showing_black_box = True
        self.problem.random_target_sentence()

class SpinyBeetle(Item): 
    """Spiny Beetle is a question problem from 3rd year JHS at DaiKyuuChuu."""

    stand_right = c.IMG("spinybeetlestandright.png")
    u.center_ground_sprite(stand_right)
    stand_right_seq = c.GRID(stand_right, 1, 1)
    stand_right_anim = c.ANIM(stand_right_seq, 1, True)

    walk_left = c.IMG("spinybeetlewalkleft.png")
    u.center_ground_sprite(walk_left)
    walk_left_seq = c.GRID(walk_left, 1, 2)
    walk_left_anim = c.ANIM(walk_left_seq, 0.1, True)

    walk_right = c.IMG("spinybeetlewalkright.png")
    u.center_ground_sprite(walk_right)
    walk_right_seq = c.GRID(walk_right, 1, 2)
    walk_right_anim = c.ANIM(walk_right_seq, 0.1, True)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def effect(self):
        """Presents a question from yomitore, qa 100, and custom questions. Returns None"""
        problems.showing_black_box = True
        self.problem.random_question()

class PowButton(Item):
    """Pow Button takes away one point from everyone."""
        
    stand_left = c.IMG("powbutton.png")
    u.center_ground_sprite(stand_left)
    stand_left_seq = c.GRID(stand_left, 1, 1)
    stand_left_anim = c.ANIM(stand_left_seq, 1, False)

    stand_right_anim = stand_left_anim
    walk_left_anim = stand_left_anim
    walk_right_anim = stand_left_anim

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def effect(self):
        """Pow Button takes one point away from everyone. Returns None"""
#         global pow_button_effect
        c.POW_BUTTON_EFFECT = True 

class Bombomb(Item):
    """Bombomb randomly mixes the order of the items on the screen."""

    stand_right = c.IMG("bombombstandright.png")
    u.center_ground_sprite(stand_right)
    stand_right_seq = c.GRID(stand_right, 1, 1)
    stand_right_anim = c.ANIM(stand_right_seq, 1, True)

    walk_left = c.IMG("bombombwalkleft.png")
    u.center_ground_sprite(walk_left)
    walk_left_seq = c.GRID(walk_left, 1, 2)
    walk_left_anim = c.ANIM(walk_left_seq, 0.1, True)

    walk_right = c.IMG("bombombwalkright.png")
    u.center_ground_sprite(walk_right)
    walk_right_seq = c.GRID(walk_right, 1, 2)
    walk_right_anim = c.ANIM(walk_right_seq, 0.1, True)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def effect(self):
        """Randomly mix the order of items on the screen. Returns None."""
#         global bombomb_effect
        c.BOMBOMB_EFFECT = True 

class QuestionBlock(Item): #unfinished
    """Question block chooses a random effect."""

    stand_right = c.IMG("questionblock.png")
    u.center_ground_sprite(stand_right)
    stand_right_seq = c.GRID(stand_right, 1, 4)
    stand_right_anim = c.ANIM(stand_right_seq, 1, True)

    walk_left = c.IMG("questionblock.png")
    u.center_ground_sprite(walk_left)
    walk_left_seq = c.GRID(walk_left, 1, 4)
    walk_left_anim = c.ANIM(walk_left_seq, 0.1, True)

    walk_right = c.IMG("questionblock.png")
    u.center_ground_sprite(walk_right)
    walk_right_seq = c.GRID(walk_right, 1, 4)
    walk_right_anim = c.ANIM(walk_right_seq, 0.1, True)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def effect(self):
        """Choose a random effect from all of the available effects. Returns None."""
        print("question block effect")

class Feather(Item): #unfinished
    """Feather allows the player to skip their turn when the item is used."""

    stand_right = c.IMG("feather.png")
    u.center_ground_sprite(stand_right)
    stand_right_seq = c.GRID(stand_right, 1, 1)
    stand_right_anim = c.ANIM(stand_right_seq, 1, True)

    walk_left = c.IMG("feather.png")
    u.center_ground_sprite(walk_left)
    walk_left_seq = c.GRID(walk_left, 1, 1)
    walk_left_anim = c.ANIM(walk_left_seq, 0.1, True)

    walk_right = c.IMG("feather.png")
    u.center_ground_sprite(walk_right)
    walk_right_seq = c.GRID(walk_right, 1, 1)
    walk_right_anim = c.ANIM(walk_right_seq, 0.1, True)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def effect(self):
        """Allows the player to skip a turn when the item is used. Returns None."""
        FEATHER_EFFECT = True

class Star(Item): #unfinished
    """Star allows the player to avoid the negative affects of other items."""

    stand_right = c.IMG("star.png")
    u.center_ground_sprite(stand_right)
    stand_right_seq = c.GRID(stand_right, 1, 1)
    stand_right_anim = c.ANIM(stand_right_seq, 1, True)

    walk_left = c.IMG("star.png")
    u.center_ground_sprite(walk_left)
    walk_left_seq = c.GRID(walk_left, 1, 1)
    walk_left_anim = c.ANIM(walk_left_seq, 0.1, True)

    walk_right = c.IMG("star.png")
    u.center_ground_sprite(walk_right)
    walk_right_seq = c.GRID(walk_right, 1, 1)
    walk_right_anim = c.ANIM(walk_right_seq, 0.1, True)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def effect(self):
        """Star allows the player to avoid the negative affects of other items. Returns None."""
        print("star effect")

    #need to set flags and call item clean up
