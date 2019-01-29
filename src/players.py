#stand lib
import math

#3rd party
import pyglet

#custom
from src.constants import *
from src.gameutil import *

class Background(pyglet.sprite.Sprite):
    background_img = pyglet.resource.image("quiz1.png")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class Player(pyglet.sprite.Sprite):
    pi, pg, pa = image_res()    #pyglet; gameutil.py

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
        self.spot       = self.x #players start off screen, right 

    def update(self, dt):
        self.delta_x = self.delta
        if GAME_JUST_STARTED:
            self.speed = "run"
        if self.spot is PLAYER_SPOTS[-1]: #the ready position
            self.speed = "run"
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
        if self.speed == "walk":
            self.walk()
        if self.speed == "run":
            self.run()

    def walk(self):
        """Walks the player left or right. Returns None."""
        diff = self.delta
        #update sprite image
        if diff != 0 and self.moving == False:
            self.moving = True
            if diff > 0:
                self.image = self.walk_left_anim
            if diff < 0:
                self.image = self.walk_right_anim
        elif diff == 0:
            self.image = self.stand_left_anim 
            self.moving = False
        #move left or right
        if diff > 0:
            self.x -= 1
        if diff < 0:
            self.x += 1

    def run(self):
        """Runs the player left or right. Returns None."""
        diff = self.delta()
        #update sprite image
        if diff != 0 and self.moving == False:
            self.moving = True
            if diff > 0:
                self.image = self.run_left_anim
            if diff < 0:
                self.image = self.run_right_anim
        elif diff == 0:
            self.image = self.stand_left_anim 
            self.moving = False
            self.speed = "walk"
        #move left or right
        if diff > 0 and diff > 3:
            self.x -= 3
        if diff > 0 and diff <= 3:
            self.x -= 1
        if diff < 0 and abs(diff) > 3:
            self.x += 3
        if diff < 0 and abs(diff) <= 3:
            self.x += 1

    def delta(self):
        """Get x distance between two spots. Returns Integer."""
        return self.x - self.spot

class FloatingPlayer(Player):
    float_height = 0
    float_deg = 0

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def float(self):
        """Makes the character float. Returns None."""
        radians = math.radians(FloatingPlayer.float_deg)
        FloatingPlayer.float_height = math.sin(radians)
        if FloatingPlayer.float_deg == 360:
            FloatingPlayer.float_deg = 0
            FloatingPlayer.float_height = 0
        FloatingPlayer.float_deg += 1
        self.y = self.y + (FloatingPlayer.float_height / 3) 

class WalkingPlayer(Player):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
class Yammy(pyglet.sprite.Sprite):
    stand_right         = Player.pi("yammy_stand_right.png")
    action_right_img    = Player.pi("yammy_action_right.png")
    action_right_seq    = Player.pg(action_right_img, 1, 2)
    action_right_anim   = Player.pa(action_right_seq, 0.2, False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.inventory              = []
        self.transition_direction   = "out"
        self.transitioning          = False
        self.transition_rate        = 3
        self.victim                 = "" 

    def update(self):
        """Yammy's main update loop. Returns None."""
        self.transition()
        self.give_item()
    
    def transition(self):
        """Toggles fading animation. Returns None."""
        td = self.transition_direction
        tr = self.transition_rate
        if self.transitioning:
            if td == "in":
                self.opacity += tr
            if td == "out":
                self.opacity -= tr
            if self.opacity >= 255:
                self.opacity = 255 
                self.transitioning = False  #reset flag
            if self.opacity <= 0:
                self.opacity = 0
                self.transitioning = False  #reset flag

    def transition_out(self):
        """Fades first inventory item out. Returns None."""
        self.inventory[0].opacity -=1

    def transition_in(self):
        """Fades first inventory item in. Returns None."""
        self.inventory[0].opacity += 1

    def toggle_transition_direction(self):
        """Toggles transition_direction. Returns None."""
        td = self.transition_direction
        if td == "in":      td = "out"
        elif td == "out":   td = "in"

    def wave_wand(self):
        """Yammy waves his magic wand. Returns None."""
        self.image = self.action_right_anim

    def take_item(self, item):
        """Adds item to Yammy's inventory. Returns None."""
        self.inventory.append(item)

    def give_item(self):
        """Gives an item to a player. Returns String."""
        if self.inventory:
            item = self.inventory[0]
            if item.opacity == 0 and item.delta_y == 0:
                item.spot_x = self.victim.spot
                item.x = self.victim.spot
                item.falling = True                 #reset flag 
                item.toggle_transition_direction()  #fade out
                item.transitioning = True           #set flag
            if item.y <= self.victim.y:
                item.falling = False                #reset flag
                self.victim.inventory.append(item)  #give item
                self.inventory.remove(item)         #remove item

class FireLight(FloatingPlayer):
    #standing
    stand_left = Player.pi("fire_light_walk_left.png")
    center_floater(stand_left)
    stand_left_seq = Player.pg(stand_left, 1, 2)
    stand_left_anim = Player.pa(stand_left_seq, 0.1, True) 

    #to the right
    walk_right = Player.pi("fire_light_walk_right.png")
    walk_right_seq = Player.pg(walk_right, 1, 2)
    walk_right_anim = Player.pa(walk_right_seq, 0.1, True)
    run_right_anim = Player.pa(walk_right_seq, 0.05, True)

    #to the left
    walk_left = Player.pi("fire_light_walk_left.png")
    walk_left_seq = Player.pg(walk_left, 1, 2)
    walk_left_anim = Player.pa(walk_left_seq, 0.1, True)
    run_left_anim = Player.pa(walk_left_seq, 0.05, True)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class Dragon(WalkingPlayer):
    #standing
    stand_left      = Player.pi("dragon_stand_left.png")
    center_walker(stand_left)
    stand_left_seq  = Player.pg(stand_left, 1, 1)
    stand_left_anim = Player.pa(stand_left_seq, 1, True) 

    #to the right
    walk_right      = Player.pi("dragon_walk_right.png")
    walk_right_seq  = Player.pg(walk_right, 1, 2)
    walk_right_anim = Player.pa(walk_right_seq, 0.1, True)
    run_right_anim  = Player.pa(walk_right_seq, 0.05, True)

    #to the left
    walk_left       = Player.pi("dragon_walk_left.png")
    walk_left_seq   = Player.pg(walk_left, 1, 2)
    walk_left_anim  = Player.pa(walk_left_seq, 0.1, True)
    run_left_anim   = Player.pa(walk_left_seq, 0.05, True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class BigBoo(FloatingPlayer):
    #standing
    stand_left      = Player.pi("big_boo_stand_left.png")
    center_floater(stand_left)
    stand_left_seq  = Player.pg(stand_left, 1, 1)
    stand_left_anim = Player.pa(stand_left_seq, 1, True) 

    #to the right
    walk_right      = Player.pi("big_boo_walk_right.png")
    walk_right_seq  = Player.pg(walk_right, 1, 1)
    walk_right_anim = Player.pa(walk_right_seq, 0.1, True)

    #to the left
    walk_left       = Player.pi("big_boo_walk_left.png")
    walk_left_seq   = Player.pg(walk_left, 1, 1)
    walk_left_anim  = Player.pa(walk_left_seq, 0.1, True)
    run_right_anim  = Player.pa(walk_right_seq, 0.05, True)
    run_left_anim   = Player.pa(walk_left_seq, 0.05, True)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class GreenKoopa(WalkingPlayer):
    #standing
    stand_left      = Player.pi("green_koopa_stand_left.png")
    center_walker(stand_left)
    stand_left_seq  = Player.pg(stand_left, 1, 1)
    stand_left_anim = Player.pa(stand_left_seq, 1, True) 

    #to the right
    walk_right      = Player.pi("green_koopa_walk_right.png")
    walk_right_seq  = Player.pg(walk_right, 1, 2)
    walk_right_anim = Player.pa(walk_right_seq, 0.1, True)
    run_right_anim  = Player.pa(walk_right_seq, 0.05, True)

    #to the left
    walk_left       = Player.pi("green_koopa_walk_left.png")
    walk_left_seq   = Player.pg(walk_left, 1, 2)
    walk_left_anim  = Player.pa(walk_left_seq, 0.1, True)
    run_left_anim   = Player.pa(walk_left_seq, 0.05, True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class BigMole(WalkingPlayer):
    #standing
    stand_left      = Player.pi("big_mole_stand_left.png")
    center_walker(stand_left)
    stand_left_seq  = Player.pg(stand_left, 1,1)
    stand_left_anim = Player.pa(stand_left_seq, 1, True) 

    #to the right
    walk_right      = Player.pi("big_mole_walk_right.png")
    walk_right_seq  = Player.pg(walk_right, 1, 2)
    walk_right_anim = Player.pa(walk_right_seq, 0.1, True)
    run_right_anim  = Player.pa(walk_right_seq, 0.05, True)

    #to the left
    walk_left       = Player.pi("big_mole_walk_left.png")
    walk_left_seq   = Player.pg(walk_left, 1, 2)
    walk_left_anim  = Player.pa(walk_left_seq, 0.1, True)
    run_left_anim   = Player.pa(walk_left_seq, 0.05, True)
 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class Mario(WalkingPlayer):
    #standing
    stand_left      = Player.pi("big_mario_stand_left.png")
    center_walker(stand_left)
    stand_left_seq  = Player.pg(stand_left, 1,1)
    stand_left_anim = Player.pa(stand_left_seq, 1, True)
    
    #to the right
    walk_right_img  = Player.pi("big_mario_walk_right.png")
    walk_right_seq  = Player.pg(walk_right_img, 1, 3)
    walk_right_anim = Player.pa(walk_right_seq, 0.1, True)
    run_right_anim  = Player.pa(walk_right_seq, 0.05, True)
    
    #to the left
    walk_left_img   = Player.pi("big_mario_walk_left.png")
    walk_left_seq   = Player.pg(walk_left_img, 1, 3)
    walk_left_anim  = Player.pa(walk_left_seq, 0.1, True)
    run_left_anim   = Player.pa(walk_left_seq, 0.05, True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class Luigi(WalkingPlayer):
    #standing
    stand_left      = Player.pi("big_luigi_stand_left.png")
    center_walker(stand_left)
    stand_left_seq  = Player.pg(stand_left, 1,1)
    stand_left_anim = Player.pa(stand_left_seq, 1, True)

    #to the right
    walk_right_img  = Player.pi("big_luigi_walk_right.png")
    walk_right_seq  = Player.pg(walk_right_img, 1, 2)
    walk_right_anim = Player.pa(walk_right_seq, 0.1, True)
    run_right_anim  = Player.pa(walk_right_seq, 0.05, True)

    #to the left
    walk_left_img   = Player.pi("big_luigi_walk_left.png")
    walk_left_seq   = Player.pg(walk_left_img, 1, 2)
    walk_left_anim  = Player.pa(walk_left_seq, 0.1, True)
    run_left_anim   = Player.pa(walk_left_seq, 0.05, True)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
