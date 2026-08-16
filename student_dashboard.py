
import customtkinter as ctk
from tkinter import messagebox
from PIL import Image
import os


class StudentDashboard:

    # =========================================================
    # INITIALIZATION
    # =========================================================

    def __init__(self, parent, database, student_id, on_logout=None):

        self.parent = parent
        self.database = database
        self.student_id = student_id
        self.on_logout = on_logout

        self.student = None

        # Colors
        self.bg_color = "#F5F7FB"
        self.sidebar_color = "#172033"
        self.card_color = "#FFFFFF"
        self.primary = "#2563EB"
        self.success = "#059669"
        self.warning = "#D97706"
        self.danger = "#DC2626"
        self.text_dark = "#172033"
        self.text_gray = "#667085"
        self.border = "#E5E7EB"

        self.load_student()

        if not self.student:
            messagebox.showerror(
                "Student Error",
                "Student record could not be found."
            )
            return

        self.create_interface()

        self.show_dashboard()

    # =========================================================
    # LOAD STUDENT
    # =========================================================

    def load_student(self):

        try:

            self.student = self.database.get_student(
                self.student_id
            )

        except Exception as e:

            print("Student Loading Error:", e)

            self.student = None

    # =========================================================
    # CREATE MAIN INTERFACE
    # =========================================================

    def create_interface(self):

        # Remove old widgets
        for widget in self.parent.winfo_children():
            widget.destroy()

        # Main container
        self.main_frame = ctk.CTkFrame(
            self.parent,
            fg_color=self.bg_color,
            corner_radius=0
        )

        self.main_frame.pack(
            fill="both",
            expand=True
        )

        # =====================================================
        # SIDEBAR
        # =====================================================

        self.sidebar = ctk.CTkFrame(
            self.main_frame,
            width=245,
            corner_radius=0,
            fg_color=self.sidebar_color
        )

        self.sidebar.pack(
            side="left",
            fill="y"
        )

        self.sidebar.pack_propagate(False)

        # =====================================================
        # SIDEBAR HEADER
        # =====================================================

        logo = ctk.CTkLabel(
            self.sidebar,
            text="🎓  STUDENT ERP",
            font=("Segoe UI", 21, "bold"),
            text_color="white"
        )

        logo.pack(
            pady=(30, 5)
        )

        portal_label = ctk.CTkLabel(
            self.sidebar,
            text="Student Portal",
            font=("Segoe UI", 12),
            text_color="#AAB4C8"
        )

        portal_label.pack(
            pady=(0, 25)
        )

        # =====================================================
        # STUDENT MINI PROFILE
        # =====================================================

        profile_box = ctk.CTkFrame(
            self.sidebar,
            fg_color="#222D42",
            corner_radius=12
        )

        profile_box.pack(
            padx=15,
            pady=(0, 25),
            fill="x"
        )

        name = (
            f"{self.student[2]} "
            f"{self.student[3]}"
        ).strip()

        if not name:
            name = "Student"

        self.sidebar_name = ctk.CTkLabel(
            profile_box,
            text=name,
            font=("Segoe UI", 14, "bold"),
            text_color="white"
        )

        self.sidebar_name.pack(
            pady=(12, 2)
        )

        self.sidebar_id = ctk.CTkLabel(
            profile_box,
            text=f"ID: {self.student_id}",
            font=("Segoe UI", 11),
            text_color="#AAB4C8"
        )

        self.sidebar_id.pack(
            pady=(0, 12)
        )

        # =====================================================
        # NAVIGATION BUTTONS
        # =====================================================

        self.create_nav_button(
            "🏠   Dashboard",
            self.show_dashboard
        )

        self.create_nav_button(
            "👤   My Profile",
            self.show_profile
        )

        self.create_nav_button(
            "📊   Attendance",
            self.show_attendance
        )

        self.create_nav_button(
            "💰   Fees",
            self.show_fees
        )

        self.create_nav_button(
            "📝   Results",
            self.show_results
        )

        self.create_nav_button(
            "📅   Exams",
            self.show_exams
        )

        self.create_nav_button(
            "🔐   Change Password",
            self.show_change_password
        )

        # Spacer
        spacer = ctk.CTkFrame(
            self.sidebar,
            fg_color="transparent"
        )

        spacer.pack(
            expand=True,
            fill="both"
        )

        # =====================================================
        # LOGOUT BUTTON
        # =====================================================

        logout_button = ctk.CTkButton(
            self.sidebar,
            text="🚪   Logout",
            height=45,
            corner_radius=10,
            fg_color="#DC2626",
            hover_color="#B91C1C",
            font=("Segoe UI", 14, "bold"),
            command=self.logout
        )

        logout_button.pack(
            padx=15,
            pady=(10, 25),
            fill="x"
        )

        # =====================================================
        # CONTENT AREA
        # =====================================================

        self.content_area = ctk.CTkFrame(
            self.main_frame,
            fg_color=self.bg_color,
            corner_radius=0
        )

        self.content_area.pack(
            side="left",
            fill="both",
            expand=True
        )

        # =====================================================
        # TOP BAR
        # =====================================================

        self.topbar = ctk.CTkFrame(
            self.content_area,
            height=75,
            fg_color="white",
            corner_radius=0
        )

        self.topbar.pack(
            fill="x"
        )

        self.topbar.pack_propagate(False)

        self.page_title = ctk.CTkLabel(
            self.topbar,
            text="Dashboard",
            font=("Segoe UI", 25, "bold"),
            text_color=self.text_dark
        )

        self.page_title.pack(
            side="left",
            padx=30
        )

        self.welcome_label = ctk.CTkLabel(
            self.topbar,
            text=f"Welcome, {self.student[2]}",
            font=("Segoe UI", 13),
            text_color=self.text_gray
        )

        self.welcome_label.pack(
            side="right",
            padx=30
        )

        # =====================================================
        # CONTENT FRAME
        # =====================================================

        self.content = ctk.CTkScrollableFrame(
            self.content_area,
            fg_color=self.bg_color,
            corner_radius=0
        )

        self.content.pack(
            fill="both",
            expand=True,
            padx=5,
            pady=5
        )

    # =========================================================
    # NAV BUTTON
    # =========================================================

    def create_nav_button(self, text, command):

        button = ctk.CTkButton(
            self.sidebar,
            text=text,
            height=44,
            corner_radius=8,
            fg_color="transparent",
            hover_color="#29364F",
            anchor="w",
            font=("Segoe UI", 13),
            text_color="#E7ECF5",
            command=command
        )

        button.pack(
            padx=12,
            pady=3,
            fill="x"
        )

    # =========================================================
    # CLEAR CONTENT
    # =========================================================

    def clear_content(self):

        for widget in self.content.winfo_children():
            widget.destroy()

    # =========================================================
    # PAGE TITLE
    # =========================================================

    def set_page_title(self, title):

        self.page_title.configure(
            text=title
        )

    # =========================================================
    # DASHBOARD
    # =========================================================

    def show_dashboard(self):

        self.clear_content()

        self.set_page_title(
            "Dashboard"
        )

        # -----------------------------------------------------
        # Welcome Banner
        # -----------------------------------------------------

        first_name = self.student[2] or "Student"

        banner = ctk.CTkFrame(
            self.content,
            fg_color="#2563EB",
            corner_radius=16
        )

        banner.pack(
            fill="x",
            padx=20,
            pady=20
        )

        ctk.CTkLabel(
            banner,
            text=f"Welcome back, {first_name}! 👋",
            font=("Segoe UI", 25, "bold"),
            text_color="white"
        ).pack(
            anchor="w",
            padx=25,
            pady=(20, 3)
        )

        ctk.CTkLabel(
            banner,
            text="Here is your academic overview.",
            font=("Segoe UI", 13),
            text_color="#DBEAFE"
        ).pack(
            anchor="w",
            padx=25,
            pady=(0, 20)
        )

        # -----------------------------------------------------
        # Get Dashboard Data
        # -----------------------------------------------------

        try:

            data = self.database.get_student_dashboard_data(
                self.student_id
            )

        except Exception as e:

            print(
                "Dashboard Data Error:",
                e
            )

            data = None

        if not data:
            return

        attendance = data["attendance"]
        fee_summary = data["fee_summary"]

        result_count = data["result_count"]
        fee_count = data["fee_count"]
        exam_count = data["exam_count"]

        # -----------------------------------------------------
        # Statistics Cards
        # -----------------------------------------------------

        cards_frame = ctk.CTkFrame(
            self.content,
            fg_color="transparent"
        )

        cards_frame.pack(
            fill="x",
            padx=20,
            pady=(0, 15)
        )

        cards_frame.grid_columnconfigure(
            (0, 1, 2, 3),
            weight=1
        )

        self.create_stat_card(
            cards_frame,
            0,
            "📊",
            "Attendance",
            f"{attendance['attendance_percentage']}%",
            "#2563EB"
        )

        self.create_stat_card(
            cards_frame,
            1,
            "📝",
            "Results",
            str(result_count),
            "#7C3AED"
        )

        self.create_stat_card(
            cards_frame,
            2,
            "💰",
            "Fee Records",
            str(fee_count),
            "#059669"
        )

        self.create_stat_card(
            cards_frame,
            3,
            "📅",
            "Exams",
            str(exam_count),
            "#D97706"
        )

        # -----------------------------------------------------
        # Quick Information
        # -----------------------------------------------------

        info_frame = ctk.CTkFrame(
            self.content,
            fg_color="transparent"
        )

        info_frame.pack(
            fill="x",
            padx=20,
            pady=10
        )

        info_frame.grid_columnconfigure(
            (0, 1),
            weight=1
        )

        # Academic Card
        academic_card = ctk.CTkFrame(
            info_frame,
            fg_color="white",
            corner_radius=14,
            border_width=1,
            border_color=self.border
        )

        academic_card.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(0, 8)
        )

        ctk.CTkLabel(
            academic_card,
            text="🎓 Academic Information",
            font=("Segoe UI", 17, "bold"),
            text_color=self.text_dark
        ).pack(
            anchor="w",
            padx=20,
            pady=(18, 15)
        )

        self.info_row(
            academic_card,
            "Student ID",
            self.student[1]
        )

        self.info_row(
            academic_card,
            "Course",
            self.student[5]
        )

        self.info_row(
            academic_card,
            "Semester",
            self.student[6]
        )

        # Fee Card
        fee_card = ctk.CTkFrame(
            info_frame,
            fg_color="white",
            corner_radius=14,
            border_width=1,
            border_color=self.border
        )

        fee_card.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=(8, 0)
        )

        ctk.CTkLabel(
            fee_card,
            text="💰 Fee Overview",
            font=("Segoe UI", 17, "bold"),
            text_color=self.text_dark
        ).pack(
            anchor="w",
            padx=20,
            pady=(18, 15)
        )

        self.info_row(
            fee_card,
            "Total Amount",
            f"₹ {fee_summary['total_amount']:.2f}"
        )

        self.info_row(
            fee_card,
            "Paid Records",
            str(fee_summary["paid_records"])
        )

        self.info_row(
            fee_card,
            "Pending Records",
            str(fee_summary["pending_records"])
        )

        # -----------------------------------------------------
        # Attendance Summary
        # -----------------------------------------------------

        attendance_card = ctk.CTkFrame(
            self.content,
            fg_color="white",
            corner_radius=14,
            border_width=1,
            border_color=self.border
        )

        attendance_card.pack(
            fill="x",
            padx=20,
            pady=15
        )

        ctk.CTkLabel(
            attendance_card,
            text="📊 Attendance Summary",
            font=("Segoe UI", 17, "bold"),
            text_color=self.text_dark
        ).pack(
            anchor="w",
            padx=20,
            pady=(18, 10)
        )

        summary = ctk.CTkFrame(
            attendance_card,
            fg_color="transparent"
        )

        summary.pack(
            fill="x",
            padx=20,
            pady=(0, 20)
        )

        summary.grid_columnconfigure(
            (0, 1, 2),
            weight=1
        )

        self.create_small_stat(
            summary,
            0,
            "Total Classes",
            attendance["total_classes"],
            "#475467"
        )

        self.create_small_stat(
            summary,
            1,
            "Present",
            attendance["present_classes"],
            "#059669"
        )

        self.create_small_stat(
            summary,
            2,
            "Absent",
            attendance["absent_classes"],
            "#DC2626"
        )

    # =========================================================
    # STAT CARD
    # =========================================================

    def create_stat_card(
        self,
        parent,
        column,
        icon,
        title,
        value,
        color
    ):

        card = ctk.CTkFrame(
            parent,
            fg_color="white",
            corner_radius=14,
            border_width=1,
            border_color=self.border
        )

        card.grid(
            row=0,
            column=column,
            sticky="nsew",
            padx=7
        )

        ctk.CTkLabel(
            card,
            text=icon,
            font=("Segoe UI Emoji", 24)
        ).pack(
            anchor="w",
            padx=18,
            pady=(15, 0)
        )

        ctk.CTkLabel(
            card,
            text=value,
            font=("Segoe UI", 25, "bold"),
            text_color=color
        ).pack(
            anchor="w",
            padx=18,
            pady=(5, 0)
        )

        ctk.CTkLabel(
            card,
            text=title,
            font=("Segoe UI", 12),
            text_color=self.text_gray
        ).pack(
            anchor="w",
            padx=18,
            pady=(0, 15)
        )

    # =========================================================
    # SMALL STAT
    # =========================================================

    def create_small_stat(
        self,
        parent,
        column,
        title,
        value,
        color
    ):

        frame = ctk.CTkFrame(
            parent,
            fg_color="#F8FAFC",
            corner_radius=10
        )

        frame.grid(
            row=0,
            column=column,
            sticky="ew",
            padx=5
        )

        ctk.CTkLabel(
            frame,
            text=str(value),
            font=("Segoe UI", 22, "bold"),
            text_color=color
        ).pack(
            pady=(12, 0)
        )

        ctk.CTkLabel(
            frame,
            text=title,
            font=("Segoe UI", 11),
            text_color=self.text_gray
        ).pack(
            pady=(0, 12)
        )

    # =========================================================
    # INFO ROW
    # =========================================================

    def info_row(
        self,
        parent,
        label,
        value
    ):

        row = ctk.CTkFrame(
            parent,
            fg_color="transparent"
        )

        row.pack(
            fill="x",
            padx=20,
            pady=5
        )

        ctk.CTkLabel(
            row,
            text=label,
            width=130,
            anchor="w",
            font=("Segoe UI", 12),
            text_color=self.text_gray
        ).pack(
            side="left"
        )

        ctk.CTkLabel(
            row,
            text=str(value or "-"),
            anchor="w",
            font=("Segoe UI", 12, "bold"),
            text_color=self.text_dark
        ).pack(
            side="left"
        )

    # =========================================================
    # PROFILE
    # =========================================================

    def show_profile(self):

        self.clear_content()

        self.set_page_title(
            "My Profile"
        )

        card = ctk.CTkFrame(
            self.content,
            fg_color="white",
            corner_radius=15,
            border_width=1,
            border_color=self.border
        )

        card.pack(
            fill="x",
            padx=25,
            pady=25
        )

        # Photo
        photo_frame = ctk.CTkFrame(
            card,
            width=150,
            height=150,
            fg_color="#EFF6FF",
            corner_radius=75
        )

        photo_frame.pack(
            pady=(25, 15)
        )

        photo_frame.pack_propagate(False)

        photo_loaded = False

        photo_path = self.student[8]

        if photo_path and os.path.exists(photo_path):

            try:

                image = Image.open(
                    photo_path
                )

                image = image.resize(
                    (120, 120)
                )

                photo = ctk.CTkImage(
                    light_image=image,
                    dark_image=image,
                    size=(120, 120)
                )

                label = ctk.CTkLabel(
                    photo_frame,
                    image=photo,
                    text=""
                )

                label.image = photo

                label.place(
                    relx=0.5,
                    rely=0.5,
                    anchor="center"
                )

                photo_loaded = True

            except Exception as e:

                print(
                    "Profile Photo Error:",
                    e
                )

        if not photo_loaded:

            ctk.CTkLabel(
                photo_frame,
                text="👤",
                font=("Segoe UI Emoji", 55)
            ).place(
                relx=0.5,
                rely=0.5,
                anchor="center"
            )

        name = (
            f"{self.student[2] or ''} "
            f"{self.student[3] or ''}"
        ).strip()

        ctk.CTkLabel(
            card,
            text=name or "Student",
            font=("Segoe UI", 24, "bold"),
            text_color=self.text_dark
        ).pack(
            pady=(0, 5)
        )

        ctk.CTkLabel(
            card,
            text=f"Student ID: {self.student[1]}",
            font=("Segoe UI", 13),
            text_color=self.text_gray
        ).pack(
            pady=(0, 25)
        )

        details = ctk.CTkFrame(
            card,
            fg_color="#F8FAFC",
            corner_radius=12
        )

        details.pack(
            fill="x",
            padx=25,
            pady=(0, 25)
        )

        self.info_row(
            details,
            "First Name",
            self.student[2]
        )

        self.info_row(
            details,
            "Last Name",
            self.student[3]
        )

        self.info_row(
            details,
            "Mobile",
            self.student[4]
        )

        self.info_row(
            details,
            "Course",
            self.student[5]
        )

        self.info_row(
            details,
            "Semester",
            self.student[6]
        )

    # =========================================================
    # ATTENDANCE
    # =========================================================

    def show_attendance(self):

        self.clear_content()

        self.set_page_title(
            "Attendance"
        )

        try:

            summary = (
                self.database.get_student_attendance_summary(
                    self.student_id
                )
            )

            records = (
                self.database.get_student_attendance(
                    self.student_id
                )
            )

        except Exception as e:

            messagebox.showerror(
                "Attendance Error",
                str(e)
            )

            return

        # Summary
        summary_card = ctk.CTkFrame(
            self.content,
            fg_color="white",
            corner_radius=15
        )

        summary_card.pack(
            fill="x",
            padx=25,
            pady=20
        )

        ctk.CTkLabel(
            summary_card,
            text="Attendance Overview",
            font=("Segoe UI", 19, "bold"),
            text_color=self.text_dark
        ).pack(
            anchor="w",
            padx=20,
            pady=(18, 12)
        )

        stats = ctk.CTkFrame(
            summary_card,
            fg_color="transparent"
        )

        stats.pack(
            fill="x",
            padx=20,
            pady=(0, 20)
        )

        stats.grid_columnconfigure(
            (0, 1, 2, 3),
            weight=1
        )

        self.create_small_stat(
            stats,
            0,
            "Total Classes",
            summary["total_classes"],
            "#475467"
        )

        self.create_small_stat(
            stats,
            1,
            "Present",
            summary["present_classes"],
            "#059669"
        )

        self.create_small_stat(
            stats,
            2,
            "Absent",
            summary["absent_classes"],
            "#DC2626"
        )

        self.create_small_stat(
            stats,
            3,
            "Percentage",
            f"{summary['attendance_percentage']}%",
            "#2563EB"
        )

        # Records
        self.create_section_title(
            "Attendance Records"
        )

        if not records:

            self.show_empty_message(
                "No attendance records found."
            )

            return

        for record in records:

            # id, student_id, student_name,
            # course, attendance_date, status

            status = str(
                record[5] or ""
            ).lower()

            color = (
                "#059669"
                if status == "present"
                else "#DC2626"
            )

            self.create_record_card(
                title=str(record[4]),
                subtitle=f"{record[3]}",
                right_text=str(record[5]),
                right_color=color
            )

    # =========================================================
    # FEES
    # =========================================================

    def show_fees(self):

        self.clear_content()

        self.set_page_title(
            "Fees"
        )

        try:

            records = self.database.get_student_fees(
                self.student_id
            )

            summary = self.database.get_student_fee_summary(
                self.student_id
            )

        except Exception as e:

            messagebox.showerror(
                "Fee Error",
                str(e)
            )

            return

        # Summary Cards

        cards = ctk.CTkFrame(
            self.content,
            fg_color="transparent"
        )

        cards.pack(
            fill="x",
            padx=20,
            pady=20
        )

        cards.grid_columnconfigure(
            (0, 1, 2),
            weight=1
        )

        self.create_stat_card(
            cards,
            0,
            "💰",
            "Total Amount",
            f"₹{summary['total_amount']:.2f}",
            "#2563EB"
        )

        self.create_stat_card(
            cards,
            1,
            "✅",
            "Paid",
            str(summary["paid_records"]),
            "#059669"
        )

        self.create_stat_card(
            cards,
            2,
            "⏳",
            "Pending",
            str(summary["pending_records"]),
            "#D97706"
        )

        self.create_section_title(
            "Fee Records"
        )

        if not records:

            self.show_empty_message(
                "No fee records found."
            )

            return

        for record in records:

            # id, student_id, student_name,
            # course, amount, status

            status = str(
                record[5] or ""
            )

            status_lower = status.lower()

            color = (
                "#059669"
                if status_lower == "paid"
                else "#D97706"
            )

            self.create_record_card(
                title=f"₹ {record[4]}",
                subtitle=(
                    f"{record[3]}  •  "
                    f"{record[2]}"
                ),
                right_text=status,
                right_color=color
            )

    # =========================================================
    # RESULTS
    # =========================================================

    def show_results(self):

        self.clear_content()

        self.set_page_title(
            "Results"
        )

        try:

            records = self.database.get_student_results(
                self.student_id
            )

        except Exception as e:

            messagebox.showerror(
                "Result Error",
                str(e)
            )

            return

        self.create_section_title(
            "Academic Results"
        )

        if not records:

            self.show_empty_message(
                "No result records found."
            )

            return

        for record in records:

            # id, student_id, student_name,
            # course, subject, marks,
            # grade, percentage, status

            self.create_result_card(
                subject=record[4],
                marks=record[5],
                grade=record[6],
                percentage=record[7],
                status=record[8]
            )

    # =========================================================
    # RESULT CARD
    # =========================================================

    def create_result_card(
        self,
        subject,
        marks,
        grade,
        percentage,
        status
    ):

        card = ctk.CTkFrame(
            self.content,
            fg_color="white",
            corner_radius=12,
            border_width=1,
            border_color=self.border
        )

        card.pack(
            fill="x",
            padx=25,
            pady=6
        )

        left = ctk.CTkFrame(
            card,
            fg_color="transparent"
        )

        left.pack(
            side="left",
            padx=20,
            pady=15
        )

        ctk.CTkLabel(
            left,
            text=str(subject),
            font=("Segoe UI", 15, "bold"),
            text_color=self.text_dark
        ).pack(
            anchor="w"
        )

        ctk.CTkLabel(
            left,
            text=f"Marks: {marks}    |    Percentage: {percentage}%",
            font=("Segoe UI", 12),
            text_color=self.text_gray
        ).pack(
            anchor="w",
            pady=(3, 0)
        )

        right = ctk.CTkFrame(
            card,
            fg_color="transparent"
        )

        right.pack(
            side="right",
            padx=20,
            pady=15
        )

        ctk.CTkLabel(
            right,
            text=f"Grade: {grade}",
            font=("Segoe UI", 14, "bold"),
            text_color=self.primary
        ).pack()

        ctk.CTkLabel(
            right,
            text=str(status),
            font=("Segoe UI", 11),
            text_color=self.success
            if str(status).lower() == "pass"
            else self.danger
        ).pack()

    # =========================================================
    # EXAMS
    # =========================================================

    def show_exams(self):

        self.clear_content()

        self.set_page_title(
            "Exams"
        )

        try:

            exams = self.database.get_student_exams(
                self.student[5],
                self.student[6]
            )

        except Exception as e:

            messagebox.showerror(
                "Exam Error",
                str(e)
            )

            return

        self.create_section_title(
            "Upcoming / Scheduled Exams"
        )

        if not exams:

            self.show_empty_message(
                "No exams found for your course and semester."
            )

            return

        for exam in exams:

            # id, exam_id, exam_name,
            # course, semester, exam_date, total_marks

            card = ctk.CTkFrame(
                self.content,
                fg_color="white",
                corner_radius=12,
                border_width=1,
                border_color=self.border
            )

            card.pack(
                fill="x",
                padx=25,
                pady=6
            )

            ctk.CTkLabel(
                card,
                text=str(exam[2]),
                font=("Segoe UI", 16, "bold"),
                text_color=self.text_dark
            ).pack(
                anchor="w",
                padx=20,
                pady=(15, 3)
            )

            ctk.CTkLabel(
                card,
                text=(
                    f"Exam ID: {exam[1]}    •    "
                    f"Course: {exam[3]}    •    "
                    f"Semester: {exam[4]}"
                ),
                font=("Segoe UI", 12),
                text_color=self.text_gray
            ).pack(
                anchor="w",
                padx=20
            )

            ctk.CTkLabel(
                card,
                text=(
                    f"📅 Date: {exam[5]}    "
                    f"•    Total Marks: {exam[6]}"
                ),
                font=("Segoe UI", 12, "bold"),
                text_color=self.primary
            ).pack(
                anchor="w",
                padx=20,
                pady=(5, 15)
            )

    # =========================================================
    # CHANGE PASSWORD
    # =========================================================

    def show_change_password(self):

        self.clear_content()

        self.set_page_title(
            "Change Password"
        )

        card = ctk.CTkFrame(
            self.content,
            width=500,
            fg_color="white",
            corner_radius=15,
            border_width=1,
            border_color=self.border
        )

        card.pack(
            padx=25,
            pady=30
        )

        ctk.CTkLabel(
            card,
            text="🔐 Change Password",
            font=("Segoe UI", 22, "bold"),
            text_color=self.text_dark
        ).pack(
            pady=(30, 5)
        )

        ctk.CTkLabel(
            card,
            text="Update your student portal password.",
            font=("Segoe UI", 12),
            text_color=self.text_gray
        ).pack(
            pady=(0, 25)
        )

        old_entry = ctk.CTkEntry(
            card,
            width=380,
            height=45,
            placeholder_text="Current Password",
            show="•"
        )

        old_entry.pack(
            pady=8
        )

        new_entry = ctk.CTkEntry(
            card,
            width=380,
            height=45,
            placeholder_text="New Password",
            show="•"
        )

        new_entry.pack(
            pady=8
        )

        confirm_entry = ctk.CTkEntry(
            card,
            width=380,
            height=45,
            placeholder_text="Confirm New Password",
            show="•"
        )

        confirm_entry.pack(
            pady=8
        )

        def update_password():

            old_password = old_entry.get().strip()
            new_password = new_entry.get().strip()
            confirm_password = confirm_entry.get().strip()

            if not old_password:

                messagebox.showwarning(
                    "Validation",
                    "Enter your current password."
                )

                return

            if not new_password:

                messagebox.showwarning(
                    "Validation",
                    "Enter a new password."
                )

                return

            if len(new_password) < 4:

                messagebox.showwarning(
                    "Validation",
                    "Password must contain at least 4 characters."
                )

                return

            if new_password != confirm_password:

                messagebox.showwarning(
                    "Validation",
                    "New passwords do not match."
                )

                return

            if old_password == new_password:

                messagebox.showwarning(
                    "Validation",
                    "New password must be different."
                )

                return

            try:

                success = (
                    self.database.change_student_password(
                        self.student_id,
                        old_password,
                        new_password
                    )
                )

                if success:

                    messagebox.showinfo(
                        "Success",
                        "Password changed successfully."
                    )

                    old_entry.delete(0, "end")
                    new_entry.delete(0, "end")
                    confirm_entry.delete(0, "end")

                else:

                    messagebox.showerror(
                        "Failed",
                        "Current password is incorrect."
                    )

            except Exception as e:

                messagebox.showerror(
                    "Error",
                    str(e)
                )

        ctk.CTkButton(
            card,
            text="Update Password",
            width=380,
            height=45,
            corner_radius=10,
            fg_color=self.primary,
            hover_color="#1D4ED8",
            font=("Segoe UI", 14, "bold"),
            command=update_password
        ).pack(
            pady=(20, 30)
        )

    # =========================================================
    # SECTION TITLE
    # =========================================================

    def create_section_title(self, title):

        ctk.CTkLabel(
            self.content,
            text=title,
            font=("Segoe UI", 19, "bold"),
            text_color=self.text_dark
        ).pack(
            anchor="w",
            padx=25,
            pady=(10, 12)
        )

    # =========================================================
    # RECORD CARD
    # =========================================================

    def create_record_card(
        self,
        title,
        subtitle,
        right_text,
        right_color
    ):

        card = ctk.CTkFrame(
            self.content,
            fg_color="white",
            corner_radius=12,
            border_width=1,
            border_color=self.border
        )

        card.pack(
            fill="x",
            padx=25,
            pady=5
        )

        left = ctk.CTkFrame(
            card,
            fg_color="transparent"
        )

        left.pack(
            side="left",
            padx=20,
            pady=14
        )

        ctk.CTkLabel(
            left,
            text=str(title),
            font=("Segoe UI", 14, "bold"),
            text_color=self.text_dark
        ).pack(
            anchor="w"
        )

        ctk.CTkLabel(
            left,
            text=str(subtitle),
            font=("Segoe UI", 11),
            text_color=self.text_gray
        ).pack(
            anchor="w",
            pady=(2, 0)
        )

        ctk.CTkLabel(
            card,
            text=str(right_text),
            font=("Segoe UI", 13, "bold"),
            text_color=right_color
        ).pack(
            side="right",
            padx=20
        )

    # =========================================================
    # EMPTY MESSAGE
    # =========================================================

    def show_empty_message(self, message):

        card = ctk.CTkFrame(
            self.content,
            fg_color="white",
            corner_radius=12
        )

        card.pack(
            fill="x",
            padx=25,
            pady=10
        )

        ctk.CTkLabel(
            card,
            text="📭",
            font=("Segoe UI Emoji", 35)
        ).pack(
            pady=(20, 5)
        )

        ctk.CTkLabel(
            card,
            text=message,
            font=("Segoe UI", 13),
            text_color=self.text_gray
        ).pack(
            pady=(0, 20)
        )

    # =========================================================
    # LOGOUT
    # =========================================================

    def logout(self):

        result = messagebox.askyesno(
            "Logout",
            "Are you sure you want to logout?"
        )

        if not result:
            return

        if self.on_logout:

            self.on_logout()

        else:

            for widget in self.parent.winfo_children():
                widget.destroy()
