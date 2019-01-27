#stand lib
import math

#3rd party
import pyglet

#custom
from src.constants import *

class Item(pyglet.sprite.Sprite):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.spot_x = self.x
        self.spot_y = self.y
        self.delta_x = 0        
        self.delta_y = 0
        self.y_speed = ITEM_Y_SPEED
        self.x_speed = ITEM_X_SPEED
        self.transition_direction = "out"
        self.moving = False
        self.falling = False
        self.transitioning = False
        self.special = False
        self.item_used = False
#        if DEBUG:
#            print(self) 

    def update(self, dt):
        if self.falling: 
            global MAIN_TIME
            MAIN_TIME += dt
            if MAIN_TIME > 5:
                MAIN_TIME = 0
            self.y += falling_item(MAIN_TIME) #add gravity

        #(current spot "x") - (where its supposed to be "spot_x")
        self.delta_x = self.x - self.spot_x 
        self.delta_y = self.y - self.spot_y
        self.walk()
        self.move() 
        self.transition()

    def move(self): 
        """Moves the items closer to spot_x and spot_y. Returns None."""
        delta_x = self.delta_x
        delta_y = self.delta_y
        if delta_x > 0:
            self.x -= self.x_speed
        if delta_x < 0:
            self.x += self.x_speed
        if delta_y > 0:
            self.y -= self.y_speed
        if delta_y < 0:
            self.y += self.y_speed

    def walk(self):
        """Changes the animation of the sprite"""
        delta_x = self.delta_x
        #update sprite image
        if delta_x != 0 and self.moving == False:
            self.moving = True
            if delta_x > 0:
                self.image = self.walk_left_anim 
            if delta_x < 0:
                self.image = self.walk_right_anim 
        elif delta_x == 0:
            self.image = self.stand_right_anim
            self.moving = False
    
    def toggle_transition_direction(self):
        """Toggles transition_direction attribute. Returns None."""
        if self.transition_direction == "in":
            self.transition_direction = "out"
        elif self.transition_direction == "out":
            self.transition_direction = "in"

    def transition(self):
        """Toggles item opacity. Returns None."""
        if self.transitioning:
            if self.transition_direction == "in":
                self.opacity += ITEM_TRANSITION_SPEED 
            if self.transition_direction == "out":
                self.opacity -= ITEM_TRANSITION_SPEED
            if self.opacity >= 255:
                self.opacity = 255
                self.transitioning = False
            if self.opacity <= 0:
                self.opacity = 0
                self.transitioning = False

class RedMushroom(Item):
    """Red Mushroom is a random English vocabulary question. Returns None."""
    
    stand_left = pyglet.resource.image("red_mushroom.png")
    center_walker(stand_left)
    stand_left_seq = pyglet.image.ImageGrid(stand_left, 1, 1)
    stand_left_anim = pyglet.image.Animation.from_image_sequence(stand_left_seq, 1, True)

    stand_right_anim = stand_left_anim
    walk_left_anim = stand_left_anim
    walk_right_anim = stand_left_anim

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

#    def effect(self):
#        """Presents a random English word. Returns None"""
#        SHOW_BLACK_BOX = True

    def delete(self):
        super(Item, self).delete()

class GreenMushroom(Item):
    """Green Mushroom is a random verb form question. Returns None."""

    stand_left = pyglet.resource.image("green_mushroom.png")
    center_walker(stand_left)
    stand_left_seq = pyglet.image.ImageGrid(stand_left, 1, 1)
    stand_left_anim = pyglet.image.Animation.from_image_sequence(stand_left_seq, 1, True)

    stand_right_anim = stand_left_anim
    walk_left_anim = stand_left_anim
    walk_right_anim = stand_left_anim

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

#    def effect(self):
#        """Presents a verb form problem. Returns None"""
#        SHOW_BLACK_BOX = True
#        problems.Problem.random_present_verb()
        
    def delete(self):
        super(Item, self).delete()

class YoshiCoin(Item):
    """Yoshi Coin is a pronunciation question. Returns None."""
    
    stand_right = pyglet.resource.image("yoshi_coin_right.png")
    center_walker(stand_right)
    stand_right_seq = pyglet.image.ImageGrid(stand_right, 1, 5)
    stand_right_anim = pyglet.image.Animation.from_image_sequence(stand_right_seq, 1, True)

    walk_left = pyglet.resource.image("yoshi_coin_left.png")
    center_walker(walk_left)
    walk_left_seq = pyglet.image.ImageGrid(walk_left, 1, 5)
    walk_left_anim = pyglet.image.Animation.from_image_sequence(walk_left_seq, 0.1, True)

    walk_right = pyglet.resource.image("yoshi_coin_right.png")
    center_walker(walk_right)
    walk_right_seq = pyglet.image.ImageGrid(walk_right, 1, 5)
    walk_right_anim = pyglet.image.Animation.from_image_sequence(walk_right_seq, 0.1, True)

    stand_left_anim = walk_left_anim

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

#    def effect(self):
#        """Presents a pronunciation problem. Returns None"""
#        SHOW_BLACK_BOX = True

    def delete(self):
        super(Item, self).delete()

class PirahnaPlant(Item):
    """Pirahna Plant is a sentence translation problem (English to Japanese). Returns None."""

    stand_right = pyglet.resource.image("pirahna_plant_small.png")
    center_walker(stand_right)
    stand_right_seq = pyglet.image.ImageGrid(stand_right, 1, 2)
    stand_right_anim = pyglet.image.Animation.from_image_sequence(stand_right_seq, 0.1, True)

    walk_left = pyglet.resource.image("pirahna_plant_small.png")
    center_walker(walk_left)
    walk_left_seq = pyglet.image.ImageGrid(walk_left, 1, 2)
    walk_left_anim = pyglet.image.Animation.from_image_sequence(walk_left_seq, 0.1, True)

    walk_right = pyglet.resource.image("pirahna_plant_small.png")
    center_walker(walk_right)
    walk_right_seq = pyglet.image.ImageGrid(walk_right, 1, 2)
    walk_right_anim = pyglet.image.Animation.from_image_sequence(walk_right_seq, 0.1, True)

    stand_left_anim = stand_right_anim

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def effect(self):
        """Presents a sentence translation problem (English to Japanese). Returns None"""
        SHOW_BLACK_BOX = True
#        self.problem.random_target_sentence()
#        problems.Problem.random_target_sentence()

    def delete(self):
        super(Item, self).delete()

class SpinyBeetle(Item): 
    """Spiny Beetle is a question problem from 3rd year JHS at DaiKyuuChuu. Returns None."""

    stand_right = pyglet.resource.image("spiny_beetle_stand_right.png")
    center_walker(stand_right)
    stand_right_seq = pyglet.image.ImageGrid(stand_right, 1, 1)
    stand_right_anim = pyglet.image.Animation.from_image_sequence(stand_right_seq, 1, True)

    walk_left = pyglet.resource.image("spiny_beetle_walk_left.png")
    center_walker(walk_left)
    walk_left_seq = pyglet.image.ImageGrid(walk_left, 1, 2)
    walk_left_anim = pyglet.image.Animation.from_image_sequence(walk_left_seq, 0.1, True)

    walk_right = pyglet.resource.image("spiny_beetle_walk_right.png")
    center_walker(walk_right)
    walk_right_seq = pyglet.image.ImageGrid(walk_right, 1, 2)
    walk_right_anim = pyglet.image.Animation.from_image_sequence(walk_right_seq, 0.1, True)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

#    def effect(self):
#        """Presents a question from yomitore, qa 100, and custom questions. Returns None"""
#        SHOW_BLACK_BOX = True

    def delete(self):
        super(Item, self).delete()

class PowButton(Item):
    """Pow Button takes away one point from everyone. Returns None."""
        
    stand_left = pyglet.resource.image("pow_button.png")
    center_walker(stand_left)
    stand_left_seq = pyglet.image.ImageGrid(stand_left, 1, 1)
    stand_left_anim = pyglet.image.Animation.from_image_sequence(stand_left_seq, 1, False)

    stand_right_anim = stand_left_anim
    walk_left_anim = stand_left_anim
    walk_right_anim = stand_left_anim

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def effect(self):
        """Pow Button takes one point away from everyone. Returns None"""
        POW_BUTTON_EFFECT = True 

    def delete(self):
        super(Item, self).delete()

class Bombomb(Item):
    """Bombomb randomly mixes the order of the items on the screen. Returns None."""

    stand_right = pyglet.resource.image("bombomb_stand_right.png")
    center_walker(stand_right)
    stand_right_seq = pyglet.image.ImageGrid(stand_right, 1, 1)
    stand_right_anim = pyglet.image.Animation.from_image_sequence(stand_right_seq, 1, True)

    walk_left = pyglet.resource.image("bombomb_walk_left.png")
    center_walker(walk_left)
    walk_left_seq = pyglet.image.ImageGrid(walk_left, 1, 2)
    walk_left_anim = pyglet.image.Animation.from_image_sequence(walk_left_seq, 0.1, True)

    walk_right = pyglet.resource.image("bombomb_walk_right.png")
    center_walker(walk_right)
    walk_right_seq = pyglet.image.ImageGrid(walk_right, 1, 2)
    walk_right_anim = pyglet.image.Animation.from_image_sequence(walk_right_seq, 0.1, True)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def effect(self):
        """Randomly mix the order of items on the screen. Returns None."""
        BOMBOMB_EFFECT = True 

    def delete(self):
        super(Item, self).delete()

class QuestionBlock(Item): #unfinished
    """Question block chooses a random effect. Returns None."""

    stand_right = pyglet.resource.image("question_block.png")
    center_walker(stand_right)
    stand_right_seq = pyglet.image.ImageGrid(stand_right, 1, 4)
    stand_right_anim = pyglet.image.Animation.from_image_sequence(stand_right_seq, 1, True)

    walk_left = pyglet.resource.image("question_block.png")
    center_walker(walk_left)
    walk_left_seq = pyglet.image.ImageGrid(walk_left, 1, 4)
    walk_left_anim = pyglet.image.Animation.from_image_sequence(walk_left_seq, 0.1, True)

    walk_right = pyglet.resource.image("question_block.png")
    center_walker(walk_right)
    walk_right_seq = pyglet.image.ImageGrid(walk_right, 1, 4)
    walk_right_anim = pyglet.image.Animation.from_image_sequence(walk_right_seq, 0.1, True)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

#    def effect(self):
#        """Choose a random effect from all of the available effects. Returns None."""
#        print("question block effect")

    def delete(self):
        super(Item, self).delete()

class Feather(Item): #unfinished
    """Feather allows the player to skip their turn when the item is used. Returns None."""

    stand_right = pyglet.resource.image("feather.png")
    center_walker(stand_right)
    stand_right_seq = pyglet.image.ImageGrid(stand_right, 1, 1)
    stand_right_anim = pyglet.image.Animation.from_image_sequence(stand_right_seq, 1, True)

    walk_left = pyglet.resource.image("feather.png")
    center_walker(walk_left)
    walk_left_seq = pyglet.image.ImageGrid(walk_left, 1, 1)
    walk_left_anim = pyglet.image.Animation.from_image_sequence(walk_left_seq, 0.1, True)

    walk_right = pyglet.resource.image("feather.png")
    center_walker(walk_right)
    walk_right_seq = pyglet.image.ImageGrid(walk_right, 1, 1)
    walk_right_anim = pyglet.image.Animation.from_image_sequence(walk_right_seq, 0.1, True)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def effect(self):
        """Allows the player to skip a turn when the item is used. Returns None."""
        FEATHER_EFFECT = True

    def delete(self):
        super(Item, self).delete()

class Star(Item): #unfinished
    """Star allows the player to avoid the negative affects of other items. Returns None."""

    stand_right = pyglet.resource.image("star.png")
    center_walker(stand_right)
    stand_right_seq = pyglet.image.ImageGrid(stand_right, 1, 1)
    stand_right_anim = pyglet.image.Animation.from_image_sequence(stand_right_seq, 1, True)

    walk_left = pyglet.resource.image("star.png")
    center_walker(walk_left)
    walk_left_seq = pyglet.image.ImageGrid(walk_left, 1, 1)
    walk_left_anim = pyglet.image.Animation.from_image_sequence(walk_left_seq, 0.1, True)

    walk_right = pyglet.resource.image("star.png")
    center_walker(walk_right)
    walk_right_seq = pyglet.image.ImageGrid(walk_right, 1, 1)
    walk_right_anim = pyglet.image.Animation.from_image_sequence(walk_right_seq, 0.1, True)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

#    def effect(self):
#        """Star allows the player to avoid the negative affects of other items. Returns None."""
#        print("star effect")

    def delete(self):
        super(Item, self).delete()
    
    #need to set flags and call item clean up
