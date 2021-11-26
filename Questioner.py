import tkinter as tk
from tkinter import messagebox
from random import randint

def Start_questions():

    global window1
    
    window1 = tk.Tk()
    window1.title("Multiplication Questiner")

    multiplicant_dl = tk.Label(window1, text = "Number of Digits in the Mutiplicant:", pady = 5, padx = 5)
    multiplier_dl = tk.Label(window1, text = "Number of Digits in the Mutiplier:", pady = 5, padx = 5)
    multiplicant_d = tk.Entry(window1)
    multiplier_d = tk.Entry(window1)
    send = tk.Button(window1, text="Send INFO", command = lambda:Materials(multiplicant_d, multiplier_d), pady = 5, padx = 5)
                          
    multiplicant_dl.grid(column=0, row=0)
    multiplier_dl.grid(column=0, row=1)
    multiplicant_d.grid(column=1, row=0)
    multiplier_d.grid(column=1, row=1)
    send.grid(column=0, row=2, columnspan = 2)
                          
    window1.mainloop()

    return
    

def Materials(multiplicant_d, multiplier_d):

    multiplicants, multipliers, questions, answers, n_questions, user_answers, user_answer1, user_answer2 = list(), list(), list(), list(), list(), list(), list(), list()
    index = int()
    
    try:
        while not index > 10:
            
            multiplicant = randint(int("1" + ("0"*(int(multiplicant_d.get())-1))), int("1" + ("0"*int(multiplicant_d.get()))))
            multiplier = randint(int("1" + ("0"*(int(multiplicant_d.get())-1))), int("1" + ("0"*int(multiplier_d.get()))))
            
            if not multiplicant in multiplicants and multiplier in multipliers:
                multiplicants.append(multiplicant)
                multipliers.append(multiplier)
                index += 1
                    
    except TypeError:
        tk.messagebox.showerror(title = "Multiplication Questiner",\
                                     message="ERORR:You should always Enter a number")    
        return
    
    else:
        window1.destroy()

    window2 = tk.Tk()
    window2.title("Multiplication Questiner")

    for multiplicant in multiplicants:
        for multiplier in multipliers:
            
            questions.append("{0} X {1} = ____".format(multiplicant, multiplier))
            answers.append((multiplicant * multiplier))

    for question, row in zip(questions, range(10)):
        
        n_questions.append(tk.Label(window2, text = question, pady = 5, padx = 5))
        user_answers.append(tk.Entry(window2))

    user_answers = Questioner(n_questions, answers, user_answers, window2)

    user_answer1 = user_answers[:int("-" + str((len(user_answer)-1)/2))]
    user_answer2 = user_answers[((len(user_answer)-1)/2):]
    
    Answer(user_answers, answers, questions, "disabled", "enabled")
    
    return n_questions
             
def Questioner(questions, answers, user_answers, window2):
    
    start = tk.Label(window2, text = "Answer The questions Given below").\
            grid(column=0, row = 0, columnspan = 2)
    send = tk.Button(window2, text = "Post Answers", command = window2.destroy)
    n_user_answers = list()

    for row in range(10):

        questions[row].grid(row = row, column = 0)
        user_answers[row].grid(row = row, column = 1)
    
    send.grid(column = 0, row = (row+1), columnspan = 2)

    for user_answer in user_answers:

        n_user_answers.append(user_answer.get())

    window2.mainloop()

    return n_user_answers


def Answer(user_answers1, user_answer2, answers, questions, state1, state2):
    
    window = tk.Tk()
    window.title("Multiplication Questiner")

    stats, n_questions, split = list(), list(), list()
    score = int()
    
    for index in range(6):
        split.append(tk.Label(window, text="", pady = 10, padx = 5))

    for question, row in zip(questions, range(10)):
        
        n_questions.append(tk.Label(window, text = question, pady = 5, padx = 5))

    for user_answer in user_answers1:
        for answer in answers:
            
            if answer == user_answer:
                stats.append(tk.Label(window, text = "Yaa! Your answer was right", padx = 5))
                stats.append(tk.Label(window, text = "Correct Answer - {0}".format(answer), padx = 5))
                stats.append(tk.Label(window, text = "Your Answer - {0}".format(user_answer), padx = 5))
                score+=1
            else:
                stats.append(tk.Label(window, text = "Oh! Ohh... Your answer was wrong", padx = 5))
                stats.append(tk.Label(window, text = "Correct Answer - {0}".format(answer), padx = 5))
                stats.append(tk.Label(window, text = "Your Answer - {0}".format(user_answer), padx = 5))
                
    for row, index in zip(range(0, 25, 5), range(5)):

        n_questions[index].grid(row = row, column = 0, columnspan = 3)
        stats[row].grid(row = row+1, column = 0, columnspan = 3)
        stats[row + 1].grid(row = row+2, column = 0, columnspan = 3)
        stats[row + 2].grid(row = row+3, column = 0, columnspan = 3)
        split[index].grid(row = row+4, column = 0, columnspan = 3)

    m_prev = tk.Button(window, text = "<<Prev", command = show(window, Answer, user_answers2, user_answer2, answers, questions, "disabled", "enabled"), state = state1)
    m_next = tk.Button(window, text = "Next>>", command = show(window, Answer, user_answers2, user_answer2, answers, questions, "enabled", "disabled"), state = state2)
    show_score = tk.Button(window, text = "Show Score", command = show(score))

    window.mainloop()

    return


def show(window, func, *args):

    window.destroy()

    return func(args)


def Show_Score(score):

    score_label = tk.Label(window, text = "Your Score = " + str(score)).grid(row = 0, column = 0)

    bye = tk.Button(window, text="Bye Have a Good Day!!", command = window.destroy, pady = 5, padx = 5).grid(row = 1, column = 0)

    return


if __name__ == '__main__':
    Start_questions()
