#std lib
from collections import namedtuple
import enum

#custom
from constants import Constants as c
import sprites as s

Coord = namedtuple("Coord", ["x", "y"])

class OptionsScreen():
    def __init__(self):
        self.coords = [Coord(50, i) for i in range(500, 200, -50)]
        self.background = c.SPRITE(c.IMG("blackbox.png"))
        self.background.scale = 6

        self.difficulty_label = c.SPRITE(c.IMG("Difficulty.png"))
        self.difficulty_label.scale = 1.5
        self.difficulty_label.x = self.coords[0].x
        self.difficulty_label.y = self.coords[0].y

        self.scores_label = c.SPRITE(c.IMG("Scores.png"))
        self.scores_label.scale = 1.5
        self.scores_label.x = self.coords[1].x
        self.scores_label.y = self.coords[1].y

        self.timer_label = c.SPRITE(c.IMG("Timer.png"))
        self.timer_label.scale = 1.5
        self.timer_label.x = self.coords[2].x
        self.timer_label.y = self.coords[2].y

        self.music_label = c.SPRITE(c.IMG("Music.png"))
        self.music_label.scale = 1.5
        self.music_label.x = self.coords[3].x
        self.music_label.y = self.coords[3].y

        self.questions_label = c.SPRITE(c.IMG("Questions.png"))
        self.questions_label.scale = 1.5
        self.questions_label.x = self.coords[4].x
        self.questions_label.y = self.coords[4].y

        self.items_label = c.SPRITE(c.IMG("Items.png"))
        self.items_label.scale = 1.5
        self.items_label.x = self.coords[5].x
        self.items_label.y = self.coords[5].y

        self.selector = s.Selector(self.coords)

    def update(self) -> None:
        self.background.draw()
        self.difficulty_label.draw()
        self.scores_label.draw()
        self.timer_label.draw()
        self.music_label.draw()
        self.questions_label.draw()
        self.items_label.draw()
        self.selector.update()

    def selector_up(self) -> None:
        self.selector.up()
        
    def selector_down(self) -> None:
        self.selector.down()
