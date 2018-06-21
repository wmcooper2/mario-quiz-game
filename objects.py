import math
import util
import pyglet
from pyglet.window import key

#setup resource dirs
resource_dir = "./resources"
pyglet.resource.path = [resource_dir]
pyglet.resource.reindex()

class Background(pyglet.sprite.Sprite):

    background_img = pyglet.resource.image("quiz1.png")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class Player(pyglet.sprite.Sprite):

    randomized = False

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.keys = dict(left=False, right=False, up=False, down=False)
        self.key_handler = key.KeyStateHandler()
        self.spot = self.x #point it is spawned (off screen r)        
        self.has_spot = False
        self.item = "None"
#        self.movement = "left"    
        self.moving = False
        self.speed = "walk"
            
    def update(self, dt):
        self.check_spots()  #check, assign spots
        self.animate()      #set moving attribute

    def delta_x(self):
        """Get the distance between objects position and spot position.
            Returns Integer."""
        return self.x - self.spot

    def animate(self):
        if self.speed == "walk":
            self.walk()
        if self.speed == "run": #add running sprite sequences for mario, speed up the timing on others
            self.run()

    def walk(self):
        """Walks the player left or right.
            Returns None."""
        delta = self.delta_x()
        #update sprite image
        if delta != 0 and self.moving == False:
            self.moving = True
            if delta > 0:
                self.image = self.walk_left_anim
            if delta < 0:
                self.image = self.walk_right_anim
        elif delta == 0:
            self.image = self.stand_left_anim 
        #move left or right
        if delta > 0:
            self.x -= 1
        if delta < 0:
            self.x += 1

    def check_spots(self):
        """Looks for an available spot closest to the upper platform."""
        def spot_available(spot):
            return util.Line.spots_avail[util.Line.spots.index(spot)] 

        def spot_unavailable(spot):
            util.Line.spots_avail[util.Line.spots.index(spot)] = False

        for spot in util.Line.spots:
            if spot_available(spot) and not self.has_spot:
                self.assign_spot(spot)
                self.has_spot = True 
                spot_unavailable(spot)

    def assign_spot(self, new_spot):
        """Assigns a spot to the players."""
        self.spot = new_spot

class FloatingPlayer(Player):
    
    float_height = 0
    float_deg = 0

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def float(self):
        """Makes the character float up and down in place.
            Returns None."""
        radians = math.radians(FloatingPlayer.float_deg)
        FloatingPlayer.float_height = math.sin(radians)
        if FloatingPlayer.float_deg == 360:
            FloatingPlayer.float_deg = 0
            FloatingPlayer.float_height = 0
        FloatingPlayer.float_deg += 1
        self.y = self.y + (FloatingPlayer.float_height / 3) 

class WalkingPlayer(Player):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
class FireLight(FloatingPlayer):
    
    #stand_left => stand_left_img because of motion while standing
    stand_left = pyglet.resource.image("fire_light_walk_left.png")
    util.center_floating_player(stand_left)
    stand_left_seq = pyglet.image.ImageGrid(stand_left, 1, 2)
    stand_left_anim = pyglet.image.Animation.from_image_sequence(stand_left_seq, 0.1, True) 
#    stand_left = pyglet.image.Animation.from_image_sequence(stand_left_seq, 0.1, True) 
    walk_right = pyglet.resource.image("fire_light_walk_right.png")
    walk_right_seq = pyglet.image.ImageGrid(walk_right, 1, 2)
    walk_right_anim = pyglet.image.Animation.from_image_sequence(walk_right_seq, 0.1, True)
    walk_left = pyglet.resource.image("fire_light_walk_left.png")
    walk_left_seq = pyglet.image.ImageGrid(walk_left, 1, 2)
    walk_left_anim = pyglet.image.Animation.from_image_sequence(walk_left_seq, 0.1, True)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(self.__class__)    
        print(self.__class__ == "objects.FireLight")

class Dragon(WalkingPlayer):
    
    stand_left = pyglet.resource.image("dragon_stand_left.png")
    util.center_walking_player(stand_left)
    stand_left_seq = pyglet.image.ImageGrid(stand_left, 1, 1)
    stand_left_anim = pyglet.image.Animation.from_image_sequence(stand_left_seq, 1, True) 
    walk_right = pyglet.resource.image("dragon_walk_right.png")
    walk_right_seq = pyglet.image.ImageGrid(walk_right, 1, 2)
    walk_right_anim = pyglet.image.Animation.from_image_sequence(walk_right_seq, 0.1, True)
    walk_left = pyglet.resource.image("dragon_walk_left.png")
    walk_left_seq = pyglet.image.ImageGrid(walk_left, 1, 2)
    walk_left_anim = pyglet.image.Animation.from_image_sequence(walk_left_seq, 0.1, True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class BigBoo(FloatingPlayer):
    
    stand_left = pyglet.resource.image("big_boo_stand_left.png")
    util.center_floating_player(stand_left)
    stand_left_seq = pyglet.image.ImageGrid(stand_left, 1, 1)
    stand_left_anim = pyglet.image.Animation.from_image_sequence(stand_left_seq, 1, True) 
    walk_right = pyglet.resource.image("big_boo_walk_right.png")
    walk_right_seq = pyglet.image.ImageGrid(walk_right, 1, 1)
    walk_right_anim = pyglet.image.Animation.from_image_sequence(walk_right_seq, 0.1, True)
    walk_left = pyglet.resource.image("big_boo_walk_left.png")
    walk_left_seq = pyglet.image.ImageGrid(walk_left, 1, 1)
    walk_left_anim = pyglet.image.Animation.from_image_sequence(walk_left_seq, 0.1, True)
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class GreenKoopa(WalkingPlayer):
    
    stand_left = pyglet.resource.image("green_koopa_stand_left.png")
    util.center_walking_player(stand_left)
    stand_left_seq = pyglet.image.ImageGrid(stand_left, 1, 1)
    stand_left_anim = pyglet.image.Animation.from_image_sequence(stand_left_seq, 1, True) 
    walk_right = pyglet.resource.image("green_koopa_walk_right.png")
    walk_right_seq = pyglet.image.ImageGrid(walk_right, 1, 2)
    walk_right_anim = pyglet.image.Animation.from_image_sequence(walk_right_seq, 0.1, True)
    walk_left = pyglet.resource.image("green_koopa_walk_left.png")
    walk_left_seq = pyglet.image.ImageGrid(walk_left, 1, 2)
    walk_left_anim = pyglet.image.Animation.from_image_sequence(walk_left_seq, 0.1, True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class BigMole(WalkingPlayer):
    
    stand_left = pyglet.resource.image("big_mole_stand_left.png")
    util.center_walking_player(stand_left)
    stand_left_seq = pyglet.image.ImageGrid(stand_left, 1,1)
    stand_left_anim = pyglet.image.Animation.from_image_sequence(stand_left_seq, 1, True) 
    walk_right = pyglet.resource.image("big_mole_walk_right.png")
    walk_right_seq = pyglet.image.ImageGrid(walk_right, 1, 2)
    walk_right_anim = pyglet.image.Animation.from_image_sequence(walk_right_seq, 0.1, True)
    walk_left = pyglet.resource.image("big_mole_walk_left.png")
    walk_left_seq = pyglet.image.ImageGrid(walk_left, 1, 2)
    walk_left_anim = pyglet.image.Animation.from_image_sequence(walk_left_seq, 0.1, True)
 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class Mario(WalkingPlayer):

    stand_left = pyglet.resource.image("big_mario_standing_left.png")
    util.center_walking_player(stand_left)
    stand_left_seq = pyglet.image.ImageGrid(stand_left, 1,1)
    stand_left_anim = pyglet.image.Animation.from_image_sequence(stand_left_seq, 1, True)
    walk_right_img = pyglet.resource.image("mario_walking_right.png")
    walk_right_seq = pyglet.image.ImageGrid(walk_right_img, 1, 3)
    walk_right_anim = pyglet.image.Animation.from_image_sequence(walk_right_seq, 0.1, True)
    walk_left_img = pyglet.resource.image("mario_walking_left.png")
    walk_left_seq = pyglet.image.ImageGrid(walk_left_img, 1, 3)
    walk_left_anim = pyglet.image.Animation.from_image_sequence(walk_left_seq, 0.1, True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.key_handler = key.KeyStateHandler()


