from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for ques in question_data:
    question = Question(ques["question"], ques["correct_answer"])
    question_bank.append(question)

print(question_bank)

quizbrain = QuizBrain(question_bank)
while quizbrain.still_has_question():
    quizbrain.next_question()
print("\nYou've completed the quiz.")
print(f"Your final score was: {quizbrain.score}/{quizbrain.question_number}.")
