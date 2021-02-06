#std lib
from constants import Constants as c
from collections import namedtuple
import sprites as s

Coord = namedtuple("Coord", ["x", "y"])

class TitleScreen():
    def __init__(self):
        self.title = c.SPRITE(c.IMG("title.png"))
        self.title.scale = 2
        self.title.x = (c.GAME_WINDOW.width - self.title.width) / 2
        self.title.y = (c.GAME_WINDOW.height - self.title.height) / 2

        self.subtitle = c.SPRITE(c.IMG("quizlabel2.png"))
        self.subtitle.x = (c.GAME_WINDOW.width - self.subtitle.width) / 2
        self.subtitle.y = (c.GAME_WINDOW.height - self.subtitle.height) / 2 - 100

        self.title_background = c.SPRITE(c.IMG("titlebackground.png"))
        self.title.ground = c.SPRITE(c.IMG("titleground.png"))
    
        self.label_center = 450 #xpos of buttons, i becomes ypos
        self.coords = [Coord(self.label_center, i) for i in range(120, 60, -30)]
        self.coords.reverse()

        self.options_button = c.LABEL("Options", font_size=c.FONT_SIZE, color=c.BLACK, bold=True)
#         self.options_button = c.SPRITE(c.IMG("optionsbtn.png"))
        self.options_button.x = self.coords[0].x + 20
        self.options_button.y = self.coords[0].y

        self.game_button = c.LABEL("Game", font_size=c.FONT_SIZE, color=c.BLACK, bold=True)
#         self.game_button = c.SPRITE(c.IMG("gamebtn.png"))
        self.game_button.x = self.coords[1].x + 20
        self.game_button.y = self.coords[1].y

        self.vertical_index = 0
        self.selector = s.Selector(self.coords)

    def update(self) -> None:
        self.title_background.draw()
        self.title.ground.draw()
        self.title.draw()
        self.subtitle.draw()
        self.options_button.draw()
        self.game_button.draw()
        self.selector.update(self.vertical_index)

#     def selector_up(self) -> None:
#         self.selector.up()

    def selector_up(self) -> None:
        print("up")
        self.vertical_index += 1
        if self.vertical_index >= len(self.coords):
            self.vertical_index = 0

    def selector_down(self) -> None:
        print("down")
        self.vertical_index -= 1
        if self.vertical_index < 0:
            self.vertical_index = len(self.coords) - 1

        
#     def selector_down(self) -> None:
#         self.selector.down()

    def is_game_selected(self) -> bool:
        return self.selector.index == 0
        
    def is_options_selected(self) -> bool:
        return self.selector.index == 1
