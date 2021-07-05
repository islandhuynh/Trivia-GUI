from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
QUESTION_FONT = ("Arial", 20, "italic")

class QuizInterface:
  def __init__(self, quiz_brain: QuizBrain):
    self.quiz = quiz_brain

    self.window = Tk()
    self.window.title("Quizzler")
    self.window.config(bg=THEME_COLOR)

    self.score_label = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="#fff")
    self.score_label.grid(column=1, row=0, pady=20)

    self.question_window = Canvas(width=300, height=250, highlightthickness=0)
    self.question_window.grid(column=0, row=1, columnspan=2, padx=20, pady=20)

    self.question_text = self.question_window.create_text(150, 125, font=QUESTION_FONT, text="", fill=THEME_COLOR, width=280)

    true_image = PhotoImage(file="images/true.png")
    false_image = PhotoImage(file="images/false.png")
    self.true_button = Button(image=true_image, highlightthickness=0, command=self.answer_true)
    self.true_button.grid(column=0, row=2, pady=20)
    self.false_button = Button(image=false_image, highlightthickness=0, command=self.answer_false)
    self.false_button.grid(column=1, row=2, pady=20)

    self.get_next_question()

    self.window.mainloop()

  def get_next_question(self):
    q_text = self.quiz.next_question()
    self.question_window.itemconfig(self.question_text, text=q_text)

  def answer_true(self):
    self.quiz.check_answer("True")
    self.score_label.config(text=f"Score: {self.quiz.score}")
    self.get_next_question()

  def answer_false(self):
    self.quiz.check_answer("False")
    self.score_label.config(text=f"Score: {self.quiz.score}")
    self.get_next_question()
