import pyglet


class Yammy(pyglet.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.inventory = []
        self.appear_rate = 3
        self.victim = None
        self.scale = 2
        # self.opacity = 0

        self.face_right = pyglet.resource.image("yammyfaceright.png")
        self.act_right = pyglet.resource.image("yammyactionright.png")
        self.seq_right = pyglet.image.ImageGrid(self.act_right, 1, 2)
        self.anim_right = pyglet.image.Animation.from_image_sequence(
            self.seq_right, 0.2, False)

    def update(self, dt):
        """Yammy's main update loop. Returns None."""
        if self.inventory:  # empty list is "False"
            self.give_item_to_victim()
            # if items:  # if transfer not complete
            # items[0].update(dt)  # important
            # items[0].transition()  # important

    def give_item_to_victim(self):
        """Gives an item to a player. Returns String."""
        if self.victim:
            item = self.inventory[0]
    #        transfer_point  = self.victim.y//2
            if item.opacity == 0 and item.delta_y == 0:
                item.spot_x = self.victim.spot
                item.x = self.victim.spot
                item.falling = not item.falling
                item.appear = not item.appear
                item.transitioning = not item.transitioning
            if item.y <= self.victim.y:
                #        if item.y <= transfer_point:
                #            item.y = transfer_point
                item.falling = not item.falling
                self.victim.inventory.append(item)  # give item
                self.inventory.remove(item)  # remove item

    def wave_wand(self):
        """Yammy waves his magic wand. Returns None."""
        self.image = self.anim_right

    def take_item(self, item):
        """Adds item to Yammy's inventory. Returns None."""
        self.inventory.append(item)
