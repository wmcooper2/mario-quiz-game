#std lib
from constants import Constants as c

class OptionsScreen():

    def __init__(self):
        pass
        self.background = c.SPRITE(c.IMG("blackbox.png"))
        self.background.scale = 6
#         self.title = c.SPRITE(c.IMG("title.png"))
#         self.title.x = (c.GAME_WINDOW.width - self.title.width) / 2
#         self.title.y = (c.GAME_WINDOW.height - self.title.height) / 2

        self.difficulty_label = c.SPRITE(c.IMG("difficulty.png"))
        self.difficulty_label.x = 100
        self.difficulty_label.y = 100

    def update(self) -> None:
        self.background.draw()
        self.difficulty_label.draw()

    def selector_up(self) -> None:
        self.selector.y = 130
        
    def selector_down(self) -> None:
        self.selector.y = 100

    def is_game_selected(self) -> bool:
        return self.selector.y == 130
        
    def is_options_selected(self) -> bool:
        return self.selector.y == 100

    
