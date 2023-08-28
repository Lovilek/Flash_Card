BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
import random

random_word_func = {}


def wrong_click():
    global random_word_func, timer
    window.after_cancel(timer)
    random_word_func = random.choice(dictionary)
    canvas.itemconfig(translate, text="English", fill="black")
    canvas.itemconfig(word, text=random_word_func["English"], fill="black")
    canvas.itemconfig(card_img, image=card_front)
    timer = window.after(3000, func=flip)


def right_click():
    dictionary.remove(random_word_func)
    wrong_click()
    df_csv = pandas.DataFrame(dictionary)
    df_csv.to_csv("data/words_to_learn.csv", index=False)


def flip():
    canvas.itemconfig(card_img, image=card_back)
    canvas.itemconfig(translate, text="Russian", fill="white")
    canvas.itemconfig(word, text=random_word_func["Russian"], fill="white")


try:
    data = pandas.read_csv("data/words_to_learn.csv")
    df = pandas.DataFrame(data)
    dictionary = df.to_dict(orient="records")
except FileNotFoundError:
    data = pandas.read_csv("data/words.csv")
    df = pandas.DataFrame(data)
    dictionary = df.to_dict(orient="records")

window = Tk()
window.title("Flash Cards")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)
timer = window.after(3000, func=flip)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_img = canvas.create_image(400, 263, image=card_front)
translate = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)
wrong_click()

right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=right_click)
right_button.grid(column=0, row=1)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=wrong_click)
wrong_button.grid(column=1, row=1)

window.mainloop()
