from tkinter import messagebox
from datetime import datetime
import customtkinter as ctk

from students import StudentModule
from teachers import TeacherModule
from courses import CourseModule
from fees import FeeModule
from attendance import AttendanceModule
from exam import ExamModule
from result import ResultModule
from reports import ReportsModule
from settings import SettingsModule


class Dashboard:

    # ======================================
    # CONSTRUCTOR
    # ======================================

    def __init__(self, root, database):

        self.root = root
        self.database = database

        # Remove previous widgets
        for widget in self.root.winfo_children():
            widget.destroy()

        # ======================================
        # WINDOW
        # ======================================

        self.root.title("Student Management System ERP")
        self.root.geometry("1450x850")
        self.root.minsize(1100, 700)

        # ======================================
        # COLORS
        # ======================================

        self.primary = "#2563EB"
        self.success = "#16A34A"
        self.warning = "#F59E0B"
        self.danger = "#DC2626"
        self.purple = "#7C3AED"
        self.cyan = "#0891B2"

        self.bg = "#F8FAFC"
        self.card_bg = "#FFFFFF"
        self.sidebar_bg = "#1E293B"

        self.text = "#111827"
        self.light_text = "#6B7280"

        # ======================================
        # FONTS
        # ======================================

        self.title_font = ("Segoe UI", 28, "bold")
        self.heading_font = ("Segoe UI", 22, "bold")
        self.card_title = ("Segoe UI", 15, "bold")
        self.card_value = ("Segoe UI", 30, "bold")
        self.button_font = ("Segoe UI", 14, "bold")

        # ======================================
        # VARIABLES
        # ======================================

        self.sidebar_width = 230
        self.sidebar_visible = True

        self.header = None
        self.main_frame = None
        self.sidebar = None
        self.content = None

        self.datetime_label = None
        self.welcome_label = None

        self.lbl_students = None
        self.lbl_teachers = None
        self.lbl_courses = None
        self.lbl_fees = None
        self.lbl_results = None
        self.lbl_exams = None

        self.cards = []
        self.menu_buttons = []

        self.datetime_after_id = None

        # ======================================
        # CREATE UI
        # ======================================

        self.create_ui()

    # ======================================
    # CREATE UI
    # ======================================

    def create_ui(self):

        # ======================================
        # HEADER
        # ======================================

        self.header = ctk.CTkFrame(
            self.root,
            height=70,
            fg_color=self.primary,
            corner_radius=0
        )

        self.header.pack(fill="x")
        self.header.pack_propagate(False)

        left_header = ctk.CTkFrame(
            self.header,
            fg_color="transparent"
        )

        left_header.pack(
            side="left",
            padx=15,
            fill="y"
        )

        self.toggle_btn = ctk.CTkButton(
            left_header,
            text="☰",
            width=45,
            height=40,
            fg_color="transparent",
            hover_color="#1D4ED8",
            font=("Segoe UI", 22, "bold"),
            command=self.toggle_sidebar
        )

        self.toggle_btn.pack(
            side="left",
            padx=(5, 10),
            pady=15
        )

        ctk.CTkLabel(
            left_header,
            text="🎓 Student Management System ERP",
            font=("Segoe UI", 24, "bold"),
            text_color="white"
        ).pack(
            side="left",
            pady=18
        )

        # ======================================
        # MAIN FRAME
        # ======================================

        self.main_frame = ctk.CTkFrame(
            self.root,
            fg_color=self.bg,
            corner_radius=0
        )

        self.main_frame.pack(
            fill="both",
            expand=True
        )

        # ======================================
        # SIDEBAR
        # ======================================

        self.create_sidebar()

        # ======================================
        # CONTENT
        # ======================================

        self.content = ctk.CTkScrollableFrame(
            self.main_frame,
            fg_color=self.bg,
            corner_radius=0
        )

        self.content.pack(
            side="left",
            fill="both",
            expand=True
        )

        # ======================================
        # SHOW DASHBOARD
        # ======================================

        self.create_dashboard_content()

    # ======================================
    # CREATE SIDEBAR
    # ======================================

    def create_sidebar(self):

        self.sidebar = ctk.CTkFrame(
            self.main_frame,
            width=self.sidebar_width,
            fg_color=self.sidebar_bg,
            corner_radius=0
        )

        self.sidebar.pack(
            side="left",
            fill="y"
        )

        self.sidebar.pack_propagate(False)

        # ======================================
        # SIDEBAR TITLE
        # ======================================

        ctk.CTkLabel(
            self.sidebar,
            text="🎓 ERP",
            font=("Segoe UI", 28, "bold"),
            text_color="white"
        ).pack(
            pady=(25, 5)
        )

        ctk.CTkLabel(
            self.sidebar,
            text="Admin Panel",
            font=("Segoe UI", 14),
            text_color="#CBD5E1"
        ).pack(
            pady=(0, 25)
        )

        # ======================================
        # MENU ITEMS
        # ======================================

        menu_items = [
            ("🏠", "Dashboard"),
            ("👨‍🎓", "Students"),
            ("👨‍🏫", "Teachers"),
            ("📚", "Courses"),
            ("💰", "Fees"),
            ("📅", "Attendance"),
            ("📝", "Result"),
            ("📖", "Exam"),
            ("📊", "Reports"),
            ("⚙", "Settings"),
            ("🚪", "Logout")
        ]

        for icon, module in menu_items:

            btn = ctk.CTkButton(
                self.sidebar,
                text=f"{icon}   {module}",
                width=200,
                height=45,
                fg_color="transparent",
                hover_color="#334155",
                corner_radius=10,
                anchor="w",
                font=self.button_font,
                command=lambda m=module: self.menu_click(m)
            )

            btn.pack(
                fill="x",
                padx=12,
                pady=5
            )

            self.menu_buttons.append(btn)

    # ======================================
    # CREATE DASHBOARD CONTENT
    # ======================================

    def create_dashboard_content(self):

        # Cancel old datetime callback
        if self.datetime_after_id is not None:

            try:
                self.root.after_cancel(
                    self.datetime_after_id
                )
            except Exception:
                pass

            self.datetime_after_id = None

        # Clear content
        for widget in self.content.winfo_children():
            widget.destroy()

        self.datetime_label = None
        self.welcome_label = None

        self.lbl_students = None
        self.lbl_teachers = None
        self.lbl_courses = None
        self.lbl_fees = None
        self.lbl_results = None
        self.lbl_exams = None

        self.cards.clear()

        # ======================================
        # TOP HEADER
        # ======================================

        top_frame = ctk.CTkFrame(
            self.content,
            fg_color="transparent"
        )

        top_frame.pack(
            fill="x",
            padx=20,
            pady=(20, 10)
        )

        self.welcome_label = ctk.CTkLabel(
            top_frame,
            text="Welcome Admin 👋",
            font=self.title_font,
            text_color=self.text
        )

        self.welcome_label.pack(
            side="left"
        )

        self.datetime_label = ctk.CTkLabel(
            top_frame,
            text="",
            font=("Segoe UI", 15),
            text_color=self.light_text
        )

        self.datetime_label.pack(
            side="right"
        )

        # ======================================
        # DASHBOARD OVERVIEW
        # ======================================

        ctk.CTkLabel(
            self.content,
            text="Dashboard Overview",
            font=self.heading_font,
            text_color=self.text
        ).pack(
            anchor="w",
            padx=20,
            pady=(5, 15)
        )

        # ======================================
        # DASHBOARD CARDS
        # ======================================

        card_frame = ctk.CTkFrame(
            self.content,
            fg_color="transparent"
        )

        card_frame.pack(
            fill="x",
            padx=20
        )

        for i in range(3):
            card_frame.grid_columnconfigure(
                i,
                weight=1
            )

        card_data = [
            (
                "👨‍🎓 Students",
                self.database.count_students(),
                self.primary
            ),
            (
                "👨‍🏫 Teachers",
                self.database.count_teachers(),
                self.success
            ),
            (
                "📚 Courses",
                self.database.count_courses(),
                self.warning
            ),
            (
                "💰 Fees",
                self.database.count_fees(),
                self.danger
            ),
            (
                "📝 Results",
                self.database.count_results(),
                self.purple
            ),
            (
                "📖 Exams",
                self.database.count_exams(),
                self.cyan
            )
        ]

        for index, (title, value, color) in enumerate(card_data):

            card = ctk.CTkFrame(
                card_frame,
                fg_color=color,
                corner_radius=15,
                height=130
            )

            card.grid(
                row=index // 3,
                column=index % 3,
                padx=10,
                pady=10,
                sticky="nsew"
            )

            card.pack_propagate(False)

            ctk.CTkLabel(
                card,
                text=title,
                font=self.card_title,
                text_color="white"
            ).pack(
                pady=(20, 5)
            )

            value_label = ctk.CTkLabel(
                card,
                text=str(value),
                font=self.card_value,
                text_color="white"
            )

            value_label.pack()

            self.cards.append(value_label)

            if index == 0:
                self.lbl_students = value_label

            elif index == 1:
                self.lbl_teachers = value_label

            elif index == 2:
                self.lbl_courses = value_label

            elif index == 3:
                self.lbl_fees = value_label

            elif index == 4:
                self.lbl_results = value_label

            elif index == 5:
                self.lbl_exams = value_label

        # ======================================
        # QUICK ACTIONS
        # ======================================

        quick_frame = ctk.CTkFrame(
            self.content,
            fg_color=self.card_bg,
            corner_radius=15
        )

        quick_frame.pack(
            fill="x",
            padx=20,
            pady=20
        )

        ctk.CTkLabel(
            quick_frame,
            text="⚡ Quick Actions",
            font=("Segoe UI", 20, "bold"),
            text_color=self.text
        ).pack(
            anchor="w",
            padx=20,
            pady=(15, 10)
        )

        button_frame = ctk.CTkFrame(
            quick_frame,
            fg_color="transparent"
        )

        button_frame.pack(
            pady=(5, 20)
        )

        buttons = [
            ("👨‍🎓 Add Student", self.primary, "Students"),
            ("👨‍🏫 Add Teacher", self.success, "Teachers"),
            ("📚 Add Course", self.warning, "Courses"),
            ("💰 Fee Module", self.danger, "Fees"),
            ("📝 Result Module", self.purple, "Result"),
            ("📖 Exam Module", self.cyan, "Exam")
        ]

        for i, (text, color, module) in enumerate(buttons):

            ctk.CTkButton(
                button_frame,
                text=text,
                width=180,
                height=45,
                fg_color=color,
                hover_color=color,
                font=self.button_font,
                command=lambda m=module: self.menu_click(m)
            ).grid(
                row=i // 3,
                column=i % 3,
                padx=10,
                pady=10
            )

        # ======================================
        # SYSTEM INFORMATION
        # ======================================

        info_frame = ctk.CTkFrame(
            self.content,
            fg_color=self.card_bg,
            corner_radius=15
        )

        info_frame.pack(
            fill="x",
            padx=20,
            pady=(0, 20)
        )

        ctk.CTkLabel(
            info_frame,
            text="📊 System Information",
            font=("Segoe UI", 20, "bold"),
            text_color=self.text
        ).pack(
            anchor="w",
            padx=20,
            pady=(15, 15)
        )

        info_grid = ctk.CTkFrame(
            info_frame,
            fg_color="transparent"
        )

        info_grid.pack(
            fill="x",
            padx=20,
            pady=(0, 20)
        )

        information = [
            ("👨‍🎓 Students", self.database.count_students()),
            ("👨‍🏫 Teachers", self.database.count_teachers()),
            ("📚 Courses", self.database.count_courses()),
            ("💰 Fees", self.database.count_fees()),
            ("📝 Results", self.database.count_results()),
            ("📖 Exams", self.database.count_exams())
        ]

        for i, (title, value) in enumerate(information):

            info_grid.grid_columnconfigure(
                i % 3,
                weight=1
            )

            box = ctk.CTkFrame(
                info_grid,
                fg_color="#EEF2FF",
                corner_radius=12,
                height=90
            )

            box.grid(
                row=i // 3,
                column=i % 3,
                padx=10,
                pady=10,
                sticky="nsew"
            )

            box.pack_propagate(False)

            ctk.CTkLabel(
                box,
                text=title,
                font=("Segoe UI", 14, "bold"),
                text_color=self.text
            ).pack(
                pady=(12, 2)
            )

            ctk.CTkLabel(
                box,
                text=str(value),
                font=("Segoe UI", 22, "bold"),
                text_color=self.primary
            ).pack()

        # ======================================
        # FOOTER
        # ======================================

        ctk.CTkLabel(
            self.content,
            text="© 2026 Student Management System ERP | Developed by Durgesh Gupta",
            font=("Segoe UI", 12),
            text_color="gray"
        ).pack(
            pady=20
        )

        # ======================================
        # REFRESH
        # ======================================

        self.refresh_dashboard()
        self.update_datetime()

    # ======================================
    # REFRESH DASHBOARD
    # ======================================

    def refresh_dashboard(self):

        try:

            if self.lbl_students is not None:
                self.lbl_students.configure(
                    text=str(
                        self.database.count_students()
                    )
                )

            if self.lbl_teachers is not None:
                self.lbl_teachers.configure(
                    text=str(
                        self.database.count_teachers()
                    )
                )

            if self.lbl_courses is not None:
                self.lbl_courses.configure(
                    text=str(
                        self.database.count_courses()
                    )
                )

            if self.lbl_fees is not None:
                self.lbl_fees.configure(
                    text=str(
                        self.database.count_fees()
                    )
                )

            if self.lbl_results is not None:
                self.lbl_results.configure(
                    text=str(
                        self.database.count_results()
                    )
                )

            if self.lbl_exams is not None:
                self.lbl_exams.configure(
                    text=str(
                        self.database.count_exams()
                    )
                )

        except Exception as error:

            print(
                "Dashboard refresh error:",
                error
            )

    # ======================================
    # UPDATE DATE & TIME
    # ======================================

    def update_datetime(self):

        if self.datetime_label is None:
            return

        try:

            if not self.datetime_label.winfo_exists():
                return

        except Exception:
            return

        current = datetime.now().strftime(
            "%d %b %Y | %I:%M:%S %p"
        )

        try:

            self.datetime_label.configure(
                text=current
            )

        except Exception:
            return

        self.datetime_after_id = self.root.after(
            1000,
            self.update_datetime
        )

    # ======================================
    # TOGGLE SIDEBAR
    # ======================================

    def toggle_sidebar(self):

        if self.sidebar_visible:

            self.sidebar.pack_forget()
            self.sidebar_visible = False

        else:

            self.sidebar.pack(
                side="left",
                fill="y"
            )

            self.sidebar.pack_propagate(False)
            self.sidebar_visible = True

    # ======================================
    # MENU CLICK
    # ======================================

    def menu_click(self, module):

        # ======================================
        # LOGOUT
        # ======================================

        if module == "Logout":

            self.logout()
            return

        # ======================================
        # DASHBOARD
        # ======================================

        if module == "Dashboard":

            self.create_dashboard_content()
            return

        # ======================================
        # CLEAR CONTENT
        # ======================================

        for widget in self.content.winfo_children():
            widget.destroy()

        # ======================================
        # STUDENTS
        # ======================================

        if module == "Students":

            StudentModule(
                self.content,
                self.database
            )

        # ======================================
        # TEACHERS
        # ======================================

        elif module == "Teachers":

            TeacherModule(
                self.content,
                self.database
            )

        # ======================================
        # COURSES
        # ======================================

        elif module == "Courses":

            CourseModule(
                self.content,
                self.database
            )

        # ======================================
        # FEES
        # ======================================

        elif module == "Fees":

            FeeModule(
                self.content,
                self.database
            )

        # ======================================
        # ATTENDANCE
        # ======================================

        elif module == "Attendance":

            AttendanceModule(
                self.content,
                self.database
            )

        # ======================================
        # RESULT
        # ======================================

        elif module == "Result":

            ResultModule(
                self.content,
                self.database
            )

        # ======================================
        # EXAM
        # ======================================

        elif module == "Exam":

            ExamModule(
                self.content,
                self.database
            )

        # ======================================
        # REPORTS
        # ======================================

        elif module == "Reports":

            ReportsModule(
                self.content,
                self.database
            )

        # ======================================
        # SETTINGS
        # ======================================

        elif module == "Settings":

            SettingsModule(
                self.content,
                self.database
            )

    # ======================================
    # LOGOUT
    # ======================================

    def logout(self):

        answer = messagebox.askyesno(
            "Logout",
            "Are you sure you want to logout?"
        )

        if not answer:
            return

        # Cancel datetime callback
        if self.datetime_after_id is not None:

            try:
                self.root.after_cancel(
                    self.datetime_after_id
                )
            except Exception:
                pass

            self.datetime_after_id = None

        # Remove dashboard
        for widget in self.root.winfo_children():
            widget.destroy()

        from login import LoginWindow

        LoginWindow(
            self.root,
            self.database
        )


# ======================================
# RUN FILE
# ======================================

if __name__ == "__main__":

    from database import Database

    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()

    database = Database()

    Dashboard(
        root,
        database
    )

    root.mainloop()