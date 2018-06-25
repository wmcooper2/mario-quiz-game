import math
import util
import pyglet
from pyglet import clock

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
    game_just_started = True #use this to prevent the last player from running on stage?
    debug = False

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.spot = self.x #initially, off screen, changed immediately
        self.delta_x = 0 #intially zero, changed immediately
        self.item = "None"
        self.moving = False
        self.speed = "walk"
        self.rotating_players = False
        self.inventory = []
#        self.debug_xpos = pyglet.text.Label(text = str(self.x), font_name = 'Times New Roman', font_size = 10, x = self.delta_x, y = 10, color = (0, 0, 0, 255))
            
    def update(self, dt):
        self.delta_x = self.x - self.spot
        if Player.game_just_started:
            self.speed = "run"
        if self.spot == util.Line.player_spots[-1]: #if the player is in the ready position
            self.speed = "run"
        self.move()
#        self.debug_xpos.draw()
        #refactor move, walk, run and call them here
        #self.change_speed
        #self.change_animation
        #self.move 

    def game_in_play(self):
        """Sets self.game_just_started to False. Returns None."""
        Player.game_just_started = False

    def move(self):
        """Moves the player. Returns None."""
        if self.speed == "walk":
            self.walk()
        if self.speed == "run":
            self.run()

    def walk(self):
        """Walks the player left or right.
            Returns None."""
        delta = self.delta_x
        #update sprite image
        if delta != 0 and self.moving == False:
            self.moving = True
            if delta > 0:
                self.image = self.walk_left_anim
            if delta < 0:
                self.image = self.walk_right_anim
        elif delta == 0:
            self.image = self.stand_left_anim 
            self.moving = False
        #move left or right
        if delta > 0:
            self.x -= 1
        if delta < 0:
            self.x += 1

    def run(self):
        """Runs the player left or right.
            Returns None."""
        delta = self.delta_x
        #update sprite image
        if delta != 0 and self.moving == False:
            self.moving = True
            if delta > 0:
                self.image = self.run_left_anim
            if delta < 0:
                self.image = self.run_right_anim
        elif delta == 0:
            self.image = self.stand_left_anim 
            self.moving = False
            self.speed = "walk"
        #move left or right
        if delta > 0 and delta > 3:
            self.x -= 3
        if delta > 0 and delta <= 3:
            self.x -= 1
        if delta < 0 and abs(delta) > 3:
            self.x += 3
        if delta < 0 and abs(delta) <= 3:
            self.x += 1

    def delta_x(self):
        """Get the distance between objects position and spot position.
            Returns Integer."""
        return self.x - self.spot

    def debug_info(self):
        """Displays sprite information. Returns None."""
        spot = pyglet.text.Label(str(self.spot), font_name = 'Times New Roman', font_size = 10, x = self.anchor_x, y = 50, batch = main_batch)
        
#label = pyglet.text.Label('Hello, world', 
#                          font_name='Times New Roman', 
#                          font_size=36,
#                          x=10, y=10)

class FloatingPlayer(Player):
    """Creates a player that floats cyclicly in the air."""    
 
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
        
class Yammy(pyglet.sprite.Sprite):
    
    stand_right = pyglet.resource.image("yammy_stand_right.png")    
    action_right_img = pyglet.resource.image("yammy_action_right.png")
    action_right_seq = pyglet.image.ImageGrid(action_right_img, 1, 2)
    action_right_anim = pyglet.image.Animation.from_image_sequence(action_right_seq, 0.2, False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fade = "out"
        self.transition = False
        self.inventory = []
        self.magic_happening = False
        self.item_fade = "out"

    def action(self):
        """Animates the magic wand wave. Returns None."""

        print("yammy timer induced action")
        def yammy_standing():
            """Returns Yammy to the standing position. Returns None."""
            self.img = Yammy.stand_right

        self.img = Yammy.action_right_anim
        my_clock = clock.Clock()
        my_clock.schedule_once(yammy_standing, 0.6) 

    def give_item2(self):
        """Gives an item to a player. Returns String."""
        if self.item_fade == "in" and self.inventory and self.inventory[0].opacity < 255:
            self.item_fade_in()
        if self.item_fade == "out" and self.inventory and self.inventory[0].opacity > 0:
            self.item_fade_out()
        if self.inventory and self.inventory[0].opacity == 255:
            self.transition = False
        if self.inventory and self.inventory[0].opacity == 0:
            self.transition = False
#            return "item gone"

    def give_item(self):
        """Gives an item to a player. Returns String."""
        pass

    def item_fade_out(self):
        """Fades first inventory item out. Returns None."""
        self.inventory[0].opacity -=1

    def item_fade_in(self):
        """Fades first inventory item in. Returns None."""
        self.inventory[0].opacity += 1

    def fading(self):
        """Toggles fading animation. Returns None."""
        if self.fade == "in" and self.opacity < 255:
            self.fade_in()
        if self.fade == "out" and self.opacity > 0:
            self.fade_out()
        if self.opacity == 255:
            self.transition = False
        if self.opacity == 0:
            self.transition = False

    def fade_in(self):
        """Fades Yammy in to 255 opacity. Returns None."""
        self.opacity += 3
    
    def fade_out(self):
        """Fades Yammy out to 0 opacity. Returns None."""
        self.opacity -= 3

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
    run_right_anim = pyglet.image.Animation.from_image_sequence(walk_right_seq, 0.05, True)
    run_left_anim = pyglet.image.Animation.from_image_sequence(walk_left_seq, 0.05, True)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

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
    run_right_anim = pyglet.image.Animation.from_image_sequence(walk_right_seq, 0.05, True)
    run_left_anim = pyglet.image.Animation.from_image_sequence(walk_left_seq, 0.05, True)

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
    run_right_anim = pyglet.image.Animation.from_image_sequence(walk_right_seq, 0.05, True)
    run_left_anim = pyglet.image.Animation.from_image_sequence(walk_left_seq, 0.05, True)
    
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
    run_right_anim = pyglet.image.Animation.from_image_sequence(walk_right_seq, 0.05, True)
    run_left_anim = pyglet.image.Animation.from_image_sequence(walk_left_seq, 0.05, True)

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
    run_right_anim = pyglet.image.Animation.from_image_sequence(walk_right_seq, 0.05, True)
    run_left_anim = pyglet.image.Animation.from_image_sequence(walk_left_seq, 0.05, True)
 
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
    run_right_anim = pyglet.image.Animation.from_image_sequence(walk_right_seq, 0.05, True)
    run_left_anim = pyglet.image.Animation.from_image_sequence(walk_left_seq, 0.05, True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
