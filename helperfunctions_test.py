from constants import LINE
from constants import NUM_PLAYERS
from constants import NUM_ITEMS
from constants import SCREEN_WIDTH

def test_top_row_spots():
    """The number of top row spots is the sum of the inventory spot and the number of players. Returns None."""
    assert (len(LINE.top_row_spots) == (NUM_PLAYERS + 1)) == True

def test_inventory_spot():
    """There is only one inventory spot. Return None."""
    assert (len(LINE.inventory_spot) == 1) == True

def test_player_spots():
    """The number of player spots matches the number of players. Returns None."""
    assert (len(LINE.player_spots) == NUM_PLAYERS) == True

def test_item_spots():
    """The number of item spots matches the number of items. Returns None."""
    assert (len(LINE.item_spots) == NUM_ITEMS) == True 
