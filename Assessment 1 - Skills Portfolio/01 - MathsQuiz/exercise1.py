from tkinter import *
from tkinter import messagebox
from random import randint, choice
import pygame

# ---------- MAIN WINDOW ----------
root = Tk()
root.geometry("600x350")
root.title("Maths Quiz Game")
pygame.mixer.init()

# ---------- GLOBAL VARIABLES ----------
difficulty = StringVar()
question = StringVar()
answer = IntVar()
givenAnswer = StringVar()
score = IntVar(value = 0)
current_question = 0
attempts = 1

# ---------- FUNCTIONS ----------
def play_correct_sound():
        pygame.mixer.music.load("correct.mp3")       
        pygame.mixer.music.play()

def play_wrong_sound():
        pygame.mixer.music.load("negative_beeps.mp3")    
        pygame.mixer.music.play()

def play_fail_sound():
        pygame.mixer.music.load("fail_trumpet.mp3")    
        pygame.mixer.music.play()

def play_cheer_sound():
        pygame.mixer.music.load("crowd_cheer.mp3")    
        pygame.mixer.music.play()
        root.after(6000, pygame.mixer.music.stop)

def clear_window():
    for widget in root.winfo_children():
        widget.destroy()

def displayMenu():
    global current_question, score
    clear_window()
    score.set(0)
    question.set("")
    givenAnswer.set("")
    current_question = 0
    label = Label(root, text="DIFFICULTY LEVEL MENU", fg="black", font=("Arial", 16, "bold"))
    label.pack(pady=30)
    button = Button(root, text="Easy (Single Digits)", command = lambda: begin_quiz("Easy"), fg="green", font=("Arial", 12, "bold"), bg="#ADD8E6")
    button.pack(pady=7)
    button = Button(root, text="Moderate (Double Digits)", command = lambda: begin_quiz("Moderate"), fg="yellow", font=("Arial", 12, "bold"), bg="#ADD8E6")
    button.pack(pady=7)
    button = Button(root, text="Advanced (Four Digits)", command = lambda: begin_quiz("Advanced"), fg="red", font=("Arial", 12, "bold"), bg="#ADD8E6")
    button.pack(pady=7)

def randomInt(level):
    if level == "Easy":
        return randint(1, 9), randint(1, 9)
    elif level == "Moderate":
        return randint(10, 99), randint(10, 99)
    else:
        return randint(1000, 9999), randint(1000, 9999)

def decideOperation():
    return choice(["+", "-"])

def begin_quiz(level):
    global difficulty, current_question, score
    difficulty.set(level)
    score.set(0)
    current_question = 0
    show_question()

def show_question():
    global num1, num2, operation, answer, attempts
    clear_window()
    attempts = 1

    num1, num2 = randomInt(difficulty.get())
    operation = decideOperation()

    question.set(f"{num1} {operation} {num2}")
    answer.set(eval(question.get()))

    label = Label(root, text=f"Question {current_question + 1} of 10", font=("Arial", 18, "bold"))
    label.pack(pady=10)
    label = Label(root, text=f"{question.get()} =", font=("Arial", 20, "bold"))
    label.pack(pady=10)
    entry1 = Entry(root, textvariable=givenAnswer, font=("Arial", 18), width=10, justify="center")
    entry1.pack(pady=10)
    button1 = Button(root, text="Reset", command=lambda: entry1.delete(0, "end"), font=("Arial", 14, "bold"), bg="lightblue")
    button1.pack(pady=10)
    button2 = Button(root, text="Submit", font=("Arial", 14, "bold"), command=checkAnswer, bg="lightblue")
    button2.pack(pady=10)
    label = Label(root, text=f"Score: {score.get()} / 100", font=("Arial", 14, "bold"), fg="green")
    label.pack(pady=10)

def checkAnswer():
    global attempts

    correct_answer = answer.get()
    attempts_allowed = 2
    current_try = attempts

    while current_try <= attempts_allowed:
        try:
            user_answer = int(givenAnswer.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number!")
            return

        if user_answer == correct_answer:
            play_correct_sound()
            if current_try == 1:
                messagebox.showinfo("Correct!", "Great job! +10 points.")
                score.set(score.get() + 10)
            else:
                messagebox.showinfo("Correct!", "Great job! +5 points.")
                score.set(score.get() + 5)
            nextQuestion()
            break

        else:
            if current_try == 1:
                play_wrong_sound()
                messagebox.showwarning("Try Again", "Wrong! Try once more.")
                givenAnswer.set("")
                attempts = 2
                return
            else:
                play_wrong_sound()
                messagebox.showerror("Incorrect", f"Wrong again! The correct answer was {correct_answer}.")
                nextQuestion()
                break

def nextQuestion():
    global current_question
    current_question += 1

    if current_question < 10:
        show_question()
    else:
        messagebox.showinfo("Quiz Completed", f"You’ve completed all {current_question} questions!")
        displayResults()

def displayResults():

    grade = ""
    if score.get() >= 90:
        play_cheer_sound()
        grade = "A+"
    elif score.get() >= 75:
        play_cheer_sound()
        grade = "A"
    elif score.get() >= 60:
        grade = "B"
    elif score.get() >= 40:
        grade = "C"
    else:
        play_fail_sound()
        grade = "F"
    
    clear_window()
    label = Label(root, text="🎉 QUIZ COMPLETED 🎉", font=("Arial", 24, "bold"), fg="green")
    label.pack(pady=30)
    label = Label(root, text=f"Your Final Score: {score.get()} / 100", font=("Arial", 18))
    label.pack(pady=10)
    label = Label(root, text=f"Grade: {grade}", font=("Arial", 18, "bold"), fg="blue")
    label.pack(pady=10)
    button = Button(root, text="Restart", fg="red", bg="#FFE4E1", font=('Arial', 15), width=15, command=restart)
    button.pack(pady=10)
    button = Button(root, text="Exit", bg="grey", font=("Arial", 14), command = root.destroy)
    button.pack(pady=5)

def restart():
    global current_question, score
    score.set(0)
    current_question = 0
    givenAnswer.set("")
    question.set("")
    displayMenu()  

# ---------- START PROGRAM ----------
displayMenu()
root.mainloop()


