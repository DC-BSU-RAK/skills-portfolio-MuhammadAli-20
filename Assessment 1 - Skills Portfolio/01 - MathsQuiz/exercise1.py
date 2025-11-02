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

# ---------- FUNCTIONS ----------
def displayMenu():
    label = Label(root, text = "DIFFICULTY LEVEL MENU", fg = "black", font = ("Arial", 16, "bold"))
    label.pack(pady = 30)
    button = Button(root, text = "Easy (Single Digits)", command = lambda: randomInt("Easy"), fg = "green", font = ("Arial", 12, "bold"), bg = "#ADD8E6")
    button.pack(pady = 7)
    button = Button(root, text = "Moderate (Double Digits)", command = lambda: randomInt("Moderate"), fg = "yellow", font = ("Arial", 12, "bold"), bg = "#ADD8E6")
    button.pack(pady = 7)
    button = Button(root, text = "Advanced (Four Digits)", command = lambda: randomInt("Advanced"), fg = "red", font = ("Arial", 12, "bold"), bg = "#ADD8E6")
    button.pack(pady = 7)

def randomInt(level):
    if level == "Easy":
        print(random.randint(1, 9))
    elif level == "Moderate":
        print(random.randint(10, 90))
    else:
        print(random.randint(1000, 9999))

def decideOperation():
    random.choice(["+", "-"])



displayMenu()

root.mainloop()


                        