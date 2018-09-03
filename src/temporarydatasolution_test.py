import temporarydatasolution as tds
import os

data = tds.Data()

def test_dictionary_exists():
    """Dictionary exists in the directory tree."""
    assert os.path.exists(data.default_dict_path) == True

def test_target_sentences_exist():
    """Target sentence file exists in the directory tree."""
    assert os.path.exists("./gamedata/targetsentences.py") == True




#test each word to make sure they are only nouns.
#do the same for the other lists in Data()
def test_data_has_nouns():
    """Data.nouns has words in it."""
    assert len(data.nouns) > 0

def test_data_instance_has_words():
    """The Data() instance is populated with words."""
    assert len(data.words) > 0

def test_total_word_count():
    """Data.words has 1450 words."""
    assert len(data.words) == 1450

def test_dictionary_loaded_into_data_instance():
    """A dictionary is loaded into Data.dictionary."""
    assert len(data.dictionary) > 0

def test_total_dictionary_word_count():
    """Data.dictionary has 1450 words."""
    assert len(data.dictionary) == 1450

