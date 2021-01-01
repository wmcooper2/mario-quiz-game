import pyglet
import math
import util
import problems
from constants import constants as c

#convenience variables
IMG = pyglet.resource.image
GRID = pyglet.image.ImageGrid
ANIM = pyglet.image.Animation.from_image_sequence
SPRITE = pyglet.sprite.Sprite

class Item(SPRITE):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #location
        self.dest_x = self.x
        self.dest_y = self.y
        self.dx = 0        
        self.dy = 0

        #speed
        self.y_speed = c.ITEM_Y_SPEED
        self.x_speed = c.ITEM_X_SPEED

        #opacity
        self.transition_direction = "out"
        self.disappear_rate = 9
        self.disappear = False
        self.max_opacity = 255
        self.min_opacity = 0

        #problem
#         self.problem = problems.Problem()

        #flags
#         self.moving = False
        self.falling = False
        self.special = False
        self.item_not_used = True

    def update(self, dt) -> None:
        if self.falling: 
            c.MAIN_TIME += dt
            if c.MAIN_TIME > 5:
                c.MAIN_TIME = 0
            self.y += util.falling_object(c.MAIN_TIME) #add gravity

        #(current spot "x") - (where its supposed to be "dest_x")
        self.dx = self.x - self.dest_x 
        self.dy = self.y - self.dest_y
        self.change_direction()
        self.move() 
        self.disappear_animation()
        print(f"{self}\t\tdx:{self.dx}, dy:{self.dy}")

    def move(self) -> None: 
        """Moves the items closer to dest_x and dest_y."""
        dx, dy = self.dx, self.dy
        if dx > 0:
            self.x -= self.x_speed
        if dx < 0:
            self.x += self.x_speed
        if dy > 0:
            self.y -= self.y_speed
        if dy < 0:
            self.y += self.y_speed

    def change_direction(self) -> None:
        """Changes the direction of the sprite."""
        dx = self.dx
        if dx != 0:
            if dx > 0:
                self.image = self.walk_left_anim 
            if dx < 0:
                self.image = self.walk_right_anim 
        elif dx == 0:
            self.image = self.stand_right_anim

    def toggle_disappear(self) -> None:
        """Toggle self.disappear flag."""
        if self.opacity <= self.min_opacity or self.opacity >= self.max_opacity:
            self.disappear = not self.disappear
            print("item.disappear:", self.disappear)

    def disappear_animation(self) -> None:
        """Make item disappear/reappear."""
        if self.disappear:
            self.opacity -= self.disappear_rate
        else:
            self.opacity += self.disappear_rate
        if self.opacity >= self.max_opacity:
            self.opacity = self.max_opacity
        elif self.opacity <= self.min_opacity:
            self.opacity = self.min_opacity
#         print("opacity:", self.opacity)

class RedMushroom(Item):
    """Red Mushroom is a random English vocabulary question. Returns None."""
    
    stand_left = IMG("redmushroom.png")
    util.center_ground_sprite(stand_left)
    stand_left_seq = GRID(stand_left, 1, 1)
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

    def delete(self):
        super(Item, self).delete()

class GreenMushroom(Item):
    """Green Mushroom is a random verb form question. Returns None."""

    stand_left = IMG("greenmushroom.png")
    util.center_ground_sprite(stand_left)
    stand_left_seq = GRID(stand_left, 1, 1)
    stand_left_anim = ANIM(stand_left_seq, 1, True)

    stand_right_anim = stand_left_anim
    walk_left_anim = stand_left_anim
    walk_right_anim = stand_left_anim

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def effect(self):
        """Presents a verb form problem. Returns None"""
        problems.showing_black_box = True
        self.problem.random_present_verb()
        
    def delete(self):
        super(Item, self).delete()

class YoshiCoin(Item):
    """Yoshi Coin is a pronunciation question. Returns None."""
    
    stand_right = IMG("yoshicoinright.png")
    util.center_ground_sprite(stand_right)
    stand_right_seq = GRID(stand_right, 1, 5)
    stand_right_anim = ANIM(stand_right_seq, 1, True)

    walk_left = IMG("yoshicoinleft.png")
    util.center_ground_sprite(walk_left)
    walk_left_seq = GRID(walk_left, 1, 5)
    walk_left_anim = ANIM(walk_left_seq, 0.1, True)

    walk_right = IMG("yoshicoinright.png")
    util.center_ground_sprite(walk_right)
    walk_right_seq = GRID(walk_right, 1, 5)
    walk_right_anim = ANIM(walk_right_seq, 0.1, True)

    stand_left_anim = walk_left_anim

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def effect(self):
        """Presents a pronunciation problem. Returns None"""
        problems.showing_black_box = True
        self.problem.random_pronunciation()

    def delete(self):
        super(Item, self).delete()

class PirahnaPlant(Item):
    """Pirahna Plant is a sentence translation problem (English to Japanese). Returns None."""

    stand_right = IMG("pirahnaplantsmall.png")
    util.center_ground_sprite(stand_right)
    stand_right_seq = GRID(stand_right, 1, 2)
    stand_right_anim = ANIM(stand_right_seq, 0.1, True)

    walk_left = IMG("pirahnaplantsmall.png")
    util.center_ground_sprite(walk_left)
    walk_left_seq = GRID(walk_left, 1, 2)
    walk_left_anim = ANIM(walk_left_seq, 0.1, True)

    walk_right = IMG("pirahnaplantsmall.png")
    util.center_ground_sprite(walk_right)
    walk_right_seq = GRID(walk_right, 1, 2)
    walk_right_anim = ANIM(walk_right_seq, 0.1, True)

    stand_left_anim = stand_right_anim

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def effect(self):
        """Presents a sentence translation problem (English to Japanese). Returns None"""
        problems.showing_black_box = True
        self.problem.random_target_sentence()

    def delete(self):
        super(Item, self).delete()

class SpinyBeetle(Item): 
    """Spiny Beetle is a question problem from 3rd year JHS at DaiKyuuChuu. Returns None."""

    stand_right = IMG("spinybeetlestandright.png")
    util.center_ground_sprite(stand_right)
    stand_right_seq = GRID(stand_right, 1, 1)
    stand_right_anim = ANIM(stand_right_seq, 1, True)

    walk_left = IMG("spinybeetlewalkleft.png")
    util.center_ground_sprite(walk_left)
    walk_left_seq = GRID(walk_left, 1, 2)
    walk_left_anim = ANIM(walk_left_seq, 0.1, True)

    walk_right = IMG("spinybeetlewalkright.png")
    util.center_ground_sprite(walk_right)
    walk_right_seq = GRID(walk_right, 1, 2)
    walk_right_anim = ANIM(walk_right_seq, 0.1, True)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def effect(self):
        """Presents a question from yomitore, qa 100, and custom questions. Returns None"""
        problems.showing_black_box = True
        self.problem.random_question()

    def delete(self):
        super(Item, self).delete()

class PowButton(Item):
    """Pow Button takes away one point from everyone. Returns None."""
        
    stand_left = IMG("powbutton.png")
    util.center_ground_sprite(stand_left)
    stand_left_seq = GRID(stand_left, 1, 1)
    stand_left_anim = ANIM(stand_left_seq, 1, False)

    stand_right_anim = stand_left_anim
    walk_left_anim = stand_left_anim
    walk_right_anim = stand_left_anim

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def effect(self):
        """Pow Button takes one point away from everyone. Returns None"""
#         global pow_button_effect
        c.POW_BUTTON_EFFECT = True 

    def delete(self):
        super(Item, self).delete()

class Bombomb(Item):
    """Bombomb randomly mixes the order of the items on the screen. Returns None."""

    stand_right = IMG("bombombstandright.png")
    util.center_ground_sprite(stand_right)
    stand_right_seq = GRID(stand_right, 1, 1)
    stand_right_anim = ANIM(stand_right_seq, 1, True)

    walk_left = IMG("bombombwalkleft.png")
    util.center_ground_sprite(walk_left)
    walk_left_seq = GRID(walk_left, 1, 2)
    walk_left_anim = ANIM(walk_left_seq, 0.1, True)

    walk_right = IMG("bombombwalkright.png")
    util.center_ground_sprite(walk_right)
    walk_right_seq = GRID(walk_right, 1, 2)
    walk_right_anim = ANIM(walk_right_seq, 0.1, True)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def effect(self):
        """Randomly mix the order of items on the screen. Returns None."""
#         global bombomb_effect
        c.BOMBOMB_EFFECT = True 

    def delete(self):
        super(Item, self).delete()

class QuestionBlock(Item): #unfinished
    """Question block chooses a random effect. Returns None."""

    stand_right = IMG("questionblock.png")
    util.center_ground_sprite(stand_right)
    stand_right_seq = GRID(stand_right, 1, 4)
    stand_right_anim = ANIM(stand_right_seq, 1, True)

    walk_left = IMG("questionblock.png")
    util.center_ground_sprite(walk_left)
    walk_left_seq = GRID(walk_left, 1, 4)
    walk_left_anim = ANIM(walk_left_seq, 0.1, True)

    walk_right = IMG("questionblock.png")
    util.center_ground_sprite(walk_right)
    walk_right_seq = GRID(walk_right, 1, 4)
    walk_right_anim = ANIM(walk_right_seq, 0.1, True)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def effect(self):
        """Choose a random effect from all of the available effects. Returns None."""
        print("question block effect")

    def delete(self):
        super(Item, self).delete()

class Feather(Item): #unfinished
    """Feather allows the player to skip their turn when the item is used. Returns None."""

    stand_right = IMG("feather.png")
    util.center_ground_sprite(stand_right)
    stand_right_seq = GRID(stand_right, 1, 1)
    stand_right_anim = ANIM(stand_right_seq, 1, True)

    walk_left = IMG("feather.png")
    util.center_ground_sprite(walk_left)
    walk_left_seq = GRID(walk_left, 1, 1)
    walk_left_anim = ANIM(walk_left_seq, 0.1, True)

    walk_right = IMG("feather.png")
    util.center_ground_sprite(walk_right)
    walk_right_seq = GRID(walk_right, 1, 1)
    walk_right_anim = ANIM(walk_right_seq, 0.1, True)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def effect(self):
        """Allows the player to skip a turn when the item is used. Returns None."""
        FEATHER_EFFECT = True

    def delete(self):
        super(Item, self).delete()

class Star(Item): #unfinished
    """Star allows the player to avoid the negative affects of other items. Returns None."""

    stand_right = IMG("star.png")
    util.center_ground_sprite(stand_right)
    stand_right_seq = GRID(stand_right, 1, 1)
    stand_right_anim = ANIM(stand_right_seq, 1, True)

    walk_left = IMG("star.png")
    util.center_ground_sprite(walk_left)
    walk_left_seq = GRID(walk_left, 1, 1)
    walk_left_anim = ANIM(walk_left_seq, 0.1, True)

    walk_right = IMG("star.png")
    util.center_ground_sprite(walk_right)
    walk_right_seq = GRID(walk_right, 1, 1)
    walk_right_anim = ANIM(walk_right_seq, 0.1, True)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def effect(self):
        """Star allows the player to avoid the negative affects of other items. Returns None."""
        print("star effect")

    def delete(self):
        super(Item, self).delete()
    
    #need to set flags and call item clean up
