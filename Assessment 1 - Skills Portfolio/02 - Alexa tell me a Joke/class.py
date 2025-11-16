from tkinter import *
import random

class JokeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Joke Game (OOP Version)")
        self.root.geometry("600x350")

        # ----------------- Jokes List -----------------
        self.jokes = [
            ("Why did the chicken cross the road?", "To get to the other side."),
            ("What happens if you boil a clown?", "You get a laughing stock."),
            ("Why did the car get a flat tire?", "Because there was a fork in the road!"),
            ("How did the hipster burn his mouth?", "He ate his pizza before it was cool."),
            ("What did the janitor say when he jumped out of the closet?", "SUPPLIES!!!!"),
            ("Why do bananas never get lonely?", "Because they hang out in bunches."),
            ("What do you call a bear with no teeth?", "A gummy bear!"),
            ("Why don't scientists trust atoms?", "They make up everything.")
        ]

        self.current_punchline = ""

        # ----------------- Labels -----------------
        self.setup_label = Label(root, text="", font=("Arial", 14), wraplength=500)
        self.setup_label.place(x=50, y=20)

        self.punchline_label = Label(root, text="", font=("Arial", 14, "italic"),
                                     fg="blue", wraplength=500)
        self.punchline_label.place(x=50, y=80)

        # ----------------- Buttons -----------------
        Button(root, text="Alexa tell me a Joke", fg="black", font=("Arial", 12, "bold"),
               bg="#ADD8E6", height=2, command=self.show_joke).place(x=120, y=130)

        Button(root, text="Show Punchline", fg="black", font=("Arial", 12, "bold"),
               bg="#FF0000", height=2, command=self.show_punchline).place(x=310, y=130)

        Button(root, text="Next Joke", fg="black", font=("Arial", 12, "bold"),
               bg="#008000", width=15, height=2, command=self.show_joke).place(x=120, y=200)

        Button(root, text="Quit", fg="black", font=("Arial", 12, "bold"),
               bg="#FFA500", width=13, height=2, command=root.destroy).place(x=310, y=200)


    # ----------------- Methods -----------------
    def show_joke(self):
        """Select and display a random joke setup."""
        joke = random.choice(self.jokes)
        self.setup_label.config(text=joke[0])  # show setup
        self.punchline_label.config(text="")   # clear punchline
        self.current_punchline = joke[1]       # store punchline

    def show_punchline(self):
        """Display the stored punchline."""
        self.punchline_label.config(text=self.current_punchline)


# ----------------- RUN APP -----------------
root = Tk()
game = JokeGame(root)   # Create object
root.mainloop()
