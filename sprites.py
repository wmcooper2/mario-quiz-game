#std lib
import math
import random
from typing import Any, Tuple

#3rd party
import pyglet

#custom
from constants import Constants as c

#TODO, rework tds import
import temporarydatasolution as tds
import util as u


#NOTE, a "Score" object (visually) is the player's mini sprite and the points
# points are represented visually with a number within the score object on screen


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
#         self.item = False

        #points/scores
        self.points = 0
        self.index = 0
        self.score = None

        #other
        self.item = None

    def update(self, dt):
        """Main update function called in the game loop."""
        self.dx = self.x - self.spot
        self.move()
        self.check_item()
#         if self.points != 0:
        if self.points != self.score.value:
            self.score.update(self)

    def center_walking_player(self, image: Any) -> None:
        """Centers the anchor point in the image."""
        image.anchor_x = image.width // 2

    def check_item(self) -> None:
        """Move the inventory on screen to match the player's position."""
        if self.item != None:
            item = self.item
            item.x, item.y = self.x, self.y

    def delete_item(self) -> None:
        """Delete player's item."""
        self.item.delete() #delete the item itself
        self.item = None   #remove reference to the item

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

    def use_item(self) -> None:
        """Player uses their item."""
        self.item = True
        item = self.item
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

    def center_floating_player(self, image: Any) -> None:
        """Centers the anchor point in the image."""
        image.anchor_x = image.width // 2
        image.anchor_y = image.height // 2

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

    def update(self, dt) -> None:
        """FireLight update loop. Overrides base class."""
        super().update(dt)
        self.float()

class BigBoo(FloatingPlayer):
    #TODO, make it so that bigboo doesn't float unless he is moving.
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

        #TODO, figure out why this method only works if within the __init__ block
        def mini_sprite(self) -> Any:
            """Makes mini-sprite version of self. Overrides base class method."""
            mini = Score(self)
            mini.scale = 0.5
            mini.image = self.walk_left_anim
            return mini

    def update(self, dt) -> None:
        """BigBoo update loop. Overrides base class."""
        super().update(dt)
        if self.dx != 0:
            self.float()

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

class Problem(pyglet.text.Label):
#     question_center_x = BOX_IMG.width // 2 + BOX.x
#     question_center_y = BOX_IMG.height // 2 + BOX.y
#     english_vocab_guide = pyglet.text.Label(text="Translate to Japanese", font_name="Comic Sans MS", anchor_x="center",  x=question_center_x, y=question_center_y + 60, font_size=12)
#     english_sentence_guide = pyglet.text.Label(text="Translate to Japanese", font_name="Comic Sans MS", anchor_x="center",  x=question_center_x, y=question_center_y + 60, font_size=12)
#     present_verb_guide = pyglet.text.Label(text="Translate to Japanese", font_name="Comic Sans MS", anchor_x="center",  x=question_center_x, y=question_center_y + 60, font_size=12)
#     japanese_vocab_guide = pyglet.text.Label(text="Translate to English", font_name="Comic Sans MS", anchor_x="center",  x=question_center_x, y=question_center_y + 60, font_size=12)
#     pronunciation_guide = pyglet.text.Label(text="Speak", font_name="Comic Sans MS", anchor_x="center",  x=question_center_x, y=question_center_y + 60, font_size=12)
#     japanese_sentence_guide = pyglet.text.Label(text="Translate to English", font_name="Comic Sans MS", anchor_x="center",  x=question_center_x, y=question_center_y + 60, font_size=12)
#     answer_my_question_guide = pyglet.text.Label(text="Answer the question", font_name="Comic Sans MS", anchor_x="center",  x=question_center_x, y=question_center_y + 60, font_size=12)
 
    def __init__(self, x=345, y=300, text="blank",  *args, **kwargs):
        super().__init__(*args, **kwargs)
#         BOX_IMG = pyglet.resource.image("blackbox.png")
        self.img = pyglet.resource.image("blackbox.png")
#         BOX = pyglet.sprite.Sprite(self.img, x=345, y=264)
        self.box = pyglet.sprite.Sprite(self.img, x=345, y=264)

#         self.q_x = Problem.question_center_x
#         self.q_y = Problem.question_center_y
#         self.question = pyglet.text.Label(text="blank", font_name="Comic Sans MS", x=self.q_x, y=self.q_y, font_size=24, width=self.BOX_IMG.width)
#         self.question.anchor_x = "center"
#         self.question.anchor_y = "center"
#         self.data = tds.Data()

#        self.past_verb_guide = pyglet.text.Label(text = "past verb guide", font_name = "Comic Sans MS", x = 300, y = 300, font_size = 18)
#        self.japanese_translation_guide = pyglet.text.Label(text = "japanese translation guide", font_name = "Comic Sans MS", x = 300, y = 300, font_size = 18)
#        self.target_sentence_guide= pyglet.text.Label(text = "target sentence guide", font_name = "Comic Sans MS", x = 300, y = 300, font_size = 18)
#        self.image_guide = pyglet.text.Label(text = "image guide", font_name = "Comic Sans MS", x = 300, y = 300, font_size = 18)
    
    def random_english_word(self):
        """Chooses a random English vocabulary word. Returns None."""
        #Student should translate the English word into Japanese
        random_word = self.data.english_word()
        basic_format = random_word + " "
        self.question.text = self.data.english_word() 

    def random_japanese_word(self):
        """Chooses a random Japanese vocabulary word. Returns None."""
        choice = self.data.english_word()
        self.question.text = self.data.japanese_word() 
    
    def random_image(self):
        """Chooses a random word and loads the associated image. Returns None."""
        self.question.text = "image word" 
        #need to change the size of the image to fit within the Vocab box dimensions
        #not completed in temporarydatasolution.py

    def random_present_verb(self):
        """Chooses random type of present-tense verb. Returns None."""
        self.question.text = self.data.random_verb() 

    def random_verb_form(self):
        """Chooses a random verb form from a random verb. Returns None."""
        self.question.text = self.data.random_verb_form()

    def random_past_verb(self):
        """Chooses a random verb's past form. Returns None."""
        self.question.text = self.data.random_past_verb() 
    
    def random_target_sentence(self):
        """Chooses a random target sentence. Returns None."""
        self.question.text = self.data.random_target_sentence() 

    def random_japanese_target_sentence(self):
        """Chooses a random Japanese target sentence. Returns None."""
        self.question.text = "Get Japanese sentences."
#        self.question.text = "日本"  #produces unexpected text
#        self.question.text = "\u65e5" + "u\672c"
#        self.question.text = "{&#26085}"
#        self.question.text = self.data.random_target_sentence_japanese()

    def random_pronunciation(self):
        """Chooses a random word that is difficult to pronuounce. Returns None."""
        self.question.text = self.data.random_pronunciation() 

    def random_question(self):
        """Chooses a random question. Returns None."""
        self.question.text = self.data.random_question()


class Score(c.SPRITE):
    def __init__(self, player, *args, **kwargs):
        super().__init__(player.left_anim, *args, **kwargs)
        self.y = c.SCORE_SPRITE_Y
        self.batch = c.SCORE_BATCH
        self.player = player
        self.value = 0
        self.number = pyglet.text.Label(
            text=str(self.value),
            y=self.y + c.POINT_Y_OFFSET,
            font_name=c.FONT,
            font_size=c.FONT_SIZE,
            batch=c.SCORE_BATCH)

    def update(self, player: Any) -> None:
        """Update the player's score."""
        #points
        if self.value != player.points:
            self.value = player.points
            self.number.text = str(self.value)
