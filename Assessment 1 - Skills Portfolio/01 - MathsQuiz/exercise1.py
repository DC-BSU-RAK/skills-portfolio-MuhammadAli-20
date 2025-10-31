import tkinter as tk
import random

def generate_question():
    global answer
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operation = random.choice(["+", "-", "*"])

    if operation == "+":
        answer = num1 + num2
    elif operation == "-":
        answer = num1 - num2
    else:
        answer = num1 * num2
        
    question_label.config(text = f"{num1} {operation} {num2} = ?")

def check_answer():
    user_answer = entry.get()
    if user_answer.isdigit() and int(user_answer) == answer:
        result_label.config(text = "Correct!", fg = "green")
    else:
        result_label.config(text =f"Wrong! Answer: {answer}", fg = "red")
    entry.delete(0, tk.END)
    generate_question()

# Create the main window

root = tk.Tk()
root.title("Maths Quiz game")
root.geometry("300x200")

question_label = tk.Label(root, text="", font = ("Arial", 16))
question_label.pack(pady = 10)

entry = tk.Entry(root, font = ("Arial", 14))
entry.pack()

check_button = tk.Button(root, text = "Check Answer", command = check_answer)
check_button.pack()

result_label = tk.Label(root, text = "", font = ("Arial", 14))
result_label.pack()

generate_question()

root.mainloop()
                        