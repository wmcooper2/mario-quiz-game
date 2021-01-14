#std lib
import math
import random
from typing import Any, List, Tuple

#3rd party
import pyglet

#custom
from constants import Constants as c
from constants import Difficulty as d
from constants import Effects as e
from constants import Items as i
# import problems as p

#TODO, finish Feather, QuestionBlock, Star classes

class Item(c.SPRITE):
    def __init__(self, img, scale=1, *args, **kwargs):
        super().__init__(img, *args, **kwargs)

        #location
        self.x=c.OFF_SCREEN_L
        self.y=c.ITEM_PLATFORM_H
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

        #flags
        self.special = False
        self.item_not_used = True

        #other
#         self.problem = p.Problem()
        self.scale = scale
        self.batch=c.ITEM_BATCH
        self.scale=c.ITEM_SCALE

    def update(self, dt) -> None:
        """Item's main update."""
        self.dt = dt
        self.dx = self.x - self.dest_x 
        self.dy = self.y - self.dest_y
        self.change_image()
        self.move() 
        self.disappear_animation()
 
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
            if dx > 0 and self.image != self.left_anim:
                self.go_left()
            elif dx < 0 and self.image != self.right_anim:
                self.go_right()
        elif dx == 0 and self.image != self.right_anim:
            self.go_right()

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

    def go_left(self) -> None:
        """Change image to the one going left."""
        self.image = self.left_anim

    def go_right(self) -> None:
        """Change image to the one going right."""
        self.image = self.right_anim

    def is_at_disappear_limit(self) -> bool:
        """Is the item at or above self.disappear_limit?"""
        return self.y >= (c.ITEM_PLATFORM_H + self.disappear_limit)

    def is_left_of_p1(self) -> bool:
        """Is the item to the left of player 1?"""
        return self.x < c.P1.x

    def is_at_or_below_p1(self) -> bool:
        """Is item at or below player 1 on y-axis?"""
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

    def is_visible(self) -> bool:
        """Is the opacity even slightly above 0? Then it's visible."""
        return self.opacity > self.min_opacity

    def within_margin(self) -> Tuple[bool, bool]:
        """Checks if item within range of destination."""
        return (abs(self.dx) <= self.x_speed, abs(self.dy) <= self.y_speed)


class Walker(Item):
    def __init__(self, img, *args, **kwargs):
        super().__init__(img, *args, **kwargs)

    def change_image(self) -> None:
        """Changes the sprite's image. Overrides base class method."""
        dx = self.dx
        if dx != 0:
            if dx > 0 and self.image != self.walk_left_anim:
                self.go_left()
            elif dx < 0 and self.image != self.walk_right_anim:
                self.go_right()
        elif dx == 0 and self.image != self.right_anim:
            self.image = self.right_anim

    def go_left(self) -> None:
        """Change image to animation walking left. Overrides base class method."""
        self.image = self.walk_left_anim

    def go_right(self) -> None:
        """Change image to animation walking right. Overrides base class method."""
        self.image = self.walk_right_anim

#WALKERS
class Bombomb(Walker):
    """Bombomb randomly mixes the order of the items on the screen."""
    def __init__(self, *args, **kwargs):
        self.right = c.IMG("bombombstandright.png")
        self.right_seq = c.GRID(self.right, 1, 1)
        self.right_anim = c.ANIM(self.right_seq, 1, True)
        self.walk_left = c.IMG("bombombwalkleft.png")
        self.walk_left_seq = c.GRID(self.walk_left, 1, 2)
        self.walk_left_anim = c.ANIM(self.walk_left_seq, 0.1, True)
        self.walk_right = c.IMG("bombombwalkright.png")
        self.walk_right_seq = c.GRID(self.walk_right, 1, 2)
        self.walk_right_anim = c.ANIM(self.walk_right_seq, 0.1, True)
        self.left = self.right
        super().__init__(self.right, *args, **kwargs)
    
    def effect(self) -> None:
        """Randomly mix the order of items on the screen."""
        print("Bombomb effect")

class SpinyBeetle(Walker): 
    """Spiny Beetle is a question problem from 3rd year JHS at DaiKyuuChuu."""
    def __init__(self, *args, **kwargs):
        self.right = c.IMG("spinybeetlestandright.png")
        self.right_seq = c.GRID(self.right, 1, 1)
        self.right_anim = c.ANIM(self.right_seq, 1, True)
        self.left = c.IMG("spinybeetlewalkleft.png")
        self.walk_left_seq = c.GRID(self.left, 1, 2)
        self.walk_left_anim = c.ANIM(self.walk_left_seq, 0.1, True)
        self.walk_right = c.IMG("spinybeetlewalkright.png")
        self.walk_right_seq = c.GRID(self.walk_right, 1, 2)
        self.walk_right_anim = c.ANIM(self.walk_right_seq, 0.1, True)
        self.left = self.right
        super().__init__(self.right, *args, **kwargs)
    
    def effect(self) -> None:
        """Presents a question from yomitore, qa 100, and custom questions."""
        print("SpinyBeetle effect")

#SLIDERS
class RedMushroom(Item):
    """Red Mushroom is a random English vocabulary question."""
    def __init__(self, *args, **kwargs):
        self.right = c.IMG("redmushroom.png")
        self.right_seq = c.GRID(self.right, 1, 1)
        self.right_anim = c.ANIM(self.right_seq, 1, True)
        self.left_anim = self.right_anim
        super().__init__(self.right, *args, **kwargs)
    
    def effect(self) -> None:
        """Presents a random English word"""
        print("RedMushroom effect")

class GreenMushroom(Item):
    """Green Mushroom is a random verb form question."""
    def __init__(self, *args, **kwargs):
        self.right = c.IMG("greenmushroom.png")
        self.right_seq = c.GRID(self.right, 1, 1)
        self.right_anim = c.ANIM(self.right_seq, 1, True)
        self.left_anim = self.right_anim
        super().__init__(self.right, *args, **kwargs)
    
    def effect(self) -> None:
        """Presents a verb form problem"""
        print("GreenMushroom effect")

class YoshiCoin(Item):
    """Yoshi Coin is a pronunciation question."""
    def __init__(self, *args, **kwargs):
        self.right = c.IMG("yoshicoinright.png")
        self.right_seq = c.GRID(self.right, 1, 5)
        self.right_anim = c.ANIM(self.right_seq, 1, True)
        self.left = c.IMG("yoshicoinleft.png")
        self.left_seq = c.GRID(self.left, 1, 5)
        self.left_anim = c.ANIM(self.left_seq, 0.1, True)
        super().__init__(self.right, *args, **kwargs)
    
    def effect(self) -> None:
        """Presents a pronunciation problem."""
        print("YoshiCoin effect")

class PirahnaPlant(Item):
    """Pirahna Plant is a sentence translation problem (English to Japanese)."""
    def __init__(self, *args, **kwargs):
        self.right = c.IMG("pirahnaplantsmall.png")
        self.right_seq = c.GRID(self.right, 1, 2)
        self.right_anim = c.ANIM(self.right_seq, 0.1, True)
        self.left_anim = self.right_anim
        super().__init__(self.right, *args, **kwargs)
    
    def effect(self) -> None:
        """Presents a sentence translation problem (English to Japanese)"""
        pass
        print("PirahnaPlant effect")

class PowButton(Item):
    """Pow Button takes away one point from everyone."""
    def __init__(self, *args, **kwargs):
        self.right = c.IMG("powbutton.png")
        self.right_seq = c.GRID(self.right, 1, 1)
        self.right_anim = c.ANIM(self.right_seq, 1, False)
        self.left_anim = self.right_anim
        self.left = self.right
        super().__init__(self.right, *args, **kwargs)
    
    def effect(self):
        """Pow Button takes one point away from everyone."""
        print("Pow effect")

class Feather(Item):
    """Feather allows the player to skip their turn when the item is used."""
    def __init__(self, *args, **kwargs):
        self.right = c.IMG("feather.png")
        self.right_seq = c.GRID(self.right, 1, 1)
        self.right_anim = c.ANIM(self.right_seq, 1, True)
        self.left = self.right
        super().__init__(self.right, *args, **kwargs)
    
    def effect(self) -> None:
        """Allows the player to skip a turn when the item is used."""
        print("Feather effect")

class QuestionBlock(Item):
    """Question block chooses a random effect."""
    def __init__(self, *args, **kwargs):
        self.right = c.IMG("questionblock.png")
        self.right_seq = c.GRID(self.right, 1, 4)
        self.right_anim = c.ANIM(self.right_seq, 1, True)
        self.left = self.right
        super().__init__(self.right, *args, **kwargs)
    
    def effect(self) -> None:
        """Choose a random effect from all of the available effects."""
        print("QuestionBlock effect")

class Star(Item):
    """Star allows the player to avoid the negative affects of other items."""
    def __init__(self, *args, **kwargs):
        self.right = c.IMG("star.png")
        self.right_seq = c.GRID(img, 1, 1)
        self.right_anim = c.ANIM(self.right_seq, 1, True)
        self.left = self.right
        super().__init__(self.right, *args, **kwargs)
    
    def effect(self) -> None:
        """Star allows the player to avoid the negative affects of other items."""
        print("Pow effect")

def add_item() -> None:
    """Adds 1 new item to c.ALL_ITEMS."""
    c.ALL_ITEMS.append(new_item())

def add_items() -> None:
    """Populates c.ALL_ITEMS."""
    for item in range(c.NUM_ITEMS):
        c.ALL_ITEMS.append(new_item())

def choose_item(difficulty: List[int]) -> Any:
    """Choose an item."""
    if difficulty == d.SUPER_EASY:
        return probability(c.SUPER_EASY_RANGE)
    elif difficulty == d.EASY:
        return probability(c.EASY_RANGE)
    elif difficulty == d.MEDIUM:
        return probability(c.MEDIUM_RANGE)
    elif difficulty == d.HARD:
        return probability(c.HARD_RANGE)
    elif difficulty == d.SUPER_HARD:
        return probability(c.SUPER_HARD_RANGE)

def probability(choices) -> Any:
    """returns a choice of item based on the passed in probability list."""
    choice = random.randrange(1, 100, 1)
    #walkers
    if choice > 0 and choice < choices[0]:            
        return i.BOMBOMB 
    elif choice >= choices[1] and choice < choices[2]:              
        return i.SPINY_BEETLE 
    #sliders
    elif choice >= choices[5] and choice <= choices[6]:                  
        return i.RED_MUSHROOM
    elif choice >= choices[4] and choice < choices[5]:               
        return i.GREEN_MUSHROOM 
    elif choice >= choices[3] and choice < choices[4]:                
        return i.YOSHI_COIN 
    elif choice >= choices[2] and choice < choices[3]:               
        return i.PIRAHNA_PLANT 
    elif choice >= choices[0] and choice < choices[1]:             
        return i.POW_BUTTON 

        #need questionblock, feather and star

def new_item() -> Any:
    """Adds new item to all_items. Returns Sprite object."""
    difficulty = c.DIFFICULTY
    choice = choose_item(difficulty)
    #walkers
    if choice == i.BOMBOMB:
        return Bombomb()
    elif choice == i.SPINY_BEETLE: 
        return SpinyBeetle()
    #sliders
    elif choice == i.RED_MUSHROOM: 
        return RedMushroom()
    elif choice == i.GREEN_MUSHROOM:
        return GreenMushroom()
    elif choice == i.YOSHI_COIN: 
        return YoshiCoin()
    elif choice == i.PIRAHNA_PLANT:
        return PirahnaPlant()
    elif choice == i.POW_BUTTON: 
        return PowButton()
    elif choice == i.FEATHER: 
        return Feather()
    elif choice == i.STAR: 
        return Star()
    elif choice == i.QUESTION_BLOCK: 
        return QuestionBlock()
