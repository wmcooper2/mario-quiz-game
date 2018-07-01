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

    def english_word(self):
        """Chooses a random English vocabulary word. Returns None."""
#        self.text = random.choice(english words
#        self.question.text = random.choice(tds.Data.words)
        self.question.text = "english word" 

    def japanese_word(self):
        """Chooses a random Japanese vocabulary word. Returns None."""
#        self.text = random.choice(japanese words
#        self.question.text = random.choice(tds.Data.words)
        self.question.text = "japanese word" 
    
    def image_word(self):
        """Chooses a random word and loads the associated image. Returns None."""
        self.question.text = "image word" 
        #need to change the size of the image to fit within the Vocab box dimensions

    def random_verb(self):
        """Chooses random type of verb form. Returns None."""
#        choice = random.choice(self.past_verb, self.present_verb, self.continuous_verb)
#        choice()
        self.question.text = "random verb" 

    def past_verb(self):
        """Chooses a random verb's past form. Returns None."""
        self.question.text = "past verb" 
    
    def present_verb(self):
        """Chooses a random verb's present form. Returns None."""
        self.question.text = "present verb" 
    
    def continuous_verb(self):
        """Chooses a random verb's continuous form. Returns None."""
        self.question.text = "continuous verb" 

    def target_sentence(self):
        """Chooses a random target sentence. Returns None."""
        self.question.text = "target sentence" 
