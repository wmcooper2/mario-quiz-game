#std lib
import math
import string as s
from string import ascii_lowercase as lowercase
from string import ascii_uppercase as uppercase
from string import ascii_letters as uppersandlowers
import random
from typing import Any, Callable, Tuple

#3rd party
import pyglet
from tabulate import tabulate

#custom
from constants import Constants as c

#TODO, rework tds import
import temporarydatasolution as tds
import util as u

all_sprites = c.IMG("allsprites2.png")
all_letters = c.IMG("letters.png")
data = tds.Data()

punc = {
    "!": {"x": 208, "y": 9},
    ".": {"x": 216, "y": 9},
    "-": {"x": 224, "y": 9},
    ",": {"x": 232, "y": 9},
    "?": {"x": 240, "y": 9},
    "#": {"x": 208, "y": 0},
    "(": {"x": 216, "y": 0},
    ")": {"x": 224, "y": 0},
    "'": {"x": 232, "y": 0},
}

#NOTE, a "Score" object (visually) is the player's mini sprite and the points
# points are represented visually with a number within the score object on screen

class Background(c.SPRITE):
    def __init__(self, *args, **kwargs):
        image = c.IMG("grassland.png")
        super().__init__(image, *args, *kwargs)
        self.batch = c.BACKGROUND_BATCH



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

        #points/scores
        self.points = 0
        self.index = 0
        self.score = None

        #other
        self.item = None
        self.scale = 1

    def update(self, dt):
        """Main update function called in the game loop."""
        self.dx = self.x - self.spot
        self.move()
        self.keep_item(self.dx)
        if self.points != self.score.value and c.SCORES:
            self.score.update(self)

    def center_walking_player(self, image: Any) -> None:
        """Centers the anchor point in the image."""
        image.anchor_x = image.width // 2

    def delete_item(self) -> None:
        """Delete player's item."""
        self.item.delete() #delete the item itself
        self.item = None   #remove reference to the item

    def keep_item(self, dx: int) -> None:
        """Move the inventory on screen to match the player's position.
            Item follows player on screen.
        """
        if dx < 0:
            self.trailing_left()
        else:
            self.trailing_right()

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

    def player_index(self) -> int:
        """Get index of player in c.PLAYERS."""
        self.index = c.PLAYERS.index(self)

    def set_score_x(self) -> None:
        """Assign x pos to self.score's sprite."""
        self.score.x = c.SCORE_SPOTS[self.index]

    def set_value_x(self) -> None:
        """Assign x pos to self.score's sprite."""
        self.score.number.x = c.SCORE_SPOTS[self.index] - c.POINT_X_OFFSET

    def set_score_number(self) -> None:
        """Set the score's number value."""
        self.score.value = 0

    def trailing_right(self) -> None:
        """Set player's item to trail on the right side."""
        if self.item:
            self.item.x, self.item.y = self._trail_right_pos(), self.y

    def trailing_left(self) -> None:
        """Set player's item to trail on the left side."""
        if self.item:
            self.item.x, self.item.y = self._trail_left_pos(), self.y

    def _trail_right_pos(self) -> int:
        """Calculate the item's trailing position for the right side of the player."""
        return self.x + self.width + 5

    def _trail_left_pos(self) -> int:
        """Calculate the item's trailing position for the left side of the player."""
        return self.x - self.item.width - 5

    def use_item(self) -> None:
        """Player uses their item."""
        if self.item:
            self.item.effect()                       
            self.item.poof()
            self.item = None

    def within_margin(self) -> Tuple[bool, bool]:
        """Checks if player within range of destination."""
        return abs(self.dx) <= self.x_speed

class FloatingPlayer(Player):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.float_height = 0
        self.float_deg = random.randrange(360)

    def center_floating_player(self, image: Any) -> None:
        """Centers the anchor point in the image."""
        image.anchor_x = image.width // 2
        image.anchor_y = image.height // 2

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
        self.left_seq = c.GRID(self.left, 1, 2)
#         self.left_anim = c.ANIM(self.left_seq, 0.1, False)  #not animated while standing 
        self.walk_right = c.IMG("firelightwalkright.png")
        self.walk_right_seq = c.GRID(self.walk_right, 1, 2)
        self.walk_right_anim = c.ANIM(self.walk_right_seq, 0.1, True)
        self.walk_left = c.IMG("firelightwalkleft.png")
        self.walk_left_seq = c.GRID(self.walk_left, 1, 2)
        self.walk_left_anim = c.ANIM(self.walk_left_seq, 0.1, True)
        self.left_anim = self.walk_left_anim

        super().__init__(self.left, *args, **kwargs)
        self.x=c.OFF_SCREEN_R
        self.y=c.FLOAT_H
        self.batch=c.PLAYER_BATCH

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
    def __init__(self, *args, **kwargs):
        self.left = c.IMG("bigboostandleft.png")
        #TODO, realign boo, too far right
#         self.center_floating_player(self.left)
        self.left_seq = c.GRID(self.left, 1, 1)
        self.left_anim = c.ANIM(self.left_seq, 1, False) 
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
        self.scale = 1.5

        #TODO, figure out why this method only works if within the __init__ block
        def mini_sprite(self) -> Any:
            """Makes mini-sprite version of self. Overrides base class method."""
            mini = Score(self)
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
        self.left_seq = c.GRID(self.left, 1, 1)
        self.left_anim = c.ANIM(self.left_seq, 1, False) 
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
        self.left_seq = c.GRID(self.left, 1, 1)
        self.left_anim = c.ANIM(self.left_seq, 1, False) 
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
        self.left_seq = c.GRID(self.left, 1,1)
        self.left_anim = c.ANIM(self.left_seq, 1, False) 
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
        self.left_seq = c.GRID(self.left, 1, 1)
        self.left_anim = c.ANIM(self.left_seq, 1, False)
        
        #attempting to use slices from a main spritesheet.
#         self.left = all_sprites.get_region(x=2, y=150, width=48, height=28)
#         self.left_seq = c.GRID(self.left, 1, 3)
#         self.left_anim = c.ANIM(self.left_seq, 1, True)

        self.walk_right = c.IMG("bigmariowalkright.png")
        self.walk_right_seq = c.GRID(self.walk_right, 1, 3)
        self.walk_right_anim = c.ANIM(self.walk_right_seq, 0.1, True)
        self.walk_left = c.IMG("bigmariowalkleft.png")
        self.walk_left_seq = c.GRID(self.walk_left, 1, 3)
#         self.walk_left_seq = c.GRID(self.left, 1, 3)
        self.walk_left_anim = c.ANIM(self.walk_left_seq, 0.1, True)

        super().__init__(self.left, *args, **kwargs)
        self.x=c.OFF_SCREEN_R
        self.y=c.WALK_H
        self.batch=c.PLAYER_BATCH
        self.scale = 2

class Luigi(WalkingPlayer):
    def __init__(self, *args, **kwargs):
#         self.left = c.IMG("bigluigistandleft.png")
        self.left = c.IMG("bigluigistandleft2.png")
        self.left_seq = c.GRID(self.left, 1, 1)
        self.left_anim = c.ANIM(self.left_seq, 1, False)

        self.walk_right = c.IMG("bigluigiwalkright2.png")
        self.walk_right_seq = c.GRID(self.walk_right, 1, 3)
        self.walk_right_anim = c.ANIM(self.walk_right_seq, 0.1, True)

        self.walk_left = c.IMG("bigluigiwalkleft2.png")
        self.walk_left_seq = c.GRID(self.walk_left, 1, 3)
        self.walk_left_anim = c.ANIM(self.walk_left_seq, 0.1, True)

        super().__init__(self.left, *args, **kwargs)
        self.x=c.OFF_SCREEN_R
        self.y=c.WALK_H
        self.batch=c.PLAYER_BATCH
        self.scale = 2

class Problem(c.LABEL):
#     english_vocab_guide = c.LABEL(text="Translate to Japanese", font_name=c.FONT, anchor_x="center",  x=center_x, y=center_y + 60, font_size=12)
#     english_sentence_guide = c.LABEL(text="Translate to Japanese", font_name=c.FONT, anchor_x="center",  x=center_x, y=center_y + 60, font_size=12)
#     present_verb_guide = c.LABEL(text="Translate to Japanese", font_name=c.FONT, anchor_x="center",  x=center_x, y=center_y + 60, font_size=12)
#     japanese_vocab_guide = c.LABEL(text="Translate to English", font_name=c.FONT, anchor_x="center",  x=center_x, y=center_y + 60, font_size=12)
#     pronunciation_guide = c.LABEL(text="Speak", font_name=c.FONT, anchor_x="center",  x=center_x, y=center_y + 60, font_size=12)
#     japanese_sentence_guide = c.LABEL(text="Translate to English", font_name=c.FONT, anchor_x="center",  x=center_x, y=center_y + 60, font_size=12)
#     answer_my_question_guide = c.LABEL(text="Answer the question", font_name=c.FONT, anchor_x="center",  x=center_x, y=center_y + 60, font_size=12)

#        self.past_verb_guide = c.LABEL(text="past verb guide", font_name=c.FONT, x=300, y=300, font_size=18)
#        self.japanese_translation_guide = c.LABEL(text="japanese translation guide", font_name=c.FONT, x=300, y=300, font_size=18)
#        self.target_sentence_guide = c.LABEL(text="target sentence guide", font_name=c.FONT, x=300, y=300, font_size=18)
#        self.image_guide = c.LABEL(text="image guide", font_name=c.FONT, x=300, y=300, font_size=18)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.img = c.IMG("blackbox.png")
        self.box = c.SPRITE(self.img, x=370, y=250)
        self.box.scale = 3
        self.center_x = (self.img.width // 2) + self.box.x
        self.center_y = (self.img.height // 2) + self.box.y
        self.showing = False
        self.decided = False
        self.letters = []        
        self.letter_scale = 3
        self.coords = {}
        self.adjustment_width = 0
        self.question = c.LABEL(
#             text="blank",
            font_name=c.FONT,
            x=self.center_x,
            y=self.center_y,
            font_size=24,
            width=self.box.width,
            batch=c.PROBLEM_BATCH)


        #setup alphabet image indices
        for letter in enumerate(lowercase):
            self.coords[letter[1]] = letter[0] * 8
        for letter in enumerate(uppercase):
            self.coords[letter[1]] = letter[0] * 8

    def random_question(self) -> str:
        """Get random question string."""
        choice = random.choice([
            self.eng_word,
            self.jap_word,
            self.jap_sentence,
            self.image_,
            self.sentence,
            self.present_verb,
            self.past_verb,
            self.pronunciation,
            self.verb_form])
        return choice()

    def lowercase_sprite(self, char) -> None:
        """Add lowercase sprite."""
        letter = c.SPRITE(
            all_letters.get_region(
                x=self.coords[char[1]],
                y=0,
                width=8,
                height=7),
            x=self.box.x+8*char[0]*self.letter_scale + self.adjustment_width,
#             x=self.box.x+8*char[0]*self.letter_scale,
#             x=self.box.x+8*char[0] + self.adjustment_width,
            y=self.box.y,
            batch=c.PROBLEM_BATCH)
        letter.scale = self.letter_scale
        self.letters.append(letter)








    #TODO
    def new_problem(self, text) -> None:
        """Setup a new problem."""

        def _clear_question_text() -> None:
            """Sets the question sprite's text to a blank string."""
            letters = []

        def _fits_on_one_line() -> bool:
            """Checks if question will fit on a single line within the inner box."""
            return question_length <= inner_box

        def _x_offset() -> int:
            """Calculates x offset of the question's text within the outer box."""
            return (self.box.width // 2) - (question_length // 2)

        def _is_ascii(char) -> bool:
            """Checks if char is a printable ascii character."""
            return char in s.printable

        _clear_question_text()
        question = text
        inner_box = self.box.width * .9     # 90% of the outer black box
        question_length = len(question)*8   # width of letter-sprite is 8px
        x_offset = 0

            


        #start here
        if _fits_on_one_line():
            for char in enumerate(question):
                text = char[1]
                text_index = char[0]
                if _is_ascii(text):
                    x_offset = _x_offset()

        #split question into words
        #for each word
            #calculate width
            #add width to total width of problem
            #if accumulated total width for the current line is too wide for black box
                # decrement the y-value to drop to the next line
            #for each letter in word
                #make a sprite and add it to the sprite list for this problem
                #make sure to add them to the batch

                    #TODO
                    # handle lowercase letters
                    if text in lowercase:
                        self.lowercase_sprite(char)

                    # handle uppercase letters
                    elif text in uppercase:
                        letter = c.SPRITE(
                            all_letters.get_region(
                                x = self.coords[text],
                                y = 8,
                                width = 8,
                                height = 8),
                            x = self.box.x + (8 * text_index * self.letter_scale) + x_offset,
                            y = self.box.y,
                            batch = c.PROBLEM_BATCH)
                        letter.scale = self.letter_scale
                        self.letters.append(letter)

                    # handle punctuation
                    elif text in punc:
                        letter = c.SPRITE(
                            all_letters.get_region(
                                x = punc[text]["x"],
                                y = punc[text]["y"],
                                width = 8,
                                height = 8),
                            x = self.box.x + (8 * text_index * self.letter_scale) + x_offset,
                            y = self.box.y,
                            batch = c.PROBLEM_BATCH)
                        letter.scale = self.letter_scale
                        self.letters.append(letter)

                else:
                    print("not printable...")
                    #probably japanese, just make a Label class sprite for now
        else:
            print("Need multiple lines.") 

        # reset the flag so that it doesn't keep choosing
        self.decided = True
 








    #TODO, remove this method, it was replaced with self.new_problem()
    def new_question(self) -> None:
        """Setup a new question."""
        self.letters = []                   #clear previous problem
        question = self.random_question()
        box_width = self.box.width * .9
        length = len(question)*8            #8px, width of letter-sprite

        #ensure question fits within the box's boundaries
        if length <= box_width:             #fits on one line
            for char in enumerate(question):
                if char[1] in s.printable:  #if is ascii
#                     print("printable char:", char)

                    #TODO, set the y pos and adjust to center x pos
                    self.adjustment_width = self.box.width // 2 - (len(question) // 2)
                    print("adjustment width:", self.adjustment_width)

        #split question into words
        #for each word
            #calculate width
            #add width to total width of problem
            #if accumulated total width for the current line is too wide for black box
                # decrement the y-value to drop to the next line
            #for each letter in word
                #make a sprite and add it to the sprite list for this problem
                #make sure to add them to the batch

                    #if lowercase
                    if char[1] in lowercase:
                        self.lowercase_sprite(char)

                    #if uppercase
                    elif char[1] in uppercase:
                        letter = c.SPRITE(
                            all_letters.get_region(
                                x=self.coords[char[1]],
                                y=8,
                                width=8,
                                height=8),
                            x=self.box.x+8*char[0]*self.letter_scale + self.adjustment_width,
#                             x=self.box.x+8*char[0]*self.letter_scale,
#                             x=self.box.x+8*char[0] + self.adjustment_width,
                            y=self.box.y,
                            batch=c.PROBLEM_BATCH)
                        letter.scale = self.letter_scale
                        self.letters.append(letter)

                    elif char[1] in punc:
                        letter = c.SPRITE(
                            all_letters.get_region(
                                x=punc[char[1]]["x"],
                                y=punc[char[1]]["y"],
                                width=8,
                                height=8),
                            x=self.box.x+8*char[0]*self.letter_scale + self.adjustment_width,
#                             x=self.box.x+8*char[0]*self.letter_scale,
#                             x=self.box.x+8*char[0] + self.adjustment_width,
                            y=self.box.y,
                            batch=c.PROBLEM_BATCH)
                        letter.scale = self.letter_scale
                        self.letters.append(letter)

                else:
                    print("not printable...")
                    #probably japanese, just make a Label class sprite for now
        else:
            print("Need multiple lines.") 
            
    def eng_word(self) -> str:
        """Chooses a random English vocabulary word."""
        return data.english_word()
    
    def image_(self) -> Any:
        """Chooses image."""
        return "image"
        #TODO, return GIF
#         self.question.text = "image word" 
        #need to change the size of the image to fit within the Vocab box dimensions
        #not completed in temporarydatasolution.py

    def jap_sentence(self) -> str:
        """Chooses Japanese target sentence."""
#         print("Get Japanese sentences.")
        return "Japanese sentence"
#        self.question.text = "日本"  #produces unexpected text
#        self.question.text = "\u65e5" + "u\672c"
#        self.question.text = "{&#26085}"
#        self.question.text = self.data.random_target_sentence_japanese()

    def jap_word(self) -> str:
        """Chooses Japanese vocabulary word."""
        eng = data.english_word()
        return data.japanese_word(eng)

    def past_verb(self) -> str:
        """Chooses verb's past form."""
        return data.random_past_verb() 

    def present_verb(self) -> str:
        """Chooses present-tense verb."""
        return data.random_verb() 

    def pronunciation(self) -> str:
        """Chooses pronunciation word."""
        return data.random_pronunciation() 

    def sentence(self) -> str:
        """Chooses target sentence."""
        return data.random_target_sentence() 

    def toggle(self) -> None:
        """Toggle the flag to show the black box."""
        self.showing = not self.showing

    def verb_form(self) -> str:
        """Chooses random verb."""
        return data.random_verb_form()

class Score(c.SPRITE):
    def __init__(self, player, *args, **kwargs):
        super().__init__(player.left_anim, *args, **kwargs)
        self.y = c.SCORE_SPRITE_Y
        self.batch = c.SCORE_BATCH
        self.player = player
        self.value = 0
        self.scale = 1.5 
        if isinstance(player, BigBoo):
            self.scale = 1 
        self.number = c.LABEL(
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

class Selector():
    def __init__(self, coords: list):
        self.pos = c.SPRITE(c.IMG("redmushroom.png"))
        coords.reverse()
        self.coords = coords

    def update(self, index: int) -> None:
        self.index = index
        self.pos.x = self.coords[self.index].x
        self.pos.y = self.coords[self.index].y
        self.pos.draw()
