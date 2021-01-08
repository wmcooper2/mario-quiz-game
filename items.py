#std lib
import math
import random
from typing import Any, List, Tuple

#3rd party
import pyglet

#custom
from constants import constants as c
from constants import Difficulty as d
from constants import Items as i
import problems as p

class Item(c.SPRITE):
    def __init__(self, scale=1, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #location
        self.x=c.OFF_SCREEN_L
        self.y=c.ITEM_PLATFORM_H
        self.dest_x = self.x
        self.dest_y = self.y
#         self.anchor_x = self.width // 2
#         self.anchor_y = 0

        #TODO
#         print("self.dest_x", self.dest_x)
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
        self.batch=c.MAIN_BATCH
        self.scale=c.ITEM_SCALE

    def update(self, dt) -> None:
        """Item's main update."""
#         print("self/anchor_x:", self, self.anchor_x)
        self.dt = dt
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

#     def center_ground_sprite(self) -> None:
#         """Center the sprites anchor to the middle-bottom of the image."""
#         self.anchor_x = self.width // 2
#         self.anchor_y = 0

    def center_ground_sprite(self, image: Any) -> None:
        """Center the sprites anchor to the middle-bottom of the image."""
        image.anchor_x = image.width // 2
        image.anchor_y = 0
#         self.anchor_x = self.width // 2
#         self.anchor_y = 0

    def change_image(self) -> None:
        """Changes the sprite's image."""
        #TODO, is the problem with it being self.image instead of self.img?
        dx = self.dx
        if dx != 0:
            if dx > 0 and self.image != self.walk_left_anim:
                self.image = self.walk_left_anim 
            elif dx < 0 and self.image != self.walk_right_anim:
                self.image = self.walk_right_anim 
        elif dx == 0 and self.image != self.stand_right_anim:
            self.image = self.stand_right_anim
#         if dx != 0:
#             if dx > 0 and self.image != self.walk_left_anim:
#                 self.img = self.stand_left_anim
#             elif dx < 0 and self.image != self.walk_right_anim:
#                 self.img = self.stand_right_anim
#         elif dx == 0 and self.image != self.stand_right_anim:
#             self.img = self.stand_right_anim

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
        #TODO, crashes here after item transfer
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
        if self == c.P1.inventory:
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

            #item is at the same spot as the player, x and y axes
            if self.is_at_or_below_p1() and self.is_over_p1():
                self.match_p1_coords()
                #TODO, the player must answer the question correctly in order to get the item.
                if c.P1.inventory:
                    c.P1.inventory.delete()         #remove item from game
                    c.P1.inventory = self           #assign x to player's x
                else:
                    c.P1.inventory = self           #assign x to player's x

    def is_visible(self) -> bool:
        """Is the opacity even slightly above 0? Then it's visible."""
        return self.opacity > self.min_opacity

    def within_margin(self) -> Tuple[bool, bool]:
        """Checks if item within range of destination."""
        return (abs(self.dx) <= self.x_speed, abs(self.dy) <= self.y_speed)


##4 important sprites
#stand_right
#stand_left
#walk_left_anim
#walk_right_anim
##images set to stand_right for debugging

class RedMushroom(Item):
    """Red Mushroom is a random English vocabulary question."""
    def __init__(self, *args, **kwargs):
        #stand right
        self.stand_right = c.IMG("redmushroom.png")
#         self.center_ground_sprite(self.stand_right)
        self.stand_right_seq = c.GRID(self.stand_right, 1, 1)
        self.stand_right_anim = c.ANIM(self.stand_right_seq, 1, True)

        self.stand_left_anim = self.stand_right_anim

        self.walk_left_anim = self.stand_left_anim
        self.walk_right_anim = self.stand_left_anim

        self.stand_left = self.stand_right
        self.img=self.stand_right
        super().__init__(*args, **kwargs)

        #TODO, set dest_x somewhere, after the object is created, set to the platform height
        #set anchor on all images? even animations?

    def effect(self):
        """Presents a random English word. Returns None"""
        p.showing_black_box = True
        self.problem.random_english_word()

class GreenMushroom(Item):
    """Green Mushroom is a random verb form question."""
    def __init__(self, *args, **kwargs):
        #stand right
        self.stand_right = c.IMG("greenmushroom.png")
#         self.center_ground_sprite(self.stand_left)
        self.stand_right_seq = c.GRID(self.stand_right, 1, 1)
        self.stand_right_anim = c.ANIM(self.stand_right_seq, 1, True)

        self.stand_left_anim = self.stand_right_anim
        self.walk_right_anim = self.stand_right_anim
        self.walk_left_anim = self.stand_left_anim

#         self.img=self.stand_right_anim
        self.stand_left = self.stand_right
        self.img=self.stand_right
        super().__init__(*args, **kwargs)

    def effect(self):
        """Presents a verb form problem. Returns None"""
        p.showing_black_box = True
        self.problem.random_present_verb()

class YoshiCoin(Item):
    """Yoshi Coin is a pronunciation question."""
    def __init__(self, *args, **kwargs):
        #stand right
        self.stand_right = c.IMG("yoshicoinright.png")
#         self.center_ground_sprite(self.stand_right)
        self.stand_right_seq = c.GRID(self.stand_right, 1, 5)
        self.stand_right_anim = c.ANIM(self.stand_right_seq, 1, True)

        self.walk_left = c.IMG("yoshicoinleft.png")
#         self.center_ground_sprite(self.walk_left)
        self.walk_left_seq = c.GRID(self.walk_left, 1, 5)
        self.walk_left_anim = c.ANIM(self.walk_left_seq, 0.1, True)

        self.walk_right = c.IMG("yoshicoinright.png")
#         self.center_ground_sprite(self.walk_right)
        self.walk_right_seq = c.GRID(self.walk_right, 1, 5)
        self.walk_right_anim = c.ANIM(self.walk_right_seq, 0.1, True)
        self.stand_left_anim = self.walk_left_anim

        self.img=self.stand_right
        super().__init__(*args, **kwargs)

    def effect(self):
        """Presents a pronunciation problem. Returns None"""
        p.showing_black_box = True
        self.problem.random_pronunciation()

class PirahnaPlant(Item):
    """Pirahna Plant is a sentence translation problem (English to Japanese)."""
    def __init__(self, *args, **kwargs):
        #stand right
        self.stand_right = c.IMG("pirahnaplantsmall.png")
#         self.center_ground_sprite(self.stand_right)
        self.stand_right_seq = c.GRID(self.stand_right, 1, 2)
        self.stand_right_anim = c.ANIM(self.stand_right_seq, 0.1, True)

        #walk left
        self.walk_left = c.IMG("pirahnaplantsmall.png")
#         self.center_ground_sprite(self.walk_left)
        self.walk_left_seq = c.GRID(self.walk_left, 1, 2)
        self.walk_left_anim = c.ANIM(self.walk_left_seq, 0.1, True)

        #walk right
        self.walk_right = c.IMG("pirahnaplantsmall.png")
#         self.center_ground_sprite(self.walk_right)
        self.walk_right_seq = c.GRID(self.walk_right, 1, 2)
        self.walk_right_anim = c.ANIM(self.walk_right_seq, 0.1, True)

        self.stand_left_anim = self.stand_right_anim
#         self.img=self.stand_right_anim
        self.img=self.stand_right
        super().__init__(*args, **kwargs)

    def effect(self):
        """Presents a sentence translation problem (English to Japanese). Returns None"""
        p.showing_black_box = True
        self.problem.random_target_sentence()

class SpinyBeetle(Item): 
    """Spiny Beetle is a question problem from 3rd year JHS at DaiKyuuChuu."""
    def __init__(self, *args, **kwargs):
        #stand right
        self.stand_right = c.IMG("spinybeetlestandright.png")
#         self.center_ground_sprite(self.stand_right)
        self.stand_right_seq = c.GRID(self.stand_right, 1, 1)
        self.stand_right_anim = c.ANIM(self.stand_right_seq, 1, True)

        #walk left
        self.walk_left = c.IMG("spinybeetlewalkleft.png")
#         self.center_ground_sprite(self.walk_left)
        self.walk_left_seq = c.GRID(self.walk_left, 1, 2)
        self.walk_left_anim = c.ANIM(self.walk_left_seq, 0.1, True)

        #walk right
        self.walk_right = c.IMG("spinybeetlewalkright.png")
#         self.center_ground_sprite(self.walk_right)
        self.walk_right_seq = c.GRID(self.walk_right, 1, 2)
        self.walk_right_anim = c.ANIM(self.walk_right_seq, 0.1, True)

#         self.img=self.stand_right_anim
        self.stand_left = self.stand_right
        self.img=self.stand_right
        super().__init__(*args, **kwargs)

    def effect(self):
        """Presents a question from yomitore, qa 100, and custom questions. Returns None"""
        p.showing_black_box = True
        self.problem.random_question()

class PowButton(Item):
    """Pow Button takes away one point from everyone."""
    def __init__(self, *args, **kwargs):
        #stand right
        self.stand_right = c.IMG("powbutton.png")
#         self.center_ground_sprite(self.stand_left)
        self.stand_right_seq = c.GRID(self.stand_right, 1, 1)
        self.stand_right_anim = c.ANIM(self.stand_right_seq, 1, False)

        self.stand_right_anim = self.stand_left_anim
        self.walk_left_anim = self.stand_left_anim
        self.walk_right_anim = self.stand_left_anim

        self.stand_left = self.stand_right
#         self.img=self.stand_right_anim
        self.img=self.stand_right
        super().__init__(*args, **kwargs)

    def effect(self):
        """Pow Button takes one point away from everyone. Returns None"""
        c.POW_BUTTON_EFFECT = True 

class Bombomb(Item):
    """Bombomb randomly mixes the order of the items on the screen."""
    def __init__(self, *args, **kwargs):
        #stand right
        self.stand_right = c.IMG("bombombstandright.png")
#         self.center_ground_sprite(self.stand_right)
        self.stand_right_seq = c.GRID(self.stand_right, 1, 1)
        self.stand_right_anim = c.ANIM(self.stand_right_seq, 1, True)

        #walk left
        self.walk_left = c.IMG("bombombwalkleft.png")
#         self.center_ground_sprite(self.walk_left)
        self.walk_left_seq = c.GRID(self.walk_left, 1, 2)
        self.walk_left_anim = c.ANIM(self.walk_left_seq, 0.1, True)

        #walk right
        self.walk_right = c.IMG("bombombwalkright.png")
#         self.center_ground_sprite(self.walk_right)
        self.walk_right_seq = c.GRID(self.walk_right, 1, 2)
        self.walk_right_anim = c.ANIM(self.walk_right_seq, 0.1, True)

        self.stand_left = self.stand_right
#         self.img=self.stand_right_anim
        self.img=self.stand_right
        super().__init__(*args, **kwargs)
    
    def effect(self):
        """Randomly mix the order of items on the screen. Returns None."""
        c.BOMBOMB_EFFECT = True 

class QuestionBlock(Item): #unfinished
    """Question block chooses a random effect."""
    def __init__(self, *args, **kwargs):
        #stand right
        self.stand_right = c.IMG("questionblock.png")
#         self.center_ground_sprite(self.stand_right)
        self.stand_right_seq = c.GRID(self.stand_right, 1, 4)
        self.stand_right_anim = c.ANIM(self.stand_right_seq, 1, True)

        #walk left
        self.walk_left = c.IMG("questionblock.png")
#         self.center_ground_sprite(self.walk_left)
        self.walk_left_seq = c.GRID(self.walk_left, 1, 4)
        self.walk_left_anim = c.ANIM(self.walk_left_seq, 0.1, True)

        #walk right
        self.walk_right = c.IMG("questionblock.png")
#         self.center_ground_sprite(self.walk_right)
        self.walk_right_seq = c.GRID(self.walk_right, 1, 4)
        self.walk_right_anim = c.ANIM(self.walk_right_seq, 0.1, True)

        self.stand_left = self.stand_right
#         self.img=self.stand_right_anim
        self.img=self.stand_right
        super().__init__(*args, **kwargs)

    def effect(self):
        """Choose a random effect from all of the available effects. Returns None."""
        pass
#         print("question block effect")

class Feather(Item): #unfinished
    """Feather allows the player to skip their turn when the item is used."""
    def __init__(self, *args, **kwargs):
        #stand right
        self.stand_right = c.IMG("feather.png")
#         self.center_ground_sprite(self.stand_right)
        self.stand_right_seq = c.GRID(self.stand_right, 1, 1)
        self.stand_right_anim = c.ANIM(self.stand_right_seq, 1, True)

        #walk left
        self.walk_left = c.IMG("feather.png")
#         self.center_ground_sprite(self.walk_left)
        self.walk_left_seq = c.GRID(self.walk_left, 1, 1)
        self.walk_left_anim = c.ANIM(self.walk_left_seq, 0.1, True)

        #walk right
        self.walk_right = c.IMG("feather.png")
#         self.center_ground_sprite(self.walk_right)
        self.walk_right_seq = c.GRID(self.walk_right, 1, 1)
        self.walk_right_anim = c.ANIM(self.walk_right_seq, 0.1, True)

        self.stand_left = self.stand_right
#         self.img=self.stand_right_anim
        self.img=self.stand_right
        super().__init__(*args, **kwargs)

    def effect(self):
        """Allows the player to skip a turn when the item is used. Returns None."""
        FEATHER_EFFECT = True

class Star(Item): #unfinished
    """Star allows the player to avoid the negative affects of other items."""
    def __init__(self, *args, **kwargs):
        #stand right
        self.stand_right = c.IMG("star.png")
#         self.center_ground_sprite(self.stand_right)
        self.stand_right_seq = c.GRID(self.stand_right, 1, 1)
        self.stand_right_anim = c.ANIM(self.stand_right_seq, 1, True)

        #walk left
        self.walk_left = c.IMG("star.png")
#         self.center_ground_sprite(self.walk_left)
        self.walk_left_seq = c.GRID(self.walk_left, 1, 1)
        self.walk_left_anim = c.ANIM(self.walk_left_seq, 0.1, True)

        #walk right
        self.walk_right = c.IMG("star.png")
#         self.center_ground_sprite(self.walk_right)
        self.walk_right_seq = c.GRID(self.walk_right, 1, 1)
        self.walk_right_anim = c.ANIM(self.walk_right_seq, 0.1, True)

        self.stand_left = self.stand_right
#         self.img=self.stand_right_anim
        self.img=self.stand_right
        super().__init__(*args, **kwargs)

    def effect(self):
        """Star allows the player to avoid the negative affects of other items."""
#         print("star effect")
        pass

def add_item() -> None:
    """Adds 1 new item to c.ALL_ITEMS."""
#     print("add_item: c.ALL_ITEMS")
#     pprint(c.ALL_ITEMS)
#     print("add_item: c.ITEM_SPOTS")
#     pprint(c.ITEM_SPOTS)
    #new item
    item = new_item()
#     print("add_item: new_item()")
#     print(item)
#     pprint(dir(item))
    #good item
#     print("add_item: existing item")
#     print(c.ALL_ITEMS[2])
#     pprint(dir(c.ALL_ITEMS[2]))
#     item.dest_x = c.ITEM_SPOTS[0]
    c.ALL_ITEMS.append(item)
#     anchor item to it's spot if ALL_ITEMS
#     new item's spot is the first element in c.ITEM_SPOTS

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
    if choice >= choices[5] and choice <= choices[6]:                  
        return i.RED_MUSHROOM
    elif choice >= choices[4] and choice < choices[5]:               
        return i.GREEN_MUSHROOM 
    elif choice >= choices[3] and choice < choices[4]:                
        return i.YOSHI_COIN 
    elif choice >= choices[2] and choice < choices[3]:               
        return i.PIRAHNA_PLANT 
    elif choice >= choices[1] and choice < choices[2]:              
        return i.SPINY_BEETLE 
    elif choice >= choices[0] and choice < choices[1]:             
        return i.POW_BUTTON 
    elif choice > 0 and choice < choices[0]:            
        return i.BOMBOMB 

def new_item() -> Any:
    """Adds new item to all_items. Returns Sprite object."""
    difficulty = c.DIFFICULTY
    choice = choose_item(difficulty)
    if choice == i.RED_MUSHROOM: 
        return RedMushroom(img=c.IMG("redmushroom.png"))
    elif choice == i.GREEN_MUSHROOM:
        return GreenMushroom(img=c.IMG("greenmushroom.png"))
    elif choice == i.YOSHI_COIN: 
        return YoshiCoin(img=c.IMG("yoshicoinright.png"))
    elif choice == i.PIRAHNA_PLANT:
        return PirahnaPlant(img=c.IMG("pirahnaplantsmall.png"))
    elif choice == i.SPINY_BEETLE: 
        return SpinyBeetle(img=c.IMG("spinybeetlestandright.png"))
    elif choice == i.POW_BUTTON: 
        return PowButton(img=c.IMG("powbutton.png"))
    elif choice == i.BOMBOMB:
        return Bombomb(img=c.IMG("bombombstandright.png"))
    elif choice == i.FEATHER: 
        return Feather(img=c.IMG("feather.png"))
    elif choice == i.STAR: 
        return Star(img=c.IMG("star.png"))
    elif choice == i.QUESTION_BLOCK: 
        return QuestionBlock(img=c.IMG("questionblock.png"))
