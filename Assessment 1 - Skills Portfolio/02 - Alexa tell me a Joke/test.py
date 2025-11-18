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

# import tkinter as tk
# import random
# import os

# def load_jokes(filename="randomJokes.txt"):
#     jokes_list = []

#     if not os.path.exists(filename):
#         jokes_list.append((
#             "randomJokes.txt not found. Did you put it in the same folder as this .py file?",
#             "Create the file and add jokes like: Why did the chicken cross the road?To get to the other side."
#         ))
#         return jokes_list

#     with open(filename, "r", encoding="utf-8") as f:
#         for line in f:
#             line = line.strip()
#             if not line:
#                 continue
#             if "?" in line:
#                 setup, punchline = line.split("?", 1)
#                 setup = setup.strip() + "?"
#                 punchline = punchline.strip()
#                 jokes_list.append((setup, punchline))

#     if not jokes_list:
#         jokes_list.append((
#             "No valid jokes found in randomJokes.txt.",
#             "Each line must have a question mark separating setup and punchline."
#         ))

#     return jokes_list

# def get_random_joke():
#     """Pick a random joke and show only the setup."""
#     global current_setup, current_punchline

#     current_setup, current_punchline = random.choice(jokes)
#     setup_label.config(text=current_setup)
#     punchline_label.config(text="")  

# def show_punchline():
#     """Show the punchline."""
#     punchline_label.config(text=current_punchline)

# def next_joke():
#     """Next joke is same as getting a random one again."""
#     get_random_joke()

# def quit_app():
#     root.destroy()

# root = tk.Tk()
# root.title("Alexa Joke Assistant")
# root.geometry("550x300")
# root.config(bg="#e6f2ff")

# jokes = load_jokes()
# current_setup = ""
# current_punchline = ""

# title_label = tk.Label(
#     root,
#     text="Alexa Joke Assistant",
#     font=("Arial", 18, "bold"),
#     bg="#e6f2ff"
# )
# title_label.pack(pady=10)

# setup_label = tk.Label(
#     root,
#     text="Click the button to hear a joke!",
#     font=("Arial", 14),
#     wraplength=500,
#     bg="#e6f2ff"
# )
# setup_label.pack(pady=10)

# punchline_label = tk.Label(
#     root,
#     text="",
#     font=("Arial", 14, "italic"),
#     fg="blue",
#     wraplength=500,
#     bg="#e6f2ff"
# )
# punchline_label.pack(pady=10)

# button_frame = tk.Frame(root, bg="#e6f2ff")
# button_frame.pack(pady=15)

# btn_tell_joke = tk.Button(
#     button_frame,
#     text="Alexa tell me a Joke",
#     font=("Arial", 12),
#     bg="#99ccff",
#     command=get_random_joke
# )
# btn_show_punchline = tk.Button(
#     button_frame,
#     text="Show Punchline",
#     font=("Arial", 12),
#     bg="#b3ffb3",
#     command=show_punchline
# )
# btn_next = tk.Button(
#     button_frame,
#     text="Next Joke",
#     font=("Arial", 12),
#     bg="#ffff99",
#     command=next_joke
# )
# btn_quit = tk.Button(
#     button_frame,
#     text="Quit",
#     font=("Arial", 12),
#     bg="#ff6666",
#     command=quit_app
# )

# btn_tell_joke.grid(row=0, column=0, padx=10, pady=5)
# btn_show_punchline.grid(row=0, column=1, padx=10, pady=5)
# btn_next.grid(row=1, column=0, padx=10, pady=5)
# btn_quit.grid(row=1, column=1, padx=10, pady=5)

# root.mainloop()

# from tkinter import *
# import random

# root = Tk()
# root.geometry("600x350")
# root.title("Random Joke Game")

# ---------------- LABELS ----------------
# setup_label = Label(root, text="", font=("Arial", 14), wraplength=500)
# setup_label.place(x=50, y=20)

# punchline_label = Label(root, text="", font=("Arial", 14, "italic"), fg="blue", wraplength=500)
# punchline_label.place(x=50, y=80)

# # ---------------- JOKES LIST ----------------
# jokes = [
#     ("Why did the chicken cross the road?", "To get to the other side."),
#     ("What happens if you boil a clown?", "You get a laughing stock."),
#     ("Why did the car get a flat tire?", "Because there was a fork in the road!"),
#     ("How did the hipster burn his mouth?", "He ate his pizza before it was cool."),
#     ("What did the janitor say when he jumped out of the closet?", "SUPPLIES!!!!"),
#     ("Have you heard about the band 1023MB?", "It's probably because they haven't got a gig yet…"),
#     ("Why does the golfer wear two pants?", "Because he's afraid he might get a 'Hole-in-one.'"),
#     ("Why should you wear glasses to maths class?", "Because it helps with division."),
#     ("Why does it take pirates so long to learn the alphabet?", "Because they could spend years at C."),
#     ("Why did the woman go on the date with the mushroom?", "Because he was a fun-ghi."),
#     ("Why do bananas never get lonely?", "Because they hang out in bunches."),
#     ("What did the buffalo say when his kid went to college?", "Bison."),
#     ("Why shouldn't you tell secrets in a cornfield?", "Too many ears."),
#     ("What do you call someone who doesn't like carbs?", "Lack-Toast Intolerant."),
#     ("Why did the can crusher quit his job?", "Because it was soda pressing."),
#     ("Why did the birthday boy wrap himself in paper?", "He wanted to live in the present."),
#     ("What does a house wear?", "A dress."),
#     ("Why couldn't the toilet paper cross the road?", "Because it got stuck in a crack."),
#     ("Why didn't the bike want to go anywhere?", "Because it was two-tired!"),
#     ("Want to hear a pizza joke?", "Nahhh, it's too cheesy!"),
#     ("Why are chemists great at solving problems?", "Because they have all of the solutions!"),
#     ("Why is it impossible to starve in the desert?", "Because of all the sand which is there!"),
#     ("What did the cheese say when it looked in the mirror?", "Halloumi!"),
#     ("Why did the developer go broke?", "Because he used up all his cache."),
#     ("Did you know that ants are the only animals that don't get sick?", "It's true! It's because they have little antibodies."),
#     ("Why did the donut go to the dentist?", "To get a filling."),
#     ("What do you call a bear with no teeth?", "A gummy bear!"),
#     ("What does a vegan zombie like to eat?", "Graaains."),
#     ("What do you call a dinosaur with only one eye?", "A Do-you-think-he-saw-us!"),
#     ("Why should you never fall in love with a tennis player?", "Because to them... love means NOTHING!"),
#     ("What did the full glass say to the empty glass?", "You look drunk."),
#     ("What's a potato's favorite form of transportation?", "The gravy train."),
#     ("What did one ocean say to the other?", "Nothing, they just waved."),
#     ("What did the right eye say to the left eye?", "Honestly, between you and me something smells."),
#     ("What do you call a dog that's been run over by a steamroller?", "Spot!"),
#     ("What's the difference between a hippo and a zippo?", "One's pretty heavy and the other's a little lighter."),
#     ("Why don't scientists trust atoms?", "They make up everything.")
# ]

# ---------------- FIXED FUNCTIONS ----------------
# current_setup = ""
# current_punchline = ""

# def tell_joke():
#     """Select a random joke and show only the setup."""
#     global current_setup, current_punchline
#     current_setup, current_punchline = random.choice(jokes)
#     setup_label.config(text=current_setup)
#     punchline_label.config(text="")  # clear previous punchline

# def show_punchline():
#     """Show the stored punchline."""
#     punchline_label.config(text=current_punchline)

# def next_joke():
#     tell_joke()

# def quit_app():
#     root.destroy()

# ---------------- BUTTONS (WITH COMMANDS ADDED) ----------------
# Button(root, text="Alexa tell me a Joke", fg="black", font=("Arial", 12, "bold"),
#        bg="#ADD8E6", height=2, command=tell_joke).place(x=120, y=130)

# Button(root, text="Show Punchline", fg="black", font=("Arial", 12, "bold"),
#        bg="#FF0000", height=2, command=show_punchline).place(x=310, y=130)

# Button(root, text="Next Joke", fg="black", font=("Arial", 12, "bold"),
#        bg="#008000", width=15, height=2, command=next_joke).place(x=120, y=200)

# Button(root, text="Quit", fg="black", font=("Arial", 12, "bold"),
#        bg="#FFA500", width=13, height=2, command=quit_app).place(x=310, y=200)

# root.mainloop()

from tkinter import *
import random

# ---------- MAIN WINDOW ----------
root = Tk()
root.geometry("600x350")
root.title("Random Joke Game")

# Labels
setup_label = Label(root, text="", font=("Arial", 14), wraplength=500)
setup_label.place(x=50, y=20)

punchline_label = Label(root, text="", font=("Arial", 14, "italic"), fg="blue", wraplength=500)
punchline_label.place(x=50, y=80)

# ---------- JOKE GAME CLASS ----------
class JokeGame:
    def __init__(self, root):
        self.root = root

        self.jokes = [
            ("Why did the chicken cross the road?", "To get to the other side."),
            ("What happens if you boil a clown?", "You get a laughing stock."),
            ("Why did the car get a flat tire?", "Because there was a fork in the road!"),
            ("How did the hipster burn his mouth?", "He ate his pizza before it was cool."),
            ("What did the janitor say when he jumped out of the closet?", "SUPPLIES!!!!"),
            ("Have you heard about the band 1023MB?", "It's probably because they haven't got a gig yet…"),
            ("Why does the golfer wear two pants?", "Because he's afraid he might get a hole-in-one."),
            ("Why should you wear glasses to maths class?", "Because it helps with division."),
            ("Why does it take pirates so long to learn the alphabet?", "Because they could spend years at C."),
            ("Why did the woman go on the date with the mushroom?", "Because he was a fun-ghi."),
            ("Why do bananas never get lonely?", "Because they hang out in bunches."),
            ("What did the buffalo say when his kid went to college?", "Bison."),
            ("Why shouldn't you tell secrets in a cornfield?", "Too many ears."),
            ("What do you call someone who doesn't like carbs?", "Lack-Toast Intolerant."),
            ("Why did the can crusher quit his job?", "Because it was soda pressing."),
            ("Why did the birthday boy wrap himself in paper?", "He wanted to live in the present."),
            ("What does a house wear?", "A dress."),
            ("Why couldn't the toilet paper cross the road?", "Because it got stuck in a crack."),
            ("Why didn't the bike want to go anywhere?", "Because it was two-tired!"),
            ("Want to hear a pizza joke?", "Nahhh, it's too cheesy!"),
            ("Why are chemists great at solving problems?", "Because they have all of the solutions!"),
            ("Why is it impossible to starve in the desert?", "Because of all the sand which is there!"),
            ("What did the cheese say when it looked in the mirror?", "Halloumi!"),
            ("Why did the developer go broke?", "Because he used up all his cache."),
            ("Did you know that ants are the only animals that don't get sick?", "Because they have little antibodies."),
            ("Why did the donut go to the dentist?", "To get a filling."),
            ("What do you call a bear with no teeth?", "A gummy bear!"),
            ("What does a vegan zombie like to eat?", "Graaains."),
            ("What do you call a dinosaur with only one eye?", "A Do-you-think-he-saw-us!"),
            ("Why should you never fall in love with a tennis player?", "Because to them... love means NOTHING!"),
            ("What did the full glass say to the empty glass?", "You look drunk."),
            ("What's a potato's favorite form of transportation?", "The gravy train."),
            ("What did one ocean say to the other?", "Nothing, they just waved."),
            ("What did the right eye say to the left eye?", "Honestly, between you and me something smells."),
            ("What do you call a dog that's been run over by a steamroller?", "Spot!"),
            ("What's the difference between a hippo and a zippo?", "One's pretty heavy and the other's a little lighter."),
            ("Why don't scientists trust atoms?", "They make up everything.")
        ]

        self.current_punchline = ""

    def show_joke(self):
        setup, punchline = random.choice(self.jokes)
        setup_label.config(text=setup)
        punchline_label.config(text="")
        self.current_punchline = punchline

    def show_punchline(self):
        punchline_label.config(text=self.current_punchline)

    def next_joke(self):
        self.show_joke()

    def quit_game(self):
        self.root.destroy()


# ---------- CREATE GAME OBJECT ----------
game = JokeGame(root)

# ---------- BUTTONS ----------
Button(root, text="Alexa tell me a Joke", fg="black", font=("Arial", 12, "bold"),
       bg="#ADD8E6", height=2, command=game.show_joke).place(x=120, y=130)

Button(root, text="Show Punchline", fg="black", font=("Arial", 12, "bold"),
       bg="#FF0000", height=2, command=game.show_punchline).place(x=310, y=130)

Button(root, text="Next Joke", fg="black", font=("Arial", 12, "bold"),
       bg="#008000", width=15, height=2, command=game.next_joke).place(x=120, y=200)

Button(root, text="Quit", fg="black", font=("Arial", 12, "bold"),
       bg="#FFA500", width=13, height=2, command=game.quit_game).place(x=310, y=200)

root.mainloop()


