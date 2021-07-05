from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizInterface
import requests

response = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")
question_data  = response.json()["results"]

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)