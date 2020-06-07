from constants import *

difficulty = [SUPER_EASY, EASY, MEDIUM, HARD, SUPER_HARD]
#item_probabilities = [SUPER_EASY_RANGE, EASY_RANGE, MEDIUM_RANGE, HARD_RANGE, SUPER_HARD_RANGE]
debug_values = [
    DEBUG, 
    ALL_RED_MUSHROOMS,
    ALL_GREEN_MUSHROOMS,
    ALL_YOSHI_COINS,
    ALL_PIRAHNA_PLANTS,
    ALL_SPINY_BEETLES,
    ALL_POW_BUTTONS,
    ALL_BOMBOMBS,    
]


def test_debug_is_off():
    """Debug values are set to False for normal gameplay."""
    assert any(debug_values) == False

def test_frame_rate_less_than_100():
    """Frame rate is less than 100."""
    assert (FRAME_SPEED > (1/100)) == True

def test_number_of_players_between_2_and_6_inclusive():
    """Number of players is >=2 and <=6."""
    assert (NUM_PLAYERS>=2 and NUM_PLAYERS<=6) == True

def test_number_of_items_less_than_10():
    """Number of items is less than 10."""
    assert(NUM_ITEMS < 10) == True

def test_game_difficulty():
    """At least one difficulty is chosen.""" 
    assert any(difficulty) == True

def test_only_one_difficulty():
    """Only one difficulty level is chosen."""
    assert difficulty.count(True) == 1

def test_super_easy_item_probability():
    """Super easy item probability equals 100."""
    result = 0
    result += SUPER_EASY_RANGE[0]           #add the first element
    for x in range(len(SUPER_EASY_RANGE)-1):
        result += (SUPER_EASY_RANGE[x+1] - SUPER_EASY_RANGE[x])
    assert result == 100  

def test_easy_item_probability():
    """Easy item probability equals 100."""
    result = 0
    result += EASY_RANGE[0]           #add the first element
    for x in range(len(EASY_RANGE)-1):
        result += (EASY_RANGE[x+1] - EASY_RANGE[x])
    assert result == 100  

def test_medium_item_probability():
    """Medium item probability equals 100."""
    result = 0
    result += MEDIUM_RANGE[0]           #add the first element
    for x in range(len(MEDIUM_RANGE)-1):
        result += (MEDIUM_RANGE[x+1] - MEDIUM_RANGE[x])
    assert result == 100  

def test_hard_item_probability():
    """Hard item probability equals 100."""
    result = 0
    result += HARD_RANGE[0]           #add the first element
    for x in range(len(HARD_RANGE)-1):
        result += (HARD_RANGE[x+1] - HARD_RANGE[x])
    assert result == 100  

def test_super_hard_item_probability():
    """Super hard item probability equals 100."""
    result = 0
    result += SUPER_HARD_RANGE[0]           #add the first element
    for x in range(len(SUPER_HARD_RANGE)-1):
        result += (SUPER_HARD_RANGE[x+1] - SUPER_HARD_RANGE[x])
    assert result == 100  
