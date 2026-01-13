from tkinter import Tk, Button, PhotoImage, Canvas, filedialog
from os import path
from functools import partial
from config import (BACKGROUND_COLOR, CARD_FRONT_IMAGE,
                   CARD_BACK_IMAGE, BUTTON_OK_IMAGE,
                   BUTTON_NOK_IMAGE, WINDOW_WIDTH, WINDOW_HEIGHT,
                   WINDOW_PADDING, WINDOW_TITLE, DATA_DIR)

class FlashcardView():
    """
    User interface component for the flashcard training application.

    FlashcardView is responsible for creating and managing the graphical
    user interface using Tkinter. It displays flashcards, handles visual
    state changes (front/back of the card), and captures user interactions
    via buttons and dialogs.

    Responsibilities:
    - Initialize and manage all Tkinter widgets
    - Display vocabulary words and their translations
    - Handle visual state transitions (e.g. flipping cards)
    - Collect user input (button clicks, file selection)
    - Forward user actions to the application controller via callbacks

    This class contains no domain logic and no persistence logic.
    All application decisions are delegated to the controller.
    """
    def __init__(self, on_button_clicked):
        self.on_button_clicked = on_button_clicked
        self.root = Tk()
        self.root.config(width=WINDOW_WIDTH, height=WINDOW_HEIGHT,
                         padx=WINDOW_PADDING, pady=WINDOW_PADDING, bg=BACKGROUND_COLOR)
        self.root.title(WINDOW_TITLE)

        #* create the canvas and load the two images with tags so we can flip
        #* as well with the two text lines
        self.canvas_card = Canvas(width=800,height=526,background=BACKGROUND_COLOR, highlightthickness=0)
        self.image_card1 = PhotoImage(file=CARD_FRONT_IMAGE)
        self.image_card2 = PhotoImage(file=CARD_BACK_IMAGE)
        self.canvas_card.create_image(0, 0, image=self.image_card2, anchor="nw", tags="bg")
        self.canvas_card.create_image(0, 0, image=self.image_card1, anchor="nw", tags="fg")
        self.canvas_card.grid(row=1,column=1,columnspan=2)
        self.canvas_card.create_text(400,150,font=("Arial",40,"italic"), tags="language")
        self.canvas_card.create_text(400,263,font=("Arial",60,"bold"), tags="word")

        #* create buttons
        self.button_image_ok = PhotoImage(file=BUTTON_OK_IMAGE)
        self.button_image_nok = PhotoImage(file=BUTTON_NOK_IMAGE)
        self.button_ok = Button(image=self.button_image_ok,  background=BACKGROUND_COLOR, highlightthickness=0,
                            command=partial(self.on_button_clicked, True))

        self.button_nok = Button(image=self.button_image_nok, background=BACKGROUND_COLOR, highlightthickness=0,
                            command=partial(self.on_button_clicked, False))
        self.button_ok.grid(row=2, column=2)
        self.button_nok.grid(row=2, column=1)


    def show_new_word(self, words: list, languages: list) -> None:
        # I have to store the languages as attributes because I can't
        # give arguments to flip_card()
        self.languages = languages
        self.words = words
        self.button_ok.config(state="disabled")
        self.button_nok.config(state="disabled")
        self.canvas_card.tag_lower("bg")
        self.canvas_card.itemconfigure("language", text=self.languages[0])
        self.canvas_card.itemconfigure("word", text=words[0])
        self.root.after(3000,self.flip_card)


    def flip_card(self) -> None:
        self.button_ok.config(state="active")
        self.button_nok.config(state="active")
        self.canvas_card.tag_lower("fg")
        self.canvas_card.itemconfigure("language", text=self.languages[1])
        self.canvas_card.itemconfigure("word", text=self.words[1])


    def get_filename(self) -> str | None :
        filename = filedialog.askopenfilename(
                            title="Select file",
                            filetypes=[("csv files", "*.csv")],
                            initialdir=DATA_DIR
                        )
        if filename:
        #* extract only the filename
            return path.basename(filename)


    def close(self) -> None:
        self.root.destroy()


    def run(self) -> None:
        self.root.mainloop()
