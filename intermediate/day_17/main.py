from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import random

# loop control flag
can_continue = True
score = 0

question_bank = []
for i in range(len(question_data)):
    question_bank.append(Question(question_data[i]['text'], question_data[i]['answer']))

# TODO: create quiz object
quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    # TODO: call quiz function to start questioning
    quiz_brain.next_question()

# TODO: track scores and display final score at end of quiz
print(f"\nFinal Score: {quiz_brain.score}/{quiz_brain.question_number}")

