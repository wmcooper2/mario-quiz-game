#std lib
from constants import Constants as c

class TitleScreen():

    def __init__(self):
        self.title = c.SPRITE(c.IMG("title.png"))
        self.title.scale = 2
        self.title.x = (c.GAME_WINDOW.width - self.title.width) / 2
        self.title.y = (c.GAME_WINDOW.height - self.title.height) / 2

        self.subtitle = c.SPRITE(c.IMG("quizlabel2.png"))
        self.subtitle.x = (c.GAME_WINDOW.width - self.subtitle.width) / 2
        self.subtitle.y = (c.GAME_WINDOW.height - self.subtitle.height) / 2 - 100

#         self.titleborder = c.SPRITE(c.IMG("titleborder.png"))
#         self.titleborder.scale = 2.5
#         self.titleborder.x = (c.GAME_WINDOW.width - self.titleborder.width) / 2
#         self.titleborder.y = (c.GAME_WINDOW.height - self.titleborder.height) / 2

        self.title_background = c.SPRITE(c.IMG("titlebackground.png"))
        self.title.ground = c.SPRITE(c.IMG("titleground.png"))
#         self.quiz_label = c.IMG("quizlabel2.png")

        self.options_button = c.SPRITE(c.IMG("optionsbtn.png"))
        self.options_button.x = (c.GAME_WINDOW.width - self.options_button.width) / 2
        self.options_button.y = 100

        self.game_button = c.SPRITE(c.IMG("gamebtn.png"))
        self.game_button.x = (c.GAME_WINDOW.width - self.game_button.width) / 2
        self.game_button.y = 130

        self.selector = c.SPRITE(c.IMG("redmushroom.png"))
        self.selector.x = (c.GAME_WINDOW.width - self.selector.width) / 2 - 50
        self.selector.y = 100 

    def update(self) -> None:
        self.title_background.draw()
        self.title.ground.draw()
        self.title.draw()
        self.subtitle.draw()
#         self.titleborder.draw()
#         self.quiz_label.draw()
        self.options_button.draw()
        self.game_button.draw()
        self.selector.draw()

    def selector_up(self) -> None:
        self.selector.y = 130
        
    def selector_down(self) -> None:
        self.selector.y = 100

    def is_game_selected(self) -> bool:
        return self.selector.y == 130
        
    def is_options_selected(self) -> bool:
        return self.selector.y == 100
