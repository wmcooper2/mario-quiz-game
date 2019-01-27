#stand lib

#3rd party
import pyglet

#custom
from src.constants import *
import src.temporarydatasolution as tds

class Problem(pyglet.text.Label):

    black_box_img = pyglet.resource.image("black_box.png")
    black_box = pyglet.sprite.Sprite(black_box_img, x = 345, y = 264)
    center_x = black_box_img.width // 2 + black_box.x
    center_y = black_box_img.height // 2 + black_box.y
    guide = pyglet.text.Label(text="default guide", \
        font_name=ENGLISH_FONT, \
        font_size=GUIDE_SIZE, \
        anchor_x="center",  x=center_x, y=center_y + 60)
    question = pyglet.text.Label(text="default question", \
        font_name=ENGLISH_FONT, \
        font_size=QUESTION_SIZE, \
        width=black_box_img.width, \
        x=center_x, y=center_y)

    def __init__(self, x = 345, y = 300, text = "blank",  *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.question.anchor_x = "center"
        self.question.anchor_y = "center"
        self.data = tds.Data()

# need to set width and mulitline flags for the sentences and questions.
    
    def random_english_word(self):
        """Chooses a random English vocabulary word. Returns None."""
        self.guide.font_name = ENGLISH_FONT
        self.guide.text = "Translate to Japanese"
        self.question.text = self.data.english_word() 

#    def random_japanese_word(self):
#        """Chooses a random Japanese vocabulary word. Returns None."""
#        choice = self.data.english_word()
#        self.guide.font_name = JAPANESE_FONT
#        self.guide.text = choice                    #put this into self.data instance
#        self.question.text = self.data.japanese_word() 
    
    def random_image(self):
        """Chooses a random word and loads the associated image. Returns None."""
        self.question.text = "image word" 

    def random_present_verb(self):
        """Chooses random type of present-tense verb. Returns None."""
        self.guide.font_name = ENGLISH_FONT
        self.guide.text = "Translate to Japanese"
        self.question.text = self.data.random_verb() 

    def random_verb_form(self):
        """Chooses a random verb form from a random verb. Returns None."""
        self.guide.font_name = ENGLISH_FONT
        self.question.text = self.data.random_verb_form()

    def random_past_verb(self):
        """Chooses a random verb's past form. Returns None."""
        self.guide.font_name = ENGLISH_FONT
        self.question.text = self.data.random_past_verb() 
    
    def random_target_sentence(self):
        """Chooses a random target sentence. Returns None."""
        self.guide.font_name = ENGLISH_FONT
        self.guide.text = "Translate to Japanese"
        self.question.text = self.data.random_target_sentence() 

#    def random_japanese_target_sentence(self):
#        """Chooses a random Japanese target sentence. Returns None."""
#        self.guide.font_name = JAPANESE_FONT
#        self.question.text = "Get Japanese sentences."

    def random_pronunciation(self):
        """Chooses a random word that is difficult to pronuounce. Returns None."""
#        self.guide.font_name = JAPANESE_FONT
#        self.guide.text = "発音練習"
        self.guide.font_name = ENGLISH_FONT
        self.guide.text = "Please say the word"
        self.question.text = self.data.random_pronunciation() 

    def random_question(self):
        """Chooses a random question. Returns None."""
        self.guide.font_name = ENGLISH_FONT
        self.guide.text = "Answer the question in English"
##        document = pyglet.text.decode_text("TEST OF DOCUMENTTEST OF DOCUMENTTEST OF DOCUMENTTEST OF DOCUMENTTEST OF DOCUMENTTEST OF DOCUMENT")
#        self.question = pyglet.text.layout.TextLayout(document, Problem.black_box_img.width, Problem.black_box_img.height//2)
##        self.question = pyglet.text.layout.TextLayout(document, Problem.black_box_img.width, Problem.black_box_img.height//2, x=300, y=300)
#        self.question = pyglet.text.layout.TextLayout(document, Problem.black_box_img.width, Problem.black_box_img.height//2)
#        self.question = pyglet.text.layout.TextLayout(document, Problem.black_box_img.width, Problem.black_box_img.height//2)
#        self.question = pyglet.text.layout.FormattedDocument(document, Problem.black_box_img.width, Problem.black_box_img.height//2)
        self.question.text = self.data.random_question()
##        self.question.text = document
