from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

# =========================== MAIN WINDOW ============================
root = Tk()
root.geometry("1000x600")
root.title("Student Manager")

# =========================================================================
#                           STYLE
# =========================================================================
style = ttk.Style()
style.theme_use("default")

style.configure("Treeview",
                background="white",
                foreground="black",
                rowheight=25,
                fieldbackground="white")

style.map('Treeview', background=[('selected', 'darkcyan')])

title_label = tk.Label(root, text="Student Manager", font=("Arial", 20, "bold"),
                       bg="teal", fg="white", pady=12)
title_label.pack(side=tk.TOP, fill=tk.X)

# =========================================================================
#                        FRAMES
# =========================================================================

detail_frame = tk.LabelFrame(root, text="Student Data Entry", font=("Arial", 14),
                             bg="lightgray", fg="black")
detail_frame.place(x=20, y=80, width=400, height=500)

data_frame = tk.Frame(root, bg="teal")
data_frame.place(x=440, y=80, width=540, height=500)

main_frame = tk.Frame(data_frame, bg="teal", bd=2, relief=tk.GROOVE)
main_frame.pack(fill=tk.BOTH, expand=True)

# Scrollbars
y_scroll = tk.Scrollbar(main_frame, orient=tk.VERTICAL)
x_scroll = tk.Scrollbar(main_frame, orient=tk.HORIZONTAL)

# =========================================================================
#                        TREEVIEW (new fields)
# =========================================================================

columns = ("Number", "Name", "C1", "C2", "C3", "Exam", "CW Total", "Percent", "Grade")

student_table = ttk.Treeview(main_frame, columns=columns,
                             yscrollcommand=y_scroll.set,
                             xscrollcommand=x_scroll.set)

y_scroll.config(command=student_table.yview)
x_scroll.config(command=student_table.xview)

y_scroll.pack(side=tk.RIGHT, fill=tk.Y)
x_scroll.pack(side=tk.BOTTOM, fill=tk.X)

for col in columns:
    student_table.heading(col, text=col)
    student_table.column(col, width=100)

student_table["show"] = "headings"
student_table.pack(fill=tk.BOTH, expand=True)

# =========================================================================
#                    INPUT FIELDS (matching assessment)
# =========================================================================

labels = ["Student No:", "Student Name:", "Coursework 1:", "Coursework 2:",
          "Coursework 3:", "Exam Mark:"]

entries = {}

y_pos = 20
for text in labels:
    lab = tk.Label(detail_frame, text=text, font=("Arial", 14), bg="lightgray")
    lab.place(x=20, y=y_pos)
    ent = tk.Entry(detail_frame, font=("Arial", 14))
    ent.place(x=180, y=y_pos, width=180, height=28)
    entries[text] = ent
    y_pos += 50

# =========================================================================
#                     CALCULATE, GRADE, HELPERS
# =========================================================================

def calculate(c1, c2, c3, exam):
    cw = c1 + c2 + c3
    percent = round((cw + exam) / 160 * 100, 2)

    if percent >= 70: grade = "A"
    elif percent >= 60: grade = "B"
    elif percent >= 50: grade = "C"
    elif percent >= 40: grade = "D"
    else: grade = "F"

    return cw, percent, grade

students = []   # list of dictionaries


# =========================================================================
#                       LOAD FROM FILE
# =========================================================================

def load_from_file():
    global students
    students.clear()
    delete_all()

    try:
        with open("studentMarks.txt", "r") as f:
            lines = f.readlines()
    except:
        messagebox.showerror("Error", "studentMarks.txt not found")
        return

    for line in lines[1:]:
        parts = line.strip().split(",")
        num = parts[0]
        name = parts[1]
        c1 = int(parts[2])
        c2 = int(parts[3])
        c3 = int(parts[4])
        exam = int(parts[5])

        cw, percent, grade = calculate(c1, c2, c3, exam)

        s = {
            "num": num,
            "name": name,
            "c1": c1, "c2": c2, "c3": c3,
            "exam": exam,
            "cw": cw,
            "percent": percent,
            "grade": grade
        }
        students.append(s)

    refresh_table()


def refresh_table():
    delete_all()
    tag = ""
    for i, s in enumerate(students):
        tag = "evenrow" if i % 2 == 0 else "oddrow"
        student_table.insert("", "end", iid=i, values=(
            s["num"], s["name"], s["c1"], s["c2"], s["c3"],
            s["exam"], s["cw"], s["percent"], s["grade"]
        ), tags=tag)


student_table.tag_configure("oddrow", background="white")
student_table.tag_configure("evenrow", background="#00CCCC")

# =========================================================================
#                            SAVE TO FILE
# =========================================================================

def save_to_file():
    with open("studentMarks.txt", "w") as f:
        f.write(str(len(students)) + "\n")
        for s in students:
            line = f"{s['num']},{s['name']},{s['c1']},{s['c2']},{s['c3']},{s['exam']}\n"
            f.write(line)

# =========================================================================
#                       BUTTON FUNCTIONS
# =========================================================================

def add_record():
    num = entries["Student No:"].get()
    name = entries["Student Name:"].get()
    c1 = int(entries["Coursework 1:"].get())
    c2 = int(entries["Coursework 2:"].get())
    c3 = int(entries["Coursework 3:"].get())
    exam = int(entries["Exam Mark:"].get())

    cw, percent, grade = calculate(c1, c2, c3, exam)

    students.append({
        "num": num, "name": name,
        "c1": c1, "c2": c2, "c3": c3,
        "exam": exam,
        "cw": cw, "percent": percent, "grade": grade
    })

    refresh_table()
    save_to_file()


def delete_all():
    for row in student_table.get_children():
        student_table.delete(row)


def delete_one():
    try:
        selected = int(student_table.selection()[0])
        students.pop(selected)
        refresh_table()
        save_to_file()
    except:
        messagebox.showerror("Error", "Select a record first")


def select_record():
    try:
        selected = int(student_table.selection()[0])
        s = students[selected]

        entries["Student No:"].delete(0, END)
        entries["Student Name:"].delete(0, END)
        entries["Coursework 1:"].delete(0, END)
        entries["Coursework 2:"].delete(0, END)
        entries["Coursework 3:"].delete(0, END)
        entries["Exam Mark:"].delete(0, END)

        entries["Student No:"].insert(0, s["num"])
        entries["Student Name:"].insert(0, s["name"])
        entries["Coursework 1:"].insert(0, s["c1"])
        entries["Coursework 2:"].insert(0, s["c2"])
        entries["Coursework 3:"].insert(0, s["c3"])
        entries["Exam Mark:"].insert(0, s["exam"])
    except:
        messagebox.showerror("Error", "Select a record first")


def update_record():
    try:
        selected = int(student_table.selection()[0])

        num = entries["Student No:"].get()
        name = entries["Student Name:"].get()
        c1 = int(entries["Coursework 1:"].get())
        c2 = int(entries["Coursework 2:"].get())
        c3 = int(entries["Coursework 3:"].get())
        exam = int(entries["Exam Mark:"].get())

        cw, percent, grade = calculate(c1, c2, c3, exam)

        students[selected] = {
            "num": num, "name": name,
            "c1": c1, "c2": c2, "c3": c3,
            "exam": exam,
            "cw": cw, "percent": percent, "grade": grade
        }

        refresh_table()
        save_to_file()

    except:
        messagebox.showerror("Error", "Select a record to update")


# =========================================================================
#                         MENU OPTIONS 1–4
# =========================================================================

def view_all():
    load_from_file()
    total = sum(s['percent'] for s in students)
    avg = round(total / len(students), 2)
    messagebox.showinfo("Summary", f"Total students: {len(students)}\nAverage: {avg}%")

def view_individual():
    q = simpledialog.askstring("Search", "Enter student number or name:")
    if not q:
        return
    q = q.lower()
    for s in students:
        if s["num"] == q or q in s["name"].lower():
            messagebox.showinfo(
                "Record",
                f"Name: {s['name']}\n"
                f"Number: {s['num']}\n"
                f"Coursework Total: {s['cw']}/60\n"
                f"Exam: {s['exam']}/100\n"
                f"Percent: {s['percent']}%\n"
                f"Grade: {s['grade']}"
            )
            return
    messagebox.showerror("Not found", "Student not found.")

def highest():
    s = max(students, key=lambda x: x['percent'])
    messagebox.showinfo("Highest", f"{s['name']} ({s['percent']}%)")

def lowest():
    s = min(students, key=lambda x: x['percent'])
    messagebox.showinfo("Lowest", f"{s['name']} ({s['percent']}%)")


# Add menu bar
menu = tk.Menu(root)
root.config(menu=menu)

stu_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Marks Menu", menu=stu_menu)
stu_menu.add_command(label="1. View all student records", command=view_all)
stu_menu.add_command(label="2. View individual record", command=view_individual)
stu_menu.add_command(label="3. Highest overall score", command=highest)
stu_menu.add_command(label="4. Lowest overall score", command=lowest)

# =========================================================================
#                           BUTTONS
# =========================================================================
btn_frame = tk.Frame(detail_frame, bg="lightgray")
btn_frame.place(x=50, y=350, width=280, height=130)

tk.Button(btn_frame, text="Add", width=12, bg="teal", fg="white",
          font=("Arial", 13), command=add_record).grid(row=0, column=0, padx=5, pady=5)

tk.Button(btn_frame, text="Select", width=12, bg="teal", fg="white",
          font=("Arial", 13), command=select_record).grid(row=0, column=1, padx=5, pady=5)

tk.Button(btn_frame, text="Update", width=12, bg="teal", fg="white",
          font=("Arial", 13), command=update_record).grid(row=1, column=0, padx=5, pady=5)

tk.Button(btn_frame, text="Delete", width=12, bg="teal", fg="white",
          font=("Arial", 13), command=delete_one).grid(row=1, column=1, padx=5, pady=5)

# =========================================================================
#                           START PROGRAM
# =========================================================================
load_from_file()
root.mainloop()


