
import customtkinter as ctk
from tkinter import messagebox

from database import Database
from dashboard import Dashboard


class LoginWindow:

    def __init__(self, root, database):

        self.root = root
        self.database = database

        # =================================================
        # WINDOW
        # =================================================

        self.root.title("Student Management System ERP")
        self.root.geometry("1100x650")
        self.root.minsize(950, 580)
        self.root.configure(fg_color="#F4F7FB")

        # =================================================
        # COLORS
        # =================================================

        self.blue = "#2563EB"
        self.dark_blue = "#1D4ED8"

        self.green = "#16A34A"
        self.dark_green = "#15803D"

        self.bg = "#F4F7FB"
        self.card = "#FFFFFF"

        self.text = "#111827"
        self.gray = "#6B7280"

        # =================================================
        # MAIN FRAME
        # =================================================

        self.main_frame = ctk.CTkFrame(
            self.root,
            fg_color=self.bg,
            corner_radius=0
        )

        self.main_frame.pack(
            fill="both",
            expand=True
        )

        # =================================================
        # LEFT PANEL
        # =================================================

        self.left_frame = ctk.CTkFrame(
            self.main_frame,
            width=470,
            fg_color=self.blue,
            corner_radius=0
        )

        self.left_frame.pack(
            side="left",
            fill="y"
        )

        self.left_frame.pack_propagate(False)

        # Decorative Circle

        ctk.CTkLabel(
            self.left_frame,
            text="●",
            font=("Arial", 90),
            text_color="#3B82F6"
        ).place(
            x=-35,
            y=-35
        )

        # Logo

        ctk.CTkLabel(
            self.left_frame,
            text="🎓",
            font=("Segoe UI Emoji", 90)
        ).pack(
            pady=(85, 10)
        )

        # Application Name

        ctk.CTkLabel(
            self.left_frame,
            text="STUDENT\nMANAGEMENT\nSYSTEM",
            font=("Segoe UI", 32, "bold"),
            text_color="white",
            justify="center"
        ).pack()

        # ERP

        ctk.CTkLabel(
            self.left_frame,
            text="E R P",
            font=("Segoe UI", 18, "bold"),
            text_color="#BFDBFE"
        ).pack(
            pady=(5, 15)
        )

        # Description

        ctk.CTkLabel(
            self.left_frame,
            text=(
                "A smart and modern solution\n"
                "for managing Students, Teachers,\n"
                "Fees, Attendance, Exams & Results."
            ),
            font=("Segoe UI", 15),
            text_color="#DBEAFE",
            justify="center"
        ).pack(
            pady=15
        )

        # =================================================
        # FEATURES
        # =================================================

        feature_frame = ctk.CTkFrame(
            self.left_frame,
            fg_color="#1D4ED8",
            corner_radius=15
        )

        feature_frame.pack(
            padx=45,
            pady=25,
            fill="x"
        )

        ctk.CTkLabel(
            feature_frame,
            text=(
                "✓  Student Management\n"
                "✓  Teacher Management\n"
                "✓  Fees & Attendance\n"
                "✓  Exams & Results\n"
                "✓  Student Portal"
            ),
            font=("Segoe UI", 13, "bold"),
            text_color="white",
            justify="left"
        ).pack(
            padx=20,
            pady=15
        )

        # =================================================
        # DEVELOPER
        # =================================================

        ctk.CTkLabel(
            self.left_frame,
            text="Developed by\nDurgesh Gupta",
            font=("Segoe UI", 14, "bold"),
            text_color="#DBEAFE",
            justify="center"
        ).pack(
            side="bottom",
            pady=25
        )

        # =================================================
        # RIGHT PANEL
        # =================================================

        self.right_frame = ctk.CTkFrame(
            self.main_frame,
            fg_color=self.bg,
            corner_radius=0
        )

        self.right_frame.pack(
            side="right",
            fill="both",
            expand=True
        )

        # =================================================
        # LOGIN CARD
        # =================================================

        self.frame = ctk.CTkFrame(
            self.right_frame,
            width=430,
            height=520,
            fg_color=self.card,
            corner_radius=25,
            border_width=1,
            border_color="#E5E7EB"
        )

        self.frame.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        self.frame.pack_propagate(False)

        # =================================================
        # ICON
        # =================================================

        ctk.CTkLabel(
            self.frame,
            text="🔐",
            font=("Segoe UI Emoji", 45)
        ).pack(
            pady=(22, 5)
        )

        # =================================================
        # TITLE
        # =================================================

        ctk.CTkLabel(
            self.frame,
            text="Welcome Back!",
            font=("Segoe UI", 28, "bold"),
            text_color=self.text
        ).pack(
            pady=(5, 2)
        )

        ctk.CTkLabel(
            self.frame,
            text="Login to access your account",
            font=("Segoe UI", 13),
            text_color=self.gray
        ).pack(
            pady=(0, 18)
        )

        # =================================================
        # LOGIN TYPE
        # =================================================

        ctk.CTkLabel(
            self.frame,
            text="Login As",
            font=("Segoe UI", 13, "bold"),
            text_color=self.text
        ).pack(
            anchor="w",
            padx=55,
            pady=(2, 5)
        )

        self.login_type = ctk.StringVar(
            value="admin"
        )

        self.login_type_menu = ctk.CTkOptionMenu(
            self.frame,
            width=320,
            height=42,
            corner_radius=10,
            variable=self.login_type,
            values=[
                "admin",
                "student"
            ],
            fg_color=self.blue,
            button_color=self.dark_blue,
            button_hover_color="#1E40AF",
            font=("Segoe UI", 13, "bold")
        )

        self.login_type_menu.pack(
            pady=(0, 8)
        )

        # =================================================
        # USERNAME / STUDENT ID
        # =================================================

        self.username = ctk.CTkEntry(
            self.frame,
            width=320,
            height=48,
            corner_radius=12,
            placeholder_text="👤  Username / Student ID",
            font=("Segoe UI", 14),
            border_width=1,
            border_color="#D1D5DB"
        )

        self.username.pack(
            pady=8
        )

        # =================================================
        # PASSWORD
        # =================================================

        self.password = ctk.CTkEntry(
            self.frame,
            width=320,
            height=48,
            corner_radius=12,
            placeholder_text="🔒  Password",
            show="*",
            font=("Segoe UI", 14),
            border_width=1,
            border_color="#D1D5DB"
        )

        self.password.pack(
            pady=8
        )

        # =================================================
        # SHOW PASSWORD
        # =================================================

        self.show_password = ctk.BooleanVar(
            value=False
        )

        self.show_password_checkbox = ctk.CTkCheckBox(
            self.frame,
            text="Show Password",
            variable=self.show_password,
            command=self.toggle_password,
            font=("Segoe UI", 12),
            text_color=self.gray,
            fg_color=self.blue,
            hover_color=self.dark_blue
        )

        self.show_password_checkbox.pack(
            anchor="w",
            padx=55,
            pady=(5, 3)
        )

        # =================================================
        # FORGOT PASSWORD
        # =================================================

        self.forgot_button = ctk.CTkButton(
            self.frame,
            text="Forgot Password?",
            width=140,
            height=25,
            fg_color="transparent",
            hover_color="#EFF6FF",
            text_color=self.blue,
            font=("Segoe UI", 12, "bold"),
            command=self.open_forgot_password
        )

        self.forgot_button.pack(
            anchor="e",
            padx=50
        )

        # =================================================
        # LOGIN BUTTON
        # =================================================

        self.login_button = ctk.CTkButton(
            self.frame,
            text="LOGIN  →",
            width=320,
            height=48,
            corner_radius=12,
            fg_color=self.blue,
            hover_color=self.dark_blue,
            font=("Segoe UI", 15, "bold"),
            command=self.login
        )

        self.login_button.pack(
            pady=(12, 8)
        )

        # =================================================
        # CREATE ADMIN ACCOUNT
        # =================================================

        self.register_button = ctk.CTkButton(
            self.frame,
            text="+  Create New Admin Account",
            width=320,
            height=42,
            corner_radius=12,
            fg_color=self.green,
            hover_color=self.dark_green,
            font=("Segoe UI", 13, "bold"),
            command=self.open_register
        )

        self.register_button.pack(
            pady=4
        )

        # =================================================
        # FOOTER
        # =================================================

        ctk.CTkLabel(
            self.frame,
            text="© 2026 Student Management System ERP",
            font=("Segoe UI", 10),
            text_color="#9CA3AF"
        ).pack(
            side="bottom",
            pady=12
        )

        # =================================================
        # SAFE FOCUS
        # =================================================

        self.root.after(
            150,
            self.set_username_focus
        )

        # =================================================
        # ENTER KEY
        # =================================================

        self.root.bind(
            "<Return>",
            self.handle_enter
        )

    # =====================================================
    # SAFE USERNAME FOCUS
    # =====================================================

    def set_username_focus(self):

        try:

            if (
                hasattr(self, "username")
                and self.username.winfo_exists()
            ):

                self.username.focus_set()

        except Exception as e:

            print(
                "Focus Error:",
                e
            )

    # =====================================================
    # ENTER KEY HANDLER
    # =====================================================

    def handle_enter(self, event=None):

        try:

            if self.root.winfo_exists():

                self.login()

        except Exception as e:

            print(
                "Enter Key Error:",
                e
            )

    # =====================================================
    # SHOW / HIDE PASSWORD
    # =====================================================

    def toggle_password(self):

        try:

            if self.show_password.get():

                self.password.configure(
                    show=""
                )

            else:

                self.password.configure(
                    show="*"
                )

        except Exception as e:

            print(
                "Password Toggle Error:",
                e
            )

    # =====================================================
    # LOGIN
    # =====================================================

    def login(self):

        try:

            username = self.username.get().strip()
            password = self.password.get().strip()

            login_type = (
                self.login_type.get()
                .strip()
                .lower()
            )

        except Exception as e:

            print(
                "Login Input Error:",
                e
            )

            return

        # -------------------------------------------------
        # Empty fields
        # -------------------------------------------------

        if username == "" or password == "":

            messagebox.showerror(
                "Login Error",
                "Please enter Username/Student ID and Password."
            )

            return

        # =================================================
        # ADMIN LOGIN
        # =================================================

        if login_type == "admin":

            user = self.database.check_login(
                username,
                password
            )

            if user:

                self.root.unbind("<Return>")

                self.clear_current_window()

                Dashboard(
                    self.root,
                    self.database
                )

                return

            messagebox.showerror(
                "Admin Login Failed",
                "Invalid Admin Username or Password."
            )

            return

        # =================================================
        # STUDENT LOGIN
        # =================================================

        if login_type == "student":

            student = self.database.check_student_login(
                username,
                password
            )

            if student:

                self.root.unbind("<Return>")

                self.open_student_portal(
                    student
                )

                return

            messagebox.showerror(
                "Student Login Failed",
                "Invalid Student ID or Password."
            )

            return

        # =================================================
        # INVALID LOGIN TYPE
        # =================================================

        messagebox.showerror(
            "Login Error",
            "Please select a valid login type."
        )

    # =====================================================
    # CLEAR CURRENT WINDOW
    # =====================================================

    def clear_current_window(self):

        try:

            self.root.unbind("<Return>")

        except Exception:

            pass

        try:

            for widget in self.root.winfo_children():

                try:

                    if widget.winfo_exists():

                        widget.destroy()

                except Exception:

                    pass

        except Exception as e:

            print(
                "Window Clear Error:",
                e
            )

    # =====================================================
    # STUDENT PORTAL
    # =====================================================

    def open_student_portal(self, student):

        try:

            from student_portal import StudentPortal

            self.clear_current_window()

            StudentPortal(
                self.root,
                self.database,
                student
            )

        except ImportError:

            messagebox.showerror(
                "Student Portal",
                "student_portal.py अभी बनाया नहीं गया है."
            )

        except Exception as e:

            print(
                "Student Portal Error:",
                e
            )

            messagebox.showerror(
                "Student Portal Error",
                str(e)
            )

    # =====================================================
    # FORGOT PASSWORD
    # =====================================================

    def open_forgot_password(self):

        try:

            from forgot_password import ForgotPasswordWindow

            self.root.unbind("<Return>")

            self.clear_current_window()

            ForgotPasswordWindow(
                self.root,
                self.database
            )

        except ImportError:

            messagebox.showerror(
                "Forgot Password",
                "forgot_password.py नहीं मिला."
            )

        except Exception as e:

            print(
                "Forgot Password Error:",
                e
            )

            messagebox.showerror(
                "Forgot Password Error",
                str(e)
            )

    # =====================================================
    # REGISTER ADMIN
    # =====================================================

    def open_register(self):

        try:

            from register import RegisterWindow

            self.root.unbind("<Return>")

            self.clear_current_window()

            RegisterWindow(
                self.root,
                self.database
            )

        except ImportError:

            messagebox.showerror(
                "Registration",
                "register.py नहीं मिला."
            )

        except Exception as e:

            print(
                "Registration Error:",
                e
            )

            messagebox.showerror(
                "Registration Error",
                str(e)
            )


# =========================================================
# RUN FILE FOR TESTING
# =========================================================

if __name__ == "__main__":

    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()

    root.title(
        "Student Management System ERP"
    )

    root.geometry(
        "1100x650"
    )

    root.minsize(
        950,
        580
    )

    database = Database()

    LoginWindow(
        root,
        database
    )

    root.mainloop()
