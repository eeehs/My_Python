from data import question_data
from question_model import Question

question_bank = []

for i in question_data:
    a = Question(i["question"], i["correct_answer"])
    question_bank.append(a)

print(question_bank[0].answer)