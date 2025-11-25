# from tkinter import *
# import tkinter as tk
# from tkinter import ttk, messagebox

# class StudentManagementSystem:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Student Manager")
#         self.root.geometry("600x400")

#         # Student data list
#         self.students = []

#         # Input Frame
#         frame = tk.Frame(root)
#         frame.pack(pady = 10)

#         tk.Label(frame, text = "Student ID").grid(row=0, column=0, padx=5, pady=5)
#         self.id_entry = tk.Entry(frame)
#         self.id_entry.grid(row=0, column=1, padx=5, pady=5)

#         tk.Label(frame, text = "Name").grid(row=0, column=2, padx=5, pady=5)
#         self.name_entry = tk.Entry(frame)
#         self.name_entry.grid(row=0, column=3, padx=5, pady=5)

#         tk.Label(frame, text = "Age").grid(row=1, column=0, padx=5, pady=5)
#         self.age_entry = tk.Entry(frame)
#         self.age_entry.grid(row=1, column=1, padx=5, pady=5)

#         tk.Label(frame, text = "Class").grid(row=1, column=0, padx=5, pady=5)
#         self.class_entry = tk.Entry(frame)
#         self.class_entry.grid(row=1, column=3, padx=5, pady=5)

#         add_btn = tk.Button(frame, text = "Add Student", command=self.add_student)
#         add_btn.grid(row=2, column=1, columnspan=2, pady=10)

#         # Treeview to show students
#         columns = ("id", "name", "age", "class")
#         self.tree = ttk.Treeview(root, columns=columns, show = "headings")
#         self.tree.heading("id", text = "Student ID")
#         self.tree.heading("id", text = "Name")
#         self.tree.heading("id", text = "Age")
#         self.tree.heading("id", text = "Class")
#         self.tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

#         # Delete button
#         del_btn = tk.Button(root, text = "Delete Selected", command=self.delete_student)
#         del_btn.pack(pady=5)

#     def add_student(self):
#         sid = self.id_entry.get().strip()
#         name = self.name_entry.get().strip()
#         age = self.age_entry.get().strip()
#         sclass = self.class_entry.get().strip()

#         if not sid or not name or not age or not sclass:
#             messagebox.showerror("Error", "All fields are required!")
#             return
        
#         if not age.isdigit():
#             messagebox.showerror("Error", "Age must be a number")
#             return
        
#         for student in self.students:
#             if student["id"] == sid:
#                 messagebox.showerror("Error", "Student ID already exists!")
#                 return
            
#         student = {"id": sid, "name": name, "age": int(age), "class": sclass}
#         self.students.append(student)
#         self.update_tree()

#         self.id_entry.delete(0, tk.END)
#         self.name_entry.delete(0, tk.END)
#         self.age_entry.delete(0, tk.END)
#         self.class_entry.delete(0, tk.END)

#     def update_tree(self):
#         for row in self.tree.get_children():
#             self.tree.delete(row)

#         for student in self.students:
#             self.tree.insert("", tk.END, values=(student["id"], student["name"], student["age"], student["class"]))

#     def delete_student(self):
#         selected = self.tree.selection()
#         if not selected:
#             messagebox.showwarning("Warning", "Select a student to delete")
#             return
        
#         sid = self.tree.item(selected[0])["values"][0]
#         self.students = [s for s in self.students if s["id"] !=sid]
#         self.update_tree()


# if __name__ == "__main__":
#     root = Tk()
#     app = StudentManagementSystem(root)
#     root.mainloop()

from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog


class StudentManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Manager")
        self.root.geometry("820x480")

        # list of all student dicts
        self.students = []

        # =========================================================
        #                      INPUT FRAME
        # =========================================================
        frame = tk.Frame(root)
        frame.pack(pady=10)

        tk.Label(frame, text="Student No").grid(row=0, column=0, padx=5, pady=5)
        self.id_entry = tk.Entry(frame)
        self.id_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame, text="Name").grid(row=0, column=2, padx=5, pady=5)
        self.name_entry = tk.Entry(frame)
        self.name_entry.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(frame, text="Coursework 1").grid(row=1, column=0, padx=5, pady=5)
        self.c1_entry = tk.Entry(frame)
        self.c1_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame, text="Coursework 2").grid(row=1, column=2, padx=5, pady=5)
        self.c2_entry = tk.Entry(frame)
        self.c2_entry.grid(row=1, column=3, padx=5, pady=5)

        tk.Label(frame, text="Coursework 3").grid(row=2, column=0, padx=5, pady=5)
        self.c3_entry = tk.Entry(frame)
        self.c3_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(frame, text="Exam Mark").grid(row=2, column=2, padx=5, pady=5)
        self.exam_entry = tk.Entry(frame)
        self.exam_entry.grid(row=2, column=3, padx=5, pady=5)

        add_btn = tk.Button(frame, text="Add Student", command=self.add_student)
        add_btn.grid(row=3, column=1, columnspan=2, pady=10)

        # =========================================================
        #                       TREEVIEW
        # =========================================================
        columns = ("id", "name", "c1", "c2", "c3", "exam", "percent", "grade")
        self.tree = ttk.Treeview(root, columns=columns, show="headings")

        self.tree.heading("id", text="Student No")
        self.tree.heading("name", text="Name")
        self.tree.heading("c1", text="C1")
        self.tree.heading("c2", text="C2")
        self.tree.heading("c3", text="C3")
        self.tree.heading("exam", text="Exam")
        self.tree.heading("percent", text="%")
        self.tree.heading("grade", text="Grade")

        for col in columns:
            self.tree.column(col, width=90)

        self.tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        del_btn = tk.Button(root, text="Delete Selected", command=self.delete_student)
        del_btn.pack(pady=5)

        # =========================================================
        #                        MENU BAR
        # =========================================================
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Menu", menu=menu)

        menu.add_command(label="1. View All Records", command=self.view_all)
        menu.add_command(label="2. View Individual", command=self.view_individual)
        menu.add_command(label="3. Highest Total", command=self.show_highest)
        menu.add_command(label="4. Lowest Total", command=self.show_lowest)
        menu.add_separator()
        menu.add_command(label="5. Sort Records", command=self.sort_records)
        menu.add_command(label="6. Add Student", command=self.add_student)
        menu.add_command(label="7. Delete Student", command=self.delete_student)
        menu.add_command(label="8. Update Student", command=self.update_student_prompt)

        # load file on start
        self.load_from_file()

    # =========================================================
    #                    FILE HANDLING
    # =========================================================
    def load_from_file(self):
        self.students.clear()
        try:
            with open("studentMarks.txt", "r") as f:
                lines = f.readlines()[1:]  # skip first line
                for line in lines:
                    sid, name, c1, c2, c3, exam = line.strip().split(",")
                    c1, c2, c3, exam = int(c1), int(c2), int(c3), int(exam)

                    percent = round(((c1 + c2 + c3 + exam) / 160) * 100, 2)
                    grade = self.get_grade(percent)

                    self.students.append({
                        "id": sid,
                        "name": name,
                        "c1": c1,
                        "c2": c2,
                        "c3": c3,
                        "exam": exam,
                        "percent": percent,
                        "grade": grade
                    })
        except FileNotFoundError:
            messagebox.showerror("Error", "studentMarks.txt not found!")

        self.update_tree()

    def save_to_file(self):
        with open("studentMarks.txt", "w") as f:
            f.write(str(len(self.students)) + "\n")
            for s in self.students:
                f.write(f"{s['id']},{s['name']},{s['c1']},{s['c2']},{s['c3']},{s['exam']}\n")

    # =========================================================
    #                    CORE LOGIC
    # =========================================================
    def get_grade(self, percent):
        if percent >= 70: return "A"
        if percent >= 60: return "B"
        if percent >= 50: return "C"
        if percent >= 40: return "D"
        return "F"

    def clear_entries(self):
        self.id_entry.delete(0, END)
        self.name_entry.delete(0, END)
        self.c1_entry.delete(0, END)
        self.c2_entry.delete(0, END)
        self.c3_entry.delete(0, END)
        self.exam_entry.delete(0, END)

    def update_tree(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        for s in self.students:
            self.tree.insert("", tk.END,
                             values=(s["id"], s["name"], s["c1"], s["c2"], s["c3"],
                                     s["exam"], s["percent"], s["grade"]))

    # =========================================================
    #                      ADD STUDENT
    # =========================================================
    def add_student(self):
        sid = self.id_entry.get().strip()
        name = self.name_entry.get().strip()

        try:
            c1 = int(self.c1_entry.get())
            c2 = int(self.c2_entry.get())
            c3 = int(self.c3_entry.get())
            exam = int(self.exam_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Marks must be integers.")
            return

        if not sid or not name:
            messagebox.showerror("Error", "Student No & Name required.")
            return

        for s in self.students:
            if s["id"] == sid:
                messagebox.showerror("Error", "Student ID already exists.")
                return

        percent = round(((c1 + c2 + c3 + exam) / 160) * 100, 2)
        grade = self.get_grade(percent)

        self.students.append({
            "id": sid,
            "name": name,
            "c1": c1,
            "c2": c2,
            "c3": c3,
            "exam": exam,
            "percent": percent,
            "grade": grade
        })

        self.save_to_file()
        self.update_tree()
        self.clear_entries()

    # =========================================================
    #                     DELETE STUDENT
    # =========================================================
    def delete_student(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Select a student to delete")
            return

        sid = self.tree.item(selected[0])["values"][0]
        self.students = [s for s in self.students if s["id"] != sid]

        self.save_to_file()
        self.update_tree()

    # =========================================================
    #                     MENU FUNCTIONS
    # =========================================================
    def view_all(self):
        self.update_tree()
        avg = sum(s["percent"] for s in self.students) / len(self.students)

        messagebox.showinfo("Summary",
                            f"Total students: {len(self.students)}\n"
                            f"Average percentage: {avg:.2f}%")

    def view_individual(self):
        q = simpledialog.askstring("Search", "Enter student number or name:")
        if not q:
            return

        q = q.lower()
        for s in self.students:
            if s["id"] == q or q in s["name"].lower():
                cw = s["c1"] + s["c2"] + s["c3"]
                msg = (
                    f"Name: {s['name']}\n"
                    f"Student Number: {s['id']}\n"
                    f"Total coursework: {cw} / 60\n"
                    f"Exam: {s['exam']} / 100\n"
                    f"Percent: {s['percent']}%\n"
                    f"Grade: {s['grade']}"
                )
                messagebox.showinfo("Record Found", msg)
                return

        messagebox.showerror("Not found", "Student not found.")

    def show_highest(self):
        best = max(self.students, key=lambda s: s["percent"])
        cw = best["c1"] + best["c2"] + best["c3"]
        msg = (
            f"Highest Overall Mark\n\n"
            f"Name: {best['name']}\n"
            f"Student Number: {best['id']}\n"
            f"Coursework Total: {cw} / 60\n"
            f"Exam: {best['exam']} / 100\n"
            f"Percent: {best['percent']}%\n"
            f"Grade: {best['grade']}"
        )
        messagebox.showinfo("Highest Overall", msg)

    def show_lowest(self):
        worst = min(self.students, key=lambda s: s["percent"])
        cw = worst["c1"] + worst["c2"] + worst["c3"]
        msg = (
            f"Lowest Overall Mark\n\n"
            f"Name: {worst['name']}\n"
            f"Student Number: {worst['id']}\n"
            f"Coursework Total: {cw} / 60\n"
            f"Exam: {worst['exam']} / 100\n"
            f"Percent: {worst['percent']}%\n"
            f"Grade: {worst['grade']}"
        )
        messagebox.showinfo("Lowest Overall", msg)

    def sort_records(self):
        self.students.sort(key=lambda s: s["percent"])
        self.update_tree()

    # =========================================================
    #                     UPDATE STUDENT
    # =========================================================
    def update_student_prompt(self):
        sid = simpledialog.askstring("Update", "Enter student number to edit:")
        if not sid:
            return

        for s in self.students:
            if s["id"] == sid:
                self.id_entry.delete(0, END)
                self.name_entry.delete(0, END)
                self.c1_entry.delete(0, END)
                self.c2_entry.delete(0, END)
                self.c3_entry.delete(0, END)
                self.exam_entry.delete(0, END)

                self.id_entry.insert(0, s["id"])
                self.name_entry.insert(0, s["name"])
                self.c1_entry.insert(0, s["c1"])
                self.c2_entry.insert(0, s["c2"])
                self.c3_entry.insert(0, s["c3"])
                self.exam_entry.insert(0, s["exam"])

                # After loading, replace Add Button with Save Button
                save_btn = tk.Button(self.root, text="Save Update",
                                     command=self.apply_update)
                save_btn.pack(pady=5)

                return

        messagebox.showerror("Error", "Student not found.")

    def apply_update(self):
        sid = self.id_entry.get().strip()
        name = self.name_entry.get().strip()

        try:
            c1 = int(self.c1_entry.get())
            c2 = int(self.c2_entry.get())
            c3 = int(self.c3_entry.get())
            exam = int(self.exam_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Marks must be integers.")
            return

        percent = round(((c1 + c2 + c3 + exam) / 160) * 100, 2)
        grade = self.get_grade(percent)

        for s in self.students:
            if s["id"] == sid:
                s["name"] = name
                s["c1"] = c1
                s["c2"] = c2
                s["c3"] = c3
                s["exam"] = exam
                s["percent"] = percent
                s["grade"] = grade
                break

        self.save_to_file()
        self.update_tree()
        self.clear_entries()
        messagebox.showinfo("Success", "Record updated successfully.")


# =========================================================
#                     RUN APP
# =========================================================
if __name__ == "__main__":
    root = Tk()
    app = StudentManagementSystem(root)
    root.mainloop()

