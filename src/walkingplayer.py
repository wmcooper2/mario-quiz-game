import pyglet
from player import Player


class WalkingPlayer(Player):
    def __init__(self, img, go_right_img, go_left_img, rest_images, anim_images, name, *args, **kwargs):
        self._center_walker(go_right_img)
        self._center_walker(go_left_img)
        super().__init__(img, go_right_img, go_left_img,
                         rest_images, anim_images, name, *args, **kwargs)

    def _center_walker(self, image):
        """Centers the anchor point in the image."""
        image.anchor_x = image.width // 2

    def _update_img(self) -> None:
        """Changes sprite's image depending on which direction it is going. Returns None.
            Example:
                if self._pos_delta() > 0: then the character will face left
                if self._pos_delta() < 0: then the character will face right
                if self._pos_delta() == 0: then the character will face left (facing yammy, the default direction)
        """
        diff = self._pos_delta()
        if diff > 0:
            self.image = self.go_left
        elif diff < 0:
            self.image = self.go_right
        elif diff == 0:
            self.image = self.look_left
