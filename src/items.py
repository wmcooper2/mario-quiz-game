#stand lib
import math

#3rd party
import pyglet

#custom
from constants import *
from gameutil import *
from itemeffects import *

def update_items(items, dt):
    """Updates item positions on screen. Returns None."""
    for item in items:
        item.spot_x = ITEM_SPOTS[items.index(item)]
        item.update(dt)

class Item(pyglet.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.delta_x        = 0        
        self.delta_y        = 0
        self.falling        = False
        self.moving         = False
        self.trans          = False
        self.trans_dir      = True  #False = disappear
        self.spot_x         = self.x
        self.spot_y         = self.y
        self.x_speed        = ITEM_X_SPEED
        self.y_speed        = ITEM_Y_SPEED

        self.deltax         = lambda: self.x - self.spot_x
        self.deltay         = lambda: self.y - self.spot_y

    def update(self, dt):
        if self.falling: 
            global MAIN_TIME
            MAIN_TIME += dt
            if MAIN_TIME > 5: MAIN_TIME = 0
            self.y += gravity(MAIN_TIME)   #gameutil.py
        self.move() 
        if self.trans: self.transition()

    def transition(self):
        """Disappears/Appears item. Returns None."""
        if self.trans_dir:  self.opacity+=ITEM_TRANSITION_SPEED
        else:               self.opacity-=ITEM_TRANSITION_SPEED
        if self.opacity >= 255:
            self.opacity    = 255
            self.trans      = not self.trans
        elif self.opacity <= 0:
            self.opacity    = 0
            self.trans      = not self.trans

    def move(self): 
        """Moves the items closer to spot_x and spot_y. Returns None."""
        dx, dy = self.deltax, self.deltay
        self.change_pos(dx, dy)
        self.change_img(dx, dy)

    def change_pos(self, dx, dy):
        """Shifts the item's image horizontally. Returns None."""
        if dx() > 0: self.x -= self.x_speed
        if dx() < 0: self.x += self.x_speed
        if dy() > 0: self.y -= self.y_speed
        if dy() < 0: self.y += self.y_speed

    def change_img(self, dx, dy):
        #update sprite image
        if dx() != 0 and not self.moving:
            self.moving = not self.moving
            if dx() > 0:     self.image = self.animl 
            elif dx() < 0:   self.image = self.animr 
        elif dx() == 0:
            self.image  = self.anims
            self.moving = not self.moving

#Notes:
# each item has face, sequence, and animation attributes
# each of those has a right, left, and slow version

class RedMushroom(Item):
    """Random English vocab. Returns None."""
    facer, seqr, animr = sprite_con("redmushroom.png", 1, 1, "go")
    facel, seql, animl = sprite_con("redmushroom.png", 1, 1, "go")
    faces, seqs, anims = sprite_con("redmushroom.png", 1, 1, "go")
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def delete(self):
        super(Item, self).delete()

class GreenMushroom(Item):
    """Random verb form. Returns None."""
    facer, seqr, animr = sprite_con("greenmushroom.png", 1, 1, "go")
    facel, seql, animl = sprite_con("greenmushroom.png", 1, 1, "go")
    faces, seqs, anims = sprite_con("greenmushroom.png", 1, 1, "go")
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class YoshiCoin(Item):
    """Pronunciation question. Returns None."""
    facer, seqr, animr = sprite_con("yoshicoinright.png", 0.1, 5, "go")
    facel, seql, animl = sprite_con("yoshicoinleft.png", 0.1, 5, "go")
    faces, seqs, anims = sprite_con("yoshicoinright.png", 0.5, 5, "go")
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def delete(self):
        super(Item, self).delete()

class PirahnaPlant(Item):
    """Sentence translation (English to Japanese). Returns None."""
    facer, seqr, animr = sprite_con("pirahnaplantsmall.png", 0.2, 2, "go")
    facel, seql, animl = sprite_con("pirahnaplantsmall.png", 0.2, 2, "go")
    faces, seqs, anims = sprite_con("pirahnaplantsmall.png", 0.8, 2, "go")
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def delete(self):
        super(Item, self).delete()

class SpinyBeetle(Item): 
    """Question problem, 3rd year JHS at Bunkyo 9th. Returns None."""
    facer, seqr, animr = sprite_con("spinybeetlegoright.png",0.1,2,"go")
    facel, seql, animl = sprite_con("spinybeetlegoleft.png",0.1,2,"go")
    faces, seqs, anims = sprite_con("spinybeetlegoright.png",0.7,2,"go")

    #__init__ not needed?
    def delete(self):
        super(Item, self).delete()

class PowButton(Item):
    """Pow Button takes away one point from everyone. Returns None."""
    facer, seqr, animr = sprite_con("powbutton.png", 1, 1, "go")
    facel, seql, animl = sprite_con("powbutton.png", 1, 1, "go")
    faces, seqs, anims = sprite_con("powbutton.png", 1, 1, "go")
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def delete(self):
        super(Item, self).delete()

class Bombomb(Item):
    """Randomly mixes items. Returns None."""
    facer, seqr, animr = sprite_con("bombombgoright.png", 0.1, 2, "go")
    facel, seql, animl = sprite_con("bombombgoleft.png", 0.1, 2, "go")
    faces, seqs, anims = sprite_con("bombombgoright.png", 0.6, 2, "go")
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def delete(self):
        super(Item, self).delete()
        
#UNFINISHED BELOW THIS LINE
class QuestionBlock(Item):
    """Chooses a random effect. Returns None."""
    facer, seqr, animr = sprite_con("questionblock.png", 1, 4, "go")
    facel, seql, animl = sprite_con("questionblock.png", 1, 4, "go")
    faces, seqs, anims = sprite_con("questionblock.png", 1, 4, "go")
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def delete(self):
        super(Item, self).delete()

class Feather(Item):
    """Allows player to skip turn. Returns None."""
    facer, seqr, animr = sprite_con("feather.png", 1, 1, "go")
    facel, seql, animl = sprite_con("feather.png", 1, 1, "go")
    faces, seqs, anims = sprite_con("feather.png", 1, 1, "go")
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def delete(self):
        super(Item, self).delete()

class Star(Item):
    """Player avoids negative affects of other items. Returns None."""
    facer, seqr, animr = sprite_con("star.png", 1, 1, "go")
    facel, seql, animl = sprite_con("star.png", 1, 1, "go")
    faces, seqs, anims = sprite_con("star.png", 1, 1, "go")
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def delete(self):
        super(Item, self).delete()
