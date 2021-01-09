#std lib
import math
from typing import Any, Tuple

#3rd party
import pyglet

#custom
from constants import constants as c
import util as u


class Background(c.SPRITE):
    background_img = c.IMG("grassland.png")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class Player(c.SPRITE):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #location
        self.spot = self.x  #initially off screen, changed immediately
        self.dx = 0         #intially zero, changed immediately
        self.dy = 0

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
        self.move()
        self.check_inventory()

    def center_floating_player(self, image: Any) -> None:
        """Centers the anchor point in the image."""
        image.anchor_x = image.width // 2
        image.anchor_y = image.height // 2

    def center_walking_player(self, image: Any) -> None:
        """Centers the anchor point in the image."""
        image.anchor_x = image.width // 2

    def check_inventory(self) -> None:
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
        elif dx == 0 and self.image != self.left_anim:
            self.image = self.left_anim 

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
    float_height = 0
    float_deg = 0

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def float(self) -> None:
        """Makes the character float up and down in place."""
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
#     stand_right = c.IMG("yammystandright.png")    
#     action_right_img = c.IMG("yammyactionright.png")
#     action_right_seq = c.GRID(action_right_img, 1, 2)
#     action_right_anim = c.ANIM(action_right_seq, 0.2, False)

    def __init__(self, img, *args, **kwargs):
        super().__init__(img, *args, **kwargs)
#         self.stand_right = c.IMG("yammystandright.png")    
        self.stand_right = img
        self.action_right_img = c.IMG("yammyactionright.png")
        self.action_right_seq = c.GRID(self.action_right_img, 1, 2)
        self.action_right_anim = c.ANIM(self.action_right_seq, 0.2, False)
        self.disappear = False
        self.disappear_rate = 3
        self.max_opacity = 255
        self.min_opacity = 0

#         self.img=self.stand_right
        self.x=30
        self.y=c.ITEM_PLATFORM_H
        self.batch=c.MAIN_BATCH
        self.scale = 2
        self.opacity = 0

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


#FLOATERS
class FireLight(FloatingPlayer):
    def __init__(self, img, *args, **kwargs):
        super().__init__(img, *args, **kwargs)
#         self.left = c.IMG("firelightwalkleft.png")
        self.left = img
        self.center_floating_player(self.left)
        self.left_seq = c.GRID(self.left, 1, 2)
        self.left_anim = c.ANIM(self.left_seq, 0.1, True)  #not animated while standing 
        self.walk_right = c.IMG("firelightwalkright.png")
        self.walk_right_seq = c.GRID(self.walk_right, 1, 2)
        self.walk_right_anim = c.ANIM(self.walk_right_seq, 0.1, True)
        self.walk_left = c.IMG("firelightwalkleft.png")
        self.walk_left_seq = c.GRID(self.walk_left, 1, 2)
        self.walk_left_anim = c.ANIM(self.walk_left_seq, 0.1, True)
    #     left_anim = c.ANIM(walk_left_seq, 0.1, True)  #Player animates while standing
        self.run_right_anim = c.ANIM(self.walk_right_seq, 0.05, True)
        self.run_left_anim = c.ANIM(self.walk_left_seq, 0.05, True)
#         self.img=self.walk_left_anim
        self.x=c.OFF_SCREEN_R
        self.y=c.FLOAT_H
        self.batch=c.MAIN_BATCH
        self.scale = 1.5

class BigBoo(FloatingPlayer):
    def __init__(self, img, *args, **kwargs):
        super().__init__(img, *args, **kwargs)
#         self.left = c.IMG("bigboostandleft.png")
        self.left = img
        self.center_floating_player(self.left)
        self.left_seq = c.GRID(self.left, 1, 1)
        self.left_anim = c.ANIM(self.left_seq, 1, True) 
        self.walk_right = c.IMG("bigboowalkright.png")
        self.walk_right_seq = c.GRID(self.walk_right, 1, 1)
        self.walk_right_anim = c.ANIM(self.walk_right_seq, 0.1, True)
        self.walk_left = c.IMG("bigboowalkleft.png")
        self.walk_left_seq = c.GRID(self.walk_left, 1, 1)
        self.walk_left_anim = c.ANIM(self.walk_left_seq, 0.1, True)
        self.run_right_anim = c.ANIM(self.walk_right_seq, 0.05, True)
        self.run_left_anim = c.ANIM(self.walk_left_seq, 0.05, True)
#         self.img=self.left
        self.x=c.OFF_SCREEN_R
        self.y=c.FLOAT_H
        self.batch=c.MAIN_BATCH

#WALKERS
class Dragon(WalkingPlayer):
    def __init__(self, img, *args, **kwargs):
        super().__init__(img, *args, **kwargs)
#         self.left = c.IMG("dragonstandleft.png")
        self.left = img
        self.center_walking_player(self.left)
        self.left_seq = c.GRID(self.left, 1, 1)
        self.left_anim = c.ANIM(self.left_seq, 1, True) 
        self.walk_right = c.IMG("dragonwalkright.png")
        self.walk_right_seq = c.GRID(self.walk_right, 1, 2)
        self.walk_right_anim = c.ANIM(self.walk_right_seq, 0.1, True)
        self.walk_left = c.IMG("dragonwalkleft.png")
        self.walk_left_seq = c.GRID(self.walk_left, 1, 2)
        self.walk_left_anim = c.ANIM(self.walk_left_seq, 0.1, True)
        self.run_right_anim = c.ANIM(self.walk_right_seq, 0.05, True)
        self.run_left_anim = c.ANIM(self.walk_left_seq, 0.05, True)

#         self.img=self.left
        self.x=c.OFF_SCREEN_R
        self.y=c.WALK_H
        self.batch=c.MAIN_BATCH
        self.scale = 2

class GreenKoopa(WalkingPlayer):
    def __init__(self, img, *args, **kwargs):
        super().__init__(img, *args, **kwargs)
#         self.left = c.IMG("greenkoopastandleft.png")
        self.left = img
        self.center_walking_player(self.left)
        self.left_seq = c.GRID(self.left, 1, 1)
        self.left_anim = c.ANIM(self.left_seq, 1, True) 
        self.walk_right = c.IMG("greenkoopawalkright.png")
        self.walk_right_seq = c.GRID(self.walk_right, 1, 2)
        self.walk_right_anim = c.ANIM(self.walk_right_seq, 0.1, True)
        self.walk_left = c.IMG("greenkoopawalkleft.png")
        self.walk_left_seq = c.GRID(self.walk_left, 1, 2)
        self.walk_left_anim = c.ANIM(self.walk_left_seq, 0.1, True)
        self.run_right_anim = c.ANIM(self.walk_right_seq, 0.05, True)
        self.run_left_anim = c.ANIM(self.walk_left_seq, 0.05, True)

#         self.img=self.left
        self.x=c.OFF_SCREEN_R
        self.y=c.WALK_H
        self.batch=c.MAIN_BATCH 
        self.scale = 2

class BigMole(WalkingPlayer):
    def __init__(self, img, *args, **kwargs):
        super().__init__(img, *args, **kwargs)
#         self.left = c.IMG("bigmolestandleft.png")
        self.left = c.IMG("bigmolestandleft.png")
        self.center_walking_player(self.left)
        self.left_seq = c.GRID(self.left, 1,1)
        self.left_anim = c.ANIM(self.left_seq, 1, True) 
        self.walk_right = c.IMG("bigmolewalkright.png")
        self.walk_right_seq = c.GRID(self.walk_right, 1, 2)
        self.walk_right_anim = c.ANIM(self.walk_right_seq, 0.1, True)
        self.walk_left = c.IMG("bigmolewalkleft.png")
        self.walk_left_seq = c.GRID(self.walk_left, 1, 2)
        self.walk_left_anim = c.ANIM(self.walk_left_seq, 0.1, True)
        self.run_right_anim = c.ANIM(self.walk_right_seq, 0.05, True)
        self.run_left_anim = c.ANIM(self.walk_left_seq, 0.05, True)

#         self.img=self.left
        self.x=c.OFF_SCREEN_R
        self.y=c.WALK_H
        self.batch=c.MAIN_BATCH
        self.scale = 1.5 

class Mario(WalkingPlayer):
    def __init__(self, img, *args, **kwargs):
        super().__init__(img, *args, **kwargs)
        self.left = img
        self.center_walking_player(self.left)
        self.left_seq = c.GRID(self.left, 1,1)
        self.left_anim = c.ANIM(self.left_seq, 1, True)
        self.walk_right = c.IMG("bigmariowalkright.png")
        self.walk_right_seq = c.GRID(self.walk_right, 1, 3)
        self.walk_right_anim = c.ANIM(self.walk_right_seq, 0.1, True)
        self.walk_left = c.IMG("bigmariowalkleft.png")
        self.walk_left_seq = c.GRID(self.walk_left, 1, 3)
        self.walk_left_anim = c.ANIM(self.walk_left_seq, 0.1, True)
        self.run_right_anim = c.ANIM(self.walk_right_seq, 0.05, True)
        self.run_left_anim = c.ANIM(self.walk_left_seq, 0.05, True)

#         self.img=self.left
        self.x=c.OFF_SCREEN_R
        self.y=c.WALK_H
        self.batch=c.MAIN_BATCH
        self.scale = 2

class Luigi(WalkingPlayer):
    def __init__(self, img, *args, **kwargs):
        super().__init__(img, *args, **kwargs)
#         self.left = c.IMG("bigluigistandleft.png")
        self.left = img
        self.center_walking_player(self.left)
        self.left_seq = c.GRID(self.left, 1,1)
        self.left_anim = c.ANIM(self.left_seq, 1, True)
        self.walk_right = c.IMG("bigluigiwalkright.png")
        self.walk_right_seq = c.GRID(self.walk_right, 1, 2)
        self.walk_right_anim = c.ANIM(self.walk_right_seq, 0.1, True)
        self.walk_left = c.IMG("bigluigiwalkleft.png")
        self.walk_left_seq = c.GRID(self.walk_left, 1, 2)
        self.walk_left_anim = c.ANIM(self.walk_left_seq, 0.1, True)
        self.run_right_anim = c.ANIM(self.walk_right_seq, 0.05, True)
        self.run_left_anim = c.ANIM(self.walk_left_seq, 0.05, True)
        
#         self.img=self.left
        self.x=c.OFF_SCREEN_R
        self.y=c.WALK_H
        self.batch=c.MAIN_BATCH
        self.scale = 2
