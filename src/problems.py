#3rd party
import pyglet

#custom
from src.constants import *
import src.temporarydatasolution as tds

class Problem(pyglet.text.Label):
    pi      = pyglet.resource.image
    sprite  = pyglet.sprite.Sprite
    label   = pyglet.text.Label

    #black box image
    bimg    = pi("black_box.png")
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

# need to set width and mulitline flags for the sentences and questions.
    
    def random_english_word(self):
        """Chooses a random English vocabulary word. Returns None."""
        self.guide.font_name = ENGLISH_FONT
        self.guide.text = "Translate to Japanese"
        self.quest.text = self.data.english_word() 

#    def random_japanese_word(self):
#        """Chooses a random Japanese vocabulary word. Returns None."""
#        choice = self.data.english_word()
#        self.guide.font_name = JAPANESE_FONT
#        self.guide.text = choice                    #put this into self.data instance
#        self.quest.text = self.data.japanese_word() 
    
    def random_image(self):
        """Chooses a random word. Returns None."""
        self.quest.text = "image word" 

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

#    def random_japanese_target_sentence(self):
#        """Chooses a random Japanese target sentence. Returns None."""
#        self.guide.font_name = JAPANESE_FONT
#        self.quest.text = "Get Japanese sentences."

    def pronunciation(self):
        """Chooses word difficult to pronuounce word. Returns None."""
#        self.guide.font_name = JAPANESE_FONT
#        self.guide.text = "発音練習"
        self.guide.font_name = ENGLISH_FONT
        self.guide.text = "Please say the word"
        self.quest.text = self.data.random_pronunciation() 

    def question(self):
        """Chooses a random quest. Returns None."""
        self.guide.font_name = ENGLISH_FONT
        self.guide.text = "Answer the quest in English"
##        document = pyglet.text.decode_text("TEST OF DOCUMENTTEST OF DOCUMENTTEST OF DOCUMENTTEST OF DOCUMENTTEST OF DOCUMENTTEST OF DOCUMENT")
#        self.quest = pyglet.text.layout.TextLayout(document, Problem.bimg.width, Problem.bimg.height//2)
##        self.quest = pyglet.text.layout.TextLayout(document, Problem.bimg.width, Problem.bimg.height//2, x=300, y=300)
#        self.quest = pyglet.text.layout.TextLayout(document, Problem.bimg.width, Problem.bimg.height//2)
#        self.quest = pyglet.text.layout.TextLayout(document, Problem.bimg.width, Problem.bimg.height//2)
#        self.quest = pyglet.text.layout.FormattedDocument(document, Problem.bimg.width, Problem.bimg.height//2)
        self.quest.text = self.data.random_question()
##        self.quest.text = document
