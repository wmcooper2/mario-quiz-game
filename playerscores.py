#3rd party
import pyglet

#custom
import players                  #needed for the players' images
from constants import constants as c

class Coin(c.SPRITE):

    coin_img = c.IMG("yellowcoin.png")
    coin_seq = c.GRID(coin_img, 1, 3)
    coin = coin_seq[0]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def delete(self):
        super().delete()

class Skull(c.SPRITE):

    skull_img = c.IMG("skull.png") 
    skull_seq = c.GRID(skull_img, 1, 1)
    skull = skull_seq[0]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def delete(self):
        super().delete()

class ScoreSprite(c.SPRITE):
    
    def __init__(self, score_sprite=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.score_sprite = score_sprite
        self.points = 0
#         self.score_y = c.SCORE_SPRITE_Y - 30
        self.score_y = c.SCORE_SPRITE_Y
#         self.score_x = ???

        self.big_score = []
        self.big_score_spots = []

        self.small_score = []
        self.small_score_spots_coins = []
        self.small_score_spots_skulls = []
        
        self.zero = pyglet.text.Label(text="0", x=self.x, y=self.score_y, font_name="Comic Sans MS", font_size=24, batch=c.MAIN_BATCH)

    def update(self, score_object, player):
        """Update the player's score. Returns None."""
        self.populate_score_spots(score_object)

        if self.points != player.points:
            self.delete_score()                     
            self.change_points(player)              
            self.set_score_images()

    def populate_score_spots(self, score_object):
        """Setup of the score spots. Returns None."""
        #populate self.small_score_spots_coins
        if not self.small_score_spots_coins:                  
            self.make_small_score_spots_coins(score_object)    
#             print("small_score_spots_coins = ", self.small_score_spots_coins) 

        #populate self.small_score_spots_skulls
        if not self.small_score_spots_skulls:                   
            self.make_small_score_spots_skulls(score_object)     
#             print("small_score_spots_skulls = ", self.small_score_spots_skulls) 

        #populate self.big_score_spots
        if not self.big_score_spots:                     
            self.make_big_score_spots(score_object)
#             print("big_score_spots = ", self.big_score_spots)

    def make_small_score_spots_coins(self, score_object):
        """Sets spots for self.small_score_spots_coins. Returns None."""
        start = score_object.x - 36
        for x in range(5):
            self.small_score_spots_coins.append(start + (x * 12)) #coin width = 12

    def make_small_score_spots_skulls(self, score_object):
        """Sets spots for self.small_score_spots_skulls. Returns None."""
        start = score_object.x - 36
        for x in range(5):
            self.small_score_spots_skulls.append(start + (x * 16)) #skull width = 16

    def make_big_score_spots(self, score_object):
        """Sets spots for self.big_score_spots. Returns None."""
        start = score_object.x - 36
        for x in range(3):
            self.big_score_spots.append(start + (x * 30))

    def delete_score(self):
        """Deletes the sprites that are the displayed score. Returns None."""
        points = self.points                #ScoreSprite.points
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
        """Changes score's points to match the associated player's points. Returns None."""
        if self.points < player.points:
            self.points += 1
        elif self.points > player.points:
            self.points -= 1
#         print(self, ", points = ", self.points)

    def set_score_images(self):
        """Adds the proper score sprites for the given point range. Returns None."""
        points = self.points                #ScoreSprite.points
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
        self.big_score.append(Coin(img=Coin.coin, x=self.big_score_spots[0], y=self.score_y, batch=c.MAIN_BATCH))
        self.big_score[0].scale = 1.5
        self.big_score.append(pyglet.text.Label(text="x", x=self.big_score_spots[1], y=self.score_y, font_name="Comic Sans MS", font_size=24, batch=c.MAIN_BATCH))
        self.big_score.append(pyglet.text.Label(text=str(self.points), x=self.big_score_spots[2], y=self.score_y, font_name="Comic Sans MS", font_size=24, batch=c.MAIN_BATCH))

    def make_small_score_coins(self):
        """Assembles the small score of coins. Returns None."""
        for x in range(self.points):
            self.small_score.append(Coin(img=Coin.coin, x=self.small_score_spots_coins[x], y=self.score_y, batch=c.MAIN_BATCH))
        
    def make_zero_score(self):
        """Assembles the zero score. Returns None."""
        self.zero.text = "0"

    def make_small_score_skulls(self):
        """Assembles the small score of skulls. Returns None."""
        for x in range(abs(self.points)):
            self.small_score.append(Skull(img=Skull.skull, x=self.small_score_spots_skulls[x], y=self.score_y, batch=c.MAIN_BATCH))

    def make_big_score_skull(self):
        """Assembles the big score of skulls. Returns None."""
        self.big_score.append(Skull(img=Skull.skull, x=self.big_score_spots[0], y=self.score_y, batch=c.MAIN_BATCH))
        self.big_score[0].scale = 1.5 
        self.big_score.append(pyglet.text.Label(text="x", x=self.big_score_spots[1], y=self.score_y, font_name="Comic Sans MS", font_size=24, batch=c.MAIN_BATCH))
        self.big_score.append(pyglet.text.Label(text=str(abs(self.points)), x=self.big_score_spots[2], y=self.score_y, font_name="Comic Sans MS", font_size=24, batch=c.MAIN_BATCH))

def make_sprite(player, score_x):
    """Makes a score sprite same as the player, but a separate instance. Returns Sprite object."""
    if isinstance(player, players.FireLight):
        score_sprite=ScoreSprite(
            img=players.FireLight.stand_left_seq[0],
            x=score_x,
            y=c.SCORE_SPRITE_Y,
            batch=c.MAIN_BATCH)
        score_sprite.y -= 5                             #readjusted for score_display only
    elif isinstance(player, players.Dragon):
        score_sprite=ScoreSprite(
            img=players.Dragon.stand_left,
            x=score_x,
            y=c.SCORE_SPRITE_Y,
            batch=c.MAIN_BATCH)
    elif isinstance(player, players.BigBoo):
        score_sprite=ScoreSprite(
            img=players.BigBoo.stand_left,
            x=score_x,
            y=c.SCORE_SPRITE_Y,
            batch=c.MAIN_BATCH)
        score_sprite.y += 15                            #readjusted for score_display only
        score_sprite.scale = 0.5
    elif isinstance(player, players.GreenKoopa):
        score_sprite=ScoreSprite(
            img=players.GreenKoopa.stand_left,
            x=score_x,
            y=c.SCORE_SPRITE_Y,
            batch=c.MAIN_BATCH)
    elif isinstance(player, players.BigMole):
        score_sprite=ScoreSprite(
            img=players.BigMole.stand_left,
            x=score_x,
            y=c.SCORE_SPRITE_Y,
            batch=c.MAIN_BATCH)
    elif isinstance(player, players.Mario):
        score_sprite=ScoreSprite(
            img=players.Mario.stand_left,
            x=score_x,
            y=c.SCORE_SPRITE_Y,
            batch=c.MAIN_BATCH)
    elif isinstance(player, players.Luigi):
        score_sprite=ScoreSprite(
            img=players.Luigi.stand_left,
            x=score_x,
            y=c.SCORE_SPRITE_Y,
            batch=c.MAIN_BATCH)
    return score_sprite
