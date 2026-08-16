
import customtkinter as ctk
from tkinter import ttk, messagebox


class CourseModule:

    def __init__(self, root, database):

        self.root = root
        self.database = database

        self.create_ui()

    # ==========================================================
    # CREATE UI
    # ==========================================================

    def create_ui(self):

        # Main Frame
        self.main_frame = ctk.CTkFrame(
            self.root,
            fg_color="#F4F7FB",
            corner_radius=0
        )

        self.main_frame.pack(
            fill="both",
            expand=True
        )

        # ======================================================
        # HEADER
        # ======================================================

        header = ctk.CTkFrame(
            self.main_frame,
            height=80,
            fg_color="#2563EB",
            corner_radius=0
        )

        header.pack(
            fill="x"
        )

        header.pack_propagate(False)

        ctk.CTkLabel(
            header,
            text="📚  Course Management",
            font=("Segoe UI", 27, "bold"),
            text_color="white"
        ).pack(
            side="left",
            padx=30
        )

        ctk.CTkLabel(
            header,
            text="Manage Courses & Fees",
            font=("Segoe UI", 13),
            text_color="#DBEAFE"
        ).pack(
            side="right",
            padx=30
        )

        # ======================================================
        # FORM CARD
        # ======================================================

        form_card = ctk.CTkFrame(
            self.main_frame,
            fg_color="white",
            corner_radius=15
        )

        form_card.pack(
            fill="x",
            padx=25,
            pady=(20, 10)
        )

        ctk.CTkLabel(
            form_card,
            text="Course Information",
            font=("Segoe UI", 18, "bold"),
            text_color="#1F2937"
        ).grid(
            row=0,
            column=0,
            columnspan=4,
            sticky="w",
            padx=25,
            pady=(18, 12)
        )

        # ======================================================
        # COURSE ID
        # ======================================================

        ctk.CTkLabel(
            form_card,
            text="Course ID",
            font=("Segoe UI", 13, "bold"),
            text_color="#374151"
        ).grid(
            row=1,
            column=0,
            padx=(25, 10),
            pady=10,
            sticky="w"
        )

        self.course_id = ctk.CTkEntry(
            form_card,
            width=230,
            height=40,
            corner_radius=8,
            placeholder_text="Enter Course ID"
        )

        self.course_id.grid(
            row=1,
            column=1,
            padx=10,
            pady=10
        )

        # ======================================================
        # COURSE NAME
        # ======================================================

        ctk.CTkLabel(
            form_card,
            text="Course Name",
            font=("Segoe UI", 13, "bold"),
            text_color="#374151"
        ).grid(
            row=1,
            column=2,
            padx=10,
            pady=10,
            sticky="w"
        )

        self.course_name = ctk.CTkEntry(
            form_card,
            width=230,
            height=40,
            corner_radius=8,
            placeholder_text="Enter Course Name"
        )

        self.course_name.grid(
            row=1,
            column=3,
            padx=(10, 25),
            pady=10
        )

        # ======================================================
        # DURATION
        # ======================================================

        ctk.CTkLabel(
            form_card,
            text="Duration",
            font=("Segoe UI", 13, "bold"),
            text_color="#374151"
        ).grid(
            row=2,
            column=0,
            padx=(25, 10),
            pady=10,
            sticky="w"
        )

        self.duration = ctk.CTkEntry(
            form_card,
            width=230,
            height=40,
            corner_radius=8,
            placeholder_text="e.g. 4 Years"
        )

        self.duration.grid(
            row=2,
            column=1,
            padx=10,
            pady=10
        )

        # ======================================================
        # COURSE FEE
        # ======================================================

        ctk.CTkLabel(
            form_card,
            text="Course Fee",
            font=("Segoe UI", 13, "bold"),
            text_color="#374151"
        ).grid(
            row=2,
            column=2,
            padx=10,
            pady=10,
            sticky="w"
        )

        self.fee = ctk.CTkEntry(
            form_card,
            width=230,
            height=40,
            corner_radius=8,
            placeholder_text="Enter Course Fee"
        )

        self.fee.grid(
            row=2,
            column=3,
            padx=(10, 25),
            pady=10
        )

        # ======================================================
        # BUTTONS
        # ======================================================

        button_frame = ctk.CTkFrame(
            form_card,
            fg_color="transparent"
        )

        button_frame.grid(
            row=3,
            column=0,
            columnspan=4,
            pady=(15, 20)
        )

        # ADD
        ctk.CTkButton(
            button_frame,
            text="➕  Add Course",
            width=145,
            height=40,
            corner_radius=8,
            fg_color="#16A34A",
            hover_color="#15803D",
            font=("Segoe UI", 13, "bold"),
            command=self.add_course
        ).pack(
            side="left",
            padx=6
        )

        # UPDATE
        ctk.CTkButton(
            button_frame,
            text="✏️  Update",
            width=130,
            height=40,
            corner_radius=8,
            fg_color="#2563EB",
            hover_color="#1D4ED8",
            font=("Segoe UI", 13, "bold"),
            command=self.update_course
        ).pack(
            side="left",
            padx=6
        )

        # DELETE
        ctk.CTkButton(
            button_frame,
            text="🗑  Delete",
            width=130,
            height=40,
            corner_radius=8,
            fg_color="#DC2626",
            hover_color="#B91C1C",
            font=("Segoe UI", 13, "bold"),
            command=self.delete_course
        ).pack(
            side="left",
            padx=6
        )

        # CLEAR
        ctk.CTkButton(
            button_frame,
            text="🔄  Clear",
            width=130,
            height=40,
            corner_radius=8,
            fg_color="#6B7280",
            hover_color="#4B5563",
            font=("Segoe UI", 13, "bold"),
            command=self.clear_fields
        ).pack(
            side="left",
            padx=6
        )

        # ======================================================
        # SEARCH CARD
        # ======================================================

        search_card = ctk.CTkFrame(
            self.main_frame,
            fg_color="white",
            corner_radius=12
        )

        search_card.pack(
            fill="x",
            padx=25,
            pady=10
        )

        ctk.CTkLabel(
            search_card,
            text="🔎  Search Course",
            font=("Segoe UI", 14, "bold"),
            text_color="#1F2937"
        ).pack(
            side="left",
            padx=(20, 10),
            pady=15
        )

        self.search_entry = ctk.CTkEntry(
            search_card,
            width=320,
            height=38,
            corner_radius=8,
            placeholder_text="Course ID / Course Name"
        )

        self.search_entry.pack(
            side="left",
            padx=10,
            pady=15
        )

        ctk.CTkButton(
            search_card,
            text="Search",
            width=110,
            height=38,
            corner_radius=8,
            fg_color="#2563EB",
            hover_color="#1D4ED8",
            command=self.search_course
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
            fg_color="#64748B",
            hover_color="#475569",
            command=self.show_all_courses
        ).pack(
            side="left",
            padx=5
        )

        # ======================================================
        # TABLE CARD
        # ======================================================

        table_card = ctk.CTkFrame(
            self.main_frame,
            fg_color="white",
            corner_radius=12
        )

        table_card.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=(5, 20)
        )

        ctk.CTkLabel(
            table_card,
            text="Course Records",
            font=("Segoe UI", 17, "bold"),
            text_color="#1F2937"
        ).pack(
            anchor="w",
            padx=20,
            pady=(15, 10)
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
            "Course.Treeview",
            background="#FFFFFF",
            foreground="#1F2937",
            rowheight=38,
            fieldbackground="#FFFFFF",
            font=("Segoe UI", 11)
        )

        style.configure(
            "Course.Treeview.Heading",
            background="#2563EB",
            foreground="white",
            font=("Segoe UI", 11, "bold"),
            padding=8
        )

        style.map(
            "Course.Treeview",
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
            pady=(0, 15)
        )

        columns = (
            "Course ID",
            "Course Name",
            "Duration",
            "Fee"
        )

        self.course_table = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            style="Course.Treeview"
        )

        self.course_table.heading(
            "Course ID",
            text="Course ID"
        )

        self.course_table.heading(
            "Course Name",
            text="Course Name"
        )

        self.course_table.heading(
            "Duration",
            text="Duration"
        )

        self.course_table.heading(
            "Fee",
            text="Course Fee"
        )

        self.course_table.column(
            "Course ID",
            width=180,
            anchor="center"
        )

        self.course_table.column(
            "Course Name",
            width=280,
            anchor="center"
        )

        self.course_table.column(
            "Duration",
            width=200,
            anchor="center"
        )

        self.course_table.column(
            "Fee",
            width=180,
            anchor="center"
        )

        scrollbar = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=self.course_table.yview
        )

        self.course_table.configure(
            yscrollcommand=scrollbar.set
        )

        self.course_table.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        # ======================================================
        # EVENTS
        # ======================================================

        self.course_table.bind(
            "<<TreeviewSelect>>",
            self.select_course
        )

        self.search_entry.bind(
            "<Return>",
            lambda event: self.search_course()
        )

        # ======================================================
        # LOAD DATA
        # ======================================================

        self.load_courses()

        self.course_id.focus()

    # ==========================================================
    # ADD COURSE
    # ==========================================================

    def add_course(self):

        course_id = self.course_id.get().strip()
        course_name = self.course_name.get().strip()
        duration = self.duration.get().strip()
        fee = self.fee.get().strip()

        if course_id == "" or course_name == "":

            messagebox.showwarning(
                "Required Fields",
                "Please enter Course ID and Course Name."
            )

            return

        try:

            self.database.add_course(
                course_id,
                course_name,
                duration,
                fee
            )

            self.load_courses()
            self.clear_fields()

            messagebox.showinfo(
                "Success",
                "Course added successfully."
            )

        except Exception as e:

            messagebox.showerror(
                "Database Error",
                str(e)
            )

    # ==========================================================
    # LOAD COURSES
    # ==========================================================

    def load_courses(self):

        for item in self.course_table.get_children():
            self.course_table.delete(item)

        try:

            courses = self.database.fetch_courses()

            for course in courses:

                self.course_table.insert(
                    "",
                    "end",
                    values=(
                        course[1],
                        course[2],
                        course[3],
                        course[4]
                    )
                )

        except Exception as e:

            messagebox.showerror(
                "Database Error",
                str(e)
            )

    # ==========================================================
    # SELECT COURSE
    # ==========================================================

    def select_course(self, event):

        selected = self.course_table.focus()

        if not selected:
            return

        data = self.course_table.item(
            selected
        )["values"]

        if not data:
            return

        self.course_id.delete(
            0,
            "end"
        )

        self.course_id.insert(
            0,
            data[0]
        )

        self.course_name.delete(
            0,
            "end"
        )

        self.course_name.insert(
            0,
            data[1]
        )

        self.duration.delete(
            0,
            "end"
        )

        self.duration.insert(
            0,
            data[2]
        )

        self.fee.delete(
            0,
            "end"
        )

        self.fee.insert(
            0,
            data[3]
        )

    # ==========================================================
    # UPDATE COURSE
    # ==========================================================

    def update_course(self):

        course_id = self.course_id.get().strip()

        if course_id == "":

            messagebox.showwarning(
                "Select Course",
                "Please select a course from the table."
            )

            return

        try:

            self.database.update_course(
                self.course_id.get().strip(),
                self.course_name.get().strip(),
                self.duration.get().strip(),
                self.fee.get().strip()
            )

            self.load_courses()
            self.clear_fields()

            messagebox.showinfo(
                "Success",
                "Course updated successfully."
            )

        except Exception as e:

            messagebox.showerror(
                "Database Error",
                str(e)
            )

    # ==========================================================
    # DELETE COURSE
    # ==========================================================

    def delete_course(self):

        course_id = self.course_id.get().strip()

        if course_id == "":

            messagebox.showwarning(
                "Select Course",
                "Please select a course to delete."
            )

            return

        confirm = messagebox.askyesno(
            "Confirm Delete",
            f"Are you sure you want to delete Course ID: {course_id}?"
        )

        if not confirm:
            return

        try:

            self.database.delete_course(
                course_id
            )

            self.load_courses()
            self.clear_fields()

            messagebox.showinfo(
                "Success",
                "Course deleted successfully."
            )

        except Exception as e:

            messagebox.showerror(
                "Database Error",
                str(e)
            )

    # ==========================================================
    # SEARCH COURSE
    # ==========================================================

    def search_course(self):

        keyword = self.search_entry.get().strip()

        if keyword == "":

            self.load_courses()
            return

        for item in self.course_table.get_children():
            self.course_table.delete(item)

        try:

            courses = self.database.search_courses(
                keyword
            )

            for course in courses:

                self.course_table.insert(
                    "",
                    "end",
                    values=(
                        course[1],
                        course[2],
                        course[3],
                        course[4]
                    )
                )

        except Exception as e:

            messagebox.showerror(
                "Search Error",
                str(e)
            )

    # ==========================================================
    # SHOW ALL
    # ==========================================================

    def show_all_courses(self):

        self.search_entry.delete(
            0,
            "end"
        )

        self.load_courses()

    # ==========================================================
    # CLEAR FIELDS
    # ==========================================================

    def clear_fields(self):

        self.course_id.delete(
            0,
            "end"
        )

        self.course_name.delete(
            0,
            "end"
        )

        self.duration.delete(
            0,
            "end"
        )

        self.fee.delete(
            0,
            "end"
        )

        self.course_table.selection_remove(
            self.course_table.selection()
        )

        self.course_id.focus()