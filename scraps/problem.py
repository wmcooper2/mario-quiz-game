import pyglet
import math
import random

from pyglet.window import key
key_handler = key.KeyStateHandler()

game_window = pyglet.window.Window(1200, 600)

class Problem(pyglet.text.Label):

    def __init__(self, x = 0, y = 0, text = "blank", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.x = x 
        self.y = y
        self.text = text
        self.anchor_x = "center"
        self.anchor_y = "center"
        self.font_name = "Comic Sans MS"
        self.font_size = 36

class SimpleProblem(Problem):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.questions = ["Who?", "What?", "When?", "Where?", "Why?", "How?"]
        self.x = 150
        self.y = 150   
 
    def new_question(self):
        self.text = random.choice(self.questions)
 
class BlackBox():
    
    def __init__(self, *args, **kwargs):
        self.width = 0
        self.height = 0
#        self.color = (0,0,0) #black
        self.color = (255,255,255) #white
        self.speed = math.floor(max(self.width, self.height)/120) #the largest dimension divided by the frame rate => one second until fully expanded is the goal.
        self.transitioning = False
        self.current_width = 0
        self.current_height = 0

    def box_at_full_size(self):
        """Checks that the problem's box is at full size. Returns Boolean."""
        return self.current_width == self.width and self.current_height == self.height

    def show_problem(self):
        """Draws the problem's text to the screen. Returns None."""
        print("showing problem")

    def update(self):
        if self.box_at_full_size():
            self.show_problem()

problems = []
test_problem = SimpleProblem()
game_window.push_handlers(key_handler)
problems.append(test_problem)

@game_window.event
def on_draw():
    game_window.clear()
    test_problem.draw()

def update(dt):
    """Main update loop. Returns None."""
    if key_handler[key.LEFT]:
        problems[0].new_question()

if __name__ == "__main__":
    pyglet.clock.schedule_interval(update, 1/10)
    pyglet.app.run()
    
