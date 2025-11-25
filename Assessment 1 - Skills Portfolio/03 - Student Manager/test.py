from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

root = Tk()
root.geometry("1320x700")
root.title("Student Manager")

title_label = Label(root, text="Student Manager", fg="white", bg="teal", font=("Arial", 20, "bold"))
title_label.pack(pady=30)

detail_frame = LabelFrame(root, text="Student Records", fg="black", bg="lightgray",
                          font=("Arial", 14, "bold"))
detail_frame.place(x=40, y=90, width=420, height=570)

data_frame = Frame(root, bg="teal")
data_frame.place(x=490, y=98, width=830, height=565)

# Student Number
id_lab = Label(detail_frame, text="Student No:", font=("Arial", 16), bg="lightgray", fg="black")
id_lab.place(x=20, y=15)
id_ent = Entry(detail_frame, bd=1, font=("Arial", 16), bg="white", fg="black")
id_ent.place(x=180, y=15, width=200, height=30)

# Student Name
name_lab = Label(detail_frame, text="Name:", font=("Arial", 16), bg="lightgray", fg="black")
name_lab.place(x=20, y=65)
name_ent = Entry(detail_frame, bd=1, font=("Arial", 16), bg="white", fg="black")
name_ent.place(x=180, y=65, width=200, height=30)

# Coursework 1
c1_lab = Label(detail_frame, text="Coursework 1:", font=("Arial", 16), bg="lightgray", fg="black")
c1_lab.place(x=20, y=115)
c1_ent = Entry(detail_frame, bd=1, font=("Arial", 16), bg="white", fg="black")
c1_ent.place(x=180, y=115, width=200, height=30)

# Coursework 2
c2_lab = Label(detail_frame, text="Coursework 2:", font=("Arial", 16), bg="lightgray", fg="black")
c2_lab.place(x=20, y=165)
c2_ent = Entry(detail_frame, bd=1, font=("Arial", 16), bg="white", fg="black")
c2_ent.place(x=180, y=165, width=200, height=30)

# Coursework 3
c3_lab = Label(detail_frame, text="Coursework 3:", font=("Arial", 16), bg="lightgray", fg="black")
c3_lab.place(x=20, y=215)
c3_ent = Entry(detail_frame, bd=1, font=("Arial", 16), bg="white", fg="black")
c3_ent.place(x=180, y=215, width=200, height=30)

# Exam Mark
exam_lab = Label(detail_frame, text="Exam Mark:", font=("Arial", 16), bg="lightgray", fg="black")
exam_lab.place(x=20, y=265)
exam_ent = Entry(detail_frame, bd=1, font=("Arial", 16), bg="white", fg="black")
exam_ent.place(x=180, y=265, width=200, height=30)

# ================== TREEVIEW ==================
main_frame = Frame(data_frame, bg="teal", bd=2, relief=tk.GROOVE)
main_frame.pack(fill=tk.BOTH, expand=True)

y_scroll = Scrollbar(main_frame, orient=VERTICAL)
x_scroll = Scrollbar(main_frame, orient=HORIZONTAL)

student_table = ttk.Treeview(
    main_frame,
    columns=("ID", "Name", "C1", "C2", "C3", "Exam", "Percent", "Grade"),
    yscrollcommand=y_scroll.set,
    xscrollcommand=x_scroll.set
)

y_scroll.config(command=student_table.yview)
x_scroll.config(command=student_table.xview)
y_scroll.pack(side=RIGHT, fill=Y)
x_scroll.pack(side=BOTTOM, fill=X)

# Headings
headings = {
    "ID": "Student No",
    "Name": "Name",
    "C1": "Coursework 1",
    "C2": "Coursework 2",
    "C3": "Coursework 3",
    "Exam": "Exam Mark",
    "Percent": "Overall %",
    "Grade": "Grade"
}

for col, text in headings.items():
    student_table.heading(col, text=text)
    student_table.column(col, width=100)

student_table["show"] = "headings"
student_table.pack(fill=BOTH, expand=True)

student_table.tag_configure("oddrow", background="white")
student_table.tag_configure("evenrow", background="#00AEAE")

# ================== LOGIC ==================
students = []

def calculate_marks(c1, c2, c3, exam):
    cw_total = c1 + c2 + c3
    percent = round(((cw_total + exam) / 160) * 100, 2)

    if percent >= 70: grade = "A"
    elif percent >= 60: grade = "B"
    elif percent >= 50: grade = "C"
    elif percent >= 40: grade = "D"
    else: grade = "F"

    return cw_total, percent, grade


def load_students_from_file():
    """Load from studentMarks.txt"""
    students.clear()
    delete_all()
    try:
        with open("studentMarks.txt", "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        messagebox.showerror("Error", "studentMarks.txt not found")
        return

    for line in lines[1:]:
        parts = line.strip().split(",")
        if len(parts) != 6:
            continue

        sid, name = parts[0], parts[1]
        c1, c2, c3, exam = map(int, parts[2:6])
        cw_total, percent, grade = calculate_marks(c1, c2, c3, exam)

        students.append({
            "id": sid, "name": name, "c1": c1, "c2": c2, "c3": c3,
            "exam": exam, "percent": percent, "grade": grade
        })

    refresh_tree()


def save_students_to_file():
    with open("studentMarks.txt", "w") as f:
        f.write(str(len(students)) + "\n")
        for s in students:
            f.write(f"{s['id']},{s['name']},{s['c1']},{s['c2']},{s['c3']},{s['exam']}\n")


def refresh_tree():
    delete_all()
    for i, s in enumerate(students):
        tag = "evenrow" if i % 2 == 0 else "oddrow"
        student_table.insert(
            "",
            "end",
            values=(s["id"], s["name"], s["c1"], s["c2"], s["c3"], s["exam"], s["percent"], s["grade"]),
            tags=(tag,)
        )


def delete_all():
    for row in student_table.get_children():
        student_table.delete(row)


def clear_entries():
    for widget in (id_ent, name_ent, c1_ent, c2_ent, c3_ent, exam_ent):
        widget.delete(0, END)


def add_record():
    try:
        sid = id_ent.get().strip()
        name = name_ent.get().strip()
        c1 = int(c1_ent.get())
        c2 = int(c2_ent.get())
        c3 = int(c3_ent.get())
        exam = int(exam_ent.get())
    except:
        messagebox.showerror("Error", "Marks must be numbers")
        return

    if not sid or not name:
        messagebox.showerror("Error", "Student No and Name required")
        return

    for s in students:
        if s["id"] == sid:
            messagebox.showerror("Error", "Student already exists")
            return

    cw_total, percent, grade = calculate_marks(c1, c2, c3, exam)

    students.append({
        "id": sid, "name": name, "c1": c1, "c2": c2, "c3": c3,
        "exam": exam, "percent": percent, "grade": grade
    })

    refresh_tree()
    save_students_to_file()
    clear_entries()


def delete_one():
    selected = student_table.selection()
    if not selected:
        messagebox.showerror("Error", "Select a record")
        return

    sid = student_table.item(selected, "values")[0]
    students[:] = [s for s in students if s["id"] != sid]

    refresh_tree()
    save_students_to_file()
    clear_entries()


def select_record():
    selected = student_table.selection()
    if not selected:
        messagebox.showerror("Error", "Select a record")
        return

    values = student_table.item(selected, "values")
    clear_entries()

    id_ent.insert(0, values[0])
    name_ent.insert(0, values[1])
    c1_ent.insert(0, values[2])
    c2_ent.insert(0, values[3])
    c3_ent.insert(0, values[4])
    exam_ent.insert(0, values[5])


def update_record():
    selected = student_table.selection()
    if not selected:
        messagebox.showerror("Error", "Select a record")
        return

    old_id = student_table.item(selected, "values")[0]

    try:
        sid = id_ent.get().strip()
        name = name_ent.get().strip()
        c1 = int(c1_ent.get())
        c2 = int(c2_ent.get())
        c3 = int(c3_ent.get())
        exam = int(exam_ent.get())
    except:
        messagebox.showerror("Error", "Marks must be numbers")
        return

    cw_total, percent, grade = calculate_marks(c1, c2, c3, exam)

    for s in students:
        if s["id"] == old_id:
            s["id"] = sid
            s["name"] = name
            s["c1"] = c1
            s["c2"] = c2
            s["c3"] = c3
            s["exam"] = exam
            s["percent"] = percent
            s["grade"] = grade
            break

    refresh_tree()
    save_students_to_file()
    clear_entries()


# ================== MENU FUNCTIONS ==================
def view_all_records():
    if not students:
        load_students_from_file()
    refresh_tree()

    if not students:
        return

    avg = round(sum(s["percent"] for s in students) / len(students), 2)
    messagebox.showinfo("Summary", f"Students: {len(students)}\nAverage: {avg}%")


def view_individual_record():
    q = simpledialog.askstring("Search", "Enter student number or name:")
    if not q:
        return

    q = q.lower()
    for s in students:
        if s["id"] == q or q in s["name"].lower():
            msg = (
                f"Name: {s['name']}\n"
                f"Student No: {s['id']}\n"
                f"Coursework Total: {s['c1'] + s['c2'] + s['c3']} / 60\n"
                f"Exam: {s['exam']} / 100\n"
                f"Percent: {s['percent']}%\n"
                f"Grade: {s['grade']}"
            )
            messagebox.showinfo("Record", msg)
            return

    messagebox.showerror("Not found", "Student not found")


def show_highest_total():
    best = max(students, key=lambda s: s["percent"])
    messagebox.showinfo("Highest", f"{best['name']} — {best['percent']}%")

def show_lowest_total():
    worst = min(students, key=lambda s: s["percent"])
    messagebox.showinfo("Lowest", f"{worst['name']} — {worst['percent']}%")

def sort_records():
    students.sort(key=lambda s: s["percent"])
    refresh_tree()

# ================== MENU BAR ==================
menubar = tk.Menu(root)
root.config(menu=menubar)

menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Student Menu", menu=menu)

menu.add_command(label="1. View all records", command=view_all_records)
menu.add_command(label="2. View individual record", command=view_individual_record)
menu.add_command(label="3. Show highest total", command=show_highest_total)
menu.add_command(label="4. Show lowest total", command=show_lowest_total)
menu.add_separator()
menu.add_command(label="5. Sort records", command=sort_records)
menu.add_command(label="6. Add record", command=add_record)
menu.add_command(label="7. Delete record", command=delete_one)
menu.add_command(label="8. Update record", command=update_record)

# ================== BUTTONS ==================
btn_frame = Frame(detail_frame, bg="lightgray")
btn_frame.place(x=40, y=400, width=310, height=130)

Button(btn_frame, text="Add", width=15, bg="teal", fg="white",
       font=("Arial", 13), command=add_record).grid(row=0, column=0, padx=2, pady=2)

Button(btn_frame, text="Select", width=15, bg="teal", fg="white",
       font=("Arial", 13), command=select_record).grid(row=0, column=1, padx=2, pady=2)

Button(btn_frame, text="View All", width=15, bg="teal", fg="white",
       font=("Arial", 13), command=view_all_records).grid(row=1, column=0, padx=2, pady=2)

Button(btn_frame, text="Update", width=15, bg="teal", fg="white",
       font=("Arial", 13), command=update_record).grid(row=1, column=1, padx=2, pady=2)

Button(btn_frame, text="Delete", width=15, bg="teal", fg="white",
       font=("Arial", 13), command=delete_one).grid(row=2, column=1, padx=2, pady=2)

# ================== START ==================
load_students_from_file()
root.mainloop()
