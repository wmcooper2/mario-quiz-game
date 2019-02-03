#stand lib
from math import sin, radians

#3rd party
import pyglet

#custom
from src.constants import *
from src.gameutil import *

class Background(pyglet.sprite.Sprite):
    background_img = pi("quiz1.png")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class Player(pyglet.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.delta_x    = 0
        self.inventory  = []
        self.item       = False
        self.moving     = False
        self.points     = 0
        self.point_index= 0
        self.rotating_players = False
        self.speed      = "walk"
        self.spot       = self.x #starts off screen, right 

    def update(self, dt):
        self.delta_x = self.delta()
        self.move()
        if self.has_item():
            self.inventory[0].y = self.height

    def has_item(self):
        """Checks if player has item. Returns None."""
        if len(self.inventory) == 0:  return False
        elif len(self.inventory) > 0: return True

    def game_in_play(self):
        """Sets self.game_just_started to False. Returns None."""
        GAME_JUST_STARTED = False

    def move(self):
        """Moves the player. Returns None."""
        if self.speed == "walk": self.walk()
        #other speed options removed

    def walk(self):
        """Walks the player left or right. Returns None."""
#        import pdb; pdb.set_trace()
        diff = self.delta()
        #update sprite image
        if diff != 0 and self.moving == False:
            self.moving = True
            if diff > 0: self.image = self.anim
            if diff < 0: self.image = self.anim
        elif diff == 0:
            if isinstance(self, FireLight):
                self.image = self.anim
            else:
                self.image = self.anim 
                self.moving = False
        if diff > 0 and diff > 3:           self.x -= 3
        elif diff > 0 and diff <= 3:        self.x -= 1
        elif diff < 0 and abs(diff) > 3:    self.x += 3
        elif diff < 0 and abs(diff) <= 3:   self.x += 1

    def delta(self):
        """Get x distance between two spots. Returns Integer."""
        return self.x - self.spot

class FloatingPlayer(Player):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.float_height = 0
        self.float_deg = 0

    def float(self):
        """Makes the character float. Returns None."""
        degrees             = self.float_deg
        self.float_height   = sin(radians(degrees))

        if degrees >= 359:      #reset float cycle
            self.float_deg      = 0
            self.float_height   = 0
        self.float_deg          += 1
        self.y                  = self.y+(self.float_height/FLOAT_SPEED) 

class WalkingPlayer(Player):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
class Yammy(pyglet.sprite.Sprite):
    faceright           = pi("yammy_stand_right.png")
    action_right_img    = pi("yammy_action_right.png")
    action_right_seq    = pg(action_right_img, 1, 2)
    action_right_anim   = pa(action_right_seq, 0.2, False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.inventory      = []
        self.trans          = False
        self.trans_dir      = "out"
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
                item.falling    = True          #reset flag 
                item.toggle_transition()        #fade out
                item.trans      = True          #set flag
            if item.y <= self.victim.y:
                item.falling    = False             #reset flag
                self.victim.inventory.append(item)  #give item
                self.inventory.remove(item)         #remove item

    def transition(self):
        """Toggles fading animation. Returns None."""
        td = self.trans_dir
        tr = self.trans_rate
        if td == "in":
            self.opacity += tr
        if td == "out":
            self.opacity -= tr
        if self.opacity >= 255:
            self.opacity = 255 
            self.trans = False  #reset flag
        if self.opacity <= 0:
            self.opacity = 0
            self.trans = False  #reset flag

    #item
    def transition_out(self):
        """Fades first inventory item out. Returns None."""
        self.inventory[0].opacity -=1

    #item
    def transition_in(self):
        """Fades first inventory item in. Returns None."""
        self.inventory[0].opacity += 1

    def toggle_transition(self):
        """Toggles trans_dir. Returns None."""
        td = self.trans_dir
        if td == "in":      td = "out"
        elif td == "out":   td = "in"

    def wave_wand(self):
        """Yammy waves his magic wand. Returns None."""
        self.image = self.action_right_anim

    def take_item(self, item):
        """Adds item to Yammy's inventory. Returns None."""
        self.inventory.append(item)

class FireLight(FloatingPlayer):
    face, seq, anim = sprite_con("firelightgoleft.png", 0.1, 2, "float")
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class BigBoo(FloatingPlayer):
    face, seq, anim = sprite_con("bigboogoleft.png", 0.1, 1, "float")
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class BigMole(WalkingPlayer):
    face, seq, anim = sprite_con("bigmolegoleft.png", 0.1, 2, "walk")
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class Dragon(WalkingPlayer):
    face, seq, anim = sprite_con("dragongoleft.png", 0.1, 2, "walk")
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class GreenKoopa(WalkingPlayer):
    face, seq, anim = sprite_con("greenkoopagoleft.png", 0.1, 2, "walk")
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class Luigi(WalkingPlayer):
    face, seq, anim = sprite_con("bigluigigoleft.png", 0.1, 2, "walk")
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class Mario(WalkingPlayer):
    face, seq, anim = sprite_con("bigmariogoleft.png", 0.1, 3, "walk")
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
