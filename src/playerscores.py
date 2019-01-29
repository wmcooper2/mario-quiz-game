#stand lib

#3rd party
import pyglet

#custom
from src.constants import *
from src.players import *

def right_answer(players):
    """Plus one point. Returns None."""
    players[0].points += 1

def wrong_answer(players):
    """Minus one point. Returns None."""
    players[0].points -= 1

def score_setup(players, spots, scores):
    """Sets up the scores in the top rows. Returns None."""
    for element in players:
        score_x = spots[players.index(element)]
        score_sprite = make_sprite(element, score_x)
        scores.append(score_sprite)
        element.point_index = scores.index(score_sprite)

class Coin(pyglet.sprite.Sprite):
    pygresimg, pygrid, pyganim = image_res()
    
    coin_img = pygresimg("yellow_coin.png")
    coin_seq = pygrid(coin_img, 1, 3)
    coin = coin_seq[0]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def delete(self):
        super().delete()

class Skull(pyglet.sprite.Sprite):
    pygresimg, pygrid, pyganim = image_res()

    skull_img = pygresimg("skull.png") 
    skull_seq = pygrid(skull_img, 1, 1)
    skull = skull_seq[0]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def delete(self):
        super().delete()

class ScoreSprite(pyglet.sprite.Sprite):
    label = pyglet.text.Label
    
    def __init__(self, score_sprite = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.score_sprite = score_sprite
        self.points = 0
        self.score_y = SCORE_SPRITE_Y - 30

        self.big_score = []
        self.big_score_spots = []

        self.small_score = []
        self.small_score_spots_coins = []
        self.small_score_spots_skulls = []
        
        self.zero = label(text="0", x=self.x, y=self.score_y, \
                font_name=ENGLISH_FONT, font_size=24, batch=MAIN_BATCH)

    def update(self, score_object, player):
        """Update player's score. Returns None."""
        self.populate_score_spots(score_object)

#        if self.points != player.points:
        if self.points is not player.points:
            self.delete_score()                     
            self.change_points(player)              
            self.set_score_images()

    def populate_score_spots(self, score_object):
        """Setup score spots. Returns None."""
        #populate self.small_score_spots_coins
        if not self.small_score_spots_coins:                  
            self.make_small_score_spots_coins(score_object)    
            if DEBUG:
#                debug_message()
                print("small_score_spots_coins = ", self.small_score_spots_coins) 

        #populate self.small_score_spots_skulls
        if not self.small_score_spots_skulls:                   
            self.make_small_score_spots_skulls(score_object)     
            if DEBUG:
                print("small_score_spots_skulls = ", self.small_score_spots_skulls) 

        #populate self.big_score_spots
        if not self.big_score_spots:                     
            self.make_big_score_spots(score_object)
            if DEBUG:
                print("big_score_spots = ", self.big_score_spots)

    def make_small_score_spots_coins(self, score_object):
        """Sets spots for self.small_score_spots_coins. Returns None."""
        start = score_object.x - 36
        for x in range(5):
            #coin width = 12
            self.small_score_spots_coins.append(start + (x * 12))

    def make_small_score_spots_skulls(self, score_object):
        """Sets spots for self.small_score_spots_skulls. Returns None."""
        start = score_object.x - 36
        for x in range(5):
            #skull width = 16
            self.small_score_spots_skulls.append(start + (x * 16))

    def make_big_score_spots(self, score_object):
        """Sets spots for self.big_score_spots. Returns None."""
        start = score_object.x - 36
        for x in range(3):
            self.big_score_spots.append(start + (x * 30))

    def delete_score(self):
        """Deletes sprites that display score. Returns None."""
        #ScoreSprite.points
        points = self.points
        if points > 5:
            self.delete_big_score()
        elif points <= 5 and points > 0:
            self.delete_small_score()
        elif points == 0:
            self.delete_zero_score()
        elif points < 0 and points >= -5:
            self.delete_small_score()
        elif points < -5:
            self.delete_big_score()
   
    def delete_big_score(self):
        """Deletes contents of big_score. Returns None."""
        self.big_score = []

    def delete_small_score(self):
        """Deletes small_score. Returns None."""
        self.small_score = []

    def delete_zero_score(self):
        """Deletes the zero score. Returns None."""
        self.zero.text = ""

    def change_points(self, player):
        """Changes score-points to match player-points. Returns None."""
        if self.points < player.points:
            self.points += 1
        elif self.points > player.points:
            self.points -= 1
#        print(self, ", points = ", self.points)

    def set_score_images(self):
        """Adds score sprite for given point range. Returns None."""
        #ScoreSprite.points
        points = self.points
        if points > 5:
            self.make_big_score_coin()
        elif points <= 5 and points > 0:
            self.make_small_score_coins()
        elif points == 0:
            self.make_zero_score()
        elif points < 0 and points >= -5:
            self.make_small_score_skulls()
        elif points < -5:
            self.make_big_score_skull()

    def make_big_score_coin(self):
        """Assembles the big score of coins. Returns None."""
        scorespot   = self.big_score_spots
        score       = self.big_score
        label       = pyglet.text.Label
        score.append(Coin(img=Coin.coin, x=scorespot[0], \
                y=self.score_y, batch=MAIN_BATCH))
        score[0].scale = 1.5
        score.append(label(text="x", x=scorespot[1], \
                y=self.score_y, font_name="Comic Sans MS", \
                font_size=24, batch=MAIN_BATCH))
        score.append(label(text=str(self.points), x=scorespot[2], \
                y=self.score_y, font_name="Comic Sans MS", \
                font_size=24, batch=MAIN_BATCH))

    def make_small_score_coins(self):
        """Assembles the small score of coins. Returns None."""
        for x in range(self.points):
            self.small_score.append(Coin(img=Coin.coin, \
                    x=self.small_score_spots_coins[x], y=self.score_y, \
                    batch=MAIN_BATCH))
        
    def make_zero_score(self):
        """Assembles the zero score. Returns None."""
        self.zero.text = "0"

    def make_small_score_skulls(self):
        """Assembles the small score of skulls. Returns None."""
        for x in range(abs(self.points)):
            self.small_score.append(Skull(img=Skull.skull, \
                    x=self.small_score_spots_skulls[x], y=self.score_y, \
                    batch=MAIN_BATCH))

    def make_big_score_skull(self):
        """Assembles score of big skulls. Returns None."""
        scorespot   = self.big_score_spots
        score       = self.big_score
        label       = pyglet.text.Label

        score.append(Skull(img=Skull.skull, x=scorespot[0], \
                y=self.score_y))
        score[0].scale = 1.5 
        score.append(label(text="x", x=scorespot[1], \
                y=self.score_y, font_name="Comic Sans MS", font_size=24))
        score.append(label(text=str(abs(self.points)), x=scorespot[2], \
                y=self.score_y, font_name="Comic Sans MS", font_size=24))
        
def make_sprite(player, score_x):
    """Makes player score sprite. Returns Sprite object."""
    if isinstance(player, FireLight):
        score_sprite = ScoreSprite(img=FireLight.stand_left_seq[0], \
                x=score_x, y=SCORE_SPRITE_Y, batch=MAIN_BATCH)
        #readjusted for score_display only
        score_sprite.y -= 5
    elif isinstance(player, Dragon):
        score_sprite = ScoreSprite(img=Dragon.stand_left, x=score_x, \
                y=SCORE_SPRITE_Y, batch=MAIN_BATCH)
    elif isinstance(player, BigBoo):
        score_sprite = ScoreSprite(img=BigBoo.stand_left, x=score_x, \
                y=SCORE_SPRITE_Y, batch=MAIN_BATCH)
        #readjusted for score_display only
        score_sprite.y += 15
        score_sprite.scale = 0.5
    elif isinstance(player, GreenKoopa):
        score_sprite = ScoreSprite(img=GreenKoopa.stand_left, x=score_x, \
                y=SCORE_SPRITE_Y, batch=MAIN_BATCH)
    elif isinstance(player, BigMole):
        score_sprite = ScoreSprite(img=BigMole.stand_left, x=score_x, \
                y=SCORE_SPRITE_Y, batch=MAIN_BATCH)
    elif isinstance(player, Mario):
        score_sprite = ScoreSprite(img=Mario.stand_left, x=score_x, \
                y=SCORE_SPRITE_Y, batch=MAIN_BATCH)
    elif isinstance(player, Luigi):
        score_sprite = ScoreSprite(img=Luigi.stand_left, x=score_x, \
                y=SCORE_SPRITE_Y, batch=MAIN_BATCH)
    return score_sprite
