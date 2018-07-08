import pyglet
from constants import *



class Score(pyglet.sprite.Sprite):
    
    coin_img = pyglet.resource.image("yellow_coin.png")
    coin_img_seq = pyglet.image.ImageGrid(coin_img, 1, 3)

    def __init__(self, score_sprite = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.score_sprite = score_sprite
        self.coin_columns = []
        self.coin_rows = [[score_sprite.y - 9], [score_sprite.y - 18]] 

    def coin_columns(self):
        """Sets the coin positions for the player's coins at the top of game_window. Returns None."""
        column_start = self.score_sprite.x - 36
        columns = []
        for x in range(5):
            columns.append(column_start + (x * 12)) #coin sprite width = 12




