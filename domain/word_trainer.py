from random import choice

class WordTrainer():
    def __init__(self, words: list):
        self.words = words
        self.languages = self.words[0]
        self.words.pop(0)


    def get_new_word(self):
        self.word_combo = choice(self.words)


    def delete_word_combo(self):
        self.words.remove(self.word_combo)
