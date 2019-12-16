#3rd party
import pyglet

#custom
from constants import *
from players import *

def minus_one(player):
    """Decrease player points by one. Returns None."""
    player[0].points -= 1

def plus_one(player):
    """Increase player points by one. Returns None."""
    player[0].points += 1

def small(char, x_pos):
    """Generic character score constructor. Returns Sprite Object."""
    return ScoreSprite(img=char.animl, x=x_pos, y=SCORE_SPRITE_Y, \
            batch=MAIN)

def score_sprite(player, x):
    """Makes player score sprite. Returns Sprite object."""
    if isinstance(player, FireLight): #score-adapted
        tiny = ScoreSprite(img=FireLight.animl, x=x, y=SCORE_SPRITE_Y, \
                batch=MAIN)
        tiny.y -= 5
        return tiny
    elif isinstance(player, BigBoo): #score-adapted
        tiny = small(BigBoo, x)
        tiny.y += 15
        tiny.scale = 0.5
        return tiny
    elif isinstance(player, Dragon):        return small(Dragon, x)
    elif isinstance(player, GreenKoopa):    return small(GreenKoopa, x)
    elif isinstance(player, BigMole):       return small(BigMole, x)
    elif isinstance(player, Mario):         return small(Mario, x)
    elif isinstance(player, Luigi):         return small(Luigi, x)

def update_scores():
    """Updates the scores on the screen. Returns None."""
    #top row scores
    for playerscore in SCORES:
        if playerscore.points==0: playerscore.zero.text="0"
        elif abs(playerscore.points)>0 and abs(playerscore.points)<=5:
            for element in playerscore.small: element.draw()
        elif abs(playerscore.points)>5:
            for element in playerscore.big: element.draw()

def setup_scores(players, spots, scores):
    """Sets up the scores in the top rows. Returns None."""
    for element in players:
        x_pos   = spots[players.index(element)]
        sprite  = score_sprite(element, x_pos)
        scores.append(sprite)
        element.point_index = scores.index(sprite)
        
class Coin(pyglet.sprite.Sprite):
    pi, pg, pa  = image_resources()
    coin_img    = pi("yellowcoin.png")
    coin_seq    = pg(coin_img, 1, 3)
    image       = coin_seq[0]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def delete(self):
        super().delete()

class Skull(pyglet.sprite.Sprite):
    pi, pg, pa  = image_resources()
    skull_img   = pi("skull.png") 
    skull_seq   = pg(skull_img, 1, 1)
    image       = skull_seq[0]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def delete(self):
        super().delete()

class ScoreSprite(pyglet.sprite.Sprite):
    def __init__(self, score_sprite=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.big            = []
        self.big_pos        = []
        self.points         = 0
        self.score_sprite   = score_sprite
        self.ypos           = SCORE_SPRITE_Y - 30
        self.small          = []
        self.smallcoinpos   = []
        self.smallskullpos  = []
        self.zero           = label(text="0", x=self.x, y=self.ypos, \
                            font_name=ENGLISH_FONT, font_size=ZERO_SIZE,\
                            batch=MAIN)

    #UPDATES
    def update(self, score_obj, player):
        """Update player's score. Returns None."""
        self.score_positions(score_obj)

        if self.points is not player.points: #change to != ???
            self.delete_score()                     
            self.update_score(player)              
            self.set_score_images()

    def update_score(self, player):
        """Updates player's score. Returns None."""
        if self.points < player.points:     self.points += 1
        elif self.points > player.points:   self.points -= 1

    #MAKE SCORE POSITIONS
    def score_positions(self, score_obj):
        """Setup score positions. Returns None."""
        if not self.smallcoins:     self.small_coin_pos(score_obj)    
        if not self.smallskullpos:  self.small_skull_pos(score_obj)     
        if not self.big_pos:        self.big_score_pos(score_obj)

    def small_coin_pos(self, score_obj):
        """Sets spots for self.smallcoins. Returns None."""
        start = score_obj.x - 36
        score = self.smallcoins
        [score.append(start+(x*COIN_WIDTH)) for x in range(MAXSCORE_S)]

    def small_skull_pos(self, score_obj):
        """Sets spots for self.smallskullpos. Returns None."""
        start = score_obj.x - 36
        score = self.smallskullpos
        [score.append(start+(x*SKULL_WIDTH)) for x in range(MAXSCORE_S)]

    def big_score_pos(self, score_obj):
        """Sets spots for self.big_pos. Returns None."""
        start = score_obj.x - 36
        score = self.big_pos
        [score.append(start+(x*COIN_WIDTH_B)) for x in range(MAXSCORE_B)]

    #ERASE THE SCORES
    def delete_score(self):
        """Deletes sprites that display score. Returns None."""
        points = self.points
        if points > 5:                      self.delete_big()
        elif points <= 5 and points > 0:    self.delete_small()
        elif points == 0:                   self.delete_zero()
        elif points < 0 and points >= -5:   self.delete_small()
        elif points < -5:                   self.delete_big()
   
    def delete_big(self):
        """Deletes contents of self.big. Returns None."""
        del self.big
        self.big = []

    def delete_small(self):
        """Deletes self.small. Returns None."""
        del self.small
        self.small = []

    def delete_zero(self):
        """Deletes the zero score. Returns None."""
        self.zero.text = ""

    def set_score_images(self):
        """Adds score sprite for given point range. Returns None."""
        points = self.points
        if points > 5:                      self.big_coins()
        elif points <= 5 and points > 0:    self.small_coins()
        elif points == 0:                   self.zero.text = "0"
        elif points < 0 and points >= -5:   self.small_skulls()
        elif points < -5:                   self.big_skulls()

    #MAKING THE SCORES
    def big_label(self, string, spot):
        """Generic big label constructor. Returns Label object."""
        return  label(text=string, x=spot, y=self.ypos, \
                font_name=SCORE_FONT, font_size=BIG_SCORE_SIZE, \
                batch=MAIN)

    def big_image(self, class_, spot):
        """Generic big image constructor. Returns Sprite object."""
        return score.append(class_(img=class_.image, x=spot, y=self.ypos,\
                batch=MAIN))

    def small_image(self, class_, list_, spot):
        """Generic small image constructor. Returns Sprite object."""
        return self.small.append(class_(img=class_.image, \
                x=list_[spot], y=self.ypos, batch=MAIN))

    def big_coins(self):
        """Assembles the big score of coins. Returns None."""
        scorespot       = self.big_pos
        score           = self.big
        score.append(big_image(Coin))
        score[0].scale  = 1.5
        score.append(self.big_label("x", scorespot[1]))
        score.append(self.big_label(str(self.points), scorespot[2]))

    def small_coins(self):
        """Assembles the small score of coins. Returns None."""
        score   = self.small
        coins   = self.smallcoinpos
        points  = self.points
        func    = self.small_image
        [score.append(func(Coin, coins, x)) for x in range(points)]
        
    def small_skulls(self):
        """Assembles the small score of skulls. Returns None."""
        score   = self.small
        skulls  = self.smallskullpos
        points  = self.points
        func    = self.small_image
        [score.append(func(Skull, skulls, x)) for x in range(points)]

    def big_skulls(self):
        """Assembles score of big skulls. Returns None."""
        scorespot       = self.big_pos
        score           = self.big
        score.append(self.big_image(Skull))
        score[0].scale  = 1.5 
        score.append(self.big_label("x", scorespot[1]))
        score.append(self.big_label(str(abs(self.points), scorespot[2])))
