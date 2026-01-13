from app.flash_card_view import FlashcardView
from domain.word_trainer import WordTrainer
from persistance.csv_handler import CsvHandler

class FlashcardApp():
    def __init__(self):
        right_answer = self.right_answer
        wrong_answer = self.wrong_answer
        self.flash_card_view = FlashcardView(right_answer, pressed_nok=wrong_answer)
        filename = self.flash_card_view.get_filename()

        if not filename:
            self.flash_card_view.close()
            return

        self.csv_handler = CsvHandler(filename)
        self.word_trainer = WordTrainer(self.csv_handler.words)
        self.word_trainer.get_new_word()
        self.flash_card_view.show_new_word(self.word_trainer.word_combo, self.word_trainer.languages)
        self.flash_card_view.run()
        self.csv_handler.write_csv(filename)

    def right_answer(self):
        self.word_trainer.delete_word_combo()
        self.word_trainer.get_new_word()
        self.flash_card_view.show_new_word(self.word_trainer.word_combo, self.word_trainer.languages)

    def wrong_answer(self):
        self.word_trainer.get_new_word()
        self.flash_card_view.show_new_word(self.word_trainer.word_combo, self.word_trainer.languages)

