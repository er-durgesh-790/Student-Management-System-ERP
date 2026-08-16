
import customtkinter as ctk
from tkinter import messagebox

from config import *
from database import Database
from login import LoginWindow
from student_login import StudentLogin


class StudentERP:

    # =========================================================
    # APPLICATION INITIALIZATION
    # =========================================================

    def __init__(self):

        self.database = None
        self.window = None

        # ==========================
        # Setup Database
        # ==========================

        self.setup_database()

        # ==========================
        # Setup Theme
        # ==========================

        self.setup_theme()

        # ==========================
        # Create Main Window
        # ==========================

        self.create_main_window()

        # ==========================
        # Setup Window Close Event
        # ==========================

        self.window.protocol(
            "WM_DELETE_WINDOW",
            self.close_application
        )

        # ==========================
        # Open Login Selection
        # ==========================

        self.open_login_selection()

        # ==========================
        # Start Application
        # ==========================

        self.run()

    # =========================================================
    # DATABASE SETUP
    # =========================================================

    def setup_database(self):

        try:

            self.database = Database()

        except Exception as e:

            print(
                "Database Initialization Error:",
                e
            )

            messagebox.showerror(
                "Database Error",
                f"Unable to initialize database.\n\n{e}"
            )

            raise

    # =========================================================
    # THEME SETUP
    # =========================================================

    def setup_theme(self):

        ctk.set_appearance_mode(
            "light"
        )

        ctk.set_default_color_theme(
            "blue"
        )

    # =========================================================
    # CREATE MAIN WINDOW
    # =========================================================

    def create_main_window(self):

        self.window = ctk.CTk()

        self.window.title(
            APP_NAME
        )

        self.window.geometry(
            "1200x700"
        )

        self.window.minsize(
            1000,
            600
        )

        self.window.resizable(
            True,
            True
        )

        self.window.configure(
            fg_color="#F5F7FB"
        )

        self.center_window()

    # =========================================================
    # CENTER WINDOW
    # =========================================================

    def center_window(self):

        self.window.update_idletasks()

        width = 1200
        height = 700

        screen_width = (
            self.window.winfo_screenwidth()
        )

        screen_height = (
            self.window.winfo_screenheight()
        )

        x = int(
            (screen_width - width) / 2
        )

        y = int(
            (screen_height - height) / 2
        )

        self.window.geometry(
            f"{width}x{height}+{x}+{y}"
        )

    # =========================================================
    # LOGIN SELECTION
    # =========================================================

    def open_login_selection(self):

        self.login_selection_frame = ctk.CTkFrame(
            self.window,
            fg_color="#F5F7FB"
        )

        self.login_selection_frame.pack(
            fill="both",
            expand=True
        )

        # =====================================================
        # Main Card
        # =====================================================

        card = ctk.CTkFrame(
            self.login_selection_frame,
            width=520,
            height=430,
            corner_radius=20,
            fg_color="white"
        )

        card.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        card.pack_propagate(False)

        # =====================================================
        # Title
        # =====================================================

        title = ctk.CTkLabel(
            card,
            text="Student Management System",
            font=(
                "Segoe UI",
                26,
                "bold"
            ),
            text_color="#172033"
        )

        title.pack(
            pady=(45, 8)
        )

        # =====================================================
        # Subtitle
        # =====================================================

        subtitle = ctk.CTkLabel(
            card,
            text="Select Login Type",
            font=(
                "Segoe UI",
                15
            ),
            text_color="#667085"
        )

        subtitle.pack(
            pady=(0, 30)
        )

        # =====================================================
        # ADMIN LOGIN BUTTON
        # =====================================================

        admin_button = ctk.CTkButton(
            card,
            text="Admin Login",
            width=330,
            height=55,
            corner_radius=12,
            font=(
                "Segoe UI",
                16,
                "bold"
            ),
            fg_color="#2563EB",
            hover_color="#1D4ED8",
            command=self.open_admin_login
        )

        admin_button.pack(
            pady=10
        )

        # =====================================================
        # STUDENT LOGIN BUTTON
        # =====================================================

        student_button = ctk.CTkButton(
            card,
            text="Student Login",
            width=330,
            height=55,
            corner_radius=12,
            font=(
                "Segoe UI",
                16,
                "bold"
            ),
            fg_color="#059669",
            hover_color="#047857",
            command=self.open_student_login
        )

        student_button.pack(
            pady=10
        )

        # =====================================================
        # EXIT BUTTON
        # =====================================================

        exit_button = ctk.CTkButton(
            card,
            text="Exit Application",
            width=330,
            height=45,
            corner_radius=10,
            font=(
                "Segoe UI",
                14
            ),
            fg_color="#E5E7EB",
            hover_color="#D1D5DB",
            text_color="#374151",
            command=self.close_application
        )

        exit_button.pack(
            pady=(20, 0)
        )

    # =========================================================
    # OPEN ADMIN LOGIN
    # =========================================================

    def open_admin_login(self):

        self.hide_login_selection()

        try:

            LoginWindow(
                self.window,
                self.database
            )

        except Exception as e:

            print(
                "Admin Login Error:",
                e
            )

            messagebox.showerror(
                "Login Error",
                f"Unable to open Admin Login.\n\n{e}"
            )

            self.show_login_selection()

    # =========================================================
    # OPEN STUDENT LOGIN
    # =========================================================

    def open_student_login(self):

        self.hide_login_selection()

        try:

            StudentLogin(
                self.window,
                self.database
            )

        except Exception as e:

            print(
                "Student Login Error:",
                e
            )

            messagebox.showerror(
                "Login Error",
                f"Unable to open Student Login.\n\n{e}"
            )

            self.show_login_selection()

    # =========================================================
    # HIDE LOGIN SELECTION
    # =========================================================

    def hide_login_selection(self):

        if hasattr(
            self,
            "login_selection_frame"
        ):

            self.login_selection_frame.pack_forget()

    # =========================================================
    # SHOW LOGIN SELECTION
    # =========================================================

    def show_login_selection(self):

        if hasattr(
            self,
            "login_selection_frame"
        ):

            self.login_selection_frame.pack(
                fill="both",
                expand=True
            )

    # =========================================================
    # RETURN TO LOGIN SELECTION
    # =========================================================

    def return_to_login_selection(self):

        try:
            # Remove current widgets safely
            for widget in self.window.winfo_children():
                try:
                    widget.destroy()
                except Exception:
                    pass

            # Small delay so pending Tkinter callbacks
            # don't operate on already destroyed widgets
            self.window.after(
                50,
                self.open_login_selection
            )

        except Exception as e:

            print(
                "Return Login Selection Error:",
                e
            )

    # =========================================================
    # APPLICATION RUN
    # =========================================================

    def run(self):

        self.window.mainloop()

    # =========================================================
    # CLOSE APPLICATION
    # =========================================================

    def close_application(self):

        try:

            if self.database:

                self.database.close()

        except Exception as e:

            print(
                "Database Close Error:",
                e
            )

        try:

            if self.window:

                self.window.destroy()

        except Exception as e:

            print(
                "Application Close Error:",
                e
            )


# =========================================================
# APPLICATION ENTRY POINT
# =========================================================

if __name__ == "__main__":

    StudentERP()
