import pyglet
import math
import util
import problems

main_time = 0

class Item(pyglet.sprite.Sprite):
    
    debug = False

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.spot_x = self.x
        self.spot_y = self.y
        self.delta_x = 0        
        self.delta_y = 0
        self.y_speed = 1
        self.x_speed = 1
        self.transition_direction = "out"
        self.transition_rate = 9
        self.moving = False
        self.falling = False
        self.transitioning = False
        self.special == False
        self.problem = problems.Problem()
        self.item_not_used = True

    def normal(self, obj):
        """Applies the item's affect to the player. Returns None."""
        pass 
    
    def special(self, obj):
        """Applies the special affect to the player. Returns None."""
        pass
    
    def update(self, dt):
        #adding gravity effect to item
        if self.falling: 
            global main_time
            main_time += dt
            if main_time > 5:
                main_time = 0
            self.y += util.falling_object(main_time)

        self.delta_x = self.x - self.spot_x #current spot "x" - where its supposed to be "spot_x"
        self.delta_y = self.y - self.spot_y
        self.walk()
        self.move() #self.x_speed)
        if Item.debug == True:
            self.debug_info()
        self.transition()

    def move(self): 
        """Moves the items closer to spot_x and spot_y. Returns None."""
        delta_x = self.delta_x
        delta_y = self.delta_y
        if delta_x > 0:
            self.x -= self.x_speed
        if delta_x < 0:
            self.x += self.x_speed
        if delta_y > 0:
            self.y -= self.y_speed
        if delta_y < 0:
            self.y += self.y_speed

    def walk(self):
        """Changes the animation of the sprite"""
        delta_x = self.delta_x
        #update sprite image
        if delta_x != 0 and self.moving == False:
            self.moving = True
            if delta_x > 0:
                self.image = self.walk_left_anim 
            if delta_x < 0:
                self.image = self.walk_right_anim 
        elif delta_x == 0:
            self.image = self.stand_right_anim
            self.moving = False
    
    def toggle_transition_direction(self):
        """Toggles transition_direction attribute. Returns None."""
        if self.transition_direction == "in":
            self.transition_direction = "out"
        elif self.transition_direction == "out":
            self.transition_direction = "in"

    def transition(self):
        """Toggles item opacity. Returns None."""
        if self.transitioning:
            if self.transition_direction == "in":
                self.opacity += self.transition_rate
            if self.transition_direction == "out":
                self.opacity -= self.transition_rate
            if self.opacity >= 255:
                self.opacity = 255
                self.transitioning = False
            if self.opacity <= 0:
                self.opacity = 0
                self.transitioning = False

class GreenMushroom(Item):
    """Green Mushroom is a random verb form question. Returns None."""

    stand_left = pyglet.resource.image("green_mushroom.png")
    util.center_ground_sprite(stand_left)
    stand_left_seq = pyglet.image.ImageGrid(stand_left, 1, 1)
    stand_left_anim = pyglet.image.Animation.from_image_sequence(stand_left_seq, 1, True)

    stand_right_anim = stand_left_anim
    walk_left_anim = stand_left_anim
    walk_right_anim = stand_left_anim

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def effect(self):
        """Presents a verb form problem. Returns None"""
        print("item effect, Items()")
        self.problem.showing_black_box = True
        self.problem.random_present_verb()

    def delete(self):
        super(Item, self).delete()

class RedMushroom(Item):
    """Red Mushroom is a random vocabulary question. Returns None."""
    
    stand_left = pyglet.resource.image("red_mushroom.png")
    util.center_ground_sprite(stand_left)
    stand_left_seq = pyglet.image.ImageGrid(stand_left, 1, 1)
    stand_left_anim = pyglet.image.Animation.from_image_sequence(stand_left_seq, 1, True)

    stand_right_anim = stand_left_anim
    walk_left_anim = stand_left_anim
    walk_right_anim = stand_left_anim

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def effect(self):
        """Presents a vocabulary word problem. Returns None"""
        print("item effect, Items()")
        self.problem.showing_black_box = True
        self.problem.random_english_word()

    def delete(self):
        super(Item, self).delete()

class PowButton(Item):
    """Pow Button takes away one point from everyone. Returns None."""
    #rethink the effect of this item
        
    stand_left = pyglet.resource.image("pow_button.png")
    util.center_ground_sprite(stand_left)
    stand_left_seq = pyglet.image.ImageGrid(stand_left, 1, 1)
    stand_left_anim = pyglet.image.Animation.from_image_sequence(stand_left_seq, 1, False)

    stand_right_anim = stand_left_anim
    walk_left_anim = stand_left_anim
    walk_right_anim = stand_left_anim

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def effect(self):
        """Presents an unknown problem. Returns None"""
        print("item effect, Items()")
        self.problem.showing_black_box = True
        self.problem.random_image()

    def delete(self):
        super(Item, self).delete()

class YoshiCoin(Item):
    """Yoshi Coin is a pronunciation question. Returns None."""
    
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

    def effect(self):
        """Presents a pronunciation problem. Returns None"""
        print("item effect, Items()")
        self.problem.showing_black_box = True
        self.problem.question.text = "pronunciation problem"
        #not complete in problems.py
        #not complete in temporarydatasolution.py

    def delete(self):
        super(Item, self).delete()

class PirahnaPlant(Item):
    """Pirahna Plant is a sentence translation problem (English to Japanese). Returns None."""

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

    def effect(self):
        """Presents a sentence translation problem (English to Japanese). Returns None"""
        print("item effect, Items()")
        self.problem.showing_black_box = True
        self.problem.random_target_sentence()

    def delete(self):
        super(Item, self).delete()

class SpinyBeetle(Item):
    """Spiny Beetle is a sentence translation problem (Japanese to English). Returns None."""

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

    def effect(self):
        """Presents a sentence translation problem (Japanese to English). Returns None"""
        print("item effect, Items()")
        self.problem.showing_black_box = True
        self.problem.text = "spiny beetle"
        #unfinished

    def delete(self):
        super(Item, self).delete()

    
