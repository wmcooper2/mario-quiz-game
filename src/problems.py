#3rd party
import pyglet

#custom
from constants import *
import temporarydatasolution as tds

def present_problem(pp, prob):
    """Presents a problem on the screen. Returns None."""
    # basic pattern:
        # draw the black box
        # change the guide
        # change the question in the problem
        # draw the guide
        # draw the question        
    item = pp.inventory[0]
#    prob.box.draw()
    FLAGS["box"] = not FLAGS["box"]

    if FLAGS["question"]:
        FLAGS["question"] = not FLAGS["question"]
        if is_eng_vocab(item):          prob.random_english_word()
        elif is_pres_verb(item):        prob.present_tense()
        elif is_j2e(item):              prob.target_sentence()
        elif is_e2j(item):              prob.pronunciation()
        elif is_pronunciation(item):    prob.question()
    prob.box.draw()
    prob.guide.draw()
    prob.quest.draw()

def is_eng_vocab(item):     return isinstance(item, RedMushroom)
def is_pres_verb(item):     return isinstance(item, GreenMushroom)
def is_j2e(item):           return isinstance(item, PirahnaPlant)
def is_e2j(item):           return isinstance(item, YoshiCoin)
def is_pronunciation(item): return isinstance(item, SpinyBeetle)

class Problem(pyglet.text.Label):
    pi      = pyglet.resource.image
    sprite  = pyglet.sprite.Sprite
    label   = pyglet.text.Label

    #black box image
    bimg    = pi("blackbox.png")
    box     = sprite(bimg, x=345, y=264)

    #box centers
    box_cx  = bimg.width // 2 + box.x
    box_cy  = bimg.height // 2 + box.y

    #box text elements
    guide   = label(text="default guide", font_name=ENGLISH_FONT, \
        font_size=GUIDE_SIZE, anchor_x="center", x=box_cx, \
        y=box_cy + 60)
    quest   = label(text="default question", font_name=ENGLISH_FONT, \
        font_size=QUESTION_SIZE, width=bimg.width, x=box_cx, \
        y=box_cy)

    def __init__(self, x=345, y=300, text="blank", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.quest.anchor_x = "center"
        self.quest.anchor_y = "center"
        self.data           = tds.Data()

    def english(self):
        """Chooses a random English word. Returns None."""
        self.guide.font_name = ENGLISH_FONT
        self.guide.text = "Translate to Japanese"
        self.quest.text = self.data.english_word() 

    def japanese(self):
        """Chooses a random Japanese word. Returns None."""
        choice = self.data.english_word()
        self.guide.font_name = JAPANESE_FONT
        self.guide.text = choice 
        self.quest.text = self.data.japanese_word() 
    
    def present_tense(self):
        """Chooses random present tense verb. Returns None."""
        self.guide.font_name = ENGLISH_FONT
        self.guide.text = "Translate to Japanese"
        self.quest.text = self.data.random_verb() 

    #nothing calls this
    def verb(self):
        """Chooses a random verb form. Returns None."""
        self.guide.font_name = ENGLISH_FONT
#        self.quide.text = 
        self.quest.text = self.data.random_verb_form()

    #nothing calls this
    def past_tense(self):
        """Chooses a random past tense verb. Returns None."""
        self.guide.font_name = ENGLISH_FONT
        self.quest.text = self.data.random_past_verb() 
    
    def target_sentence(self):
        """Chooses a random target sentence. Returns None."""
        self.guide.font_name = ENGLISH_FONT
        self.guide.text = "Translate to Japanese"
        self.quest.text = self.data.random_target_sentence() 

    def japanese_target_sentence(self):
        """Chooses a random Japanese target sentence. Returns None."""
        self.guide.font_name = JAPANESE_FONT
        self.quest.text = "Get Japanese sentences."

    def pronunciation(self):
        """Chooses word difficult to pronuounce word. Returns None."""
        #problems displaying japanese characters in pyglet
#        self.guide.font_name = JAPANESE_FONT
#        self.guide.text = "発音練習"
        self.guide.font_name = ENGLISH_FONT
        self.guide.text = "Please say the word"
        self.quest.text = self.data.random_pronunciation() 

    def question(self):
        """Chooses a random quest. Returns None."""
        self.guide.font_name = ENGLISH_FONT
        self.guide.text = "Answer the quest in English"
        self.quest.text = self.data.random_question()
