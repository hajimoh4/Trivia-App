from tkinter import *
from turtle import bgcolor

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quizbrain: QuizBrain):
        self.quiz = quizbrain
        self.window = Tk()
        self.window.title("Quizzlo")
        self.window.config(padx=30, pady=30, bg=THEME_COLOR)

        
        self.score_label = Label(text = f"Score : {self.quiz.score} / {len(self.quiz.question_list)}", fg = "white", bg=THEME_COLOR, font=("Arial", 15, "bold"))
        self.score_label.grid(row = 0, column=1)
        

        self.canvas = Canvas(width=300, height=300, bg="white")
        self.question_text = self.canvas.create_text(150, 150, width=200,
        text= "....", 
        font= ("Arial", 15, "italic"),
        fill=THEME_COLOR)
        self.canvas.grid(row = 1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        fale_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=fale_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        

        self.get_next_question()




        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text = q_text)
        else:
             self.false_button.config(state="disabled")
             self.true_button.config(state="disabled")
            
             self.canvas.itemconfig(self.question_text, text=f"You Scored a {self.quiz.score} / {len(self.quiz.question_list)}!")
             
            
         

        

    

    
    def true_pressed(self):
        
        self.give_feedback(self.quiz.check_answer("True"))

    

    def false_pressed(self):
    
        self.give_feedback(self.quiz.check_answer("False"))

    
    def give_feedback(self, is_right):


        if is_right:
            self.canvas.config(bg="green")

        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
        self.score_label.config(text=f"Score: {self.quiz.score}")


    
        





