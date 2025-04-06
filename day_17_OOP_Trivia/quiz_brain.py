import html

class QuizBrain:
    
    def __init__(self, question_bank: list) -> None:
        self.q_number = 0
        self.q_list = question_bank
        self.score = 0
    
    def next_question(self) -> None:
        question = self.q_list[self.q_number]
        self.q_number += 1
        q_text = html.unescape(question.text)
        user_answer = input(f"Q.{self.q_number}: {q_text} (True/False)? ")
        self.check_answer(user_answer, question.answer)
        
    def still_has_questions(self) -> bool:
        return self.q_number < len(self.q_list)
    
    def check_answer(self, user_answer: str, correct_answer:str) -> bool:
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correcy answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.q_number}")