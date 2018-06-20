import util
import items
import pyglet
import random
import objects


#game_window
game_window = pyglet.window.Window(1000,563) #16:9 screen
SCREEN_W = game_window.width
SCREEN_H = game_window.height
OFF_SCREEN_R = 1100
FLOAT_H = 100
WALK_H = 63

#determine number of players
num_players = 6

#create the spots for player positions on the screen
spots = util.Line(screen_w = SCREEN_W, num_players=num_players)
spots.line_up()

#setup images
game_objects = []
main_batch = pyglet.graphics.Batch()

#background
background = objects.Background(img = objects.Background.background_img, batch = main_batch)

#fire_light
fire_light = objects.FireLight(img = objects.FireLight.fire_light_img, x = OFF_SCREEN_R, y = FLOAT_H, batch = main_batch)
fire_light.scale = 2
game_window.push_handlers(fire_light)
game_window.push_handlers(fire_light.key_handler)

#dragon
dragon = objects.Dragon(img = objects.Dragon.dragon_img, x = OFF_SCREEN_R, y = WALK_H, batch = main_batch)
dragon.scale = 2
game_window.push_handlers(dragon)

#big_boo
big_boo = objects.BigBoo(img = objects.BigBoo.big_boo_img, x = OFF_SCREEN_R, y = FLOAT_H, batch = main_batch)
game_window.push_handlers(big_boo) 

#green_koopa
green_koopa = objects.GreenKoopa(img = objects.GreenKoopa.green_koopa_img, x = OFF_SCREEN_R, y = WALK_H, batch = main_batch) 
green_koopa.scale = 2
game_window.push_handlers(green_koopa)

#big_mole
big_mole = objects.BigMole(img = objects.BigMole.big_mole_img, x = OFF_SCREEN_R, y = WALK_H, batch = main_batch)
big_mole.scale = 2
game_window.push_handlers(big_mole)

#mario
mario = objects.Mario(img = objects.Mario.mario_img, x = OFF_SCREEN_R, y = WALK_H, batch = main_batch)
mario.scale = 2
game_window.push_handlers(mario)

#add lakitu, luigi, peach, toad

##randomize player selection... use the objects, not the names of images
player_list = [big_boo, green_koopa, big_mole, fire_light, dragon, mario]
def randomize_players():
    if objects.Player.randomized == False:
        objects.Player.randomized = True
        random_players = []
        copy = player_list[:]
        for x in range(num_players):
            player_choice = random.choice(copy)
            random_players.append(player_choice)
            copy.remove(player_choice)
        for player in random_players:
            game_objects.append(player) 
randomize_players()

@game_window.event
def on_draw():
    game_window.clear()
    main_batch.draw()

def update(dt):
    for obj in game_objects:
        obj.update(dt)
    fire_light.floating()
    big_boo.floating()

if __name__ == "__main__":
    pyglet.clock.schedule_interval(update, 1/120)
    pyglet.app.run()
