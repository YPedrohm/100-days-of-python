class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} True/False: ")
        self.check_awnser(user_answer, current_question.answer)

    def check_awnser(self, user_awnser ,correct_awnser):
        if user_awnser.lower() == correct_awnser.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong!")
        print(f"Correct answer: {correct_awnser}")
        print(f"Your current score is: {self.score}/{self.question_number}\n")





