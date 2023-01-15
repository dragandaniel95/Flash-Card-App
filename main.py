import random
from tkinter import*
import pandas
BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")

words_dict = data.to_dict(orient="records")
current_card = random.choice(words_dict)
print(current_card)


def is_known():
    words_dict.remove(current_card)
    data_file = pandas.DataFrame(words_dict)   # Creare data frame dintr-un dictionar
    data_file.to_csv("data/words_to_learn.csv", index=False)  # Introducere date in data frame-ul creat (CSV nou)
    next_card()


def next_card():
    global current_card
    global flip_timer
    current_card = random.choice(words_dict)
    window.after_cancel(flip_timer)
    french_choice = current_card["French"]
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=french_choice, fill="black")
    canvas.itemconfig(canvas_image, image=card_front)
    flip_timer = window.after(3000, change_card)


def change_card():
    global current_card
    english_choice = current_card["English"]
    canvas.itemconfig(card_title, text="English")
    canvas.itemconfig(card_word, text=english_choice)
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(card_title, fill="white")
    canvas.itemconfig(card_word, fill="white")


window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title("Flashy")
flip_timer = window.after(3000, change_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text="Language", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)


wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, bg=BACKGROUND_COLOR, command=next_card)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, bg=BACKGROUND_COLOR, command=is_known)
right_button.grid(row=1, column=1)


next_card()
window.mainloop()
