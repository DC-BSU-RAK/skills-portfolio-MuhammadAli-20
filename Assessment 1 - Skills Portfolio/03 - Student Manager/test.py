import tkinter as tk
from tkinter import messagebox, simpledialog, scrolledtext

# ----------------------- LOAD DATA -----------------------
def load_students():
    students = []
    with open("studentMarks.txt", "r") as file:
        lines = file.readlines()

        for line in lines[1:]:  # skip first line
            data = line.strip().split(",")

            number = data[0]
            name = data[1]
            c1, c2, c3 = int(data[2]), int(data[3]), int(data[4])
            exam = int(data[5])

            coursework_total = c1 + c2 + c3
            overall_total = coursework_total + exam
            percentage = round((overall_total / 160) * 100, 2)

            if percentage >= 70:
                grade = "A"
            elif percentage >= 60:
                grade = "B"
            elif percentage >= 50:
                grade = "C"
            elif percentage >= 40:
                grade = "D"
            else:
                grade = "F"

            students.append({
                "number": number,
                "name": name,
                "coursework_total": coursework_total,
                "exam": exam,
                "percentage": percentage,
                "grade": grade
            })
    return students


students = load_students()


# ----------------------- GUI FUNCTIONS -----------------------

def view_all_students():
    output.delete("1.0", tk.END)
    total_percentage = 0

    for s in students:
        output.insert(tk.END, f"Name: {s['name']}\n")
        output.insert(tk.END, f"Student Number: {s['number']}\n")
        output.insert(tk.END, f"Coursework Total: {s['coursework_total']}/60\n")
        output.insert(tk.END, f"Exam Mark: {s['exam']}/100\n")
        output.insert(tk.END, f"Overall Percentage: {s['percentage']}%\n")
        output.insert(tk.END, f"Grade: {s['grade']}\n")
        output.insert(tk.END, "----------------------------\n")

        total_percentage += s['percentage']

    avg = round(total_percentage / len(students), 2)
    output.insert(tk.END, f"\nTotal Students: {len(students)}\n")
    output.insert(tk.END, f"Class Average Percentage: {avg}%\n")


def view_individual():
    search = simpledialog.askstring("Find Student", "Enter student number or name:")

    if not search:
        return

    search = search.lower()
    output.delete("1.0", tk.END)

    for s in students:
        if search in s['name'].lower() or search == s['number']:
            output.insert(tk.END, f"Name: {s['name']}\n")
            output.insert(tk.END, f"Student Number: {s['number']}\n")
            output.insert(tk.END, f"Coursework Total: {s['coursework_total']}/60\n")
            output.insert(tk.END, f"Exam Mark: {s['exam']}/100\n")
            output.insert(tk.END, f"Overall Percentage: {s['percentage']}%\n")
            output.insert(tk.END, f"Grade: {s['grade']}\n")
            return

    messagebox.showerror("Not Found", "Student not found.")


def highest_score():
    highest = max(students, key=lambda s: s['percentage'])
    show_single_record(highest)


def lowest_score():
    lowest = min(students, key=lambda s: s['percentage'])
    show_single_record(lowest)


def show_single_record(s):
    output.delete("1.0", tk.END)
    output.insert(tk.END, f"Name: {s['name']}\n")
    output.insert(tk.END, f"Student Number: {s['number']}\n")
    output.insert(tk.END, f"Coursework Total: {s['coursework_total']}/60\n")
    output.insert(tk.END, f"Exam Mark: {s['exam']}/100\n")
    output.insert(tk.END, f"Overall Percentage: {s['percentage']}%\n")
    output.insert(tk.END, f"Grade: {s['grade']}\n")


# ----------------------- GUI SETUP -----------------------

root = tk.Tk()
root.title("Student Manager")
root.geometry("600x500")

title = tk.Label(root, text="Student Manager App", font=("Arial", 16, "bold"))
title.pack()

# Text area
output = scrolledtext.ScrolledText(root, width=70, height=20, font=("Arial", 11))
output.pack(pady=10)

# Buttons
frame = tk.Frame(root)
frame.pack()

tk.Button(frame, text="View All Students", width=20, command=view_all_students).grid(row=0, column=0, padx=5, pady=5)
tk.Button(frame, text="View Individual", width=20, command=view_individual).grid(row=0, column=1, padx=5, pady=5)
tk.Button(frame, text="Highest Score", width=20, command=highest_score).grid(row=1, column=0, padx=5, pady=5)
tk.Button(frame, text="Lowest Score", width=20, command=lowest_score).grid(row=1, column=1, padx=5, pady=5)

root.mainloop()
