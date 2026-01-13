from random import choice, randint

class WordTrainer():
    def __init__(self, words: list):
        self.words = words
        self.languages = self.words[0]
        #self.words.pop(0)


    def get_new_word(self):
        index = randint(1,len(self.words)-1)
        self.word_combo = self.words[index]


    def delete_word_combo(self):
        self.words.remove(self.word_combo)
