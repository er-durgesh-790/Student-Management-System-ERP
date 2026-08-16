
import customtkinter as ctk
from tkinter import ttk, filedialog, messagebox
from PIL import Image
import shutil
import os


class StudentModule:

    def __init__(self, root, database):

        self.root = root
        self.database = database
        self.photo_path = ""
        self.photo_image = None

        # ==============================
        # COLORS
        # ==============================

        self.bg_color = "#F1F5F9"
        self.card_color = "#FFFFFF"
        self.primary = "#2563EB"
        self.primary_hover = "#1D4ED8"
        self.success = "#16A34A"
        self.success_hover = "#15803D"
        self.warning = "#F59E0B"
        self.warning_hover = "#D97706"
        self.danger = "#DC2626"
        self.danger_hover = "#B91C1C"
        self.text_color = "#111827"
        self.muted_text = "#64748B"
        self.border_color = "#E2E8F0"

        self.create_ui()


    # =========================================================
    # CREATE UI
    # =========================================================

    def create_ui(self):

        # ==============================
        # MAIN FRAME
        # ==============================

        self.main_frame = ctk.CTkFrame(
            self.root,
            fg_color=self.bg_color,
            corner_radius=0
        )

        self.main_frame.pack(
            fill="both",
            expand=True
        )

        # ==============================
        # PAGE HEADER
        # ==============================

        header = ctk.CTkFrame(
            self.main_frame,
            fg_color=self.primary,
            corner_radius=12
        )

        header.pack(
            fill="x",
            padx=20,
            pady=(20, 10)
        )

        ctk.CTkLabel(
            header,
            text="👨‍🎓  Student Management",
            font=("Segoe UI", 25, "bold"),
            text_color="white"
        ).pack(
            side="left",
            padx=20,
            pady=18
        )

        ctk.CTkLabel(
            header,
            text="Student Registration & Records",
            font=("Segoe UI", 14),
            text_color="#DBEAFE"
        ).pack(
            side="right",
            padx=20
        )

        # ==============================
        # FORM CARD
        # ==============================

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
            text="📝 Student Information",
            font=("Segoe UI", 20, "bold"),
            text_color=self.text_color
        ).grid(
            row=0,
            column=0,
            columnspan=4,
            padx=20,
            pady=(18, 15),
            sticky="w"
        )

        # Column configuration

        form_card.grid_columnconfigure(1, weight=1)
        form_card.grid_columnconfigure(3, weight=1)

        # ==============================
        # STUDENT ID
        # ==============================

        ctk.CTkLabel(
            form_card,
            text="Student ID",
            font=("Segoe UI", 14, "bold"),
            text_color=self.text_color
        ).grid(
            row=1,
            column=0,
            padx=(20, 10),
            pady=8,
            sticky="w"
        )

        self.student_id = ctk.CTkEntry(
            form_card,
            height=40,
            placeholder_text="Enter Student ID",
            border_color=self.border_color
        )

        self.student_id.grid(
            row=1,
            column=1,
            padx=10,
            pady=8,
            sticky="ew"
        )

        # ==============================
        # FIRST NAME
        # ==============================

        ctk.CTkLabel(
            form_card,
            text="First Name",
            font=("Segoe UI", 14, "bold"),
            text_color=self.text_color
        ).grid(
            row=1,
            column=2,
            padx=10,
            pady=8,
            sticky="w"
        )

        self.first_name = ctk.CTkEntry(
            form_card,
            height=40,
            placeholder_text="Enter First Name",
            border_color=self.border_color
        )

        self.first_name.grid(
            row=1,
            column=3,
            padx=(10, 20),
            pady=8,
            sticky="ew"
        )

        # ==============================
        # LAST NAME
        # ==============================

        ctk.CTkLabel(
            form_card,
            text="Last Name",
            font=("Segoe UI", 14, "bold"),
            text_color=self.text_color
        ).grid(
            row=2,
            column=0,
            padx=(20, 10),
            pady=8,
            sticky="w"
        )

        self.last_name = ctk.CTkEntry(
            form_card,
            height=40,
            placeholder_text="Enter Last Name",
            border_color=self.border_color
        )

        self.last_name.grid(
            row=2,
            column=1,
            padx=10,
            pady=8,
            sticky="ew"
        )

        # ==============================
        # MOBILE
        # ==============================

        ctk.CTkLabel(
            form_card,
            text="Mobile",
            font=("Segoe UI", 14, "bold"),
            text_color=self.text_color
        ).grid(
            row=2,
            column=2,
            padx=10,
            pady=8,
            sticky="w"
        )

        self.mobile = ctk.CTkEntry(
            form_card,
            height=40,
            placeholder_text="Enter Mobile Number",
            border_color=self.border_color
        )

        self.mobile.grid(
            row=2,
            column=3,
            padx=(10, 20),
            pady=8,
            sticky="ew"
        )

        # ==============================
        # COURSE
        # ==============================

        ctk.CTkLabel(
            form_card,
            text="Course",
            font=("Segoe UI", 14, "bold"),
            text_color=self.text_color
        ).grid(
            row=3,
            column=0,
            padx=(20, 10),
            pady=8,
            sticky="w"
        )

        self.course = ctk.CTkEntry(
            form_card,
            height=40,
            placeholder_text="Enter Course",
            border_color=self.border_color
        )

        self.course.grid(
            row=3,
            column=1,
            padx=10,
            pady=8,
            sticky="ew"
        )

        # ==============================
        # SEMESTER
        # ==============================

        ctk.CTkLabel(
            form_card,
            text="Semester",
            font=("Segoe UI", 14, "bold"),
            text_color=self.text_color
        ).grid(
            row=3,
            column=2,
            padx=10,
            pady=8,
            sticky="w"
        )

        self.semester = ctk.CTkEntry(
            form_card,
            height=40,
            placeholder_text="Enter Semester",
            border_color=self.border_color
        )

        self.semester.grid(
            row=3,
            column=3,
            padx=(10, 20),
            pady=8,
            sticky="ew"
        )

        # ==============================
        # PHOTO
        # ==============================

        ctk.CTkLabel(
            form_card,
            text="Student Photo",
            font=("Segoe UI", 14, "bold"),
            text_color=self.text_color
        ).grid(
            row=4,
            column=0,
            padx=(20, 10),
            pady=12,
            sticky="nw"
        )

        photo_button_frame = ctk.CTkFrame(
            form_card,
            fg_color="transparent"
        )

        photo_button_frame.grid(
            row=4,
            column=1,
            padx=10,
            pady=12,
            sticky="nw"
        )

        self.photo_btn = ctk.CTkButton(
            photo_button_frame,
            text="📷  Choose Photo",
            width=180,
            height=40,
            fg_color=self.primary,
            hover_color=self.primary_hover,
            font=("Segoe UI", 13, "bold"),
            command=self.choose_photo
        )

        self.photo_btn.pack()

        self.photo_label = ctk.CTkLabel(
            form_card,
            text="No Photo",
            width=120,
            height=120,
            fg_color="#F8FAFC",
            corner_radius=10,
            text_color=self.muted_text
        )

        self.photo_label.grid(
            row=4,
            column=2,
            columnspan=2,
            padx=20,
            pady=12,
            sticky="w"
        )

        # ==============================
        # BUTTONS
        # ==============================

        button_frame = ctk.CTkFrame(
            form_card,
            fg_color="transparent"
        )

        button_frame.grid(
            row=5,
            column=0,
            columnspan=4,
            pady=(10, 20)
        )

        ctk.CTkButton(
            button_frame,
            text="➕  Add Student",
            width=160,
            height=42,
            fg_color=self.success,
            hover_color=self.success_hover,
            font=("Segoe UI", 13, "bold"),
            command=self.add_student
        ).pack(
            side="left",
            padx=6
        )

        ctk.CTkButton(
            button_frame,
            text="✏️  Update",
            width=140,
            height=42,
            fg_color=self.primary,
            hover_color=self.primary_hover,
            font=("Segoe UI", 13, "bold"),
            command=self.update_student
        ).pack(
            side="left",
            padx=6
        )

        ctk.CTkButton(
            button_frame,
            text="🗑️  Delete",
            width=140,
            height=42,
            fg_color=self.danger,
            hover_color=self.danger_hover,
            font=("Segoe UI", 13, "bold"),
            command=self.delete_student
        ).pack(
            side="left",
            padx=6
        )

        ctk.CTkButton(
            button_frame,
            text="🔄  Clear",
            width=140,
            height=42,
            fg_color="#64748B",
            hover_color="#475569",
            font=("Segoe UI", 13, "bold"),
            command=self.clear_form
        ).pack(
            side="left",
            padx=6
        )

        # ==============================
        # SEARCH CARD
        # ==============================

        search_card = ctk.CTkFrame(
            self.main_frame,
            fg_color=self.card_color,
            corner_radius=15
        )

        search_card.pack(
            fill="x",
            padx=20,
            pady=10
        )

        ctk.CTkLabel(
            search_card,
            text="🔍 Search Students",
            font=("Segoe UI", 18, "bold"),
            text_color=self.text_color
        ).pack(
            side="left",
            padx=(20, 15),
            pady=15
        )

        self.search_entry = ctk.CTkEntry(
            search_card,
            width=300,
            height=40,
            placeholder_text="Student ID / Name / Mobile"
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
            font=("Segoe UI", 13, "bold"),
            command=self.search_student
        ).pack(
            side="left",
            padx=5
        )

        ctk.CTkButton(
            search_card,
            text="📋 Show All",
            width=120,
            height=40,
            fg_color="#64748B",
            hover_color="#475569",
            font=("Segoe UI", 13, "bold"),
            command=self.load_students
        ).pack(
            side="left",
            padx=5
        )

        # ==============================
        # TABLE CARD
        # ==============================

        table_card = ctk.CTkFrame(
            self.main_frame,
            fg_color=self.card_color,
            corner_radius=15
        )

        table_card.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(10, 20)
        )

        ctk.CTkLabel(
            table_card,
            text="📋 Student Records",
            font=("Segoe UI", 19, "bold"),
            text_color=self.text_color
        ).pack(
            anchor="w",
            padx=20,
            pady=(15, 5)
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

        # ==============================
        # TREEVIEW STYLE
        # ==============================

        style = ttk.Style()

        try:
            style.theme_use("clam")
        except Exception:
            pass

        style.configure(
            "Student.Treeview",
            background="#FFFFFF",
            foreground="#111827",
            rowheight=38,
            fieldbackground="#FFFFFF",
            font=("Segoe UI", 11)
        )

        style.configure(
            "Student.Treeview.Heading",
            background="#2563EB",
            foreground="white",
            font=("Segoe UI", 11, "bold"),
            relief="flat"
        )

        style.map(
            "Student.Treeview",
            background=[
                ("selected", "#DBEAFE")
            ],
            foreground=[
                ("selected", "#111827")
            ]
        )

        columns = (
            "Student ID",
            "First Name",
            "Last Name",
            "Mobile",
            "Course",
            "Semester"
        )

        self.student_table = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            style="Student.Treeview"
        )

        column_widths = {
            "Student ID": 130,
            "First Name": 150,
            "Last Name": 150,
            "Mobile": 150,
            "Course": 160,
            "Semester": 120
        }

        for col in columns:

            self.student_table.heading(
                col,
                text=col
            )

            self.student_table.column(
                col,
                width=column_widths[col],
                anchor="center"
            )

        scrollbar = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=self.student_table.yview
        )

        self.student_table.configure(
            yscrollcommand=scrollbar.set
        )

        self.student_table.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        self.student_table.bind(
            "<ButtonRelease-1>",
            self.select_student
        )

        # Load existing students

        self.load_students()


    # =========================================================
# ADD STUDENT
# =========================================================

    def add_student(self):
        student_id = self.student_id.get().strip()
        first_name = self.first_name.get().strip()
        last_name = self.last_name.get().strip()
        mobile = self.mobile.get().strip()
        course = self.course.get().strip()
        semester = self.semester.get().strip()

        if student_id == "" or first_name == "":
            messagebox.showwarning(
                "Required Fields",
                "Please enter Student ID and First Name."
            )
            return

        try:
            success = self.database.add_student(
                student_id,
                first_name,
                last_name,
                mobile,
                course,
                semester,
                self.photo_path
            )

            if success:
                messagebox.showinfo(
                    "Success",
                    "Student added successfully."
                )
                self.load_students()
                self.clear_form()
            else:
                messagebox.showerror(
                    "Error",
                    "Student could not be added."
                )
        except Exception as e:
            messagebox.showerror(
                "Error",
                f"Unable to add student.\n\n{e}"
            )

    # =========================================================
    # LOAD STUDENTS
    # =========================================================

    def load_students(self):

        if not hasattr(self, "student_table"):
            return

        for item in self.student_table.get_children():

            self.student_table.delete(item)

        try:

            students = self.database.fetch_students()

            for student in students:

                self.student_table.insert(
                    "",
                    "end",
                    values=(
                        student[1],
                        student[2],
                        student[3],
                        student[4],
                        student[5],
                        student[6]
                    )
                )

        except Exception as e:

            messagebox.showerror(
                "Error",
                f"Unable to load students.\n\n{e}"
            )


    # =========================================================
    # CLEAR FORM
    # =========================================================

    def clear_form(self):

        self.student_id.delete(0, "end")
        self.first_name.delete(0, "end")
        self.last_name.delete(0, "end")
        self.mobile.delete(0, "end")
        self.course.delete(0, "end")
        self.semester.delete(0, "end")

        self.photo_path = ""
        self.photo_image = None

        self.photo_btn.configure(
            text="📷  Choose Photo"
        )

        self.photo_label.configure(
            image=None,
            text="No Photo"
        )


    # =========================================================
    # SELECT STUDENT
    # =========================================================

    def select_student(self, event):

        selected = self.student_table.focus()

        if selected == "":
            return

        data = self.student_table.item(selected)

        row = data["values"]

        if not row:
            return

        self.student_id.delete(0, "end")
        self.student_id.insert(0, row[0])

        self.first_name.delete(0, "end")
        self.first_name.insert(0, row[1])

        self.last_name.delete(0, "end")
        self.last_name.insert(0, row[2])

        self.mobile.delete(0, "end")
        self.mobile.insert(0, row[3])

        self.course.delete(0, "end")
        self.course.insert(0, row[4])

        self.semester.delete(0, "end")
        self.semester.insert(0, row[5])


    # =========================================================
    # UPDATE STUDENT
    # =========================================================

    def update_student(self):

        student_id = self.student_id.get().strip()

        if student_id == "":

            messagebox.showwarning(
                "Select Student",
                "Please select a student first."
            )

            return

        try:

            self.database.update_student(
                student_id,
                self.first_name.get().strip(),
                self.last_name.get().strip(),
                self.mobile.get().strip(),
                self.course.get().strip(),
                self.semester.get().strip()
            )

            messagebox.showinfo(
                "Success",
                "Student updated successfully."
            )

            self.load_students()
            self.clear_form()

        except Exception as e:

            messagebox.showerror(
                "Error",
                f"Unable to update student.\n\n{e}"
            )


    # =========================================================
    # DELETE STUDENT
    # =========================================================

    def delete_student(self):

        student_id = self.student_id.get().strip()

        if student_id == "":

            messagebox.showwarning(
                "Select Student",
                "Please select a student first."
            )

            return

        answer = messagebox.askyesno(
            "Confirm Delete",
            f"Are you sure you want to delete student {student_id}?"
        )

        if not answer:
            return

        try:

            self.database.delete_student(
                student_id
            )

            messagebox.showinfo(
                "Success",
                "Student deleted successfully."
            )

            self.load_students()
            self.clear_form()

        except Exception as e:

            messagebox.showerror(
                "Error",
                f"Unable to delete student.\n\n{e}"
            )


    # =========================================================
    # SEARCH STUDENT
    # =========================================================

    def search_student(self):

        keyword = self.search_entry.get().strip()

        for item in self.student_table.get_children():

            self.student_table.delete(item)

        try:

            students = self.database.search_students(
                keyword
            )

            for student in students:

                self.student_table.insert(
                    "",
                    "end",
                    values=(
                        student[1],
                        student[2],
                        student[3],
                        student[4],
                        student[5],
                        student[6]
                    )
                )

        except Exception as e:

            messagebox.showerror(
                "Search Error",
                f"Unable to search students.\n\n{e}"
            )


    # =========================================================
    # CHOOSE PHOTO
    # =========================================================

    def choose_photo(self):

        file = filedialog.askopenfilename(
            title="Select Student Photo",
            filetypes=[
                (
                    "Image Files",
                    "*.jpg *.jpeg *.png"
                )
            ]
        )

        if file == "":
            return

        try:

            # Create photos folder

            if not os.path.exists("photos"):

                os.makedirs("photos")

            filename = os.path.basename(file)

            destination = os.path.join(
                "photos",
                filename
            )

            # Copy image

            shutil.copy(
                file,
                destination
            )

            self.photo_path = destination

            self.photo_btn.configure(
                text="✅ Photo Selected"
            )

            # ==============================
            # PHOTO PREVIEW
            # ==============================

            image = Image.open(self.photo_path)

            image.thumbnail((120, 120))

            self.photo_image = ctk.CTkImage(
                light_image=image,
                dark_image=image,
                size=(120, 120)
            )

            self.photo_label.configure(
                image=self.photo_image,
                text=""
            )

            messagebox.showinfo(
                "Photo Selected",
                "Student photo selected successfully."
            )

        except Exception as e:

            messagebox.showerror(
                "Photo Error",
                f"Unable to load photo.\n\n{e}"
            )