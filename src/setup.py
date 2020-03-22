from sharedconstants import main_batch
from yammy import Yammy
from walkingplayer import WalkingPlayer
from floatingplayer import FloatingPlayer
from background import Background
import pyglet
pyglet.resource.path = ["./images"]  # dont move this


YAMMY_PLATFORM_H: int = 264
YAMMY_X: int = 30
OFF_SCREEN_RIGHT: int = 1100
OFF_SCREEN_LEFT: int = -100
FLOAT_HEIGHT: int = 100
FLOAT_SPEED: int = 3
GROUND_HEIGHT: int = 63

# game background image
background_img = pyglet.resource.image("quiz1.png")
BACKGROUND = Background(img=background_img, batch=main_batch)

# PLAYER SETUP
# load player images into resources
yammy_img = pyglet.resource.image("yammyfaceright.png")

fire_light_img = pyglet.resource.image("firelightgoleft.png")
fire_light_go_right = pyglet.resource.image("firelightgoright.png")
fire_light_go_left = pyglet.resource.image("firelightgoleft.png")

boo_img = pyglet.resource.image("bigboofaceleft.png")
boo_go_right = pyglet.resource.image("bigboogoright.png")
boo_go_left = pyglet.resource.image("bigboogoleft.png")

mole_img = pyglet.resource.image("bigmolefaceleft.png")
mole_go_right = pyglet.resource.image("bigmolegoright.png")
mole_go_left = pyglet.resource.image("bigmolegoleft.png")

dragon_img = pyglet.resource.image("dragonfaceleft.png")
dragon_go_right = pyglet.resource.image("dragongoright.png")
dragon_go_left = pyglet.resource.image("dragongoleft.png")

koopa_img = pyglet.resource.image("greenkoopafaceleft.png")
koopa_go_right = pyglet.resource.image("greenkoopagoright.png")
koopa_go_left = pyglet.resource.image("greenkoopagoleft.png")

luigi_img = pyglet.resource.image("bigluigifaceleft.png")
luigi_go_right = pyglet.resource.image("bigluigigoright.png")
luigi_go_left = pyglet.resource.image("bigluigigoleft.png")

mario_img = pyglet.resource.image("bigmariofaceleft.png")
mario_go_right = pyglet.resource.image("bigmariogoright.png")
mario_go_left = pyglet.resource.image("bigmariogoleft.png")

# instantiate player sprites
yammy = Yammy(yammy_img, x=YAMMY_X, y=YAMMY_PLATFORM_H, batch=main_batch)
yammy.name = "yammy"
fire_light = FloatingPlayer(fire_light_img, fire_light_go_right,
                            fire_light_go_left, rest_images=1, anim_images=2, name="Fire Light", x=OFF_SCREEN_RIGHT, y=FLOAT_HEIGHT, batch=main_batch)
boo = FloatingPlayer(boo_img, boo_go_right,
                     boo_go_left, rest_images=1, anim_images=1, name="Big Boo", x=OFF_SCREEN_RIGHT, y=FLOAT_HEIGHT, batch=main_batch)
mole = WalkingPlayer(mole_img, mole_go_right, mole_go_left, rest_images=1, anim_images=2, name="Big Mole",
                     x=OFF_SCREEN_RIGHT, y=GROUND_HEIGHT, batch=main_batch)
dragon = WalkingPlayer(dragon_img, dragon_go_right,
                       dragon_go_left, rest_images=1, anim_images=2, name="Dragon", x=OFF_SCREEN_RIGHT, y=GROUND_HEIGHT, batch=main_batch)
koopa = WalkingPlayer(koopa_img, koopa_go_right,
                      koopa_go_left, rest_images=1, anim_images=2, name="Koopa Troopa", x=OFF_SCREEN_RIGHT, y=GROUND_HEIGHT, batch=main_batch)
luigi = WalkingPlayer(luigi_img, luigi_go_right,
                      luigi_go_left, rest_images=1, anim_images=2, name="Luigi", x=OFF_SCREEN_RIGHT, y=GROUND_HEIGHT, batch=main_batch)
mario = WalkingPlayer(mario_img, mario_go_right,
                      mario_go_left, rest_images=1, anim_images=3, name="Mario", x=OFF_SCREEN_RIGHT, y=GROUND_HEIGHT, batch=main_batch)
players = [fire_light, boo, mole, dragon, koopa, luigi, mario]
