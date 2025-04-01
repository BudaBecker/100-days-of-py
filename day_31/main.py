import tkinter as tk
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

def main_game():
    
    def next_card():
        global current_card
        current_card = random.choice(to_learn)
        canvas.itemconfig(card_title, text=selected_language, fill="black")
        canvas.itemconfig(card_word, text=current_card[selected_language].lower(), fill="black")
        canvas.itemconfig(card_background, image=card_front_img)
        window.after(3000, func=flip_card)
    
    def flip_card():
        canvas.itemconfig(card_title, text="Português", fill="white")
        canvas.itemconfig(card_word, text=current_card["Português"].lower(), fill="white")
        canvas.itemconfig(card_background, image=card_back_img)
    
    window = tk.Tk()
    window.title("Flashy")
    window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
    
    canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
    card_front_img = tk.PhotoImage(file="images/card_front.png")
    card_back_img = tk.PhotoImage(file="images/card_back.png")
    card_background = canvas.create_image(400, 263, image=card_front_img)
    canvas.grid(row=0, column=0, columnspan=2)
    card_title = canvas.create_text(400, 150, text="clique em um botão", font=("Verdana", 40, "italic"))
    card_word = canvas.create_text(400, 263, text="Pronto?", font=("Verdana", 60, "bold"))
    
    cross_image = tk.PhotoImage(file="images/wrong.png")
    unknow_button = tk.Button(image=cross_image, highlightthickness=0, command=next_card)
    unknow_button.grid(row=1, column=0)
    
    check_image = tk.PhotoImage(file="images/right.png")
    known_button = tk.Button(image=check_image, highlightthickness=0, command=next_card)
    known_button.grid(row=1, column=1)
    
    window.mainloop()

class Language(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Seleção de Idioma")
        self.language = None

        self.portuguese_button = tk.Button(self, text="FRANÇAIS", command=self.french_return)
        self.portuguese_button.pack(pady=10)

        self.english_button = tk.Button(self, text="ENGLISH", command=self.english_return)
        self.english_button.pack(pady=10)

    def french_return(self):
        self.language = "Français"
        self.destroy()

    def english_return(self):
        self.language = "English"
        self.destroy()

def get_language():
    lang = Language()
    lang.config(padx=50, pady=50)
    lang.mainloop()
    return lang.language

if __name__ == "__main__":
    selected_language = get_language()
    if selected_language == "Français":
        data = pandas.read_csv("data/french_words.csv")
        to_learn = data.to_dict(orient="records")
        main_game()
    elif selected_language == "English":
        data = pandas.read_csv("data/english_words.csv")
        to_learn = data.to_dict(orient="records")
        main_game()
    else:
        print("Nenhum idioma selecionado.")