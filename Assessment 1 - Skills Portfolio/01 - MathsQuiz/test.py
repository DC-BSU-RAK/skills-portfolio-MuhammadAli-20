import tkinter as tk
from tkinter import messagebox
import random

# ---------- FUNCTIONS ----------

def displayMenu():
    """Display difficulty selection menu"""
    clear_window()
    tk.Label(root, text="DIFFICULTY LEVEL", font=("Arial", 18, "bold")).pack(pady=20)
    tk.Button(root, text="1. Easy (Single Digits)", width=25, command=lambda: start_quiz("easy")).pack(pady=5)
    tk.Button(root, text="2. Moderate (Double Digits)", width=25, command=lambda: start_quiz("moderate")).pack(pady=5)
    tk.Button(root, text="3. Advanced (Four Digits)", width=25, command=lambda: start_quiz("advanced")).pack(pady=5)


def randomInt(level):
    """Return two random integers based on difficulty level"""
    if level == "easy":
        return random.randint(1, 9), random.randint(1, 9)
    elif level == "moderate":
        return random.randint(10, 99), random.randint(10, 99)
    else:
        return random.randint(1000, 9999), random.randint(1000, 9999)


def decideOperation():
    """Randomly decide addition or subtraction"""
    return random.choice(["+", "-"])


def displayProblem():
    """Display the next arithmetic problem"""
    global num1, num2, operation, attempt
    attempt = 1  # reset attempt count
    num1, num2 = randomInt(difficulty)
    operation = decideOperation()

    # Make sure subtraction is not negative
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
    """Check if user's answer is correct"""
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
    """Show final score and rank"""
    clear_window()
    grade = ""
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
    """Clear all widgets from window"""
    for widget in root.winfo_children():
        widget.destroy()


# ---------- MAIN PROGRAM ----------

root = tk.Tk()
root.title("Maths Quiz")
root.geometry("400x400")
root.resizable(False, False)

displayMenu()

root.mainloop()
