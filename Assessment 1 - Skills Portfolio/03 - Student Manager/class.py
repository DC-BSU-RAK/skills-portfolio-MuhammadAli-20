from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog


class StudentManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Manager")
        self.root.geometry("1200x600")
        self.root.configure(bg="#e7eef7")

        # list to store all student records
        self.students = []

        # ====================== MAIN LAYOUT ==========================
        main_frame = tk.Frame(root, bg="#e7eef7")
        main_frame.pack(fill="both", expand=True)

        # configure grid for centering
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=3)
        main_frame.rowconfigure(0, weight=1)

        # ====================== LEFT — ENTRY PANEL =====================
        left_frame = tk.Frame(main_frame, bg="white", bd=2, relief="groove")
        left_frame.grid(row=0, column=0, padx=40, pady=40, sticky="ns")

        # Title bar
        title_bar = tk.Frame(left_frame, bg="#4a90e2", height=50)
        title_bar.pack(fill="x")

        tk.Label(title_bar, text="STUDENT ENTRY PANEL",
                 font=("Arial", 16, "bold"), bg="#4a90e2", fg="white").pack(pady=5)

        # Entry form container
        form_frame = tk.Frame(left_frame, bg="white")
        form_frame.pack(padx=20, pady=20)

        def add_label(text, row):
            tk.Label(form_frame, text=text, bg="white", font=("Arial", 12)).grid(row=row, column=0, sticky="w", pady=10)

        def add_entry(row):
            entry = tk.Entry(form_frame, width=20, font=("Arial", 12))
            entry.grid(row=row, column=1, pady=10)
            return entry

        add_label("Student No", 0)
        self.id_entry = add_entry(0)

        add_label("Name", 1)
        self.name_entry = add_entry(1)

        add_label("Coursework 1", 2)
        self.c1_entry = add_entry(2)

        add_label("Coursework 2", 3)
        self.c2_entry = add_entry(3)

        add_label("Coursework 3", 4)
        self.c3_entry = add_entry(4)

        add_label("Exam Mark", 5)
        self.exam_entry = add_entry(5)

        # ====================== RIGHT — STUDENT TABLE ====================
        right_frame = tk.Frame(main_frame, bg="#e7eef7")
        right_frame.grid(row=0, column=1, padx=20, pady=40, sticky="nsew")

        columns = ("id", "name", "c1", "c2", "c3", "exam", "percent", "grade")
        self.tree = ttk.Treeview(right_frame, columns=columns, show="headings")

        headings = {
            "id": "Student No",
            "name": "Name",
            "c1": "C1",
            "c2": "C2",
            "c3": "C3",
            "exam": "Exam",
            "percent": "%",
            "grade": "Grade"
        }

        for col, txt in headings.items():
            self.tree.heading(col, text=txt)
            self.tree.column(col, width=100, anchor="center")

        self.tree.pack(fill="both", expand=True)

        # ====================== MENU BAR ==============================
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

        # load studentMarks.txt on start
        self.load_from_file()

    # ====================== FILE HANDLING =============================

    def load_from_file(self):
        self.students.clear()
        try:
            with open("studentMarks.txt", "r") as f:
                lines = f.readlines()[1:]  # skip the first line
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

    # =================== GRADE CALCULATION ============================

    def get_grade(self, percent):
        if percent >= 70: return "A"
        if percent >= 60: return "B"
        if percent >= 50: return "C"
        if percent >= 40: return "D"
        return "F"

    # ========================== TREE UPDATE ===========================

    def update_tree(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        for s in self.students:
            self.tree.insert("", tk.END,
                             values=(s["id"], s["name"], s["c1"], s["c2"], s["c3"],
                                     s["exam"], s["percent"], s["grade"]))

    # ========================== ADD STUDENT ===========================

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
            messagebox.showerror("Error", "Student No & Name are required.")
            return

        # prevent duplicate ID
        for s in self.students:
            if s["id"] == sid:
                messagebox.showerror("Error", "Student ID already exists.")
                return

        percent = round(((c1 + c2 + c3 + exam) / 160) * 100, 2)
        grade = self.get_grade(percent)

        self.students.append({
            "id": sid, "name": name,
            "c1": c1, "c2": c2, "c3": c3,
            "exam": exam, "percent": percent, "grade": grade
        })

        self.save_to_file()
        self.update_tree()

    # ========================== DELETE ================================

    def delete_student(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Select a student to delete")
            return

        sid = self.tree.item(selected[0])["values"][0]
        self.students = [s for s in self.students if s["id"] != sid]

        self.save_to_file()
        self.update_tree()

    # ========================= MENU FUNCTIONS =========================

    def view_all(self):
        self.update_tree()
        avg = sum(s["percent"] for s in self.students) / len(self.students)
        messagebox.showinfo("Summary", f"Total students: {len(self.students)}\nAverage %: {avg:.2f}%")

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
        messagebox.showinfo("Highest Overall",
                            f"{best['name']} ({best['percent']}%)\nCW: {cw}/60\nExam: {best['exam']}/100")

    def show_lowest(self):
        worst = min(self.students, key=lambda s: s["percent"])
        cw = worst["c1"] + worst["c2"] + worst["c3"]
        messagebox.showinfo("Lowest Overall",
                            f"{worst['name']} ({worst['percent']}%)\nCW: {cw}/60\nExam: {worst['exam']}/100")

    def sort_records(self):
        self.students.sort(key=lambda s: s["percent"])
        self.update_tree()

    # ========================== UPDATE STUDENT ========================

    def update_student_prompt(self):
        sid = simpledialog.askstring("Update", "Enter student number:")
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

                save_btn = tk.Button(self.root, text="Save Update", bg="#4a90e2",
                                     fg="white", font=("Arial", 12), command=self.apply_update)
                save_btn.place(x=50, y=550)

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

        self.save_to_file()
        self.update_tree()

        messagebox.showinfo("Success", "Record updated successfully.")


# =========================== RUN APP ================================

if __name__ == "__main__":
    root = Tk()
    app = StudentManagementSystem(root)
    root.mainloop()
