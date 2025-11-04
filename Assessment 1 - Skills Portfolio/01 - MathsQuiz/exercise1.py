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
    return random.choice(["+", "-"])






                        