from tkinter import *
from tkinter import Toplevel, messagebox, filedialog
from tkinter import ttk
from tkinter.ttk import Treeview
root = Tk()
root.title("Student Manager")
root.configure(bg="black")
root.geometry("1180x800+50+50")

dataentryframe = Frame(root, bg = "black", relief = GROOVE, borderwidth = 5)
dataentryframe.place(x=15, y=15, width=300, height=620)

la1 = Label(dataentryframe, text=" ======>Menu<======", font=("times", 20, "bold"), bg="black", foreground="white")
la1.place(x=0, y=90)

addbtn = Button(dataentryframe, text="1. Add student")

showdataframe = Frame(root, bg = "black", relief=GROOVE, borderwidth = 5)
showdataframe.place(x = 340, y= 140, width = 830, height=495)

titledataframe = Frame(root, bg = "black", relief=GROOVE, borderwidth = 5)
titledataframe.place(x = 340, y= 15, width = 830, height=100)

title = Label(titledataframe, text = "Student Manager", font=("times", 35, "bold"), foreground="white", bg="black", width=25)
title.place(x=17, y=15)


root.mainloop()