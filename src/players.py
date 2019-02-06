#import pdb; pdb.set_trace()

#stand lib
from math import sin, radians

#3rd party
import pyglet

#custom
from src.constants import *
from src.gameutil import *

class Player(pyglet.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.inventory  = []
#        self.item       = False     #check gameutil.py, item_clean_up()
        self.points     = 0
        self.point_index= 0
        self.spot       = self.x    #starts off screen, right 
        self.delta      = lambda: self.x - self.spot

    def update(self, dt):
        self.move()
        self.take_item()

    def take_item(self):
        """Sets player's item to player's pos. Returns None."""
        if self.inventory: self.inventory[0].y = self.height

    def move(self):
        """Walks the player left or right. Returns None."""
        diff = self.delta()
        self.change_img(diff)
        self.change_pos(diff)
    
    def change_img(self, diff):
        """Changes sprite's image. Returns None."""
        if diff > 0:    self.image = self.animl
        elif diff < 0:  self.image = self.animr
        elif diff == 0:
            if isinstance(self, FireLight): self.image = self.animl
            else:                           self.image = self.animl

    def change_pos(self, diff):
        """Shifts the player's image horizontally. Returns None."""
        if diff > 0 and diff > 3:           self.x -= 3
        elif diff > 0 and diff <= 3:        self.x -= 1
        elif diff < 0 and abs(diff) > 3:    self.x += 3
        elif diff < 0 and abs(diff) <= 3:   self.x += 1

class FloatingPlayer(Player):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.float_height   = 0
        self.float_deg      = 0

    def float(self):
        """Makes the character float. Returns None."""
        degrees                 = self.float_deg
        self.float_height       = sin(radians(degrees))
        if degrees >= 359:      #reset float cycle
            self.float_deg      = 0
            self.float_height   = 0
        self.float_deg          += 1
        self.y                  = self.y+(self.float_height/FLOAT_SPEED) 

class WalkingPlayer(Player):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class FireLight(FloatingPlayer):
    facer, seqr, animr = sprite_con("firelightgoright.png",0.1,2,"float")
    facel, seql, animl = sprite_con("firelightgoleft.png",0.1,2,"float")
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class BigBoo(FloatingPlayer):
    facer, seqr, animr = sprite_con("bigboogoleft.png", 0.1, 1, "float")
    facel, seql, animl = sprite_con("bigboogoleft.png", 0.1, 1, "float")
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class BigMole(WalkingPlayer):
    facer, seqr, animr = sprite_con("bigmolegoright.png", 0.1, 2, "walk")
    facel, seql, animl = sprite_con("bigmolegoleft.png", 0.1, 2, "walk")
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class Dragon(WalkingPlayer):
    facer, seqr, animr = sprite_con("dragongoright.png", 0.1, 2, "walk")
    facel, seql, animl = sprite_con("dragongoleft.png", 0.1, 2, "walk")
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class GreenKoopa(WalkingPlayer):
    facer, seqr, animr = sprite_con("greenkoopagoright.png",0.1,2,"walk")
    facel, seql, animl = sprite_con("greenkoopagoleft.png",0.1,2,"walk")
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class Luigi(WalkingPlayer):
    facer, seqr, animr = sprite_con("bigluigigoright.png", 0.1, 2, "walk")
    facel, seql, animl = sprite_con("bigluigigoleft.png", 0.1, 2, "walk")
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class Mario(WalkingPlayer):
    facer, seqr, animr = sprite_con("bigmariogoright.png", 0.1, 3, "walk")
    facel, seql, animl = sprite_con("bigmariogoleft.png", 0.1, 3, "walk")
    def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
         
class Yammy(pyglet.sprite.Sprite):
    faceright           = pi("yammyfaceright.png")
    action_right_img    = pi("yammyactionright.png")
    action_right_seq    = pg(action_right_img, 1, 2)
    action_right_anim   = pa(action_right_seq, 0.2, False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.inventory      = []
        self.trans          = False
        self.trans_dir      = False
        self.trans_rate     = 3
        self.victim         = "" 

    def update(self, dt):
        """Yammy's main update loop. Returns None."""
        if self.trans: self.transition()
        self.give_item()
        items = self.inventory
        if items:                     #only if len() > 0
            items[0].update(dt)       #update the item
            items[0].transition()     #transition the item

    def give_item(self):
        """Gives an item to a player. Returns String."""
        if self.inventory:
            item = self.inventory[0]
            if item.opacity == 0 and item.delta_y == 0:
                item.spot_x     = self.victim.spot
                item.x          = self.victim.spot
                item.falling    = not item.falling
                item.trans_dir  = not item.trans_dir
                item.trans      = not item.trans
            if item.y <= self.victim.y:
                item.falling    = not item.falling
                self.victim.inventory.append(item)  #give item
                self.inventory.remove(item)         #remove item

    def transition(self):
        """Toggles fading animation. Returns None."""
        td, tr = self.trans_dir, self.trans_rate
        if td:          self.opacity += tr
        elif not td:    self.opacity -= tr
        if self.opacity >= 255:
            self.opacity = 255 
            self.trans = not self.trans
        elif self.opacity <= 0:
            self.opacity = 0
            self.trans = not self.trans

    #item
    def transition_out(self):
        """Fades first inventory item out. Returns None."""
        self.inventory[0].opacity -=1

    #item
    def transition_in(self):
        """Fades first inventory item in. Returns None."""
        self.inventory[0].opacity += 1

    def wave_wand(self):
        """Yammy waves his magic wand. Returns None."""
        self.image = self.action_right_anim

    def take_item(self, item):
        """Adds item to Yammy's inventory. Returns None."""
        self.inventory.append(item)

