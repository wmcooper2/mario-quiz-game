#std lib
import math
from typing import Tuple

#3rd party
import pyglet

#custom
from constants import constants as c
import util


class Background(c.SPRITE):
    background_img = c.IMG("grassland.png")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class Player(c.SPRITE):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #location
        self.spot = self.x      #initially off screen, changed immediately
        self.dx = 0        #intially zero, changed immediately

        #speed
        self.x_speed = c.PLAYER_X_SPEED
        self.y_speed = c.PLAYER_Y_SPEED

        #flags
        self.rotating_players = False
        self.item = False

        #other
        self.inventory = []
        self.points = 0
        self.point_index = 0

    def update(self, dt):
        """Main update function called in the game loop."""
        self.dx = self.x - self.spot
        #TODO, make util.Line.player_spots[-1] into "main_position"
#         if c.GAME_JUST_STARTED or self.spot == util.Line.player_spots[-1]:
#             self.speed = "run"
#         if self.spot == util.Line.player_spots[-1]: #if the player is in the ready position
#             self.speed = "run"
        self.move()

        if self.inventory:
            item = self.inventory
            item.x, item.y = self.x, self.y

    def use_item(self):
        """Player uses the item in their inventory. Returns None."""
        self.item = True
        item = self.inventory[0]
        if item.item_not_used == True:
            item.effect()                       
            item.item_not_used = False          #dont need to reset to False, instance is destroyed after use. 

    def game_in_play(self):
        """Sets c.GAME_JUST_STARTED to False. Returns None."""
        c.GAME_JUST_STARTED = False

    def move(self) -> None: 
        """Moves the players closer to dest_x and dest_y."""
        dx = self.dx
        if dx != 0:
            if dx > 0 and self.image != self.walk_left_anim:
                self.image = self.walk_left_anim
            elif dx < 0 and self.image != self.walk_right_anim:
                self.image = self.walk_right_anim
        elif dx == 0 and self.image != self.stand_left_anim:
            self.image = self.stand_left_anim 

        if dx > 0:
            self.x -= self.x_speed
        elif dx < 0:
            self.x += self.x_speed

        #if player within range of the speed "step", then just make delta == 0
        close_x = self.within_margin()
        if close_x:
            self.x = self.spot

    def within_margin(self) -> Tuple[bool, bool]:
        """Checks if player within range of destination."""
        return abs(self.dx) <= self.x_speed


class FloatingPlayer(Player):
    """Creates a player that floats cyclicly in the air."""    
 
    float_height = 0
    float_deg = 0

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def float(self):
        """Makes the character float up and down in place.
            Returns None."""
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
        
class Yammy(c.SPRITE):
    
    stand_right = c.IMG("yammystandright.png")    
    action_right_img = c.IMG("yammyactionright.png")
    action_right_seq = c.GRID(action_right_img, 1, 2)
    action_right_anim = c.ANIM(action_right_seq, 0.2, False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.disappear = False
        self.disappear_rate = 3
        self.max_opacity = 255
        self.min_opacity = 0

    def update(self) -> None:
        """Yammy's main update loop."""
        self.disappear_animation()

    def toggle_disappear(self) -> None:
        """Toggle self.disappear flag."""
        if self.opacity <= self.min_opacity or self.opacity >= self.max_opacity:
            self.disappear = not self.disappear

    def disappear_animation(self) -> None:
        """Make Yammy disappear/reappear."""
        if self.disappear:
            self.opacity -= self.disappear_rate
        else:
            self.opacity += self.disappear_rate
        if self.opacity >= self.max_opacity:
            self.opacity = self.max_opacity
        elif self.opacity <= self.min_opacity:
            self.opacity = self.min_opacity

    def wave_wand(self) -> None:
        """Yammy waves his magic wand."""
        self.image = self.action_right_anim

class FireLight(FloatingPlayer):
    stand_left = c.IMG("firelightwalkleft.png")
    util.center_floating_player(stand_left)
    stand_left_seq = c.GRID(stand_left, 1, 2)
    stand_left_anim = c.ANIM(stand_left_seq, 0.1, True)  #Player not animated while standing 
    walk_right = c.IMG("firelightwalkright.png")
    walk_right_seq = c.GRID(walk_right, 1, 2)
    walk_right_anim = c.ANIM(walk_right_seq, 0.1, True)
    walk_left = c.IMG("firelightwalkleft.png")
    walk_left_seq = c.GRID(walk_left, 1, 2)
    walk_left_anim = c.ANIM(walk_left_seq, 0.1, True)
#     stand_left_anim = c.ANIM(walk_left_seq, 0.1, True)  #Player animates while standing
    run_right_anim = c.ANIM(walk_right_seq, 0.05, True)
    run_left_anim = c.ANIM(walk_left_seq, 0.05, True)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class Dragon(WalkingPlayer):
    stand_left = c.IMG("dragonstandleft.png")
    util.center_walking_player(stand_left)
    stand_left_seq = c.GRID(stand_left, 1, 1)
    stand_left_anim = c.ANIM(stand_left_seq, 1, True) 
    walk_right = c.IMG("dragonwalkright.png")
    walk_right_seq = c.GRID(walk_right, 1, 2)
    walk_right_anim = c.ANIM(walk_right_seq, 0.1, True)
    walk_left = c.IMG("dragonwalkleft.png")
    walk_left_seq = c.GRID(walk_left, 1, 2)
    walk_left_anim = c.ANIM(walk_left_seq, 0.1, True)
    run_right_anim = c.ANIM(walk_right_seq, 0.05, True)
    run_left_anim = c.ANIM(walk_left_seq, 0.05, True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class BigBoo(FloatingPlayer):
    stand_left = c.IMG("bigboostandleft.png")
    util.center_floating_player(stand_left)
    stand_left_seq = c.GRID(stand_left, 1, 1)
    stand_left_anim = c.ANIM(stand_left_seq, 1, True) 
    walk_right = c.IMG("bigboowalkright.png")
    walk_right_seq = c.GRID(walk_right, 1, 1)
    walk_right_anim = c.ANIM(walk_right_seq, 0.1, True)
    walk_left = c.IMG("bigboowalkleft.png")
    walk_left_seq = c.GRID(walk_left, 1, 1)
    walk_left_anim = c.ANIM(walk_left_seq, 0.1, True)
    run_right_anim = c.ANIM(walk_right_seq, 0.05, True)
    run_left_anim = c.ANIM(walk_left_seq, 0.05, True)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class GreenKoopa(WalkingPlayer):
    stand_left = c.IMG("greenkoopastandleft.png")
    util.center_walking_player(stand_left)
    stand_left_seq = c.GRID(stand_left, 1, 1)
    stand_left_anim = c.ANIM(stand_left_seq, 1, True) 
    walk_right = c.IMG("greenkoopawalkright.png")
    walk_right_seq = c.GRID(walk_right, 1, 2)
    walk_right_anim = c.ANIM(walk_right_seq, 0.1, True)
    walk_left = c.IMG("greenkoopawalkleft.png")
    walk_left_seq = c.GRID(walk_left, 1, 2)
    walk_left_anim = c.ANIM(walk_left_seq, 0.1, True)
    run_right_anim = c.ANIM(walk_right_seq, 0.05, True)
    run_left_anim = c.ANIM(walk_left_seq, 0.05, True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class BigMole(WalkingPlayer):
    stand_left = c.IMG("bigmolestandleft.png")
    util.center_walking_player(stand_left)
    stand_left_seq = c.GRID(stand_left, 1,1)
    stand_left_anim = c.ANIM(stand_left_seq, 1, True) 
    walk_right = c.IMG("bigmolewalkright.png")
    walk_right_seq = c.GRID(walk_right, 1, 2)
    walk_right_anim = c.ANIM(walk_right_seq, 0.1, True)
    walk_left = c.IMG("bigmolewalkleft.png")
    walk_left_seq = c.GRID(walk_left, 1, 2)
    walk_left_anim = c.ANIM(walk_left_seq, 0.1, True)
    run_right_anim = c.ANIM(walk_right_seq, 0.05, True)
    run_left_anim = c.ANIM(walk_left_seq, 0.05, True)
 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class Mario(WalkingPlayer):
    stand_left = c.IMG("bigmariostandleft.png")
    util.center_walking_player(stand_left)
    stand_left_seq = c.GRID(stand_left, 1,1)
    stand_left_anim = c.ANIM(stand_left_seq, 1, True)
    walk_right_img = c.IMG("bigmariowalkright.png")
    walk_right_seq = c.GRID(walk_right_img, 1, 3)
    walk_right_anim = c.ANIM(walk_right_seq, 0.1, True)
    walk_left_img = c.IMG("bigmariowalkleft.png")
    walk_left_seq = c.GRID(walk_left_img, 1, 3)
    walk_left_anim = c.ANIM(walk_left_seq, 0.1, True)
    run_right_anim = c.ANIM(walk_right_seq, 0.05, True)
    run_left_anim = c.ANIM(walk_left_seq, 0.05, True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class Luigi(WalkingPlayer):
    stand_left = c.IMG("bigluigistandleft.png")
    util.center_walking_player(stand_left)
    stand_left_seq = c.GRID(stand_left, 1,1)
    stand_left_anim = c.ANIM(stand_left_seq, 1, True)
    walk_right_img = c.IMG("bigluigiwalkright.png")
    walk_right_seq = c.GRID(walk_right_img, 1, 2)
    walk_right_anim = c.ANIM(walk_right_seq, 0.1, True)
    walk_left_img = c.IMG("bigluigiwalkleft.png")
    walk_left_seq = c.GRID(walk_left_img, 1, 2)
    walk_left_anim = c.ANIM(walk_left_seq, 0.1, True)
    run_right_anim = c.ANIM(walk_right_seq, 0.05, True)
    run_left_anim = c.ANIM(walk_left_seq, 0.05, True)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

def yammy_sprite():       #not a playing character
    yammy = Yammy(img=Yammy.stand_right, x=30, y=c.ITEM_PLATFORM_H, batch=c.MAIN_BATCH)
    yammy.scale = 2
    yammy.opacity = 0
    return yammy

def firelight_sprite():
    fire_light = FireLight(img=FireLight.walk_left_anim, x=c.OFF_SCREEN_R, y=c.FLOAT_H, batch=c.MAIN_BATCH)
    fire_light.scale = 1.5
    return fire_light

def dragon_sprite():
    dragon = Dragon(img=Dragon.stand_left, x=c.OFF_SCREEN_R, y=c.WALK_H, batch=c.MAIN_BATCH)
    dragon.scale = 2
    return dragon

def bigboo_sprite():
    big_boo = BigBoo(img=BigBoo.stand_left, x=c.OFF_SCREEN_R, y=c.FLOAT_H, batch=c.MAIN_BATCH)
    return big_boo

def greenkoopa_sprite():
    green_koopa = GreenKoopa(img=GreenKoopa.stand_left, x=c.OFF_SCREEN_R, y=c.WALK_H, batch=c.MAIN_BATCH) 
    green_koopa.scale = 2
    return green_koopa

def bigmole_sprite():
    big_mole = BigMole(img=BigMole.stand_left, x=c.OFF_SCREEN_R, y=c.WALK_H, batch=c.MAIN_BATCH)
    big_mole.scale = 1.5 
    return big_mole

def mario_sprite():
    mario = Mario(img=Mario.stand_left, x=c.OFF_SCREEN_R, y=c.WALK_H, batch=c.MAIN_BATCH)
    mario.scale = 2
    return mario

def luigi_sprite():
    luigi = Luigi(img=Luigi.stand_left, x=c.OFF_SCREEN_R, y=c.WALK_H, batch=c.MAIN_BATCH)
    luigi.scale = 2
    return luigi
