import pyglet
import util

class Item(pyglet.sprite.Sprite):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.spot = self.x
        self.delta = 0        
        self.moving = False

    def normal(self, obj):
        """Applies the item's affect to the player. Returns None."""
        pass 
    
    def special(self, obj):
        """Applies the special affect to the player. Returns None."""
        pass
    
    def update(self, dt):
        self.delta_x = self.x - self.spot
        self.walk()
        self.move()

    def move(self):
        """Moves the items left or right. Returns None."""
        #move left or right
        delta = self.delta_x
        if delta > 0:
            self.x -= 1
        if delta < 0:
            self.x += 1

    def walk(self):
        """Changes the animation of the sprite"""
        delta = self.delta_x
        #update sprite image
        if delta != 0 and self.moving == False:
            self.moving = True
            if delta > 0:
                self.image = self.walk_left_anim 
            if delta < 0:
                self.image = self.walk_right_anim 
        elif delta == 0:
            self.image = self.stand_right_anim
            self.moving = False
        
class GreenMushroom(Item):
    """Green Mushroom is a free point. Returns None."""

    stand_left = pyglet.resource.image("green_mushroom.png")
    util.center_ground_sprite(stand_left)
    stand_left_seq = pyglet.image.ImageGrid(stand_left, 1, 1)
    stand_left_anim = pyglet.image.Animation.from_image_sequence(stand_left_seq, 1, True)

#    stand_right = pyglet.resource.image("green_mushroom.png")
#    util.center_ground_sprite(stand_right)
#    stand_right_seq = pyglet.image.ImageGrid(stand_right, 1, 1)
#    stand_right_anim = pyglet.image.Animation.from_image_sequence(stand_right_seq, 1, True)
#
#    walk_left = pyglet.resource.image("green_mushroom.png")
#    util.center_ground_sprite(walk_left)
#    walk_left_seq = pyglet.image.ImageGrid(walk_left, 1, 2)
#    walk_left_anim = pyglet.image.Animation.from_image_sequence(walk_left_seq, 0.1, True)
#
#    walk_right = pyglet.resource.image("green_mushroom.png")
#    util.center_ground_sprite(walk_right)
#    walk_right_seq = pyglet.image.ImageGrid(walk_right, 1, 2)
#    walk_right_anim = pyglet.image.Animation.from_image_sequence(walk_right_seq, 0.1, True)

    stand_right_anim = stand_left_anim
    walk_left_anim = stand_left_anim
    walk_right_anim = stand_left_anim

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class RedMushroom(Item):
    """Red Mushroom is a vocabulary question. Returns None."""
    
    stand_left = pyglet.resource.image("red_mushroom.png")
    util.center_ground_sprite(stand_left)
    stand_left_seq = pyglet.image.ImageGrid(stand_left, 1, 1)
    stand_left_anim = pyglet.image.Animation.from_image_sequence(stand_left_seq, 1, True)

#    stand_right = pyglet.resource.image("red_mushroom.png")
#    util.center_ground_sprite(stand_right)
#    stand_right_seq = pyglet.image.ImageGrid(stand_right, 1, 1)
#    stand_right_anim = pyglet.image.Animation.from_image_sequence(stand_right_seq, 1, True)
#
#    walk_left = pyglet.resource.image("red_mushroom.png")
#    util.center_ground_sprite(walk_left)
#    walk_left_seq = pyglet.image.ImageGrid(walk_left, 1, 2)
#    walk_left_anim = pyglet.image.Animation.from_image_sequence(walk_left_seq, 0.1, True)
#
#    walk_right = pyglet.resource.image("red_mushroom.png")
#    util.center_ground_sprite(walk_right)
#    walk_right_seq = pyglet.image.ImageGrid(walk_right, 1, 2)
#    walk_right_anim = pyglet.image.Animation.from_image_sequence(walk_right_seq, 0.1, True)

    stand_right_anim = stand_left_anim
    walk_left_anim = stand_left_anim
    walk_right_anim = stand_left_anim

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class PowButton(Item):
    """Pow Button takes away one point from everyone. Returns None."""
        
    stand_left = pyglet.resource.image("pow_button.png")
    util.center_ground_sprite(stand_left)
    stand_left_seq = pyglet.image.ImageGrid(stand_left, 1, 1)
    stand_left_anim = pyglet.image.Animation.from_image_sequence(stand_left_seq, 1, False)

#    stand_right = pyglet.resource.image("pow_button.png")
#    util.center_ground_sprite(stand_right)
#    stand_right_seq = pyglet.image.ImageGrid(stand_right, 1, 1)
#    stand_right_anim = pyglet.image.Animation.from_image_sequence(stand_right_seq, 1, True)
#
#    walk_left = pyglet.resource.image("pow_button.png")
#    util.center_ground_sprite(walk_left)
#    walk_left_seq = pyglet.image.ImageGrid(walk_left, 1, 2)
#    walk_left_anim = pyglet.image.Animation.from_image_sequence(walk_left_seq, 0.1, True)
#
#    walk_right = pyglet.resource.image("pow_button.png")
#    util.center_ground_sprite(walk_right)
#    walk_right_seq = pyglet.image.ImageGrid(walk_right, 1, 2)
#    walk_right_anim = pyglet.image.Animation.from_image_sequence(walk_right_seq, 0.1, True)

    stand_right_anim = stand_left_anim
    walk_left_anim = stand_left_anim
    walk_right_anim = stand_left_anim

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class YoshiCoin(Item):
    """Yoshi Coin is a translation question. Returns None."""

#    stand_left_img = pyglet.resource.image("yoshi_coin_left.png")
#    util.center_ground_sprite(stand_left_img)
#    stand_left_seq = pyglet.image.ImageGrid(stand_left_img, 1, 5)
#    stand_left_anim = pyglet.image.Animation.from_image_sequence(stand_left_seq, 0.1, True) 
    
    stand_right = pyglet.resource.image("yoshi_coin_right.png")
    util.center_ground_sprite(stand_right)
    stand_right_seq = pyglet.image.ImageGrid(stand_right, 1, 5)
    stand_right_anim = pyglet.image.Animation.from_image_sequence(stand_right_seq, 1, True)

    walk_left = pyglet.resource.image("yoshi_coin_left.png")
    util.center_ground_sprite(walk_left)
    walk_left_seq = pyglet.image.ImageGrid(walk_left, 1, 5)
    walk_left_anim = pyglet.image.Animation.from_image_sequence(walk_left_seq, 0.1, True)

    walk_right = pyglet.resource.image("yoshi_coin_right.png")
    util.center_ground_sprite(walk_right)
    walk_right_seq = pyglet.image.ImageGrid(walk_right, 1, 5)
    walk_right_anim = pyglet.image.Animation.from_image_sequence(walk_right_seq, 0.1, True)

    stand_left_anim = walk_left_anim

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class PirahnaPlant(Item):
    """Pirahna Plant takes a point from away from the player. Returns None."""
    
#    stand_left = pyglet.resource.image("pirahna_plant_small.png")
#    util.center_ground_sprite(stand_left)
#    stand_left_seq = pyglet.image.ImageGrid(stand_left, 1, 2)
#    stand_left_anim = pyglet.image.Animation.from_image_sequence(stand_left_seq, 0.3, True)

    stand_right = pyglet.resource.image("pirahna_plant_small.png")
    util.center_ground_sprite(stand_right)
    stand_right_seq = pyglet.image.ImageGrid(stand_right, 1, 2)
    stand_right_anim = pyglet.image.Animation.from_image_sequence(stand_right_seq, 0.1, True)

    walk_left = pyglet.resource.image("pirahna_plant_small.png")
    util.center_ground_sprite(walk_left)
    walk_left_seq = pyglet.image.ImageGrid(walk_left, 1, 2)
    walk_left_anim = pyglet.image.Animation.from_image_sequence(walk_left_seq, 0.1, True)

    walk_right = pyglet.resource.image("pirahna_plant_small.png")
    util.center_ground_sprite(walk_right)
    walk_right_seq = pyglet.image.ImageGrid(walk_right, 1, 2)
    walk_right_anim = pyglet.image.Animation.from_image_sequence(walk_right_seq, 0.1, True)

    stand_left_anim = stand_right_anim

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class SpinyBeetle(Item):
    """Spiny Beetle takes away two points from a player. Returns None."""

#    stand_left = pyglet.resource.image("spiny_beetle_stand_left.png")
#    util.center_ground_sprite(stand_left)
#    stand_left_seq = pyglet.image.ImageGrid(stand_left, 1, 1)
#    stand_left_anim = pyglet.image.Animation.from_image_sequence(stand_left_seq, 1, True)

    stand_right = pyglet.resource.image("spiny_beetle_stand_right.png")
    util.center_ground_sprite(stand_right)
    stand_right_seq = pyglet.image.ImageGrid(stand_right, 1, 1)
    stand_right_anim = pyglet.image.Animation.from_image_sequence(stand_right_seq, 1, True)

    walk_left = pyglet.resource.image("spiny_beetle_walk_left.png")
    util.center_ground_sprite(walk_left)
    walk_left_seq = pyglet.image.ImageGrid(walk_left, 1, 2)
    walk_left_anim = pyglet.image.Animation.from_image_sequence(walk_left_seq, 0.1, True)

    walk_right = pyglet.resource.image("spiny_beetle_walk_right.png")
    util.center_ground_sprite(walk_right)
    walk_right_seq = pyglet.image.ImageGrid(walk_right, 1, 2)
    walk_right_anim = pyglet.image.Animation.from_image_sequence(walk_right_seq, 0.1, True)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    
