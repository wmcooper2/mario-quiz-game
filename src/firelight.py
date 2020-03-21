from math import sin, radians
import pyglet
from floatingplayer import FloatingPlayer


class FireLight(FloatingPlayer):
    def __init__(self, img, go_right_img, go_left_img, *args, **kwargs):
        # print("FireLight() args: ", args)
        # print("FireLight() kwargs: ", kwargs)
        # print("FireLight() args: ", self.__dict__)
        super().__init__(img, go_right_img, go_left_img, *args, **kwargs)

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
            self.image = self.go_left

    def update(self):
        self._update_img()
        self._update_pos()
        self._float()
        # self._take()
