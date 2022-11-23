class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        print(f'Answer is {current_question.answer}')
        self.question_number += 1
        user_input = input(f'Q{self.question_number}: {current_question.text} (True/False): ').title()
        if user_input == current_question.answer:
            self.score += 1
            print('You got it.')
            print(f'The right answer is {current_question.answer}')
            print(f'Your score is {self.score}/{self.question_number}')
        else:
            print('Wrong.')
            print(f'The right answer is {current_question.answer}')
            print(f'Your score is {self.score}/{self.question_number}')

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
