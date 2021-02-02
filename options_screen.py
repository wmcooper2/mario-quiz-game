#std lib
from collections import namedtuple
import enum

#3rd party
import pyglet

#custom
from constants import Constants as c
from constants import Difficulty
import sprites as s

Coord = namedtuple("Coord", ["x", "y"])

class Difficulties():
    def __init__(self, y):
        self.y = y
        self.coords = [Coord(i, self.y) for i in range(300, 900, 200)]
        self.choices = Difficulty
        self.batch = pyglet.graphics.Batch()

        self._easy = c.LABEL("EASY", x=self.coords[0][0], y=self.coords[0][1], font_size=c.FONT_SIZE, color=c.WHITE, bold=True, batch=self.batch)
        self._easy = c.LABEL("NORMAL", x=self.coords[1][0], y=self.coords[1][1], font_size=c.FONT_SIZE, color=c.WHITE, bold=True, batch=self.batch)
        self._easy = c.LABEL("HARD", x=self.coords[2][0], y=self.coords[2][1], font_size=c.FONT_SIZE, color=c.WHITE, bold=True, batch=self.batch)
# 

    def update(self):
        self.batch.draw()
    

class OnOff():
    def __init__(self, y):
        self.y = y
        self.on = c.LABEL("ON", x=300, y=self.y, font_size=c.FONT_SIZE, color=c.WHITE, bold=True)
        self.off = c.LABEL("OFF", x=400, y=self.y, font_size=c.FONT_SIZE, color=c.WHITE, bold=True)
        #TODO, if true...set c.PROBLEM_TIMER = True

    def update(self):
        self.on.draw()
        self.off.draw()

#TODO
class HighlightBox():
    def __init__(self, x, y, w, h):
        #x1, y1, x2, y2 for lines
        self.bottom = ((x, y), (x+w, y))
        #TODO
        self.top = (x, y, w, h)
        self.left = (x, y, w, h)
        self.right = (x, y, w, h)
#         self.batch = batch...
        #self.left = pyglet.shapes.Line(x1,y1,x2,y2, batch=self.batch)

    def update(self):
        if self.is_highlighting:
            self.batch.draw()
            

class OptionsScreen():
    def __init__(self):
        self.label_x = 50
        self.label_x_offset = 35

        #coords step value is space between labels
        # 2 wide-spaced coords for question and item options
        self.coords = [Coord(self.label_x, i) for i in range(500, 300, -50)]
        self.coords.append(Coord(self.label_x, 250))
        self.coords.append(Coord(self.label_x, 150))

        #convenience variables
        self._diff_pos = self.coords[0]
        self._score_pos = self.coords[1]
        self._timer_pos = self.coords[2]
        self._music_pos = self.coords[3]
        self._quest_pos = self.coords[4]
        self._items_pos = self.coords[5]



        self.background = c.SPRITE(c.IMG("blackbox.png"))
        self.background.scale = 6

        self.difficulty_label = c.LABEL("Difficulty", font_size=c.FONT_SIZE, color=c.WHITE, bold=True)
        self.difficulty_label.x = self._diff_pos.x + self.label_x_offset
        self.difficulty_label.y = self._diff_pos.y
        self.difficulty_choices = Difficulties(self._diff_pos.y)

        self.scores_label = c.LABEL("Scores", font_size=c.FONT_SIZE, color=c.WHITE, bold=True)
        self.scores_label.x = self._score_pos.x + self.label_x_offset
        self.scores_label.y = self._score_pos.y
        self.score_on_off = OnOff(self._score_pos.y)

        self.timer_label = c.LABEL("Timer", font_size=c.FONT_SIZE, color=c.WHITE, bold=True)
        self.timer_label.x = self._timer_pos.x + self.label_x_offset
        self.timer_label.y = self._timer_pos.y
        self.timer_on_off = OnOff(self._timer_pos.y)

        self.music_label = c.LABEL("Music", font_size=c.FONT_SIZE, color=c.WHITE, bold=True)
        self.music_label.x = self._music_pos.x + self.label_x_offset
        self.music_label.y = self._music_pos.y
        self.music_on_off = OnOff(self._music_pos.y)

        self.questions_label = c.LABEL("Questions", font_size=c.FONT_SIZE, color=c.WHITE, bold=True)
        self.questions_label.x = self._quest_pos.x + self.label_x_offset
        self.questions_label.y = self._quest_pos.y

        self.items_label= c.LABEL("Items", font_size=c.FONT_SIZE, color=c.WHITE, bold=True)
        self.items_label.x = self._items_pos.x + self.label_x_offset
        self.items_label.y = self._items_pos.y

        self.selector = s.Selector(self.coords)
        self.selector.pos.scale = 2

    def update(self) -> None:
        self.background.draw()
        self.difficulty_label.draw()
        self.scores_label.draw()
        self.score_on_off.update()
        self.timer_label.draw()
        self.timer_on_off.update()
        self.music_label.draw()
        self.music_on_off.update()
        self.questions_label.draw()
        self.items_label.draw()
        self.selector.update()
        self.difficulty_choices.update()

    def selector_up(self) -> None:
        self.selector.up()
        
    def selector_down(self) -> None:
        self.selector.down()
