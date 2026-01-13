from random import randint

class WordTrainer():
    """
    Domain component responsible for managing the flashcard training logic.

    WordTrainer operates on a mutable list of vocabulary pairs and controls
    the learning workflow. It selects random word pairs for training, tracks
    the currently active word, and removes known words from the training set.

    Responsibilities:
    - Store and manage the list of vocabulary word pairs
    - Extract and expose the source and target languages
    - Select a random word pair for training
    - Remove correctly answered word pairs from the dataset

    This class contains no user interface code and no persistence logic.
    It represents pure domain behavior and can be tested independently.
    """
    def __init__(self, words: list):
        self.words = words
        self.languages = self.words[0]


    def get_new_word(self) -> None:
        index = randint(1,len(self.words)-1)
        self.word_combo = self.words[index]


    def delete_word_combo(self) -> None:
        self.words.remove(self.word_combo)
