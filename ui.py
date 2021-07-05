from tkinter import *

THEME_COLOR = "#375362"
QUESTION_FONT = ("Arial", 20, "italic")

class QuizInterface:
  def __init__(self):
    self.window = Tk()
    self.window.title("Quizzler")
    self.window.config(bg=THEME_COLOR)

    self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="#fff")
    self.score_label.grid(column=1, row=0, pady=20)

    self.question_window = Canvas(width=300, height=250, highlightthickness=0)
    self.question_window.grid(column=0, row=1, columnspan=2, padx=20, pady=20)

    self.question_text = self.question_window.create_text(150, 125, font=QUESTION_FONT, text="Test", fill=THEME_COLOR)

    true_image = PhotoImage(file="images/true.png")
    false_image = PhotoImage(file="images/false.png")
    self.true_button = Button(image=true_image, highlightthickness=0)
    self.true_button.grid(column=0, row=2, pady=20)
    self.false_button = Button(image=false_image, highlightthickness=0)
    self.false_button.grid(column=1, row=2, pady=20)

    self.window.mainloop()