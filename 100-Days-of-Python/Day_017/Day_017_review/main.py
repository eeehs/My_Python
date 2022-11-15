from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
question_bank = []

for i in question_data:
    a = Question(i["question"], i["correct_answer"])
    question_bank.append(a)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")