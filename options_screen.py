#std lib
from collections import namedtuple
import enum

#3rd party
import pyglet

#custom
from constants import Constants as c
from constants import Difficulty as d
from constants import QuestionTypes
import sprites as s

Coord = namedtuple("Coord", ["x", "y"])


class Placeholder():
    def __init__(self, y):
        self.y = y
        self.label_width = 100
        self.label_height = 50
        self.horizontal_index = 0
        self.coords = [Coord(i, self.y) for i in range(300, 500, 100)]
        self.batch = pyglet.graphics.Batch()
        self.highlight = HighlightBox(
            self.coords[self.horizontal_index],
            self.label_width,
            self.label_height)
        self.temp1 = c.LABEL("temp1",
            x=self.coords[0].x,
            y=self.y,
            font_size=c.FONT_SIZE,
            color=c.WHITE,
            bold=True,
            batch=self.batch)
        self.temp2 = c.LABEL("temp2",
            x=self.coords[1].x,
            y=self.y,
            font_size=c.FONT_SIZE,
            color=c.WHITE,
            bold=True,
            batch=self.batch)

    def left(self) -> None:
        self.horizontal_index -= 1
        if self.horizontal_index < 0:
            self.horizontal_index = len(self.coords) - 1 

    def right(self) -> None:
        self.horizontal_index += 1
        if self.horizontal_index >= len(self.coords):
            self.horizontal_index = 0

    def update(self):
        self.batch.draw()
        self.highlight.update(self.coords[self.horizontal_index])

class Difficulties():
    def __init__(self, y):
        self.y = y
        self.label_width = 200
        self.label_height = 50
        self.coords = [Coord(i, self.y) for i in range(300, 900, 200)]
        self.choices = d
        self.horizontal_index = 0
        self.batch = pyglet.graphics.Batch()
        self.highlight = HighlightBox(
            self.coords[self.horizontal_index],
            self.label_width,
            self.label_height)
        self._easy = c.LABEL("EASY",
            x=self.coords[0][0],
            y=self.coords[0][1],
            font_size=c.FONT_SIZE,
            color=c.WHITE,
            bold=True,
            batch=self.batch)
        self._normal = c.LABEL("NORMAL",
            x=self.coords[1][0],
            y=self.coords[1][1],
            font_size=c.FONT_SIZE,
            color=c.WHITE,
            bold=True,
            batch=self.batch)
        self._hard = c.LABEL("HARD",
            x=self.coords[2][0],
            y=self.coords[2][1],
            font_size=c.FONT_SIZE,
            color=c.WHITE,
            bold=True,
            batch=self.batch)

    def left(self) -> None:
        self.horizontal_index -= 1
        if self.horizontal_index < 0:
            self.horizontal_index = len(self.coords) - 1 

    def right(self) -> None:
        self.horizontal_index += 1
        if self.horizontal_index >= len(self.coords):
            self.horizontal_index = 0

    def update(self):
        self.batch.draw()

        #pass in new coord to reposition the highlight
        self.highlight.update(self.coords[self.horizontal_index])

        #update constants.py value
        if self.horizontal_index == 0:
            c.DIFFICULTY = d.EASY
        elif self.horizontal_index == 1:
            c.DIFFICULTY = d.MEDIUM
        elif self.horizontal_index == 2:
            c.DIFFICULTY = d.HARD

class OnOff():
    #TODO, if true...set c.PROBLEM_TIMER = True
    def __init__(self, y):
        self.y = y
        self.label_width = 100
        self.label_height = 50
        self.horizontal_index = 0
        self.coords = [Coord(i, self.y) for i in range(300, 500, 100)]
        self.batch = pyglet.graphics.Batch()
        self.highlight = HighlightBox(
            self.coords[self.horizontal_index],
            self.label_width,
            self.label_height)
        self.on = c.LABEL("ON",
            x=self.coords[0].x,
            y=self.y,
            font_size=c.FONT_SIZE,
            color=c.WHITE,
            bold=True,
            batch=self.batch)
        self.off = c.LABEL("OFF",
            x=self.coords[1].x,
            y=self.y,
            font_size=c.FONT_SIZE,
            color=c.WHITE,
            bold=True,
            batch=self.batch)

    def left(self) -> None:
        self.horizontal_index -= 1
        if self.horizontal_index < 0:
            self.horizontal_index = len(self.coords) - 1 

    def right(self) -> None:
        self.horizontal_index += 1
        if self.horizontal_index >= len(self.coords):
            self.horizontal_index = 0

    def update(self):
        self.batch.draw()
        self.highlight.update(self.coords[self.horizontal_index])

class HighlightBox():
    def __init__(self, coord: Coord, w: int, h: int):
        self.coord = coord
        self.w = w
        self.h = h
        self.margin = 6
        self.thickness = 6
        self.batch = pyglet.graphics.Batch()
        self.bottom = pyglet.shapes.Line(
            coord.x,
            coord.y,
            coord.x + self.w,
            coord.y,
            width=self.thickness,
            batch=self.batch)
        self.top = pyglet.shapes.Line(
            coord.x,
            coord.y + self.h,
            coord.x + self.w,
            coord.y + self.h,
            width=self.thickness,
            batch=self.batch)
        self.left = pyglet.shapes.Line(
            coord.x + self.margin//2,
            coord.y,
            coord.x + self.margin//2,
            coord.y + self.h,
            width=self.thickness,
            batch=self.batch)
        self.right = pyglet.shapes.Line(
            coord.x + self.w - self.margin//2,
            coord.y + self.h,
            coord.x + self.w - self.margin//2,
            coord.y,
            width=self.thickness,
            batch=self.batch)
        self.batch.draw()

    def update(self, coord: Coord):
        self.bottom.position = (
            coord.x,
            coord.y,
            coord.x + self.w,
            coord.y)
        self.top.position = (
            coord.x,
            coord.y + self.h,
            coord.x + self.w,
            coord.y + self.h)
        self.left.position = (
            coord.x + self.margin//2,
            coord.y,
            coord.x + self.margin//2,
            coord.y + self.h)
        self.right.position = (
            coord.x + self.w - self.margin//2,
            coord.y + self.h,
            coord.x + self.w - self.margin//2,
            coord.y)
        self.batch.draw()

class Scores(OnOff):
    def __init__(self, y, *args, **kwargs):
        super().__init__(y, *args, **kwargs)

    def update(self):
        super().update()

        #change the constant in constants.py
        if self.horizontal_index == 1:
            c.SCORES = False

        if self.horizontal_index == 0:
            c.SCORES = True

class Music(OnOff):
    def __init__(self, y, *args, **kwargs):
        super().__init__(y, *args, **kwargs)

    def update(self):
        super().update()
        #change the constant in constants.py
        if self.horizontal_index == 1:
            if c.MUSIC_PLAYER.playing:
                c.MUSIC_PLAYER.pause()
        if self.horizontal_index == 0:
            if not c.MUSIC_PLAYER.playing:
                c.MUSIC_PLAYER.play()

class Timer(OnOff):
    def __init__(self, y, *args, **kwargs):
        super().__init__(y, *args, **kwargs)

    def update(self):
        super().update()

        #change the constant in constants.py
        if self.horizontal_index == 0:
            c.TIMER = False
        else:
            c.TIMER = True

class Questions():
    def __init__(self, y: int):
        self._top_row_y = y
        self._bottom_row_y = self._top_row_y - 50 

        #Coords
        self._top_row = [Coord(i, self._top_row_y) for i in range(300, 900, 150)]
        self._bottom_row = [Coord(i, self._bottom_row_y) for i in range(300, 900, 150)]
        self.coords = self._top_row + self._bottom_row

        #Labels
        self.label_width = 100
        self.label_height = 50
        self.label_text = [
            "Japanese Vocab",
            "English Vocab",
            "Random Verbs",
            "Dictionary Verbs",
            "Past Tense Verbs",
            "English Sentences",
            "Japanese Sentences",
            "Pronunciations"]

        self.choices = [
            QuestionTypes.WORD_JAPANESE,
            QuestionTypes.WORD_ENGLISH,
            QuestionTypes.VERB_FORM,
            QuestionTypes.VERB_DICT,
            QuestionTypes.VERB_PAST,
            QuestionTypes.SENTENCE_ENGLISH,
            QuestionTypes.SENTENCE_JAPANESE,
            QuestionTypes.PRONUNCIATION]

        self.labels = [
            c.LABEL(
                self.label_text[_label[0]],
                x=self.coords[_label[0]].x,
                y=self.coords[_label[0]].y + 30,
                font_size=10,
                color=c.WHITE,
                align="center",
                width=self.label_width - 20,
                multiline=True,
                batch=c.OPTIONS_BATCH) for _label in enumerate(self.choices)]

        self._types = QuestionTypes
        self.batch = pyglet.graphics.Batch()
        self.horizontal_index = 0
        self.highlight = HighlightBox(
            self.coords[self.horizontal_index],
            self.label_width,
            self.label_height)
        # change opacity on highlight

    def update(self) -> None:
        # add/remove item to c.QUESTION_TYPES
        self.batch.draw()
        #pass in new coord to reposition the highlight
        self.highlight.update(self.coords[self.horizontal_index])

    def left(self) -> None:
        self.horizontal_index -= 1
        if self.horizontal_index < 0:
            self.horizontal_index = len(self.coords) - 1 

    def right(self) -> None:
        self.horizontal_index += 1
        if self.horizontal_index >= len(self.coords):
            self.horizontal_index = 0



class Items():
    def __init__(self):
        pass
        #list of sprite objects for items
        # images only
        # add custom highlight option to toggle choices 
        # change opacity on highlight

    def update(self) -> None:
        # add/remove item to c.ALL_ITEMS
        pass


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
        self.difficulties = Difficulties(self._diff_pos.y)

        self.scores_label = c.LABEL("Scores", font_size=c.FONT_SIZE, color=c.WHITE, bold=True)
        self.scores_label.x = self._score_pos.x + self.label_x_offset
        self.scores_label.y = self._score_pos.y
        self.scores = Scores(self._score_pos.y)

        self.timer_label = c.LABEL("Timer", font_size=c.FONT_SIZE, color=c.WHITE, bold=True)
        self.timer_label.x = self._timer_pos.x + self.label_x_offset
        self.timer_label.y = self._timer_pos.y
        self.timer = Timer(self._timer_pos.y)

        self.music_label = c.LABEL("Music", font_size=c.FONT_SIZE, color=c.WHITE, bold=True)
        self.music_label.x = self._music_pos.x + self.label_x_offset
        self.music_label.y = self._music_pos.y
        self.music = Music(self._music_pos.y)

        self.questions_label = c.LABEL("Questions", font_size=c.FONT_SIZE, color=c.WHITE, bold=True)
        self.questions_label.x = self._quest_pos.x + self.label_x_offset
        self.questions_label.y = self._quest_pos.y
        #TODO
#         self.questions = Placeholder(self._quest_pos.y)
        self.questions = Questions(self._quest_pos.y)

        self.items_label= c.LABEL("Items", font_size=c.FONT_SIZE, color=c.WHITE, bold=True)
        self.items_label.x = self._items_pos.x + self.label_x_offset
        self.items_label.y = self._items_pos.y
        #TODO
        self.items = Placeholder(self._items_pos.y)

        self.selector = s.Selector(self.coords)
        self.selector.pos.scale = 2

        self.vertical_indices = [7,5,3,2,1,0]
        self.vertical_index = len(self.vertical_indices) - 1
        self.option_choices = [
            self.items,
            self.questions,
            self.music,
            self.timer,
            self.scores,
            self.difficulties
        ]

    def update(self) -> None:
        self.background.draw()
        self.difficulty_label.draw()
        self.scores_label.draw()
        self.scores.update()
        self.timer_label.draw()
        self.timer.update()
        self.music_label.draw()
        self.music.update()
        self.questions_label.draw()
        self.items_label.draw()
        self.selector.update(self.vertical_index)
        
        #update choices
        self.difficulties.update()
        self.scores.update()
        self.timer.update()
        self.music.update()
        self.questions.update()
        self.items.update()

        #draw labels and highlights
        c.OPTIONS_BATCH.draw()

    def selector_up(self) -> None:
        self.vertical_index += 1
        if self.vertical_index >= len(self.coords):
            self.vertical_index = 0

    def selector_down(self) -> None:
        self.vertical_index -= 1
        if self.vertical_index < 0:
            self.vertical_index = len(self.coords) - 1

    #TODO, fix index issue...
    def selector_left(self) -> None:
        self.option_choices[self.vertical_index].left()

    def selector_right(self) -> None:
        self.option_choices[self.vertical_index].right()
