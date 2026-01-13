from app.flash_card_view import FlashcardView
from domain.word_trainer import WordTrainer
from persistance.csv_handler import CsvHandler

class FlashcardApp():
    """
    Application controller for the flashcard trainer.

    This class coordinates the overall application flow by connecting
    the user interface (FlashcardView), the domain logic (WordTrainer),
    and the persistence layer (CsvHandler).

    Responsibilities:
    - Initialize and wire together view, domain, and persistence components
    - Handle user interactions via registered callbacks
    - Control the learning workflow (new word, correct/incorrect answers)
    - Manage application startup and shutdown, including saving progress

    The controller contains no GUI-specific code and no domain logic;
    it only orchestrates communication between components.
    """

    def __init__(self):
        self.flash_card_view = FlashcardView(self.on_button_clicked)
        filename = self.flash_card_view.get_filename()

        # if user aborts the filedialog we close the main window and end the program
        if not filename:
            self.flash_card_view.close()
            return

        self.csv_handler = CsvHandler(filename=filename)
        self.word_trainer = WordTrainer(self.csv_handler.words)
        self.on_button_clicked(False)
        #self.word_trainer.get_new_word()
        #self.flash_card_view.show_new_word(self.word_trainer.word_combo, self.word_trainer.languages)
        self.flash_card_view.run()
        self.csv_handler.write_csv(filename)


    def on_button_clicked(self, correct: bool) -> None:
        if correct:
            self.word_trainer.delete_word_combo()
        self.word_trainer.get_new_word()
        self.flash_card_view.show_new_word(self.word_trainer.word_combo, self.word_trainer.languages)

