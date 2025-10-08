from question_model import Question
from data import question_data

question_bank = []
print(len(question_data))
for text, answer in range(len(question_data)):
    question_bank.append(Question(text, answer))

