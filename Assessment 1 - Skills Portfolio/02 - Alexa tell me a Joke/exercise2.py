from tkinter import *

root = Tk()
root.geometry("600x350")
root.title("Random Joke Game")

button = Button(root, text = "Alexa tell me a Joke", fg = "black", bg = "#ADD8E6")
button.place(x = 120, y = 130)

root.mainloop()