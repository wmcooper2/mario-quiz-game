#std lib

#3rd party
import pyglet

#custom
from constants import Constants as c
from problems import Problem


def play_game() -> None:
    """Draw all the visual elements."""
    #update these vars each time through the loop
    c.P1 = c.PLAYERS[0]
    item = c.P1.inventory
    question = c.NEW_QUESTION
    scores = c.SCORE_DISPLAY
    PROB = Problem
    BB = PROB.BLACK_BOX

    if item:
        #QUESTION
        # basic pattern:
            # draw the black box
            # change the guide
            # change the question in the problem
            # draw the guide
            # draw the question        
        #         BB.draw()
        #         S_BB = True     #set flag
        if question:
            question = False    #reset flag
            #simple vocab
            if isinstance(item, RedMushroom):    
                PROB.random_english_word()
            #verbs
            elif isinstance(item, GreenMushroom):  
                PROB.random_present_verb()
            #Japanese to English translation
            elif isinstance(item, PirahnaPlant):   
                PROB.random_target_sentence()
            #pronunciation
            elif isinstance(item, YoshiCoin):      
                PROB.random_pronunciation()
            #answer the question
            elif isinstance(item, SpinyBeetle):    
                PROB.random_question()
    #         PROB.guide.draw()
    #         PROB.question.draw()

    #SCORES
#     for score in scores:
#         if score.points == 0:
#             score.zero.draw()
#         elif abs(score.points) > 0 and abs(score.points) <= 5:
#             for element in score.small_score:
#                 element.draw()
#         elif abs(score.points) > 5:
#             for element in score.big_score:
#                 element.draw()
    c.GAME_WINDOW.clear()
    c.BACKGROUND_BATCH.draw()
    c.YAMMY_BATCH.draw()
    c.PLAYER_BATCH.draw()
    c.SCORE_BATCH.draw()
    c.ITEM_BATCH.draw()
