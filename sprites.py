#std lib
import math
import random
from typing import Any, Tuple

#3rd party
import pyglet

#custom
from constants import constants as c
import util as u


#NOTE, a "Score" object (visually) is the mini sprite and the number-points
# points are the number of points within the score object


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

        #points/scores
        self.points = 0
        self.index = 0
#         self.score = Score(self)

        #other
        self.inventory = []

    def update(self, dt):
        """Main update function called in the game loop."""
        self.dx = self.x - self.spot
        self.move()
        self.check_inventory()
        if self.points != 0:
            self.score.update(self)

    def center_floating_player(self, image: Any) -> None:
        """Centers the anchor point in the image."""
        image.anchor_x = image.width // 2
        image.anchor_y = image.height // 2

    def center_walking_player(self, image: Any) -> None:
        """Centers the anchor point in the image."""
        image.anchor_x = image.width // 2

    def check_inventory(self) -> None:
        """Move the inventory on screen to match the player's position."""
        if self == c.P1:
            print("inventory?:", self.inventory)
            if self.inventory:
                item = self.inventory
                item.x, item.y = self.x, self.y

    def game_in_play(self):
        """Sets c.GAME_JUST_STARTED to False. Returns None."""
        c.GAME_JUST_STARTED = False

    def player_index(self) -> int:
        """Get index of player in c.PLAYERS."""
        self.index = c.PLAYERS.index(self)

    def mini_sprite(self) -> None:
        """Make a mini sprite from self."""
        self.score = Score(self)

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

    def set_score_x(self) -> None:
        """Assign x pos to self.score's sprite."""
        self.score.x = c.SCORE_SPOTS[self.index]

    def set_value_x(self) -> None:
        """Assign x pos to self.score's sprite."""
        self.score.number.x = c.SCORE_SPOTS[self.index] - c.POINT_X_OFFSET

    def set_score_number(self) -> None:
        """Set the score's number value."""
        self.score.value = 0

    def use_item(self):
        """Player uses the item in their inventory. Returns None."""
        self.item = True
        item = self.inventory[0]
        if item.item_not_used == True:
            item.effect()                       
            item.item_not_used = False          #dont need to reset to False, instance is destroyed after use. 

    def within_margin(self) -> Tuple[bool, bool]:
        """Checks if player within range of destination."""
        return abs(self.dx) <= self.x_speed

class FloatingPlayer(Player):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.float_height = 0
        self.float_deg = random.randrange(360)

    def float(self) -> None:
        """Makes the character float up and down in place."""
        degrees = math.radians(self.float_deg)
        self.float_height = math.sin(degrees)
        if self.float_deg == 360:
            self.float_deg = 0
            self.float_height = 0
        self.float_deg += 1
        self.y = self.y + (self.float_height / 3) 

class WalkingPlayer(Player):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class Yammy(c.SPRITE):
    def __init__(self, *args, **kwargs):
        self.right = c.IMG("yammystandright.png")
        self.action_right = c.IMG("yammyactionright.png")
        self.action_right_seq = c.GRID(self.action_right, 1, 2)
        self.action_right_anim = c.ANIM(self.action_right_seq, 0.2, False)
        self.disappear = False
        self.disappear_rate = 3
        self.max_opacity = 255
        self.min_opacity = 0

        super().__init__(self.right, *args, **kwargs)
        self.x=30
        self.y=c.ITEM_PLATFORM_H
        self.batch=c.YAMMY_BATCH
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
    def __init__(self, *args, **kwargs):
        self.left = c.IMG("firelightwalkleft.png")
        self.center_floating_player(self.left)
        self.left_seq = c.GRID(self.left, 1, 2)
        self.left_anim = c.ANIM(self.left_seq, 0.1, True)  #not animated while standing 
        self.walk_right = c.IMG("firelightwalkright.png")
        self.walk_right_seq = c.GRID(self.walk_right, 1, 2)
        self.walk_right_anim = c.ANIM(self.walk_right_seq, 0.1, True)
        self.walk_left = c.IMG("firelightwalkleft.png")
        self.walk_left_seq = c.GRID(self.walk_left, 1, 2)
        self.walk_left_anim = c.ANIM(self.walk_left_seq, 0.1, True)

        super().__init__(self.left, *args, **kwargs)
        self.x=c.OFF_SCREEN_R
        self.y=c.FLOAT_H
        self.batch=c.PLAYER_BATCH
        self.scale = 1.5

        def mini_sprite(self) -> Any:
            """Makes mini-sprite version of self. Overrides base class method."""
            mini = Score(self)
            mini.y -= 5                             #readjusted for score_display only
            mini.image = self.left_anim
            return mini

class BigBoo(FloatingPlayer):
    def __init__(self, *args, **kwargs):
        self.left = c.IMG("bigboostandleft.png")
        self.center_floating_player(self.left)
        self.left_seq = c.GRID(self.left, 1, 1)
        self.left_anim = c.ANIM(self.left_seq, 1, True) 
        self.walk_right = c.IMG("bigboowalkright.png")
        self.walk_right_seq = c.GRID(self.walk_right, 1, 1)
        self.walk_right_anim = c.ANIM(self.walk_right_seq, 0.1, True)
        self.walk_left = c.IMG("bigboowalkleft.png")
        self.walk_left_seq = c.GRID(self.walk_left, 1, 1)
        self.walk_left_anim = c.ANIM(self.walk_left_seq, 0.1, True)

        super().__init__(self.left, *args, **kwargs)
        self.x=c.OFF_SCREEN_R
        self.y=c.FLOAT_H
        self.batch=c.PLAYER_BATCH

        def mini_sprite(self) -> Any:
            """Makes mini-sprite version of self. Overrides base class method."""
            mini = Score(self)
            mini.scale = 0.5
            mini.image = self.walk_left_anim
            return mini

#WALKERS
class Dragon(WalkingPlayer):
    def __init__(self, *args, **kwargs):
        self.left = c.IMG("dragonstandleft.png")
        self.center_walking_player(self.left)
        self.left_seq = c.GRID(self.left, 1, 1)
        self.left_anim = c.ANIM(self.left_seq, 1, True) 
        self.walk_right = c.IMG("dragonwalkright.png")
        self.walk_right_seq = c.GRID(self.walk_right, 1, 2)
        self.walk_right_anim = c.ANIM(self.walk_right_seq, 0.1, True)
        self.walk_left = c.IMG("dragonwalkleft.png")
        self.walk_left_seq = c.GRID(self.walk_left, 1, 2)
        self.walk_left_anim = c.ANIM(self.walk_left_seq, 0.1, True)

        super().__init__(self.left, *args, **kwargs)
        self.x=c.OFF_SCREEN_R
        self.y=c.WALK_H
        self.batch=c.PLAYER_BATCH
        self.scale = 2

class GreenKoopa(WalkingPlayer):
    def __init__(self, *args, **kwargs):
        self.left = c.IMG("greenkoopastandleft.png")
        self.center_walking_player(self.left)
        self.left_seq = c.GRID(self.left, 1, 1)
        self.left_anim = c.ANIM(self.left_seq, 1, True) 
        self.walk_right = c.IMG("greenkoopawalkright.png")
        self.walk_right_seq = c.GRID(self.walk_right, 1, 2)
        self.walk_right_anim = c.ANIM(self.walk_right_seq, 0.1, True)
        self.walk_left = c.IMG("greenkoopawalkleft.png")
        self.walk_left_seq = c.GRID(self.walk_left, 1, 2)
        self.walk_left_anim = c.ANIM(self.walk_left_seq, 0.1, True)

        super().__init__(self.left, *args, **kwargs)
        self.x=c.OFF_SCREEN_R
        self.y=c.WALK_H
        self.batch=c.PLAYER_BATCH
        self.scale = 2

class BigMole(WalkingPlayer):
    def __init__(self, *args, **kwargs):
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

        super().__init__(self.left, *args, **kwargs)
        self.x=c.OFF_SCREEN_R
        self.y=c.WALK_H
        self.batch=c.PLAYER_BATCH
        self.scale = 1.5 

class Mario(WalkingPlayer):
    def __init__(self, *args, **kwargs):
        self.left = c.IMG("bigmariostandleft.png")
        self.center_walking_player(self.left)
        self.left_seq = c.GRID(self.left, 1,1)
        self.left_anim = c.ANIM(self.left_seq, 1, True)
        self.walk_right = c.IMG("bigmariowalkright.png")
        self.walk_right_seq = c.GRID(self.walk_right, 1, 3)
        self.walk_right_anim = c.ANIM(self.walk_right_seq, 0.1, True)
        self.walk_left = c.IMG("bigmariowalkleft.png")
        self.walk_left_seq = c.GRID(self.walk_left, 1, 3)
        self.walk_left_anim = c.ANIM(self.walk_left_seq, 0.1, True)

        super().__init__(self.left, *args, **kwargs)
        self.x=c.OFF_SCREEN_R
        self.y=c.WALK_H
        self.batch=c.PLAYER_BATCH
        self.scale = 2

class Luigi(WalkingPlayer):
    def __init__(self, *args, **kwargs):
        self.left = c.IMG("bigluigistandleft.png")
        self.center_walking_player(self.left)
        self.left_seq = c.GRID(self.left, 1,1)
        self.left_anim = c.ANIM(self.left_seq, 1, True)
        self.walk_right = c.IMG("bigluigiwalkright.png")
        self.walk_right_seq = c.GRID(self.walk_right, 1, 2)
        self.walk_right_anim = c.ANIM(self.walk_right_seq, 0.1, True)
        self.walk_left = c.IMG("bigluigiwalkleft.png")
        self.walk_left_seq = c.GRID(self.walk_left, 1, 2)
        self.walk_left_anim = c.ANIM(self.walk_left_seq, 0.1, True)

        super().__init__(self.left, *args, **kwargs)
        self.x=c.OFF_SCREEN_R
        self.y=c.WALK_H
        self.batch=c.PLAYER_BATCH
        self.scale = 2


#SCORES
class Coin(c.SPRITE):
    def __init__(self, *args, **kwargs):
        self.coin = c.IMG("yellowcoin.png")
#         coin_img = c.IMG("yellowcoin.png")
#         coin_seq = c.GRID(coin_img, 1, 3)
        super().__init__(self.coin, *args, **kwargs)

class Skull(c.SPRITE):
    def __init__(self, *args, **kwargs):
        self.skull = c.IMG("skull.png") 
#         skull_img = c.IMG("skull.png") 
#         skull_seq = c.GRID(skull_img, 1, 1)
        super().__init__(self.skull, *args, **kwargs)

class Score(c.SPRITE):
    def __init__(self, player, *args, **kwargs):
        super().__init__(player.left_anim, *args, **kwargs)
        self.y = c.SCORE_SPRITE_Y
        self.batch = c.SCORE_BATCH
        self.player = player
#         self.value_x = 0
        self.value = 0
        self.number = pyglet.text.Label(
            text=str(self.value),
#             x=0,
            y=self.y,
            font_name=c.FONT,
            font_size=c.FONT_SIZE,
            batch=c.SCORE_BATCH)

    def update(self, player: Any) -> None:
        """Update the player's score."""
        #points
        if self.value != player.points:
            self.value = player.points
            self.number.text = str(self.value)
        
        #sprite
        #add item to player's sprite so the player doesn't "carry" it around







#     def change_points(self, player) -> None:
#         """Changes score's points to match the associated player's points."""
#         if self.points < player.points:
#             self.points += 1
#         elif self.points > player.points:
#             self.points -= 1


#         self.populate_score_spots(score_object)

#         if self.points != player.points:
#             self.delete_score()                     
#             self.change_points(player)              
#             self.set_score_images()


#     def populate_score_spots(self, score_object) -> None:
#         """Setup of the score spots."""
#         #populate self.small_score_spots_coins
#         if not self.small_score_spots_coins:                  
#             self.make_small_score_spots_coins(score_object)    
# 
#         #populate self.small_score_spots_skulls
#         if not self.small_score_spots_skulls:                   
#             self.make_small_score_spots_skulls(score_object)     
# 
#         #populate self.big_score_spots
#         if not self.big_score_spots:                     
#             self.make_big_score_spots(score_object)

#     def make_small_score_spots_coins(self, score_object):
#         """Sets spots for self.small_score_spots_coins. Returns None."""
#         start = score_object.x - 36
#         for x in range(5):
#             self.small_score_spots_coins.append(start + (x * 12)) #coin width = 12

#     def make_small_score_spots_skulls(self, score_object):
#         """Sets spots for self.small_score_spots_skulls. Returns None."""
#         start = score_object.x - 36
#         for x in range(5):
#             self.small_score_spots_skulls.append(start + (x * 16)) #skull width = 16

#     def make_big_score_spots(self, score_object):
#         """Sets spots for self.big_score_spots. Returns None."""
#         start = score_object.x - 36
#         for x in range(3):
#             self.big_score_spots.append(start + (x * 30))

#     def delete_score(self):
#         """Deletes the sprites that are the displayed score. Returns None."""
#         points = self.points                #Score.points
#         if points > 5:
#             self.delete_big_score()
#         elif points <= 5 and points > 0:
#             self.delete_small_score()
#         elif points == 0:
#             self.delete_zero_score()
#         elif points < 0 and points >= -5:
#             self.delete_small_score()
#         elif points < -5:
#             self.delete_big_score()

#     def delete_big_score(self):
#         """Deletes contents of big_score. Returns None."""
#         self.big_score = []

#     def delete_small_score(self):
#         """Deletes small_score. Returns None."""
#         self.small_score = []

#     def delete_zero_score(self):
#         """Deletes the zero score. Returns None."""
#         self.zero.text = ""

#     def set_score_images(self):
#         """Adds the proper score sprites for the given point range. Returns None."""
#         points = self.points                #Score.points
#         if points > 5:
#             self.make_big_score_coin()
#         elif points <= 5 and points > 0:
#             self.make_small_score_coins()
#         elif points == 0:
#             self.make_zero_score()
#         elif points < 0 and points >= -5:
#             self.make_small_score_skulls()
#         elif points < -5:
#             self.make_big_score_skull()

#     def make_big_score_coin(self):
#         """Assembles the big score of coins. Returns None."""
#         self.big_score.append(
#             Coin(
#                 img=Coin.coin,
#                 x=self.big_score_spots[0],
#                 y=self.score_y,
#                 batch=c.MAIN_BATCH))
#         self.big_score[0].scale = 1.5
#         self.big_score.append(
#             pyglet.text.Label(
#                 text="x",x=self.big_score_spots[1],
#                 y=self.score_y,
#                 font_name="Comic Sans MS",
#                 font_size=24,
#                 batch=c.MAIN_BATCH))
#         self.big_score.append(
#             pyglet.text.Label(
#                 text=str(self.points),
#                 x=self.big_score_spots[2],
#                 y=self.score_y,
#                 font_name="Comic Sans MS",
#                 font_size=24,
#                 batch=c.MAIN_BATCH))

#     def make_small_score_coins(self):
#         """Assembles the small score of coins. Returns None."""
#         for x in range(self.points):
#             self.small_score.append(
#                 Coin(
#                     img=Coin.coin,
#                     x=self.small_score_spots_coins[x],
#                     y=self.score_y,
#                     batch=c.MAIN_BATCH))
 
#     def make_zero_score(self):
#         """Assembles the zero score. Returns None."""
#         self.zero.text = "0"

#     def make_small_score_skulls(self):
#         """Assembles the small score of skulls. Returns None."""
#         for x in range(abs(self.points)):
#             self.small_score.append(
#                 Skull(
#                     img=Skull.skull,
#                     x=self.small_score_spots_skulls[x],
#                     y=self.score_y,
#                     batch=c.MAIN_BATCH))

#     def make_big_score_skull(self):
#         """Assembles the big score of skulls. Returns None."""
#         self.big_score.append(
#               Skull(
#                     img=Skull.skull,
#                     x=self.big_score_spots[0],
#                     y=self.score_y,
#                     batch=c.MAIN_BATCH))
#         self.big_score[0].scale = 1.5 
#         self.big_score.append(
#             pyglet.text.Label(
#                 text="x",
#                 x=self.big_score_spots[1],
#                 y=self.score_y,
#                 font_name="Comic Sans MS",
#                 font_size=24,
#                 batch=c.MAIN_BATCH))
#         self.big_score.append(
#             pyglet.text.Label(
#                 text=str(abs(self.points)),
#                 x=self.big_score_spots[2],
#                 y=self.score_y,
#                 font_name="Comic Sans MS",
#                 font_size=24,
#                 batch=c.MAIN_BATCH))
