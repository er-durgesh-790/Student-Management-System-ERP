import customtkinter as ctk
from tkinter import ttk, messagebox


class ResultModule:

    def __init__(self, parent, database):

        self.parent = parent
        self.database = database

        # ==========================================
        # COLORS
        # ==========================================

        self.primary = "#2563EB"
        self.primary_hover = "#1D4ED8"

        self.success = "#16A34A"
        self.success_hover = "#15803D"

        self.warning = "#F59E0B"
        self.warning_hover = "#D97706"

        self.danger = "#DC2626"
        self.danger_hover = "#B91C1C"

        self.purple = "#7C3AED"
        self.purple_hover = "#6D28D9"

        self.cyan = "#0891B2"

        self.bg = "#F8FAFC"
        self.card_bg = "#FFFFFF"

        self.text = "#111827"
        self.light_text = "#64748B"

        self.border = "#E2E8F0"

        # ==========================================
        # MAIN FRAME
        # ==========================================

        self.main_frame = ctk.CTkFrame(
            self.parent,
            fg_color=self.bg,
            corner_radius=0
        )

        self.main_frame.pack(
            fill="both",
            expand=True
        )

        self.create_ui()

    # ==========================================================
    # CREATE UI
    # ==========================================================

    def create_ui(self):

        # ======================================================
        # PAGE HEADER
        # ======================================================

        header = ctk.CTkFrame(
            self.main_frame,
            fg_color=self.primary,
            corner_radius=15,
            height=85
        )

        header.pack(
            fill="x",
            padx=20,
            pady=(20, 10)
        )

        header.pack_propagate(False)

        ctk.CTkLabel(
            header,
            text="📝  Result Management",
            font=("Segoe UI", 28, "bold"),
            text_color="white"
        ).pack(
            side="left",
            padx=25,
            pady=20
        )

        ctk.CTkLabel(
            header,
            text="Manage student academic results",
            font=("Segoe UI", 14),
            text_color="#DBEAFE"
        ).pack(
            side="right",
            padx=25
        )

        # ======================================================
        # FORM CARD
        # ======================================================

        form_card = ctk.CTkFrame(
            self.main_frame,
            fg_color=self.card_bg,
            corner_radius=15
        )

        form_card.pack(
            fill="x",
            padx=20,
            pady=10
        )

        # Form Heading

        ctk.CTkLabel(
            form_card,
            text="📋 Result Details",
            font=("Segoe UI", 20, "bold"),
            text_color=self.text
        ).grid(
            row=0,
            column=0,
            columnspan=4,
            padx=20,
            pady=(18, 15),
            sticky="w"
        )

        # ======================================================
        # STUDENT ID
        # ======================================================

        ctk.CTkLabel(
            form_card,
            text="Student ID",
            font=("Segoe UI", 13, "bold"),
            text_color=self.text
        ).grid(
            row=1,
            column=0,
            padx=20,
            pady=8,
            sticky="w"
        )

        self.student_id = ctk.CTkEntry(
            form_card,
            width=240,
            height=40,
            placeholder_text="Enter Student ID"
        )

        self.student_id.grid(
            row=1,
            column=1,
            padx=10,
            pady=8
        )

        self.student_id.bind(
            "<FocusOut>",
            self.fetch_student
        )

        # ======================================================
        # STUDENT NAME
        # ======================================================

        ctk.CTkLabel(
            form_card,
            text="Student Name",
            font=("Segoe UI", 13, "bold"),
            text_color=self.text
        ).grid(
            row=1,
            column=2,
            padx=20,
            pady=8,
            sticky="w"
        )

        self.student_name = ctk.CTkEntry(
            form_card,
            width=240,
            height=40,
            placeholder_text="Student Name"
        )

        self.student_name.grid(
            row=1,
            column=3,
            padx=10,
            pady=8
        )

        # ======================================================
        # COURSE
        # ======================================================

        ctk.CTkLabel(
            form_card,
            text="Course",
            font=("Segoe UI", 13, "bold"),
            text_color=self.text
        ).grid(
            row=2,
            column=0,
            padx=20,
            pady=8,
            sticky="w"
        )

        self.course = ctk.CTkEntry(
            form_card,
            width=240,
            height=40,
            placeholder_text="Enter Course"
        )

        self.course.grid(
            row=2,
            column=1,
            padx=10,
            pady=8
        )

        # ======================================================
        # SUBJECT
        # ======================================================

        ctk.CTkLabel(
            form_card,
            text="Subject",
            font=("Segoe UI", 13, "bold"),
            text_color=self.text
        ).grid(
            row=2,
            column=2,
            padx=20,
            pady=8,
            sticky="w"
        )

        self.subject = ctk.CTkEntry(
            form_card,
            width=240,
            height=40,
            placeholder_text="Enter Subject"
        )

        self.subject.grid(
            row=2,
            column=3,
            padx=10,
            pady=8
        )

        # ======================================================
        # MARKS
        # ======================================================

        ctk.CTkLabel(
            form_card,
            text="Marks",
            font=("Segoe UI", 13, "bold"),
            text_color=self.text
        ).grid(
            row=3,
            column=0,
            padx=20,
            pady=8,
            sticky="w"
        )

        self.marks = ctk.CTkEntry(
            form_card,
            width=240,
            height=40,
            placeholder_text="0 - 100"
        )

        self.marks.grid(
            row=3,
            column=1,
            padx=10,
            pady=8
        )

        self.marks.bind(
            "<KeyRelease>",
            self.calculate_result
        )

        self.marks.bind(
            "<FocusOut>",
            self.validate_marks
        )

        # ======================================================
        # GRADE
        # ======================================================

        ctk.CTkLabel(
            form_card,
            text="Grade",
            font=("Segoe UI", 13, "bold"),
            text_color=self.text
        ).grid(
            row=3,
            column=2,
            padx=20,
            pady=8,
            sticky="w"
        )

        self.grade = ctk.CTkEntry(
            form_card,
            width=240,
            height=40,
            placeholder_text="Automatic Grade"
        )

        self.grade.grid(
            row=3,
            column=3,
            padx=10,
            pady=8
        )

        # ======================================================
        # PERCENTAGE
        # ======================================================

        ctk.CTkLabel(
            form_card,
            text="Percentage",
            font=("Segoe UI", 13, "bold"),
            text_color=self.text
        ).grid(
            row=4,
            column=0,
            padx=20,
            pady=8,
            sticky="w"
        )

        self.percentage = ctk.CTkEntry(
            form_card,
            width=240,
            height=40,
            placeholder_text="Automatic Percentage"
        )

        self.percentage.grid(
            row=4,
            column=1,
            padx=10,
            pady=8
        )

        # ======================================================
        # RESULT STATUS
        # ======================================================

        ctk.CTkLabel(
            form_card,
            text="Result Status",
            font=("Segoe UI", 13, "bold"),
            text_color=self.text
        ).grid(
            row=4,
            column=2,
            padx=20,
            pady=8,
            sticky="w"
        )

        self.status = ctk.CTkComboBox(
            form_card,
            width=240,
            height=40,
            values=[
                "Pass",
                "Fail"
            ],
            state="readonly"
        )

        self.status.grid(
            row=4,
            column=3,
            padx=10,
            pady=8
        )

        self.status.set("Pass")

        # ======================================================
        # BUTTON FRAME
        # ======================================================

        button_frame = ctk.CTkFrame(
            form_card,
            fg_color="transparent"
        )

        button_frame.grid(
            row=5,
            column=0,
            columnspan=4,
            pady=(15, 20)
        )

        # ADD

        ctk.CTkButton(
            button_frame,
            text="➕ Add Result",
            width=150,
            height=42,
            fg_color=self.success,
            hover_color=self.success_hover,
            font=("Segoe UI", 13, "bold"),
            command=self.add_result
        ).pack(
            side="left",
            padx=7
        )

        # UPDATE

        ctk.CTkButton(
            button_frame,
            text="✏ Update",
            width=150,
            height=42,
            fg_color=self.primary,
            hover_color=self.primary_hover,
            font=("Segoe UI", 13, "bold"),
            command=self.update_result
        ).pack(
            side="left",
            padx=7
        )

        # DELETE

        ctk.CTkButton(
            button_frame,
            text="🗑 Delete",
            width=150,
            height=42,
            fg_color=self.danger,
            hover_color=self.danger_hover,
            font=("Segoe UI", 13, "bold"),
            command=self.delete_result
        ).pack(
            side="left",
            padx=7
        )

        # CLEAR

        ctk.CTkButton(
            button_frame,
            text="🧹 Clear",
            width=150,
            height=42,
            fg_color=self.warning,
            hover_color=self.warning_hover,
            font=("Segoe UI", 13, "bold"),
            command=self.clear_fields
        ).pack(
            side="left",
            padx=7
        )

        # ======================================================
        # SEARCH CARD
        # ======================================================

        search_card = ctk.CTkFrame(
            self.main_frame,
            fg_color=self.card_bg,
            corner_radius=15
        )

        search_card.pack(
            fill="x",
            padx=20,
            pady=10
        )

        ctk.CTkLabel(
            search_card,
            text="🔍 Search Results",
            font=("Segoe UI", 18, "bold"),
            text_color=self.text
        ).pack(
            side="left",
            padx=(20, 10),
            pady=15
        )

        self.search_entry = ctk.CTkEntry(
            search_card,
            width=330,
            height=40,
            placeholder_text="Student ID / Name / Course / Subject"
        )

        self.search_entry.pack(
            side="left",
            padx=10,
            pady=15
        )

        ctk.CTkButton(
            search_card,
            text="🔍 Search",
            width=120,
            height=40,
            fg_color=self.primary,
            hover_color=self.primary_hover,
            command=self.search_result
        ).pack(
            side="left",
            padx=5
        )

        ctk.CTkButton(
            search_card,
            text="📋 Show All",
            width=120,
            height=40,
            fg_color=self.purple,
            hover_color=self.purple_hover,
            command=self.load_results
        ).pack(
            side="left",
            padx=5
        )

        # ======================================================
        # TABLE CARD
        # ======================================================

        table_card = ctk.CTkFrame(
            self.main_frame,
            fg_color=self.card_bg,
            corner_radius=15
        )

        table_card.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(5, 20)
        )

        ctk.CTkLabel(
            table_card,
            text="📊 Result Records",
            font=("Segoe UI", 18, "bold"),
            text_color=self.text
        ).pack(
            anchor="w",
            padx=20,
            pady=(15, 5)
        )

        # ======================================================
        # TREEVIEW STYLE
        # ======================================================

        style = ttk.Style()

        try:
            style.theme_use("clam")
        except:
            pass

        style.configure(
            "Result.Treeview",
            background="#FFFFFF",
            foreground="#111827",
            rowheight=38,
            fieldbackground="#FFFFFF",
            font=("Segoe UI", 11),
            borderwidth=0
        )

        style.configure(
            "Result.Treeview.Heading",
            background="#2563EB",
            foreground="white",
            font=("Segoe UI", 11, "bold"),
            padding=10
        )

        style.map(
            "Result.Treeview",
            background=[
                ("selected", "#DBEAFE")
            ],
            foreground=[
                ("selected", "#111827")
            ]
        )

        # ======================================================
        # TABLE
        # ======================================================

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

        columns = (
            "Student ID",
            "Student Name",
            "Course",
            "Subject",
            "Marks",
            "Grade",
            "Percentage",
            "Status"
        )

        self.result_table = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            style="Result.Treeview"
        )

        # ======================================================
        # COLUMN SETTINGS
        # ======================================================

        widths = {
            "Student ID": 120,
            "Student Name": 170,
            "Course": 140,
            "Subject": 150,
            "Marks": 90,
            "Grade": 90,
            "Percentage": 120,
            "Status": 100
        }

        for col in columns:

            self.result_table.heading(
                col,
                text=col
            )

            self.result_table.column(
                col,
                width=widths[col],
                anchor="center"
            )

        # ======================================================
        # SCROLLBARS
        # ======================================================

        vertical_scrollbar = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=self.result_table.yview
        )

        horizontal_scrollbar = ttk.Scrollbar(
            table_frame,
            orient="horizontal",
            command=self.result_table.xview
        )

        self.result_table.configure(
            yscrollcommand=vertical_scrollbar.set,
            xscrollcommand=horizontal_scrollbar.set
        )

        self.result_table.pack(
            side="left",
            fill="both",
            expand=True
        )

        vertical_scrollbar.pack(
            side="right",
            fill="y"
        )

        horizontal_scrollbar.pack(
            side="bottom",
            fill="x"
        )

        # ======================================================
        # TABLE EVENT
        # ======================================================

        self.result_table.bind(
            "<<TreeviewSelect>>",
            self.select_result
        )

        # ======================================================
        # LOAD DATA
        # ======================================================

        self.load_results()

    # ==========================================================
    # LOAD RESULTS
    # ==========================================================

    def load_results(self):

        for item in self.result_table.get_children():
            self.result_table.delete(item)

        try:

            results = self.database.fetch_results()

            for row in results:

                item = self.result_table.insert(
                    "",
                    "end",
                    values=(
                        row[1],
                        row[2],
                        row[3],
                        row[4],
                        row[5],
                        row[6],
                        row[7],
                        row[8]
                    )
                )

                # Pass / Fail color

                if str(row[8]).lower() == "pass":

                    self.result_table.item(
                        item,
                        tags=("pass",)
                    )

                else:

                    self.result_table.item(
                        item,
                        tags=("fail",)
                    )

            self.result_table.tag_configure(
                "pass",
                foreground="#15803D"
            )

            self.result_table.tag_configure(
                "fail",
                foreground="#DC2626"
            )

        except Exception as e:

            messagebox.showerror(
                "Database Error",
                str(e)
            )

    # ==========================================================
    # ADD RESULT
    # ==========================================================

    def add_result(self):

        if (
            self.student_id.get().strip() == "" or
            self.student_name.get().strip() == "" or
            self.course.get().strip() == "" or
            self.subject.get().strip() == "" or
            self.marks.get().strip() == ""
        ):

            messagebox.showerror(
                "Required Fields",
                "Please fill all required fields."
            )

            return

        try:

            marks = float(
                self.marks.get().strip()
            )

            if marks < 0 or marks > 100:

                messagebox.showerror(
                    "Invalid Marks",
                    "Marks must be between 0 and 100."
                )

                return

            self.database.add_result(

                self.student_id.get().strip(),
                self.student_name.get().strip(),
                self.course.get().strip(),
                self.subject.get().strip(),
                self.marks.get().strip(),
                self.grade.get().strip(),
                self.percentage.get().strip(),
                self.status.get()
            )

            messagebox.showinfo(
                "Success",
                "Result Added Successfully."
            )

            self.clear_fields()
            self.load_results()

        except Exception as e:

            messagebox.showerror(
                "Database Error",
                str(e)
            )

    # ==========================================================
    # UPDATE RESULT
    # ==========================================================

    def update_result(self):

        student_id = self.student_id.get().strip()

        if student_id == "":

            messagebox.showerror(
                "Error",
                "Please select a result first."
            )

            return

        try:

            marks = float(
                self.marks.get().strip()
            )

            if marks < 0 or marks > 100:

                messagebox.showerror(
                    "Invalid Marks",
                    "Marks must be between 0 and 100."
                )

                return

            self.database.update_result(

                student_id,
                self.student_name.get().strip(),
                self.course.get().strip(),
                self.subject.get().strip(),
                self.marks.get().strip(),
                self.grade.get().strip(),
                self.percentage.get().strip(),
                self.status.get()
            )

            messagebox.showinfo(
                "Success",
                "Result Updated Successfully."
            )

            self.clear_fields()
            self.load_results()

        except Exception as e:

            messagebox.showerror(
                "Database Error",
                str(e)
            )

    # ==========================================================
    # DELETE RESULT
    # ==========================================================

    def delete_result(self):

        student_id = self.student_id.get().strip()

        if student_id == "":

            messagebox.showerror(
                "Error",
                "Please select a result first."
            )

            return

        confirm = messagebox.askyesno(
            "Confirm Delete",
            "Are you sure you want to delete this result?"
        )

        if not confirm:
            return

        try:

            self.database.delete_result(
                student_id
            )

            messagebox.showinfo(
                "Success",
                "Result Deleted Successfully."
            )

            self.clear_fields()
            self.load_results()

        except Exception as e:

            messagebox.showerror(
                "Database Error",
                str(e)
            )

    # ==========================================================
    # SEARCH RESULT
    # ==========================================================

    def search_result(self):

        keyword = self.search_entry.get().strip()

        if keyword == "":
            self.load_results()
            return

        for item in self.result_table.get_children():
            self.result_table.delete(item)

        try:

            results = self.database.search_results(
                keyword
            )

            for row in results:

                item = self.result_table.insert(
                    "",
                    "end",
                    values=(
                        row[1],
                        row[2],
                        row[3],
                        row[4],
                        row[5],
                        row[6],
                        row[7],
                        row[8]
                    )
                )

                if str(row[8]).lower() == "pass":

                    self.result_table.item(
                        item,
                        tags=("pass",)
                    )

                else:

                    self.result_table.item(
                        item,
                        tags=("fail",)
                    )

        except Exception as e:

            messagebox.showerror(
                "Search Error",
                str(e)
            )

    # ==========================================================
    # SELECT RESULT
    # ==========================================================

    def select_result(self, event=None):

        selected = self.result_table.focus()

        if selected == "":
            return

        data = self.result_table.item(
            selected
        )["values"]

        if not data:
            return

        self.clear_fields(
            reset_status=False
        )

        self.student_id.insert(
            0,
            data[0]
        )

        self.student_name.insert(
            0,
            data[1]
        )

        self.course.insert(
            0,
            data[2]
        )

        self.subject.insert(
            0,
            data[3]
        )

        self.marks.insert(
            0,
            data[4]
        )

        self.grade.insert(
            0,
            data[5]
        )

        self.percentage.insert(
            0,
            data[6]
        )

        self.status.set(
            data[7]
        )

    # ==========================================================
    # CLEAR FIELDS
    # ==========================================================

    def clear_fields(self, reset_status=True):

        self.student_id.delete(
            0,
            "end"
        )

        self.student_name.delete(
            0,
            "end"
        )

        self.course.delete(
            0,
            "end"
        )

        self.subject.delete(
            0,
            "end"
        )

        self.marks.delete(
            0,
            "end"
        )

        self.grade.delete(
            0,
            "end"
        )

        self.percentage.delete(
            0,
            "end"
        )

        if reset_status:
            self.status.set("Pass")

    # ==========================================================
    # CALCULATE RESULT
    # ==========================================================

    def calculate_result(self, event=None):

        value = self.marks.get().strip()

        if value == "":

            self.grade.delete(
                0,
                "end"
            )

            self.percentage.delete(
                0,
                "end"
            )

            self.status.set("Pass")

            return

        try:

            marks = float(value)

            if marks > 100:
                marks = 100

            if marks < 0:
                marks = 0

            # Percentage

            self.percentage.delete(
                0,
                "end"
            )

            self.percentage.insert(
                0,
                f"{marks:.2f}%"
            )

            # Grade

            if marks >= 90:
                grade = "A+"

            elif marks >= 80:
                grade = "A"

            elif marks >= 70:
                grade = "B"

            elif marks >= 60:
                grade = "C"

            elif marks >= 40:
                grade = "D"

            else:
                grade = "F"

            self.grade.delete(
                0,
                "end"
            )

            self.grade.insert(
                0,
                grade
            )

            # Status

            if marks >= 40:

                self.status.set(
                    "Pass"
                )

            else:

                self.status.set(
                    "Fail"
                )

        except ValueError:

            self.grade.delete(
                0,
                "end"
            )

            self.percentage.delete(
                0,
                "end"
            )

            self.status.set(
                "Pass"
            )

    # ==========================================================
    # VALIDATE MARKS
    # ==========================================================

    def validate_marks(self, event=None):

        value = self.marks.get().strip()

        if value == "":
            return

        try:

            marks = float(value)

            if marks < 0:

                messagebox.showwarning(
                    "Invalid Marks",
                    "Marks cannot be less than 0."
                )

                self.marks.delete(
                    0,
                    "end"
                )

                self.marks.focus()

                return

            if marks > 100:

                messagebox.showwarning(
                    "Invalid Marks",
                    "Marks cannot be greater than 100."
                )

                self.marks.delete(
                    0,
                    "end"
                )

                self.marks.focus()

                return

        except ValueError:

            messagebox.showwarning(
                "Invalid Input",
                "Please enter numbers only."
            )

            self.marks.delete(
                0,
                "end"
            )

            self.marks.focus()

    # ==========================================================
    # FETCH STUDENT
    # ==========================================================

    def fetch_student(self, event=None):

        student_id = self.student_id.get().strip()

        if student_id == "":
            return

        try:

            student = self.database.get_student(
                student_id
            )

            if student:

                self.student_name.delete(
                    0,
                    "end"
                )

                self.student_name.insert(
                    0,
                    student[2]
                )

                self.course.delete(
                    0,
                    "end"
                )

                self.course.insert(
                    0,
                    student[5]
                )

            else:

                self.student_name.delete(
                    0,
                    "end"
                )

                self.course.delete(
                    0,
                    "end"
                )

                messagebox.showwarning(
                    "Student Not Found",
                    "No student found with this Student ID."
                )

        except Exception as e:

            messagebox.showerror(
                "Database Error",
                str(e)
            )