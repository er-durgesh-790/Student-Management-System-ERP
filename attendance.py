
import customtkinter as ctk
from tkinter import ttk
from tkinter import messagebox
from datetime import date


class AttendanceModule:

    def __init__(self, parent, database):

        self.parent = parent
        self.database = database

        # ==========================
        # Colors
        # ==========================

        self.bg_color = "#F5F7FB"
        self.card_color = "#FFFFFF"

        self.primary = "#2563EB"
        self.primary_hover = "#1D4ED8"

        self.success = "#16A34A"
        self.success_hover = "#15803D"

        self.warning = "#F59E0B"
        self.warning_hover = "#D97706"

        self.danger = "#DC2626"
        self.danger_hover = "#B91C1C"

        self.secondary = "#64748B"
        self.secondary_hover = "#475569"

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
            corner_radius=12,
            height=80
        )

        header.pack(
            fill="x",
            padx=20,
            pady=(20, 10)
        )

        header.pack_propagate(False)

        title_frame = ctk.CTkFrame(
            header,
            fg_color="transparent"
        )

        title_frame.pack(
            side="left",
            padx=20,
            pady=10
        )

        ctk.CTkLabel(
            title_frame,
            text="📋  Attendance Management",
            font=("Arial", 26, "bold"),
            text_color="white"
        ).pack(anchor="w")

        ctk.CTkLabel(
            title_frame,
            text="Manage student attendance records",
            font=("Arial", 13),
            text_color="#DBEAFE"
        ).pack(anchor="w")

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
            text="Student Attendance Details",
            font=("Arial", 18, "bold"),
            text_color="#1E293B"
        ).grid(
            row=0,
            column=0,
            columnspan=4,
            sticky="w",
            padx=20,
            pady=(18, 12)
        )

        # Make columns responsive

        for column in range(4):
            form_card.grid_columnconfigure(
                column,
                weight=1
            )

        # ==========================
        # Student ID
        # ==========================

        ctk.CTkLabel(
            form_card,
            text="Student ID",
            font=("Arial", 13, "bold"),
            text_color="#475569"
        ).grid(
            row=1,
            column=0,
            padx=20,
            pady=(5, 5),
            sticky="w"
        )

        self.student_id = ctk.CTkEntry(
            form_card,
            width=220,
            height=38,
            placeholder_text="Enter Student ID",
            corner_radius=8
        )

        self.student_id.grid(
            row=2,
            column=0,
            padx=20,
            pady=(0, 15),
            sticky="ew"
        )

        # ==========================
        # Student Name
        # ==========================

        ctk.CTkLabel(
            form_card,
            text="Student Name",
            font=("Arial", 13, "bold"),
            text_color="#475569"
        ).grid(
            row=1,
            column=1,
            padx=20,
            pady=(5, 5),
            sticky="w"
        )

        self.student_name = ctk.CTkEntry(
            form_card,
            width=220,
            height=38,
            placeholder_text="Enter Student Name",
            corner_radius=8
        )

        self.student_name.grid(
            row=2,
            column=1,
            padx=20,
            pady=(0, 15),
            sticky="ew"
        )

        # ==========================
        # Course
        # ==========================

        ctk.CTkLabel(
            form_card,
            text="Course",
            font=("Arial", 13, "bold"),
            text_color="#475569"
        ).grid(
            row=1,
            column=2,
            padx=20,
            pady=(5, 5),
            sticky="w"
        )

        self.course = ctk.CTkEntry(
            form_card,
            width=220,
            height=38,
            placeholder_text="Enter Course",
            corner_radius=8
        )

        self.course.grid(
            row=2,
            column=2,
            padx=20,
            pady=(0, 15),
            sticky="ew"
        )

        # ==========================
        # Date
        # ==========================

        ctk.CTkLabel(
            form_card,
            text="Attendance Date",
            font=("Arial", 13, "bold"),
            text_color="#475569"
        ).grid(
            row=3,
            column=0,
            padx=20,
            pady=(5, 5),
            sticky="w"
        )

        self.attendance_date = ctk.CTkEntry(
            form_card,
            width=220,
            height=38,
            corner_radius=8
        )

        self.attendance_date.grid(
            row=4,
            column=0,
            padx=20,
            pady=(0, 18),
            sticky="ew"
        )

        self.attendance_date.insert(
            0,
            str(date.today())
        )

        # ==========================
        # Status
        # ==========================

        ctk.CTkLabel(
            form_card,
            text="Attendance Status",
            font=("Arial", 13, "bold"),
            text_color="#475569"
        ).grid(
            row=3,
            column=1,
            padx=20,
            pady=(5, 5),
            sticky="w"
        )

        self.status = ctk.CTkComboBox(
            form_card,
            values=[
                "Present",
                "Absent",
                "Leave"
            ],
            width=220,
            height=38,
            corner_radius=8,
            button_color=self.primary,
            button_hover_color=self.primary_hover
        )

        self.status.grid(
            row=4,
            column=1,
            padx=20,
            pady=(0, 18),
            sticky="ew"
        )

        self.status.set("Present")

        # =====================================================
        # Button Card
        # =====================================================

        button_card = ctk.CTkFrame(
            self.main_frame,
            fg_color=self.card_color,
            corner_radius=15
        )

        button_card.pack(
            fill="x",
            padx=20,
            pady=5
        )

        ctk.CTkLabel(
            button_card,
            text="Actions",
            font=("Arial", 16, "bold"),
            text_color="#1E293B"
        ).pack(
            side="left",
            padx=(20, 15)
        )

        # Add

        ctk.CTkButton(
            button_card,
            text="＋  Add",
            width=120,
            height=38,
            corner_radius=8,
            fg_color=self.success,
            hover_color=self.success_hover,
            font=("Arial", 13, "bold"),
            command=self.add_attendance
        ).pack(
            side="left",
            padx=5,
            pady=12
        )

        # Update

        ctk.CTkButton(
            button_card,
            text="✎  Update",
            width=120,
            height=38,
            corner_radius=8,
            fg_color=self.primary,
            hover_color=self.primary_hover,
            font=("Arial", 13, "bold"),
            command=self.update_attendance
        ).pack(
            side="left",
            padx=5,
            pady=12
        )

        # Delete

        ctk.CTkButton(
            button_card,
            text="✕  Delete",
            width=120,
            height=38,
            corner_radius=8,
            fg_color=self.danger,
            hover_color=self.danger_hover,
            font=("Arial", 13, "bold"),
            command=self.delete_attendance
        ).pack(
            side="left",
            padx=5,
            pady=12
        )

        # Clear

        ctk.CTkButton(
            button_card,
            text="⟳  Clear",
            width=120,
            height=38,
            corner_radius=8,
            fg_color=self.secondary,
            hover_color=self.secondary_hover,
            font=("Arial", 13, "bold"),
            command=self.clear_fields
        ).pack(
            side="left",
            padx=5,
            pady=12
        )

        # =====================================================
        # Search Card
        # =====================================================

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
            text="🔎",
            font=("Arial", 20)
        ).pack(
            side="left",
            padx=(20, 5),
            pady=12
        )

        ctk.CTkLabel(
            search_card,
            text="Search Attendance",
            font=("Arial", 15, "bold"),
            text_color="#1E293B"
        ).pack(
            side="left",
            padx=5
        )

        self.search_entry = ctk.CTkEntry(
            search_card,
            width=300,
            height=38,
            placeholder_text="Student ID / Name / Course",
            corner_radius=8
        )

        self.search_entry.pack(
            side="left",
            padx=15,
            pady=10
        )

        ctk.CTkButton(
            search_card,
            text="Search",
            width=110,
            height=38,
            corner_radius=8,
            fg_color=self.primary,
            hover_color=self.primary_hover,
            command=self.search_attendance
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
            fg_color=self.secondary,
            hover_color=self.secondary_hover,
            command=self.show_all_attendance
        ).pack(
            side="left",
            padx=5
        )

        # =====================================================
        # Table Card
        # =====================================================

        table_card = ctk.CTkFrame(
            self.main_frame,
            fg_color=self.card_color,
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
            text="Attendance Records",
            font=("Arial", 17, "bold"),
            text_color="#1E293B"
        ).pack(
            anchor="w",
            padx=20,
            pady=(15, 8)
        )

        # =====================================================
        # Treeview Style
        # =====================================================

        style = ttk.Style()

        try:
            style.theme_use("clam")
        except:
            pass

        style.configure(
            "Attendance.Treeview",
            background="#FFFFFF",
            foreground="#334155",
            rowheight=38,
            fieldbackground="#FFFFFF",
            font=("Arial", 11)
        )

        style.configure(
            "Attendance.Treeview.Heading",
            background="#2563EB",
            foreground="white",
            font=("Arial", 11, "bold"),
            padding=8
        )

        style.map(
            "Attendance.Treeview",
            background=[
                ("selected", "#DBEAFE")
            ],
            foreground=[
                ("selected", "#1E3A8A")
            ]
        )

        # =====================================================
        # Table
        # =====================================================

        table_frame = ctk.CTkFrame(
            table_card,
            fg_color="#FFFFFF",
            corner_radius=8
        )

        table_frame.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=(0, 15)
        )

        columns = (
            "Student ID",
            "Student Name",
            "Course",
            "Date",
            "Status"
        )

        self.attendance_table = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            style="Attendance.Treeview"
        )

        # Column configuration

        widths = {
            "Student ID": 130,
            "Student Name": 220,
            "Course": 180,
            "Date": 150,
            "Status": 140
        }

        for col in columns:

            self.attendance_table.heading(
                col,
                text=col
            )

            self.attendance_table.column(
                col,
                width=widths[col],
                anchor="center"
            )

        # Scrollbar

        scrollbar = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=self.attendance_table.yview
        )

        self.attendance_table.configure(
            yscrollcommand=scrollbar.set
        )

        self.attendance_table.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        # =====================================================
        # Table Tags
        # =====================================================

        self.attendance_table.tag_configure(
            "present",
            background="#ECFDF5",
            foreground="#166534"
        )

        self.attendance_table.tag_configure(
            "absent",
            background="#FEF2F2",
            foreground="#991B1B"
        )

        self.attendance_table.tag_configure(
            "leave",
            background="#FFFBEB",
            foreground="#92400E"
        )

        # Load Records

        self.load_attendance()

        # Select Event

        self.attendance_table.bind(
            "<<TreeviewSelect>>",
            self.select_attendance
        )

    # =========================================================
    # ADD ATTENDANCE
    # =========================================================

    def add_attendance(self):

        student_id = self.student_id.get().strip()
        student_name = self.student_name.get().strip()
        course = self.course.get().strip()
        attendance_date = self.attendance_date.get().strip()
        status = self.status.get()

        if student_id == "" or student_name == "":

            messagebox.showerror(
                "Required Fields",
                "Please enter Student ID and Student Name."
            )

            return

        try:

            self.database.add_attendance(
                student_id,
                student_name,
                course,
                attendance_date,
                status
            )

            self.load_attendance()
            self.clear_fields()

            messagebox.showinfo(
                "Success",
                "Attendance Added Successfully."
            )

        except Exception as e:

            messagebox.showerror(
                "Database Error",
                str(e)
            )

    # =========================================================
    # LOAD ATTENDANCE
    # =========================================================

    def load_attendance(self):

        for item in self.attendance_table.get_children():
            self.attendance_table.delete(item)

        try:

            attendance = self.database.fetch_attendance()

            for row in attendance:

                status = str(row[5]).lower()

                if status == "present":
                    tag = "present"

                elif status == "absent":
                    tag = "absent"

                else:
                    tag = "leave"

                self.attendance_table.insert(
                    "",
                    "end",
                    values=(
                        row[1],
                        row[2],
                        row[3],
                        row[4],
                        row[5]
                    ),
                    tags=(tag,)
                )

        except Exception as e:

            print("Attendance Load Error:", e)

    # =========================================================
    # SELECT ATTENDANCE
    # =========================================================

    def select_attendance(self, event):

        selected = self.attendance_table.focus()

        if not selected:
            return

        data = self.attendance_table.item(
            selected
        )["values"]

        if not data:
            return

        self.student_id.delete(0, "end")
        self.student_id.insert(0, data[0])

        self.student_name.delete(0, "end")
        self.student_name.insert(0, data[1])

        self.course.delete(0, "end")
        self.course.insert(0, data[2])

        self.attendance_date.delete(0, "end")
        self.attendance_date.insert(0, data[3])

        self.status.set(data[4])

    # =========================================================
    # UPDATE ATTENDANCE
    # =========================================================

    def update_attendance(self):

        student_id = self.student_id.get().strip()

        if student_id == "":

            messagebox.showerror(
                "Error",
                "Please select an attendance record first."
            )

            return

        try:

            self.database.update_attendance(
                self.student_id.get(),
                self.student_name.get(),
                self.course.get(),
                self.attendance_date.get(),
                self.status.get()
            )

            self.load_attendance()
            self.clear_fields()

            messagebox.showinfo(
                "Success",
                "Attendance Updated Successfully."
            )

        except Exception as e:

            messagebox.showerror(
                "Database Error",
                str(e)
            )

    # =========================================================
    # DELETE ATTENDANCE
    # =========================================================

    def delete_attendance(self):

        student_id = self.student_id.get().strip()

        if student_id == "":

            messagebox.showerror(
                "Error",
                "Please select an attendance record first."
            )

            return

        confirm = messagebox.askyesno(
            "Confirm Delete",
            "Are you sure you want to delete this attendance record?"
        )

        if not confirm:
            return

        try:

            self.database.delete_attendance(
                student_id
            )

            self.load_attendance()
            self.clear_fields()

            messagebox.showinfo(
                "Success",
                "Attendance Deleted Successfully."
            )

        except Exception as e:

            messagebox.showerror(
                "Database Error",
                str(e)
            )

    # =========================================================
    # SEARCH ATTENDANCE
    # =========================================================

    def search_attendance(self):

        keyword = self.search_entry.get().strip()

        if keyword == "":
            self.load_attendance()
            return

        for item in self.attendance_table.get_children():
            self.attendance_table.delete(item)

        try:

            attendance = self.database.search_attendance(
                keyword
            )

            for row in attendance:

                status = str(row[5]).lower()

                if status == "present":
                    tag = "present"

                elif status == "absent":
                    tag = "absent"

                else:
                    tag = "leave"

                self.attendance_table.insert(
                    "",
                    "end",
                    values=(
                        row[1],
                        row[2],
                        row[3],
                        row[4],
                        row[5]
                    ),
                    tags=(tag,)
                )

        except Exception as e:

            messagebox.showerror(
                "Search Error",
                str(e)
            )

    # =========================================================
    # SHOW ALL
    # =========================================================

    def show_all_attendance(self):

        self.search_entry.delete(
            0,
            "end"
        )

        self.load_attendance()

    # =========================================================
    # CLEAR FIELDS
    # =========================================================

    def clear_fields(self):

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

        self.attendance_date.delete(
            0,
            "end"
        )

        self.attendance_date.insert(
            0,
            str(date.today())
        )

        self.status.set(
            "Present"
        )
