from tkinter import *
from random import randint, choice
from tkinter import messagebox

# ---------- MAIN WINDOW ----------
root = Tk()
root.geometry("650x500")
root.title("Maths Quiz Game")

# ---------- VARIABLES ----------
question = StringVar()
answer = IntVar()
givenAnswer = StringVar()
score = IntVar()
questionNumber = IntVar()
difficulty = StringVar()
attempt = IntVar(value=1)

# ---------- FUNCTIONS ----------

def clear_window():
    for widget in root.winfo_children():
        widget.destroy()

def displayMenu():
    clear_window()
    Label(root, text="DIFFICULTY LEVEL MENU", font=('arial', 22, 'bold')).pack(pady=30)

    Button(root, text="Easy (Single Digits)", width=25, bg="#AEEEEE", fg="green",
           font=('arial', 14, 'bold'), command=lambda: start_quiz("Easy")).pack(pady=10)
    Button(root, text="Moderate (Double Digits)", width=25, bg="#AEEEEE", fg="orange",
           font=('arial', 14, 'bold'), command=lambda: start_quiz("Moderate")).pack(pady=10)
    Button(root, text="Advanced (Four Digits)", width=25, bg="#AEEEEE", fg="red",
           font=('arial', 14, 'bold'), command=lambda: start_quiz("Advanced")).pack(pady=10)


def randomInt(level):
    """Return numbers based on difficulty"""
    if level == "Easy":
        return randint(1, 9), randint(1, 9)
    elif level == "Moderate":
        return randint(10, 99), randint(10, 99)
    else:
        return randint(1000, 9999), randint(1000, 9999)


def decideOperation():
    """Return random + or -"""
    return choice(['+', '-'])


def start_quiz(level):
    """Initialize game and show first question"""
    difficulty.set(level)
    score.set(0)
    questionNumber.set(0)
    attempt.set(1)
    generateQuestion()


def generateQuestion():
    """Generate and display the question"""
    clear_window()
    questionNumber.set(questionNumber.get() + 1)
    attempt.set(1)

    # generate numbers based on difficulty
    num1, num2 = randomInt(difficulty.get())
    operator = decideOperation()

    # avoid negative results
    if operator == '-' and num1 < num2:
        num1, num2 = num2, num1

    question.set(f"{num1} {operator} {num2}")
    answer.set(eval(question.get()))

    Label(root, text=f"Question {questionNumber.get()} of 10", font=('arial', 16, 'bold')).grid(row=0, column=0, pady=10)
    Label(root, text=f"{question.get()} =", font=('arial', 24, 'bold')).grid(row=1, column=0, pady=10)

    Entry(root, textvariable=givenAnswer, font=('arial', 20), width=10, justify="center").grid(row=2, column=0, pady=10)

    Button(root, text="Submit", bg="lightblue", font=('arial', 14, 'bold'), command=checkAnswer).grid(row=3, column=0, pady=10)
    Label(root, text=f"Score: {score.get()} / 100", font=('arial', 14, 'bold'), fg="blue").grid(row=4, column=0, pady=5)
    Button(root, text="Quit", bg="grey", font=('arial', 12), command=displayMenu).grid(row=5, column=0, pady=10)


def checkAnswer():
    """Check user's answer and handle scoring"""
    try:
        user_ans = int(givenAnswer.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number!")
        return

    correct_ans = answer.get()

    # correct
    if user_ans == correct_ans:
        if attempt.get() == 1:
            score.set(score.get() + 10)
            messagebox.showinfo("Correct!", "✅ Great job! +10 points.")
        else:
            score.set(score.get() + 5)
            messagebox.showinfo("Correct!", "✅ Correct on second try! +5 points.")
        nextQuestion()

    # wrong on first try
    else:
        if attempt.get() == 1:
            attempt.set(2)
            messagebox.showwarning("Try Again", "❌ Wrong! Try one more time.")
            givenAnswer.set("")  # clear entry
        else:
            messagebox.showerror("Incorrect", f"Wrong again! Correct answer was {correct_ans}.")
            nextQuestion()


def nextQuestion():
    """Move to next question or show final results"""
    if questionNumber.get() < 10:
        generateQuestion()
    else:
        displayResults()


def displayResults():
    """Show final score and grade"""
    clear_window()
    Label(root, text="🎉 QUIZ COMPLETED 🎉", font=('arial', 24, 'bold'), fg="green").pack(pady=30)
    Label(root, text=f"Your Final Score: {score.get()} / 100", font=('arial', 18)).pack(pady=10)

    grade = ""
    if score.get() >= 90:
        grade = "A+"
    elif score.get() >= 75:
        grade = "A"
    elif score.get() >= 60:
        grade = "B"
    elif score.get() >= 40:
        grade = "C"
    else:
        grade = "F"

    Label(root, text=f"Grade: {grade}", font=('arial', 18, 'bold'), fg="blue").pack(pady=10)
    Button(root, text="Play Again", bg="#AEEEEE", font=('arial', 14, 'bold'), command=displayMenu).pack(pady=10)
    Button(root, text="Exit", bg="grey", font=('arial', 14), command=root.destroy).pack(pady=5)


# ---------- START PROGRAM ----------
displayMenu()
root.mainloop()
