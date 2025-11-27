from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

class StudentManagementSystem:
    def __init__(self, root):

        # basic window setup
        self.root = root
        self.root.title("Student Manager")
        self.root.geometry("1200x600")
        self.root.configure(bg = "#061A40")

        # in-memory list to store student records
        self.students = []

        # main layout frame
        main_frame = tk.Frame(root, bg = "#061A40")
        main_frame.pack(fill = "both", expand = True)

        # layout configuration
        main_frame.columnconfigure(0, weight = 1)
        main_frame.columnconfigure(1, weight = 3)
        main_frame.rowconfigure(0, weight = 1)

        # left panel (entry form)
        left_frame = tk.Frame(main_frame, bg = "white", bd = 2, relief = "groove")
        left_frame.grid(row = 0, column = 0, padx = 40, pady = 40, sticky = "ns")

        # header bar
        title_bar = tk.Frame(left_frame, bg = "#4a90e2", height = 50)
        title_bar.pack(fill = "x")

        label = Label(title_bar, text = "STUDENT INFORMATION PANEL", font = ("Arial", 16, "bold"), bg = "#4a90e2", fg = "white")
        label.pack(pady = 5)

        # container for input fields
        form_frame = tk.Frame(left_frame, bg = "white")
        form_frame.pack(padx = 20, pady = 20)

        # helper functions
        def add_label(text, row):
            label = Label(form_frame, text = text, bg = "white", font = ("Arial", 12, "bold"))
            label.grid(row = row, column = 0, sticky = "w", pady = 10)

        def add_entry(row):
            entry = tk.Entry(form_frame, width = 20, font = ("Arial", 12))
            entry.grid(row = row, column = 1, pady = 10)
            return entry

        # input fields
        add_label("Student No.", 0)
        self.id_entry = add_entry(0)

        add_label("Name", 1)
        self.name_entry = add_entry(1)

        add_label("Coursework 1 Marks", 2)
        self.c1_entry = add_entry(2)

        add_label("Coursework 2 Marks", 3)
        self.c2_entry = add_entry(3)

        add_label("Coursework 3 Marks", 4)
        self.c3_entry = add_entry(4)

        add_label("Exam Mark", 5)
        self.exam_entry = add_entry(5)

        # reset button
        reset_btn = tk.Button(left_frame, text = "Reset", bg = "#4a90e2", fg = "white", font = ("Arial", 12, "bold"), command = self.reset_fields)
        reset_btn.pack(pady = 20)

        # table section
        right_frame = tk.Frame(main_frame, bg = "#061A40")
        right_frame.grid(row = 0, column = 1, padx = 20, pady = 40, sticky = "nsew")

        # table columns
        columns = ("id", "name", "c1", "c2", "c3", "cw_total", "exam", "percent", "grade")
        self.tree = ttk.Treeview(right_frame, columns = columns, show = "headings")

        # table styles
        style = ttk.Style()
        style.theme_use("default")

        style.configure("Treeview.Heading", background = "#4a90e2", foreground = "white", font = ("Arial", 12, "bold"))

        style.configure("Treeview", background = "white", foreground = "black", rowheight = 28, font = ("Arial", 11, "bold"))

        style.map("Treeview", background = [("selected", "#a3c1f7")])

        # header names
        headings = {
            "id": "Student No.",
            "name": "Name",
            "c1": "C1",
            "c2": "C2",
            "c3": "C3",
            "cw_total": "CW Total",
            "exam": "Exam",
            "percent": "%",
            "grade": "Grade"
        }

        # configure columns
        for col, txt in headings.items():
            self.tree.heading(col, text = txt)

            if col == "id":
                self.tree.column(col, width = 90, anchor = "center")
            elif col == "name":
                self.tree.column(col, width = 220, anchor = "center")
            elif col in ("c1", "c2", "c3"):
                self.tree.column(col, width = 60, anchor = "center")
            elif col == "cw_total":
                self.tree.column(col, width = 90, anchor = "center")
            elif col == "exam":
                self.tree.column(col, width = 80, anchor = "center")
            elif col == "percent":
                self.tree.column(col, width = 70, anchor = "center")
            elif col == "grade":
                self.tree.column(col, width = 80, anchor = "center")

        # alternating row colors
        self.tree.tag_configure("blue", background = "#cfe2ff")
        self.tree.tag_configure("white", background = "white")

        self.tree.pack(fill = "both", expand = True)

        # top menu bar
        menubar = tk.Menu(self.root)
        self.root.config(menu = menubar)

        menu = tk.Menu(menubar, tearoff = 0)
        menubar.add_cascade(label = "Menu", menu = menu)

        # menu options
        menu.add_command(label = "1. View All Records", command = self.view_all)
        menu.add_command(label = "2. View Individual", command = self.view_individual)
        menu.add_command(label = "3. Highest Total", command = self.show_highest)
        menu.add_command(label = "4. Lowest Total", command = self.show_lowest)
        menu.add_separator()
        menu.add_command(label = "5. Sort Records", command = self.sort_records)
        menu.add_command(label = "6. Add Student", command = self.add_student)
        menu.add_command(label = "7. Delete Student", command = self.delete_student)
        menu.add_command(label = "8. Update Student", command = self.update_student_prompt)

        # load existing file
        self.load_from_file()

    # clear fields
    def reset_fields(self):
        self.id_entry.delete(0, END)
        self.name_entry.delete(0, END)
        self.c1_entry.delete(0, END)
        self.c2_entry.delete(0, END)
        self.c3_entry.delete(0, END)
        self.exam_entry.delete(0, END)

    # load from file
    def load_from_file(self):
        self.students.clear()
        try:
            with open("studentMarks.txt", "r", encoding = "utf-8") as f:
                lines = [line.strip() for line in f if line.strip()]

                # skip first line (count)
                for line in lines[1:]:
                    student_id, name, c1, c2, c3, exam = line.split(",")

                    # convert marks
                    c1, c2, c3, exam = int(c1), int(c2), int(c3), int(exam)
                    cw_total = c1 + c2 + c3
                    percent = round(((cw_total + exam) / 160) * 100, 2)
                    grade = self.get_grade(percent)

                    self.students.append({
                        "id": student_id, "name": name,
                        "c1": c1, "c2": c2, "c3": c3,
                        "cw_total": cw_total,
                        "exam": exam,
                        "percent": percent,
                        "grade": grade
                    })
        except:
            messagebox.showerror("Error", "studentMarks.txt not found!")

        self.update_tree()

    # writes updated list back to the file
    def save_to_file(self):
        with open("studentMarks.txt", "w", encoding = "utf-8") as f:
            f.write(str(len(self.students)) + "\n")
            for student_record in self.students:
                f.write(
                    f"{student_record['id']},{student_record['name']},"
                    f"{student_record['c1']},{student_record['c2']},"
                    f"{student_record['c3']},{student_record['exam']}\n"
                )

    # grading logic
    def get_grade(self, percent):
        if percent >= 70:
            return "A"
        if percent >= 60:
            return "B"
        if percent >= 50:
            return "C"
        if percent >= 40:
            return "D"
        return "F"

    # refresh table display
    def update_tree(self):
        self.tree.delete(*self.tree.get_children())

        for index, student_record in enumerate(self.students):
            tag = "blue" if index % 2 == 0 else "white"
            self.tree.insert(
                "",
                tk.END,
                values = (
                    student_record["id"], student_record["name"],
                    student_record["c1"], student_record["c2"], student_record["c3"],
                    student_record["cw_total"], student_record["exam"],
                    student_record["percent"], student_record["grade"]
                ),
                tags = (tag,)
            )

    # adds a new student to the list
    def add_student(self):
        student_id = self.id_entry.get().strip()
        name = self.name_entry.get().strip()

        try:
            c1 = int(self.c1_entry.get())
            c2 = int(self.c2_entry.get())
            c3 = int(self.c3_entry.get())
            exam = int(self.exam_entry.get())
        except:
            messagebox.showerror("Error", "Marks must be integers.")
            return

        if not student_id or not name:
            messagebox.showerror("Error", "Student No & Name required.")
            return

        for student_record in self.students:
            if student_record["id"] == student_id:
                messagebox.showerror("Error", "Student ID already exists.")
                return

        cw_total = c1 + c2 + c3
        percent = round(((cw_total + exam) / 160) * 100, 2)
        grade = self.get_grade(percent)

        self.students.append({
            "id": student_id, "name": name,
            "c1": c1, "c2": c2, "c3": c3,
            "cw_total": cw_total,
            "exam": exam,
            "percent": percent,
            "grade": grade
        })

        self.save_to_file()
        self.load_from_file()
        self.reset_fields()

    # delete selected record
    def delete_student(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Select a student to delete")
            return

        student_id = self.tree.item(selected[0], "values")[0]
        self.students = [
            student_record for student_record in self.students
            if student_record["id"] != student_id
        ]

        self.save_to_file()
        self.load_from_file()

        messagebox.showinfo("Success", "Student deleted successfully.")

    # display all students
    def view_all(self):
        self.update_tree()
        if not self.students:
            messagebox.showinfo("Summary", "No students available.")
            return

        avg = sum(student_record["percent"] for student_record in self.students) / len(self.students)
        messagebox.showinfo(
            "Summary",
            f"Total students: {len(self.students)}\nAverage %: {avg:.2f}%"
        )

    # search by student ID or name
    def view_individual(self):
        search_query = simpledialog.askstring("Search", "Enter student number or name:")
        if not search_query:
            return

        search_query = search_query.lower()

        for student_record in self.students:
            if student_record["id"] == search_query or search_query in student_record["name"].lower():
                self.tree.delete(*self.tree.get_children())
                self.tree.insert("", tk.END, values = (
                    student_record["id"], student_record["name"],
                    student_record["c1"], student_record["c2"], student_record["c3"],
                    student_record["cw_total"], student_record["exam"],
                    student_record["percent"], student_record["grade"]
                ))
                return

        messagebox.showerror("Not found", "Student not found.")

    # show student with highest % score
    def show_highest(self):
        if not self.students:
            messagebox.showinfo("Info", "No students to evaluate.")
            return

        highest_student = max(self.students, key = lambda student: student["percent"])
        self.tree.delete(*self.tree.get_children())
        self.tree.insert("", tk.END, values = (
            highest_student["id"], highest_student["name"],
            highest_student["c1"], highest_student["c2"], highest_student["c3"],
            highest_student["cw_total"], highest_student["exam"],
            highest_student["percent"], highest_student["grade"]
        ))

    # show student with lowest % score
    def show_lowest(self):
        if not self.students:
            messagebox.showinfo("Info", "No students to evaluate.")
            return

        lowest_student = min(self.students, key = lambda student: student["percent"])
        self.tree.delete(*self.tree.get_children())
        self.tree.insert("", tk.END, values = (
            lowest_student["id"], lowest_student["name"],
            lowest_student["c1"], lowest_student["c2"], lowest_student["c3"],
            lowest_student["cw_total"], lowest_student["exam"],
            lowest_student["percent"], lowest_student["grade"]
        ))

    # sorts students by percentage
    def sort_records(self):
        choice = simpledialog.askstring("Sort Records", "A = Ascending\nD = Descending")
        if not choice:
            return

        if choice.lower() == "a":
            self.students.sort(key = lambda student_record: student_record["percent"])
        elif choice.lower() == "d":
            self.students.sort(key = lambda student_record: student_record["percent"], reverse = True)
        else:
            messagebox.showerror("Error", "Enter A or D")
            return

        self.update_tree()

    # prepares form for editing an existing record
    def update_student_prompt(self):
        student_id = simpledialog.askstring("Update", "Enter student number:")
        if not student_id:
            return

        for student_record in self.students:
            if student_record["id"] == student_id:
                self.reset_fields()

                self.id_entry.insert(0, student_record["id"])
                self.name_entry.insert(0, student_record["name"])
                self.c1_entry.insert(0, student_record["c1"])
                self.c2_entry.insert(0, student_record["c2"])
                self.c3_entry.insert(0, student_record["c3"])
                self.exam_entry.insert(0, student_record["exam"])

                save_btn = tk.Button(
                    self.root,
                    text = "Save Update",
                    bg = "#4a90e2",
                    fg = "white",
                    font = ("Arial", 12),
                    command = self.apply_update
                )
                save_btn.place(x = 50, y = 550)
                return

        messagebox.showerror("Error", "Student not found.")

    # saves updated record
    def apply_update(self):
        student_id = self.id_entry.get().strip()

        try:
            c1 = int(self.c1_entry.get())
            c2 = int(self.c2_entry.get())
            c3 = int(self.c3_entry.get())
            exam = int(self.exam_entry.get())
        except:
            messagebox.showerror("Error", "Marks must be integers.")
            return

        cw_total = c1 + c2 + c3
        percent = round(((cw_total + exam) / 160) * 100, 2)
        grade = self.get_grade(percent)

        for student_record in self.students:
            if student_record["id"] == student_id:
                student_record["name"] = self.name_entry.get()
                student_record["c1"] = c1
                student_record["c2"] = c2
                student_record["c3"] = c3
                student_record["cw_total"] = cw_total
                student_record["exam"] = exam
                student_record["percent"] = percent
                student_record["grade"] = grade

        self.save_to_file()
        self.load_from_file()
        messagebox.showinfo("Success", "Record updated successfully.")

if __name__ == "__main__":
    root = Tk()
    app = StudentManagementSystem(root)
    root.mainloop()
