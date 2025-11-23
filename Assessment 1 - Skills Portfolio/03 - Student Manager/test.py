from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

root = Tk()
root.geometry("1320x700")  
root.title("Student Manager")

style = ttk.Style()
style.theme_use("default")

style.configure(
    "Treeview",
    background="white",
    foreground="black",
    rowheight=25,
    fieldbackground="white"
)

style.map(
    "Treeview",
    background=[("selected", "darkcyan")]   # fixed invalid colour name
)

# ================== TITLE ==================
title_label = tk.Label(
    root,
    text="Student Manager",
    font=("Arial", 20, "bold"),
    padx=15,
    pady=15,
    border=0,
    relief=tk.GROOVE,
    bg="teal",
    foreground="white",
)
title_label.pack(side=tk.TOP, fill=tk.X)

# ================== FRAMES ==================
detail_frame = tk.LabelFrame(
    root, text="Student Records",
    font=("Arial", 14),
    bg="lightgray",
    foreground="black",
    relief=tk.GROOVE
)
detail_frame.place(x=40, y=90, width=420, height=570)

data_frame = tk.Frame(
    root,
    bg="teal",
    relief=tk.GROOVE
)
data_frame.place(x=490, y=98, width=830, height=565)

# ================== ENTRY FIELDS (repurposed for marks) ==================
# ID -> Student Number
id_lab = tk.Label(
    detail_frame,
    text="Student No:",
    font=("Arial", 16),
    bg="lightgray",
    foreground="black"
)
id_lab.place(x=20, y=15)

id_ent = tk.Entry(
    detail_frame,
    bd=1,
    font=("Arial", 16),
    bg="white",
    foreground="black"
)
id_ent.place(x=150, y=17, width=220, height=30)

# Name
name_lab = tk.Label(
    detail_frame,
    text="Name:",
    font=("Arial", 16),
    bg="lightgray",
    foreground="black"
)
name_lab.place(x=20, y=65)

name_ent = tk.Entry(
    detail_frame,
    bd=1,
    font=("Arial", 16),
    bg="white",
    foreground="black"
)
name_ent.place(x=150, y=65, width=220, height=30)

# Gender (was) -> Coursework 1
gen_lab = tk.Label(
    detail_frame,
    text="Coursework 1:",
    font=("Arial", 16),
    bg="lightgray",
    foreground="black"
)
gen_lab.place(x=20, y=113)

gen_ent = tk.Entry(
    detail_frame,
    bd=1,
    font=("Arial", 16),
    bg="white",
    foreground="black"
)
gen_ent.place(x=150, y=113, width=220, height=30)

# Age (was) -> Coursework 2
age_lab = tk.Label(
    detail_frame,
    text="Coursework 2:",
    font=("Arial", 16),
    bg="lightgray",
    foreground="black"
)
age_lab.place(x=20, y=161)

age_ent = tk.Entry(
    detail_frame,
    bd=1,
    font=("Arial", 16),
    bg="white",
    foreground="black"
)
age_ent.place(x=150, y=161, width=220, height=30)

# ent_lab / ent_ent -> Coursework 3
ent_lab = tk.Label(
    detail_frame,
    text="Coursework 3:",
    font=("Arial", 16),
    bg="lightgray",
    foreground="black"
)
ent_lab.place(x=20, y=209)

ent_ent = tk.Entry(
    detail_frame,
    bd=1,
    font=("Arial", 16),
    bg="white",
    foreground="black"
)
ent_ent.place(x=150, y=209, width=220, height=30)

# mid_lab / mid_ent -> Exam Mark
mid_lab = tk.Label(
    detail_frame,
    text="Exam Mark:",
    font=("Arial", 16),
    bg="lightgray",
    foreground="black"
)
mid_lab.place(x=20, y=257)

mid_ent = tk.Entry(
    detail_frame,
    bd=1,
    font=("Arial", 16),
    bg="white",
    foreground="black"
)
mid_ent.place(x=150, y=257, width=220, height=30)

# fin_lab / fin_ent -> Overall %
fin_lab = tk.Label(
    detail_frame,
    text="Overall %:",
    font=("Arial", 16),
    bg="lightgray",
    foreground="black"
)
fin_lab.place(x=20, y=305)

fin_ent = tk.Entry(
    detail_frame,
    bd=1,
    font=("Arial", 16),
    bg="white",
    foreground="black"
)
fin_ent.place(x=150, y=305, width=220, height=30)

# gpa_lab / gpa_ent -> Grade
gpa_lab = tk.Label(
    detail_frame,
    text="Grade:",
    font=("Arial", 16),
    bg="lightgray",
    foreground="black"
)
gpa_lab.place(x=20, y=353)

gpa_ent = tk.Entry(
    detail_frame,
    bd=1,
    font=("Arial", 16),
    bg="white",
    foreground="black"
)
gpa_ent.place(x=150, y=353, width=220, height=30)

# ================== TREEVIEW FRAME ==================
main_frame = tk.Frame(
    data_frame,
    bg="teal",
    bd=2,
    relief=tk.GROOVE
)
main_frame.pack(fill=tk.BOTH, expand=True)

y_scroll = tk.Scrollbar(main_frame, orient=tk.VERTICAL)
x_scroll = tk.Scrollbar(main_frame, orient=tk.HORIZONTAL)

# Treeview database
student_table = ttk.Treeview(
    main_frame,
    columns=(
        "ID", "Name", "C1", "C2", "C3",
        "Exam", "Percent", "Grade"
    ),
    yscrollcommand=y_scroll.set,
    xscrollcommand=x_scroll.set
)

y_scroll.config(command=student_table.yview)
x_scroll.config(command=student_table.xview)

y_scroll.pack(side=tk.RIGHT, fill=tk.Y)
x_scroll.pack(side=tk.BOTTOM, fill=tk.X)

# Change headings to match assessment
student_table.heading("ID", text="Student No")
student_table.heading("Name", text="Name")
student_table.heading("C1", text="Coursework 1")
student_table.heading("C2", text="Coursework 2")
student_table.heading("C3", text="Coursework 3")
student_table.heading("Exam", text="Exam Mark")
student_table.heading("Percent", text="Overall %")
student_table.heading("Grade", text="Grade")

student_table["show"] = "headings"

for col in ("ID", "Name", "C1", "C2", "C3", "Exam", "Percent", "Grade"):
    student_table.column(col, width=100)

student_table.pack(fill=tk.BOTH, expand=True)

# striped rows
student_table.tag_configure("oddrow", background="white")
student_table.tag_configure("evenrow", background="#00AEAE")

# ================== STUDENT DATA LOGIC ==================

students = []   # each student is a dict


def calculate_marks(c1, c2, c3, exam):
    cw_total = c1 + c2 + c3
    overall = cw_total + exam
    percent = round((overall / 160) * 100, 2)

    if percent >= 70:
        grade = "A"
    elif percent >= 60:
        grade = "B"
    elif percent >= 50:
        grade = "C"
        grade = "C"
    elif percent >= 40:
        grade = "D"
    else:
        grade = "F"
    return cw_total, percent, grade


def load_students_from_file():
    """Load data from studentMarks.txt into 'students' list and Treeview."""
    global students
    students.clear()
    delete_all()

    try:
        with open("studentMarks.txt", "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        messagebox.showerror("Error", "studentMarks.txt not found.")
        return

    for line in lines[1:]:  # skip first line (number of students)
        parts = line.strip().split(",")
        if len(parts) != 6:
            continue

        sid = parts[0]
        name = parts[1]
        c1 = int(parts[2])
        c2 = int(parts[3])
        c3 = int(parts[4])
        exam = int(parts[5])

        cw_total, percent, grade = calculate_marks(c1, c2, c3, exam)

        students.append({
            "id": sid,
            "name": name,
            "c1": c1,
            "c2": c2,
            "c3": c3,
            "exam": exam,
            "cw_total": cw_total,
            "percent": percent,
            "grade": grade
        })

    refresh_tree()


def save_students_to_file():
    """Write 'students' list back to studentMarks.txt in original format."""
    with open("studentMarks.txt", "w") as f:
        f.write(str(len(students)) + "\n")
        for s in students:
            line = f"{s['id']},{s['name']},{s['c1']},{s['c2']},{s['c3']},{s['exam']}\n"
            f.write(line)


def refresh_tree():
    """Repopulate Treeview from 'students' list."""
    delete_all()
    for index, s in enumerate(students):
        tag = "evenrow" if index % 2 == 0 else "oddrow"
        student_table.insert(
            "",
            "end",
            values=(
                s["id"], s["name"], s["c1"], s["c2"], s["c3"],
                s["exam"], s["percent"], s["grade"]
            ),
            tags=(tag,)
        )


# ================== CRUD FUNCTIONS ==================

def clear_entries():
    id_ent.delete(0, END)
    name_ent.delete(0, END)
    gen_ent.delete(0, END)
    age_ent.delete(0, END)
    ent_ent.delete(0, END)
    mid_ent.delete(0, END)
    fin_ent.delete(0, END)
    gpa_ent.delete(0, END)


def add_record():
    """Menu 6: Add student record + update file."""
    try:
        sid = id_ent.get().strip()
        name = name_ent.get().strip()
        c1 = int(gen_ent.get())
        c2 = int(age_ent.get())
        c3 = int(ent_ent.get())
        exam = int(mid_ent.get())
    except ValueError:
        messagebox.showerror("Error", "Coursework and exam marks must be integers.")
        return

    if not sid or not name:
        messagebox.showerror("Error", "Student number and name are required.")
        return

    # check duplicate id
    for s in students:
        if s["id"] == sid:
            messagebox.showerror("Error", "Student number already exists.")
            return

    cw_total, percent, grade = calculate_marks(c1, c2, c3, exam)

    students.append({
        "id": sid,
        "name": name,
        "c1": c1,
        "c2": c2,
        "c3": c3,
        "exam": exam,
        "cw_total": cw_total,
        "percent": percent,
        "grade": grade
    })

    refresh_tree()
    save_students_to_file()
    clear_entries()


def delete_all():
    for record in student_table.get_children():
        student_table.delete(record)


def delete_one():
    """Menu 7: Delete a student record from table + file."""
    selected = student_table.selection()
    if not selected:
        messagebox.showerror("Error", "Please select a record to delete.")
        return

    item = selected[0]
    values = student_table.item(item, "values")
    sid = values[0]

    # remove from list
    global students
    students = [s for s in students if s["id"] != sid]

    refresh_tree()
    save_students_to_file()
    clear_entries()


def select_record():
    """Fill entry boxes from selected row (for updating)."""
    selected = student_table.selection()
    if not selected:
        messagebox.showerror("Error", "Please select a record first.")
        return

    item = selected[0]
    values = student_table.item(item, "values")

    clear_entries()
    id_ent.insert(0, values[0])
    name_ent.insert(0, values[1])
    gen_ent.insert(0, values[2])
    age_ent.insert(0, values[3])
    ent_ent.insert(0, values[4])
    mid_ent.insert(0, values[5])
    fin_ent.insert(0, values[6])
    gpa_ent.insert(0, values[7])


def update_record():
    """Menu 8: Update a student's record and file."""
    selected = student_table.selection()
    if not selected:
        messagebox.showerror("Error", "Please select a record to update.")
        return

    item = selected[0]
    old_values = student_table.item(item, "values")
    old_id = old_values[0]

    try:
        sid = id_ent.get().strip()
        name = name_ent.get().strip()
        c1 = int(gen_ent.get())
        c2 = int(age_ent.get())
        c3 = int(ent_ent.get())
        exam = int(mid_ent.get())
    except ValueError:
        messagebox.showerror("Error", "Coursework and exam marks must be integers.")
        return

    cw_total, percent, grade = calculate_marks(c1, c2, c3, exam)

    # update in list
    for s in students:
        if s["id"] == old_id:
            s["id"] = sid
            s["name"] = name
            s["c1"] = c1
            s["c2"] = c2
            s["c3"] = c3
            s["exam"] = exam
            s["cw_total"] = cw_total
            s["percent"] = percent
            s["grade"] = grade
            break

    refresh_tree()
    save_students_to_file()
    clear_entries()


# ================== MENU 1–5 FUNCTIONS ==================

def view_all_records():
    """Menu 1: View all student records + summary."""
    if not students:
        load_students_from_file()

    refresh_tree()
    if not students:
        return
    total_percent = sum(s["percent"] for s in students)
    avg = round(total_percent / len(students), 2)

    messagebox.showinfo(
        "Class Summary",
        f"Number of students: {len(students)}\nAverage percentage: {avg}%"
    )


def view_individual_record():
    """Menu 2: Ask user for student number or name, then show result."""
    if not students:
        load_students_from_file()

    q = simpledialog.askstring("Search", "Enter student number or name:")
    if not q:
        return
    q_lower = q.lower()

    for s in students:
        if s["id"] == q or q_lower in s["name"].lower():
            msg = (
                f"Name: {s['name']}\n"
                f"Student Number: {s['id']}\n"
                f"Total coursework mark: {s['cw_total']} / 60\n"
                f"Exam mark: {s['exam']} / 100\n"
                f"Overall percentage: {s['percent']}%\n"
                f"Grade: {s['grade']}"
            )
            messagebox.showinfo("Student Record", msg)
            return

    messagebox.showerror("Not found", "No student found with that name/number.")


def show_highest_total():
    """Menu 3: Show student with highest total score (percentage)."""
    if not students:
        load_students_from_file()
    if not students:
        return

    best = max(students, key=lambda s: s["percent"])
    msg = (
        f"Highest overall mark\n\n"
        f"Name: {best['name']}\n"
        f"Student Number: {best['id']}\n"
        f"Total coursework mark: {best['cw_total']} / 60\n"
        f"Exam mark: {best['exam']} / 100\n"
        f"Overall percentage: {best['percent']}%\n"
        f"Grade: {best['grade']}"
    )
    messagebox.showinfo("Highest Overall", msg)


def show_lowest_total():
    """Menu 4: Show student with lowest total score (percentage)."""
    if not students:
        load_students_from_file()
    if not students:
        return

    worst = min(students, key=lambda s: s["percent"])
    msg = (
        f"Lowest overall mark\n\n"
        f"Name: {worst['name']}\n"
        f"Student Number: {worst['id']}\n"
        f"Total coursework mark: {worst['cw_total']} / 60\n"
        f"Exam mark: {worst['exam']} / 100\n"
        f"Overall percentage: {worst['percent']}%\n"
        f"Grade: {worst['grade']}"
    )
    messagebox.showinfo("Lowest Overall", msg)


def sort_records():
    """Menu 5: Sort student records by percentage ascending."""
    if not students:
        load_students_from_file()
    students.sort(key=lambda s: s["percent"])
    refresh_tree()


# ================== MENU BAR ==================
menubar = tk.Menu(root)
root.config(menu=menubar)

marks_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Student Menu", menu=marks_menu)

marks_menu.add_command(label="1. View all records", command=view_all_records)
marks_menu.add_command(label="2. View individual record", command=view_individual_record)
marks_menu.add_command(label="3. Show highest total", command=show_highest_total)
marks_menu.add_command(label="4. Show lowest total", command=show_lowest_total)
marks_menu.add_separator()
marks_menu.add_command(label="5. Sort by percentage (asc)", command=sort_records)
marks_menu.add_command(label="6. Add record", command=add_record)
marks_menu.add_command(label="7. Delete record", command=delete_one)
marks_menu.add_command(label="8. Update record", command=update_record)

# ================== BUTTONS (your original layout) ==================
btn_frame = tk.Frame(
    detail_frame,
    bg="lightgray",
    bd=0,
    relief=tk.GROOVE
)
btn_frame.place(x=40, y=400, width=310, height=130)

# Add Button
add_btn = tk.Button(
    btn_frame,
    bg="teal",
    foreground="white",
    text="Add",
    bd=2,
    font=("Arial", 13), width=15,
    command=add_record
)
add_btn.grid(row=0, column=0, padx=2, pady=2)

# Update Button (loads selected record into entries)
update_btn = tk.Button(
    btn_frame,
    bg="teal",
    foreground="white",
    text="Select",
    bd=2,
    font=("Arial", 13), width=15,
    command=select_record
)
update_btn.grid(row=0, column=1, padx=2, pady=2)

# "Calculate" – just view all & summary
print_btn = tk.Button(
    btn_frame,
    bg="teal",
    foreground="white",
    text="View All + Summary",
    bd=2,
    font=("Arial", 13), width=15,
    command=view_all_records
)
print_btn.grid(row=1, column=0, padx=2, pady=2)

# Save Button (update)
cal_btn = tk.Button(
    btn_frame,
    bg="teal",
    foreground="white",
    text="Save Update",
    bd=2,
    font=("Arial", 13), width=15,
    command=update_record
)
cal_btn.grid(row=1, column=1, padx=2, pady=2)

# Delete Button
delete_btn = tk.Button(
    btn_frame,
    bg="teal",
    foreground="white",
    text="Delete",
    bd=2,
    font=("Arial", 13), width=15,
    command=delete_one
)
delete_btn.grid(row=2, column=1, padx=2, pady=2)

# ================== START ==================
load_students_from_file()
root.mainloop()
