import pyglet
import temporarydatasolution as tds
import constants

class Problem(pyglet.text.Label):

    vocab_black_box_img = pyglet.resource.image("black_box.png")
    vocab_black_box = pyglet.sprite.Sprite(vocab_black_box_img, x = 345, y = 264)
    question_center_x = vocab_black_box_img.width // 2 + vocab_black_box.x
    question_center_y = vocab_black_box_img.height // 2 + vocab_black_box.y
    english_vocab_guide = pyglet.text.Label(text=constants.GUIDE, font_name=constants.FONT_NAME, anchor_x="center",  x=question_center_x, y=question_center_y + 60, font_size=constants.GUIDE_SIZE)
    english_sentence_guide = pyglet.text.Label(text=constants.GUIDE, font_name=constants.FONT_NAME, anchor_x="center",  x=question_center_x, y=question_center_y + 60, font_size=constants.GUIDE_SIZE)
    present_verb_guide = pyglet.text.Label(text=constants.GUIDE, font_name=constants.FONT_NAME, anchor_x="center",  x=question_center_x, y=question_center_y + 60, font_size=constants.GUIDE_SIZE)
    japanese_vocab_guide = pyglet.text.Label(text=constants.GUIDE, font_name=constants.FONT_NAME, anchor_x="center",  x=question_center_x, y=question_center_y + 60, font_size=constants.GUIDE_SIZE)
    pronunciation_guide = pyglet.text.Label(text="Speak", font_name=constants.FONT_NAME, anchor_x="center",  x=question_center_x, y=question_center_y + 60, font_size=constants.GUIDE_SIZE)
    japanese_sentence_guide = pyglet.text.Label(text=constants.GUIDE, font_name=constants.FONT_NAME, anchor_x="center",  x=question_center_x, y=question_center_y + 60, font_size=constants.GUIDE_SIZE)
    answer_my_question_guide = pyglet.text.Label(text="Answer the question", font_name=constants.FONT_NAME, anchor_x="center",  x=question_center_x, y=question_center_y + 60, font_size=constants.GUIDE_SIZE)

    def __init__(self, x = 345, y = 300, text = "blank",  *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.q_x = Problem.question_center_x
        self.q_y = Problem.question_center_y
        self.question = pyglet.text.Label(text="blank", font_name=constants.FONT_NAME, x=self.q_x, y=self.q_y, font_size=constants.QUESTION_SIZE, width=self.vocab_black_box_img.width)
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

    def random_present_verb(self):
        """Chooses random type of present-tense verb. Returns None."""
        self.question.text = self.data.random_verb() 

    def random_verb_form(self):
        """Chooses a random verb form from a random verb. Returns None."""
        self.question.text = self.data.random_verb_form()

    def random_past_verb(self):
        """Chooses a random verb's past form. Returns None."""
        self.question.text = self.data.random_past_verb() 
    
    def random_target_sentence(self):
        """Chooses a random target sentence. Returns None."""
        self.question.text = self.data.random_target_sentence() 

    def random_japanese_target_sentence(self):
        """Chooses a random Japanese target sentence. Returns None."""
        self.question.text = "Get Japanese sentences."

    def random_pronunciation(self):
        """Chooses a random word that is difficult to pronuounce. Returns None."""
        self.question.text = self.data.random_pronunciation() 

    def random_question(self):
        """Chooses a random question. Returns None."""
        self.question.text = self.data.random_question()
