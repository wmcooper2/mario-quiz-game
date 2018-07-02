#need to import stuff from Total English Assistant to get vocab words
#create separate list of questions to randomly choose from too.
import pyglet
import temporarydatasolution as tds

class Problem(pyglet.text.Label):

    showing_black_box = False
    vocab_black_box_img = pyglet.resource.image("black_box.png")
    vocab_black_box = pyglet.sprite.Sprite(vocab_black_box_img, x = 345, y = 300)
    question_center_x = vocab_black_box_img.width // 2 + vocab_black_box.x
    question_center_y = vocab_black_box_img.height // 2 + vocab_black_box.y

    def __init__(self, x = 345, y = 300, text = "blank",  *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.q_x = Problem.question_center_x
        self.q_y = Problem.question_center_y
        self.question = pyglet.text.Label(text = "blank", font_name = "Comic Sans MS", x = self.q_x, y = self.q_y, font_size = 24)
        self.question.anchor_x = "center"
        self.question.anchor_y = "center"
        self.data = tds.Data()

    def random_english_word(self):
        """Chooses a random English vocabulary word. Returns None."""
        self.question.text = self.data.english_word() 

    def random_japanese_word(self):
        """Chooses a random Japanese vocabulary word. Returns None."""
        choice = self.data.english_word()
        self.question.text = self.data.japanese_word() 
    
    def random_image(self):
        """Chooses a random word and loads the associated image. Returns None."""
        self.question.text = "image word" 
        #need to change the size of the image to fit within the Vocab box dimensions
        #not completed in temporarydatasolution.py

    def random_present_verb(self):
        """Chooses random type of present-tense verb. Returns None."""
        self.question.text = self.data.random_verb() 

    def random_verb_form(self):
        """Chooses a random verb form from a random verb. Returns None."""
        self.question.text = self.data.random_verb_form()

    def random_past_verb(self):
        """Chooses a random verb's past form. Returns None."""
        self.question.text = self.data.random_past_verb() 
    
#    def continuous_verb(self):
#        """Chooses a random verb's continuous form. Returns None."""
#        self.question.text = self.data.random_continuous_verb() 

    def random_target_sentence(self):
        """Chooses a random target sentence. Returns None."""
        self.question.text = self.data.random_target_sentence() 
