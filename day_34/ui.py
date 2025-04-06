import tkinter as tk

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")

class QuizInterface():
    
    def __init__(self, quiz_brain):
        self.quiz = quiz_brain
        
        self.window = tk.Tk()
        self.window.title("TriviaQuiz")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.score_label = tk.Label(text="", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        
        self.canvas = tk.Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="", font=FONT, fill=THEME_COLOR, width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        
        true_img = tk.PhotoImage(file="images/true.png")
        self.true_button = tk.Button(image=true_img,highlightthickness=0, bd=0, activebackground=THEME_COLOR, command=self.check_true)
        self.true_button.grid(row=2, column=0)
        false_img = tk.PhotoImage(file="images/false.png")
        self.false_button = tk.Button(image=false_img, highlightthickness=0, bd=0, activebackground=THEME_COLOR, command=self.check_false)
        self.false_button.grid(row=2, column=1)
        
        self.get_next_question()
        
        self.window.mainloop()
        
    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="End of quiz")
            self.canvas.update()
            self.window.after(2000, self.window.quit())
        
    def check_true(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)
        
    def check_false(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)
        
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="#00fa08")
        else:
            self.canvas.config(bg="#fa0000")
        self.canvas.update()
        self.window.after(500, self.get_next_question())