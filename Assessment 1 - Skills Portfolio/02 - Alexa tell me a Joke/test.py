# from tkinter import *
# from random import randint,choice

# root = Tk()
# root.geometry("600x500")
# root.title("Maths Quiz")

# question = StringVar()
# answer = StringVar()
# givenAnswer = StringVar()
# score = IntVar()
# questionNumber = IntVar()

# def generateQuestion():

#     global questionLabel

#     questionNumber.set(questionNumber.get() + 1)

#     number1 = randint(1 , 10)
#     number2 = randint(1 , 10)

#     operator = choice(['+' , '-' , '*' , '/'])

#     question.set(str(number1) + operator + str(number2))
#     answer.set(eval(question.get()))

#     if questionLabel:
#         questionLabel.destroy()

#     questionLabel = Label(root , text=f"Question : {question.get()}" , font=('arial' , 20))
#     questionLabel.grid(row=2 , column=0)

# def checkAnswer():

#     global scoreLabel

#     if questionNumber.get() > 10 :
#         return

#     global resultLabel

#     if resultLabel:
#         resultLabel.destroy()

#     if str(answer.get()) == givenAnswer.get():
#         score.set(score.get() + 1)
#         resultLabel = Label(root , text="Correct" , font=('arial' , 20), fg="green")
#         resultLabel.grid(row=4 , column=0)
#         scoreLabel = Label(root , text=f"Score : {score.get()}" , font=('arial' , 20) , fg="black")
#         scoreLabel.grid(row=5 , column=0)

#     else:
#         resultLabel = Label(root , text="Incorrect" , font=('arial' , 20) , fg="red")
#         resultLabel.grid(row=4 , column=0)


#     if questionNumber.get() == 10:
#         scoreLabel.destroy()
#         scoreLabel = Label(root , text=f"Final Score : {score.get()}" , font=('arial' , 20) , fg="black")
#         scoreLabel.grid(row=5 , column=0)
    
#     else:
#         generateQuestion()
        
# def restart():

#     global scoreLabel
#     scoreLabel.destroy()

#     score.set(0)
#     questionNumber.set(0)
#     generateQuestion()

#     scoreLabel = Label(root , text=f"Score : {score.get()}" , font=('arial' , 20) , fg="black")
#     scoreLabel.grid(row=5 , column=0)
# # User Interface



# headingLabel = Label(root , text="Maths Quiz" , font=('arial' , 25) )
# headingLabel.grid(row=0 , column=0)

# questionScale = Scale(root , from_=0 , to=10 , orient=HORIZONTAL , length=400, variable=questionNumber)
# questionScale.grid(row=1 , column=0)

# completeQuestionLabel = Label(root , text="10th question")
# completeQuestionLabel.grid(row=1 , column=1)

# questionLabel = Label(root , text=question.get() , font=('arial' , 20))
# questionLabel.grid(row=2 , column=0)

# answerEntry = Entry(root , textvariable=givenAnswer ,  font=('arial' , 20), width=25)
# answerEntry.grid(row=3 , column=0)

# submitButton = Button(root , text="Submit" , fg="yellow", bg="grey", font=('arial' , 15) , command=checkAnswer)
# submitButton.grid(row=3 , column=1)

# resultLabel = Label(root , text="Result" , font=('arial' , 20) , fg="blue")
# resultLabel.grid(row=4 , column=0)

# scoreLabel = Label(root , text=f"Score : {score.get()}" , font=('arial' , 20) , fg="black")
# scoreLabel.grid(row=5 , column=0)

# submitButton = Button(root , text="Restart" , fg="red", font=('arial' , 15), width=35 , command=restart)
# submitButton.grid(row=6 , column=0)

# generateQuestion()

# root.mainloop()

import tkinter as tk
import random
import os

# --------- LOAD JOKES FROM FILE ---------
def load_jokes(filename="randomJokes.txt"):
    jokes_list = []

    if not os.path.exists(filename):
        # Fallback joke if file not found
        jokes_list.append((
            "randomJokes.txt not found. Did you put it in the same folder as this .py file?",
            "Create the file and add jokes like: Why did the chicken cross the road?To get to the other side."
        ))
        return jokes_list

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if "?" in line:
                setup, punchline = line.split("?", 1)
                setup = setup.strip() + "?"
                punchline = punchline.strip()
                jokes_list.append((setup, punchline))

    if not jokes_list:
        jokes_list.append((
            "No valid jokes found in randomJokes.txt.",
            "Each line must have a question mark separating setup and punchline."
        ))

    return jokes_list

# --------- CALLBACK FUNCTIONS ---------
def get_random_joke():
    """Pick a random joke and show only the setup."""
    global current_setup, current_punchline

    current_setup, current_punchline = random.choice(jokes)
    setup_label.config(text=current_setup)
    punchline_label.config(text="")  # hide punchline

def show_punchline():
    """Show the punchline."""
    punchline_label.config(text=current_punchline)

def next_joke():
    """Next joke is same as getting a random one again."""
    get_random_joke()

def quit_app():
    root.destroy()

# --------- MAIN WINDOW SETUP ---------
root = tk.Tk()
root.title("Alexa Joke Assistant")
root.geometry("550x300")
root.config(bg="#e6f2ff")

# Load jokes once
jokes = load_jokes()
current_setup = ""
current_punchline = ""

# Title
title_label = tk.Label(
    root,
    text="Alexa Joke Assistant",
    font=("Arial", 18, "bold"),
    bg="#e6f2ff"
)
title_label.pack(pady=10)

# Setup label
setup_label = tk.Label(
    root,
    text="Click the button to hear a joke!",
    font=("Arial", 14),
    wraplength=500,
    bg="#e6f2ff"
)
setup_label.pack(pady=10)

# Punchline label
punchline_label = tk.Label(
    root,
    text="",
    font=("Arial", 14, "italic"),
    fg="blue",
    wraplength=500,
    bg="#e6f2ff"
)
punchline_label.pack(pady=10)

# Buttons frame
button_frame = tk.Frame(root, bg="#e6f2ff")
button_frame.pack(pady=15)

btn_tell_joke = tk.Button(
    button_frame,
    text="Alexa tell me a Joke",
    font=("Arial", 12),
    bg="#99ccff",
    command=get_random_joke
)
btn_show_punchline = tk.Button(
    button_frame,
    text="Show Punchline",
    font=("Arial", 12),
    bg="#b3ffb3",
    command=show_punchline
)
btn_next = tk.Button(
    button_frame,
    text="Next Joke",
    font=("Arial", 12),
    bg="#ffff99",
    command=next_joke
)
btn_quit = tk.Button(
    button_frame,
    text="Quit",
    font=("Arial", 12),
    bg="#ff6666",
    command=quit_app
)

btn_tell_joke.grid(row=0, column=0, padx=10, pady=5)
btn_show_punchline.grid(row=0, column=1, padx=10, pady=5)
btn_next.grid(row=1, column=0, padx=10, pady=5)
btn_quit.grid(row=1, column=1, padx=10, pady=5)

root.mainloop()
