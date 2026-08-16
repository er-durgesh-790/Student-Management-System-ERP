
import customtkinter as ctk
from tkinter import ttk, messagebox


class ExamModule:

    def __init__(self, parent, database):

        self.parent = parent
        self.database = database

        # ==========================
        # Colors
        # ==========================

        self.bg_color = "#F3F6FB"
        self.card_color = "#FFFFFF"

        self.primary = "#2563EB"
        self.primary_hover = "#1D4ED8"

        self.success = "#16A34A"
        self.success_hover = "#15803D"

        self.warning = "#F59E0B"
        self.warning_hover = "#D97706"

        self.danger = "#DC2626"
        self.danger_hover = "#B91C1C"

        self.gray = "#6B7280"
        self.dark = "#111827"

        # ==========================
        # Main Frame
        # ==========================

        self.main_frame = ctk.CTkFrame(
            parent,
            fg_color=self.bg_color,
            corner_radius=0
        )

        self.main_frame.pack(
            fill="both",
            expand=True
        )

        self.create_ui()

    # =========================================================
    # CREATE UI
    # =========================================================

    def create_ui(self):

        # ==========================
        # Header
        # ==========================

        header = ctk.CTkFrame(
            self.main_frame,
            fg_color=self.primary,
            corner_radius=0,
            height=80
        )

        header.pack(
            fill="x"
        )

        header.pack_propagate(False)

        ctk.CTkLabel(
            header,
            text="📝  Exam Management",
            font=("Segoe UI", 28, "bold"),
            text_color="white"
        ).pack(
            side="left",
            padx=30
        )

        ctk.CTkLabel(
            header,
            text="Manage examinations, schedules & marks",
            font=("Segoe UI", 13),
            text_color="#DBEAFE"
        ).pack(
            side="right",
            padx=30
        )

        # ==========================
        # Statistics Cards
        # ==========================

        stats_frame = ctk.CTkFrame(
            self.main_frame,
            fg_color="transparent"
        )

        stats_frame.pack(
            fill="x",
            padx=20,
            pady=(18, 8)
        )

        self.total_card = self.create_stat_card(
            stats_frame,
            "📚",
            "Total Exams",
            "0",
            self.primary
        )

        self.total_card.pack(
            side="left",
            fill="x",
            expand=True,
            padx=7
        )

        self.course_card = self.create_stat_card(
            stats_frame,
            "🎓",
            "Courses",
            "0",
            self.success
        )

        self.course_card.pack(
            side="left",
            fill="x",
            expand=True,
            padx=7
        )

        self.upcoming_card = self.create_stat_card(
            stats_frame,
            "📅",
            "Scheduled Exams",
            "0",
            self.warning
        )

        self.upcoming_card.pack(
            side="left",
            fill="x",
            expand=True,
            padx=7
        )

        # ==========================
        # Form Card
        # ==========================

        form_card = ctk.CTkFrame(
            self.main_frame,
            fg_color=self.card_color,
            corner_radius=15
        )

        form_card.pack(
            fill="x",
            padx=20,
            pady=10
        )

        ctk.CTkLabel(
            form_card,
            text="Exam Information",
            font=("Segoe UI", 19, "bold"),
            text_color=self.dark
        ).grid(
            row=0,
            column=0,
            columnspan=4,
            sticky="w",
            padx=25,
            pady=(18, 10)
        )

        # ==========================
        # Exam ID
        # ==========================

        ctk.CTkLabel(
            form_card,
            text="Exam ID",
            font=("Segoe UI", 13, "bold")
        ).grid(
            row=1,
            column=0,
            padx=20,
            pady=8,
            sticky="w"
        )

        self.exam_id = ctk.CTkEntry(
            form_card,
            width=220,
            height=40,
            corner_radius=8,
            placeholder_text="Enter Exam ID"
        )

        self.exam_id.grid(
            row=1,
            column=1,
            padx=10,
            pady=8
        )

        # ==========================
        # Exam Name
        # ==========================

        ctk.CTkLabel(
            form_card,
            text="Exam Name",
            font=("Segoe UI", 13, "bold")
        ).grid(
            row=1,
            column=2,
            padx=20,
            pady=8,
            sticky="w"
        )

        self.exam_name = ctk.CTkEntry(
            form_card,
            width=220,
            height=40,
            corner_radius=8,
            placeholder_text="Enter Exam Name"
        )

        self.exam_name.grid(
            row=1,
            column=3,
            padx=10,
            pady=8
        )

        # ==========================
        # Course
        # ==========================

        ctk.CTkLabel(
            form_card,
            text="Course",
            font=("Segoe UI", 13, "bold")
        ).grid(
            row=2,
            column=0,
            padx=20,
            pady=8,
            sticky="w"
        )

        self.course = ctk.CTkEntry(
            form_card,
            width=220,
            height=40,
            corner_radius=8,
            placeholder_text="e.g. B.Tech ECE"
        )

        self.course.grid(
            row=2,
            column=1,
            padx=10,
            pady=8
        )

        # ==========================
        # Semester
        # ==========================

        ctk.CTkLabel(
            form_card,
            text="Semester",
            font=("Segoe UI", 13, "bold")
        ).grid(
            row=2,
            column=2,
            padx=20,
            pady=8,
            sticky="w"
        )

        self.semester = ctk.CTkComboBox(
            form_card,
            width=220,
            height=40,
            corner_radius=8,
            values=[
                "1st Semester",
                "2nd Semester",
                "3rd Semester",
                "4th Semester",
                "5th Semester",
                "6th Semester",
                "7th Semester",
                "8th Semester"
            ]
        )

        self.semester.grid(
            row=2,
            column=3,
            padx=10,
            pady=8
        )

        self.semester.set("Select Semester")

        # ==========================
        # Exam Date
        # ==========================

        ctk.CTkLabel(
            form_card,
            text="Exam Date",
            font=("Segoe UI", 13, "bold")
        ).grid(
            row=3,
            column=0,
            padx=20,
            pady=8,
            sticky="w"
        )

        self.exam_date = ctk.CTkEntry(
            form_card,
            width=220,
            height=40,
            corner_radius=8,
            placeholder_text="DD-MM-YYYY"
        )

        self.exam_date.grid(
            row=3,
            column=1,
            padx=10,
            pady=8
        )

        # ==========================
        # Total Marks
        # ==========================

        ctk.CTkLabel(
            form_card,
            text="Total Marks",
            font=("Segoe UI", 13, "bold")
        ).grid(
            row=3,
            column=2,
            padx=20,
            pady=8,
            sticky="w"
        )

        self.total_marks = ctk.CTkEntry(
            form_card,
            width=220,
            height=40,
            corner_radius=8,
            placeholder_text="e.g. 100"
        )

        self.total_marks.grid(
            row=3,
            column=3,
            padx=10,
            pady=8
        )

        # ==========================
        # Buttons
        # ==========================

        button_frame = ctk.CTkFrame(
            form_card,
            fg_color="transparent"
        )

        button_frame.grid(
            row=4,
            column=0,
            columnspan=4,
            pady=(15, 20)
        )

        ctk.CTkButton(
            button_frame,
            text="➕  Add Exam",
            width=135,
            height=40,
            corner_radius=8,
            fg_color=self.success,
            hover_color=self.success_hover,
            font=("Segoe UI", 13, "bold"),
            command=self.add_exam
        ).pack(
            side="left",
            padx=6
        )

        ctk.CTkButton(
            button_frame,
            text="✏️  Update",
            width=135,
            height=40,
            corner_radius=8,
            fg_color=self.primary,
            hover_color=self.primary_hover,
            font=("Segoe UI", 13, "bold"),
            command=self.update_exam
        ).pack(
            side="left",
            padx=6
        )

        ctk.CTkButton(
            button_frame,
            text="🗑  Delete",
            width=135,
            height=40,
            corner_radius=8,
            fg_color=self.danger,
            hover_color=self.danger_hover,
            font=("Segoe UI", 13, "bold"),
            command=self.delete_exam
        ).pack(
            side="left",
            padx=6
        )

        ctk.CTkButton(
            button_frame,
            text="🔄  Clear",
            width=135,
            height=40,
            corner_radius=8,
            fg_color=self.gray,
            hover_color="#4B5563",
            font=("Segoe UI", 13, "bold"),
            command=self.clear_fields
        ).pack(
            side="left",
            padx=6
        )

        # ==========================
        # Search Card
        # ==========================

        search_card = ctk.CTkFrame(
            self.main_frame,
            fg_color=self.card_color,
            corner_radius=15
        )

        search_card.pack(
            fill="x",
            padx=20,
            pady=8
        )

        ctk.CTkLabel(
            search_card,
            text="🔎 Search Exams",
            font=("Segoe UI", 16, "bold"),
            text_color=self.dark
        ).pack(
            side="left",
            padx=(20, 10)
        )

        self.search_entry = ctk.CTkEntry(
            search_card,
            width=350,
            height=38,
            corner_radius=8,
            placeholder_text="Exam ID / Exam Name / Course"
        )

        self.search_entry.pack(
            side="left",
            padx=10,
            pady=12
        )

        ctk.CTkButton(
            search_card,
            text="Search",
            width=110,
            height=38,
            corner_radius=8,
            fg_color=self.primary,
            hover_color=self.primary_hover,
            command=self.search_exam
        ).pack(
            side="left",
            padx=5
        )

        ctk.CTkButton(
            search_card,
            text="Show All",
            width=110,
            height=38,
            corner_radius=8,
            fg_color=self.gray,
            hover_color="#4B5563",
            command=self.load_exams
        ).pack(
            side="left",
            padx=5
        )

        # ==========================
        # Table Card
        # ==========================

        table_card = ctk.CTkFrame(
            self.main_frame,
            fg_color=self.card_color,
            corner_radius=15
        )

        table_card.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(8, 15)
        )

        ctk.CTkLabel(
            table_card,
            text="📋 Exam Records",
            font=("Segoe UI", 17, "bold"),
            text_color=self.dark
        ).pack(
            anchor="w",
            padx=20,
            pady=(12, 5)
        )

        table_frame = ctk.CTkFrame(
            table_card,
            fg_color="transparent"
        )

        table_frame.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=10
        )

        # ==========================
        # Treeview Style
        # ==========================

        style = ttk.Style()

        try:
            style.theme_use("clam")
        except:
            pass

        style.configure(
            "Treeview",
            background="#FFFFFF",
            foreground="#111827",
            rowheight=34,
            fieldbackground="#FFFFFF",
            font=("Segoe UI", 11)
        )

        style.configure(
            "Treeview.Heading",
            background="#2563EB",
            foreground="white",
            font=("Segoe UI", 11, "bold"),
            relief="flat"
        )

        style.map(
            "Treeview",
            background=[
                ("selected", "#DBEAFE")
            ],
            foreground=[
                ("selected", "#111827")
            ]
        )

        columns = (
            "Exam ID",
            "Exam Name",
            "Course",
            "Semester",
            "Exam Date",
            "Total Marks"
        )

        self.exam_table = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings"
        )

        widths = {
            "Exam ID": 110,
            "Exam Name": 180,
            "Course": 150,
            "Semester": 130,
            "Exam Date": 130,
            "Total Marks": 120
        }

        for col in columns:

            self.exam_table.heading(
                col,
                text=col
            )

            self.exam_table.column(
                col,
                width=widths[col],
                anchor="center"
            )

        scrollbar = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=self.exam_table.yview
        )

        self.exam_table.configure(
            yscrollcommand=scrollbar.set
        )

        self.exam_table.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        # ==========================
        # Select Event
        # ==========================

        self.exam_table.bind(
            "<<TreeviewSelect>>",
            self.select_exam
        )

        # ==========================
        # Load Data
        # ==========================

        self.load_exams()

    # =========================================================
    # STAT CARD
    # =========================================================

    def create_stat_card(
        self,
        parent,
        icon,
        title,
        value,
        color
    ):

        card = ctk.CTkFrame(
            parent,
            fg_color=self.card_color,
            corner_radius=15,
            height=85
        )

        card.pack_propagate(False)

        ctk.CTkLabel(
            card,
            text=icon,
            font=("Segoe UI Emoji", 27)
        ).pack(
            side="left",
            padx=(18, 8)
        )

        info = ctk.CTkFrame(
            card,
            fg_color="transparent"
        )

        info.pack(
            side="left",
            fill="both",
            expand=True
        )

        ctk.CTkLabel(
            info,
            text=title,
            font=("Segoe UI", 11),
            text_color="gray"
        ).pack(
            anchor="w",
            pady=(12, 0)
        )

        value_label = ctk.CTkLabel(
            info,
            text=value,
            font=("Segoe UI", 20, "bold"),
            text_color=color
        )

        value_label.pack(
            anchor="w"
        )

        card.value_label = value_label

        return card

    # =========================================================
    # ADD EXAM
    # =========================================================

    def add_exam(self):

        exam_id = self.exam_id.get().strip()
        exam_name = self.exam_name.get().strip()
        course = self.course.get().strip()
        semester = self.semester.get().strip()
        exam_date = self.exam_date.get().strip()
        total_marks = self.total_marks.get().strip()

        if not exam_id or not exam_name or not course:

            messagebox.showerror(
                "Missing Information",
                "Please fill Exam ID, Exam Name and Course."
            )

            return

        if not semester or semester == "Select Semester":

            messagebox.showerror(
                "Missing Information",
                "Please select a semester."
            )

            return

        if not exam_date:

            messagebox.showerror(
                "Missing Information",
                "Please enter Exam Date."
            )

            return

        if not total_marks:

            messagebox.showerror(
                "Missing Information",
                "Please enter Total Marks."
            )

            return

        try:

            if float(total_marks) <= 0:

                raise ValueError

        except ValueError:

            messagebox.showerror(
                "Invalid Marks",
                "Total Marks must be a valid positive number."
            )

            return

        try:

            success = self.database.add_exam(
                exam_id,
                exam_name,
                course,
                semester,
                exam_date,
                total_marks
            )

            if not success:
                messagebox.showerror(
                    "Duplicate Exam ID",
                    f"Exam ID '{exam_id}' already exists."
                )
                return

            self.load_exams()
            self.clear_fields()

            messagebox.showinfo(
                "Success",
                "Exam added successfully."
            )

        except Exception as e:

            messagebox.showerror(
                "Error",
                f"Unable to add exam.\n\n{e}"
            )

    # =========================================================
    # LOAD EXAMS
    # =========================================================

    def load_exams(self):

        if not hasattr(self, "exam_table"):
            return

        for item in self.exam_table.get_children():

            self.exam_table.delete(item)

        try:

            exams = self.database.fetch_exams()

            courses = set()

            for exam in exams:

                self.exam_table.insert(
                    "",
                    "end",
                    values=(
                        exam[1],
                        exam[2],
                        exam[3],
                        exam[4],
                        exam[5],
                        exam[6]
                    )
                )

                if exam[3]:
                    courses.add(str(exam[3]))

            # Update Statistics

            self.total_card.value_label.configure(
                text=str(len(exams))
            )

            self.course_card.value_label.configure(
                text=str(len(courses))
            )

            self.upcoming_card.value_label.configure(
                text=str(len(exams))
            )

        except Exception as e:

            print("Error loading exams:", e)

    # =========================================================
    # SELECT EXAM
    # =========================================================

    def select_exam(self, event):

        selected = self.exam_table.focus()

        if not selected:
            return

        data = self.exam_table.item(
            selected,
            "values"
        )

        if not data:
            return

        self.exam_id.delete(0, "end")
        self.exam_id.insert(0, data[0])

        self.exam_name.delete(0, "end")
        self.exam_name.insert(0, data[1])

        self.course.delete(0, "end")
        self.course.insert(0, data[2])

        self.semester.set(data[3])

        self.exam_date.delete(0, "end")
        self.exam_date.insert(0, data[4])

        self.total_marks.delete(0, "end")
        self.total_marks.insert(0, data[5])

    # =========================================================
    # UPDATE EXAM
    # =========================================================

    def update_exam(self):

        exam_id = self.exam_id.get().strip()

        if not exam_id:

            messagebox.showwarning(
                "Select Exam",
                "Please select an exam from the table first."
            )

            return

        exam_name = self.exam_name.get().strip()
        course = self.course.get().strip()
        semester = self.semester.get()
        exam_date = self.exam_date.get().strip()
        total_marks = self.total_marks.get().strip()

        if not exam_name or not course:

            messagebox.showerror(
                "Error",
                "Please fill all required fields."
            )

            return

        try:

            self.database.update_exam(
                exam_id,
                exam_name,
                course,
                semester,
                exam_date,
                total_marks
            )

            self.load_exams()
            self.clear_fields()

            messagebox.showinfo(
                "Success",
                "Exam updated successfully."
            )

        except Exception as e:

            messagebox.showerror(
                "Error",
                f"Unable to update exam.\n\n{e}"
            )

    # =========================================================
    # DELETE EXAM
    # =========================================================

    def delete_exam(self):

        exam_id = self.exam_id.get().strip()

        if not exam_id:

            messagebox.showwarning(
                "Select Exam",
                "Please select an exam from the table first."
            )

            return

        confirm = messagebox.askyesno(
            "Confirm Delete",
            f"Are you sure you want to delete Exam ID: {exam_id}?"
        )

        if not confirm:
            return

        try:

            self.database.delete_exam(
                exam_id
            )

            self.load_exams()
            self.clear_fields()

            messagebox.showinfo(
                "Success",
                "Exam deleted successfully."
            )

        except Exception as e:

            messagebox.showerror(
                "Error",
                f"Unable to delete exam.\n\n{e}"
            )

    # =========================================================
    # SEARCH EXAM
    # =========================================================

    def search_exam(self):

        keyword = self.search_entry.get().strip()

        if keyword == "":

            self.load_exams()
            return

        for item in self.exam_table.get_children():

            self.exam_table.delete(item)

        try:

            exams = self.database.search_exams(
                keyword
            )

            for exam in exams:

                self.exam_table.insert(
                    "",
                    "end",
                    values=(
                        exam[1],
                        exam[2],
                        exam[3],
                        exam[4],
                        exam[5],
                        exam[6]
                    )
                )

        except Exception as e:

            messagebox.showerror(
                "Search Error",
                f"Unable to search exams.\n\n{e}"
            )

    # =========================================================
    # CLEAR FIELDS
    # =========================================================

    def clear_fields(self):

        self.exam_id.delete(
            0,
            "end"
        )

        self.exam_name.delete(
            0,
            "end"
        )

        self.course.delete(
            0,
            "end"
        )

        self.semester.set(
            "Select Semester"
        )

        self.exam_date.delete(
            0,
            "end"
        )

        self.total_marks.delete(
            0,
            "end"
        )

        self.exam_id.focus()