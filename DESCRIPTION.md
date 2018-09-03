# Game Description

Up to 6 players compete in an English review game for points. Players take turns answering questions/problems that appear on the screen. The game will continue indefinitely (it is up to the user to quit the game).

* This Super Mario World styled game is meant for up to 6 teams.
* It is intended to be a review of the content in the Total English book series ([Rakuten][Book2]).
* Some custom questions/problems have been added (will be modified later)


# Instructions
### Run the game
From the root directory, run `game.py`


### Keyboard Controls
* up arrow      randomly mixes players
* down arrow    (none)
* left arrow    rotates players left
* right arrow   rotates players right
* 1             gives item to player in "ready position" (next player)
* f             fade Yammy character
* a             rotates items left
* s             randomly mixes items
* d             rotates items right
* o             when a problem is showing, player gets point
* x             when a problem is showing, player loses point



# Developer Notes
### Known Bugs
* There are few tests for this program.
* Long sentences do not wrap within the black box.
* Japanese characters are cut in half within each character's individual box showing only the left half of each character in a string.
* a thin, vertical black line appears next to the character sprites.
* players' "0" scores are not center aligned with their score-display sprites.
* when a player's score is >=|6| the large numbered scores dont disappear to allow a clean visual of the new score.
* Bombomb does not have a set up question, defaults to "default question"

### File Info
* Game constants/settings are in "constants.py"
* Questions/problems are found in "marioquiz/gamedata/"


### Tests
run `./Test` from the root directory


### Resources
Mario sprites taken from;
* [Spriters Resource](https://www.spriters-resource.com/snes/smarioworld/)
* [Mario Universe](http://www.mariouniverse.com/maps-snes-smw/)

[Book2]: https://item.rakuten.co.jp/learners/10000360/?scid=af_pc_etc&sc2id=af_113_0_10001868
