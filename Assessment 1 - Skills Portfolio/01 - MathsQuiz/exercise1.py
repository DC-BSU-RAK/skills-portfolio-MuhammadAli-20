# import tkinter as tk
# import random

# def generate_question():
#     global answer
#     num1 = random.randint(1, 10)
#     num2 = random.randint(1, 10)
#     operation = random.choice(["+", "-", "*"])

#     if operation == "+":
#         answer = num1 + num2
#     elif operation == "-":
#         answer = num1 - num2
#     else:
#         answer = num1 * num2
        
#     question_label.config(text = f"{num1} {operation} {num2} = ?")

# def check_answer():
#     user_answer = entry.get()
#     if user_answer.isdigit() and int(user_answer) == answer:
#         result_label.config(text = "Correct!", fg = "green")
#     else:
#         result_label.config(text =f"Wrong! Answer: {answer}", fg = "red")
#     entry.delete(0, tk.END)
#     generate_question()

# # Create the main window
# from tkinter import *
# from tkinter import messagebox 
# root = tk.Tk()
# root.title("Maths Quiz game")
# root.geometry("300x200")

# question_label = tk.Label(root, text="", font = ("Arial", 16))
# question_label.pack(pady = 10)

# entry = tk.Entry(root, font = ("Arial", 14))
# entry.pack()

# check_button = tk.Button(root, text = "Check Answer", command = check_answer)
# check_button.pack()

# result_label = tk.Label(root, text = "", font = ("Arial", 14))
# result_label.pack()

# generate_question()

# root.mainloop()

import tkinter as tk
from tkinter import *
from tkinter import messagebox
import random

# ---------- MAIN WINDOW ----------
root = Tk()
root.title("Maths Quiz Game")
root.geometry("600x350")

# ---------- GLOBAL VARIABLES ----------
difficulty = ""
score = 0
question_no = 0
num1 = num2 = 0
operation = ""
attempt = 1


# ---------- FUNCTIONS ----------
def displayMenu():
    """Show difficulty selection menu"""
    clear_window()
    label = Label(root, text="DIFFICULTY LEVEL MENU", fg="black", font=("Arial", 16, "bold"))
    label.pack(pady=30)

    # FIXED: buttons now call start_quiz() not randomInt()
    Button(root, text="Easy (Single Digits)", command=lambda: start_quiz("Easy"),
           fg="green", font=("Arial", 12, "bold"), bg="#ADD8E6").pack(pady=7)

    Button(root, text="Moderate (Double Digits)", command=lambda: start_quiz("Moderate"),
           fg="orange", font=("Arial", 12, "bold"), bg="#ADD8E6").pack(pady=7)

    Button(root, text="Advanced (Four Digits)", command=lambda: start_quiz("Advanced"),
           fg="red", font=("Arial", 12, "bold"), bg="#ADD8E6").pack(pady=7)


def randomInt(level):
    """Return two random integers based on difficulty"""
    if level == "Easy":
        return random.randint(1, 9), random.randint(1, 9)
    elif level == "Moderate":
        return random.randint(10, 99), random.randint(10, 99)
    else:
        return random.randint(1000, 9999), random.randint(1000, 9999)


def decideOperation():
    """Randomly decide addition or subtraction"""
    return random.choice(["+", "-"])


def displayProblem():
    """Display the next arithmetic problem"""
    global num1, num2, operation, attempt
    attempt = 1
    num1, num2 = randomInt(difficulty)  # FIXED: now randomInt returns values
    operation = decideOperation()

    # Avoid negative results
    if operation == "-" and num1 < num2:
        num1, num2 = num2, num1

    clear_window()
    tk.Label(root, text=f"Question {question_no + 1} of 10", font=("Arial", 14, "bold")).pack(pady=10)
    tk.Label(root, text=f"{num1} {operation} {num2} =", font=("Arial", 20)).pack(pady=10)
    tk.Label(root, text="Enter your answer:", font=("Arial", 12)).pack()

    global answer_entry
    answer_entry = tk.Entry(root, font=("Arial", 14), width=10, justify="center")
    answer_entry.pack(pady=10)

    tk.Button(root, text="Submit", command=checkAnswer).pack(pady=10)


def isCorrect(user_answer):
    """Check whether user's answer is correct"""
    if operation == "+":
        return user_answer == (num1 + num2)
    else:
        return user_answer == (num1 - num2)


def checkAnswer():
    """Handle answer checking and scoring"""
    global score, question_no, attempt

    try:
        user_answer = int(answer_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number!")
        return

    if isCorrect(user_answer):
        if attempt == 1:
            score += 10
            messagebox.showinfo("Correct!", "Great job! +10 points.")
        else:
            score += 5
            messagebox.showinfo("Correct!", "Correct on second try! +5 points.")
        nextQuestion()
    else:
        if attempt == 1:
            attempt += 1
            messagebox.showwarning("Try Again", "That's not right. Try once more!")
        else:
            messagebox.showerror("Wrong", "Incorrect again. Moving to next question.")
            nextQuestion()


def nextQuestion():
    """Move to next question or finish quiz"""
    global question_no
    question_no += 1
    if question_no < 10:
        displayProblem()
    else:
        displayResults()


def displayResults():
    """Show final score and grade"""
    clear_window()
    if score >= 90:
        grade = "A+"
    elif score >= 75:
        grade = "A"
    elif score >= 60:
        grade = "B"
    elif score >= 40:
        grade = "C"
    else:
        grade = "F"

    tk.Label(root, text="Quiz Completed!", font=("Arial", 18, "bold")).pack(pady=20)
    tk.Label(root, text=f"Your final score: {score}/100", font=("Arial", 14)).pack(pady=10)
    tk.Label(root, text=f"Your grade: {grade}", font=("Arial", 14, "bold")).pack(pady=10)

    tk.Button(root, text="Play Again", command=displayMenu).pack(pady=10)
    tk.Button(root, text="Exit", command=root.destroy).pack(pady=5)


def start_quiz(level):
    """Initialize quiz variables and start"""
    global difficulty, score, question_no
    difficulty = level
    score = 0
    question_no = 0
    displayProblem()


def clear_window():
    """Remove all widgets"""
    for widget in root.winfo_children():
        widget.destroy()


# ---------- MAIN PROGRAM ----------
displayMenu()
root.mainloop()



                        