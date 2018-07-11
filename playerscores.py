import util
import pyglet
import players                  #needed for the players' images
from constants import *

class Coin(pyglet.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class Skull(pyglet.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class ScoreSprite(pyglet.sprite.Sprite):
    
    coin_img = pyglet.resource.image("yellow_coin.png")
    coin_seq = pyglet.image.ImageGrid(coin_img, 1, 3)
    coin = coin_seq[0]
    skull = pyglet.resource.image("skull.png") 

    def __init__(self, score_sprite = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.score_sprite = score_sprite
        self.columns = []
        self.points = 0
        self.score_y = SCORE_SPRITE_Y - 30        
        self.big_score = []
        self.small_score = []
        self.big_score_spots = []
        self.small_score_spots = []
        
        self.zero = pyglet.text.Label(text = "0", x = self.x, y = self.score_y, font_name = "Comic Sans MS", font_size = 24, batch = main_batch)
        self.score_img = ""                     #change this between skull, coin and zero

    def update(self, score_object, player):
        """Update the player's score. Returns None."""
        if not self.columns:                    #if self.columns is empty
            self.score_columns(score_object)    #making x spots for coins and skulls (small score)
            print(", score_columns = ", self.columns)            

        if self.points != player.points:
            self.delete_score()                     #all deletes up to print statements works at the right point ranges
            self.change_points(player)              #adjusting the points based on the player instance's points, all point changes work
            self.set_score_images()
#            self.assemble_score()

    def score_columns(self, score_object):
        """Sets the columns for the score's images, not the score_sprite. Returns None."""
        column_start = score_object.x - 36
        for x in range(5):
            self.columns.append(column_start + (x * 12)) #coin width = 12

    def delete_score(self):
        """Deletes the sprites that are the displayed score. Returns None."""
        points = self.points                #ScoreSprite.points
        if points > 5:
            self.delete_big_score_coin()
        elif points <= 5 and points > 0:
            self.delete_small_score_coins()
        elif points == 0:
            self.delete_zero()
        elif points < 0 and points >= -5:
            self.delete_small_score_skulls()
        elif points < -5:
            self.delete_big_score_skull()
   
    def delete_big_score_coin(self):
        """Deletes contents of big_score with coin instance in it. Returns None."""
        print("deleting big_score coin list.")

    def delete_small_score_coins(self):
        """Deletes coins from small_score. Returns None."""
        print("deleting small score, coins.")

    def delete_zero(self):
        """Deletes the zero label. Returns None."""
        print("deleting zero label.")

    def delete_small_score_skulls(self):
        """Deletes skulls from small_score. Returns None."""
        print("deleting small score, skulls.")
       
    def delete_big_score_skull(self):
        """Deletes contents of big_score with skull instance in it. Returns None."""
        print("deleting big_score skull list.") 

#
#    def delete_score2(self):
#        """Deletes the sprites that are the displayed score. Returns None."""
##        print("delete_score")
#        if self.points == 0:
#            super(pyglet.text.Label, self.zero).delete()                    #works
#        elif self.points > 5:
#            print("points > 5")
##            super(Coin, self.big_score[0]).delete()
#        elif self.points <= 5 and self.points > 0:
#            print("points <= 5 and >0")
##            for thing in self.small_score:
##                super(Coin, thing).delete()  
##            while len(self.small_score) > 0:
##            temp = self.small_score[:]
#            for x in range(len(self.small_score)):
##            for thing in temp:
#                print("self.small_score = ", self.small_score)
##                super(Coin, self.small_score[-1]).delete()
##                super(Coin, self.small_score[0]).delete()
##                self.small_score[x].delete()
##        elif self.points < -5:
#            super(Skull, self.big_score[0]).delete()
#        elif self.points < 0 and self.points >= -5:
##            for thing in self.small_score:
#            for x in range(len(self.small_score)):
#                print("deleting small_score element")
##                super(Skull, thing).delete()

    def change_points(self, player):
        """Changes score's points to match the associated player's points. Returns None."""
        if self.points < player.points:
            self.points += 1
        elif self.points > player.points:
            self.points -= 1
        print(self, ", points = ", self.points)


    def set_score_images2(self):
        """Adds the proper score sprites for the given point range. Returns None."""
        if self.points == 0:                    #maybe dont need the zero assignment, drawn in on_draw() anyway
#            print("score is zero")
            self.score_img = self.zero
        elif self.points > 0:
#            pass
            print("score is coins")
#            self.score_img = self.coin
#            self.score_img = Coin(img = self.coin, x = self.columns[x], y = self.score_y, batch = main_batch)  
        elif self.points < 0:
            print("score is skulls")
            self.score_img = self.skull

    def set_score_images(self):
        """Adds the proper score sprites for the given point range. Returns None."""
        if self.points == 0:                    #maybe dont need the zero assignment, drawn in on_draw() anyway
            print("score image is  zero")
#            self.score_img = self.zero
        elif self.points > 0:
            print("score image is coins")
#            self.score_img = self.coin
#            self.score_img = Coin(img = self.coin, x = self.columns[x], y = self.score_y, batch = main_batch)  
        elif self.points < 0:
            print("score image is skulls")
#            self.score_img = self.skull

    def assemble_score(self):
        """Assembles the final score display. Returns None."""
        if abs(self.points) > 5:
            self.make_big_score_coin()
        elif abs(self.points) <= 5 and abs(self.points) > 0:
            self.make_small_score_coins()    
    
    def make_big_score_coin(self):
        """Assembles the pieces for the big score display. Returns None."""
        print("make_big_score")
        self.big_score.append(1)                    #debug appended value
        
    def make_small_score_coins(self):
        """Assembles the pieces for the small score display. Returns None."""
        print("make_small_score")

        for x in range(abs(self.points)):
            self.small_score.append(Coin(img = self.coin, x = self.columns[x], y = self.score_y, batch = main_batch))   #debug appended value
#        for spot in self.small_score.spots:
#            self.small_score.append(self.coin, x = self.small_score_spots[spot], y = self.score_y, batch = main_batch)

def make_sprite(player, score_x):
    if isinstance(player, players.FireLight):
        score_sprite = ScoreSprite(img = players.FireLight.stand_left_seq[0], x = score_x, y = SCORE_SPRITE_Y, batch = main_batch)
        score_sprite.y -= 5                             #readjusted for score_display only
    elif isinstance(player, players.Dragon):
        score_sprite = ScoreSprite(img = players.Dragon.stand_left, x = score_x, y = SCORE_SPRITE_Y, batch = main_batch)
    elif isinstance(player, players.BigBoo):
        score_sprite = ScoreSprite(img = players.BigBoo.stand_left, x = score_x, y = SCORE_SPRITE_Y, batch = main_batch)
        score_sprite.y += 15                            #readjusted for score_display only
        score_sprite.scale = 0.5
    elif isinstance(player, players.GreenKoopa):
        score_sprite = ScoreSprite(img = players.GreenKoopa.stand_left, x = score_x, y = SCORE_SPRITE_Y, batch = main_batch)
    elif isinstance(player, players.BigMole):
        score_sprite = ScoreSprite(img = players.BigMole.stand_left, x = score_x, y = SCORE_SPRITE_Y, batch = main_batch)
    elif isinstance(player, players.Mario):
        score_sprite = ScoreSprite(img = players.Mario.stand_left, x = score_x, y = SCORE_SPRITE_Y, batch = main_batch)
    elif isinstance(player, players.Luigi):
        score_sprite = ScoreSprite(img = players.Luigi.stand_left, x = score_x, y = SCORE_SPRITE_Y, batch = main_batch)
    return score_sprite
