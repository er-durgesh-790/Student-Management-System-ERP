
import customtkinter as ctk
from tkinter import messagebox


class RegisterWindow:

    # ======================================
    # CONSTRUCTOR
    # ======================================

    def __init__(self, root, database):

        self.root = root
        self.database = database

        # Remove Previous Widgets
        for widget in self.root.winfo_children():
            widget.destroy()

        # ======================================
        # WINDOW
        # ======================================

        self.root.title("Create Account - Student Management System ERP")
        self.root.geometry("750x750")
        self.root.minsize(650, 700)
        self.root.resizable(False, False)

        # ======================================
        # COLORS
        # ======================================

        self.primary = "#2563EB"
        self.primary_dark = "#1D4ED8"

        self.bg = "#EFF6FF"
        self.card_bg = "#FFFFFF"

        self.text = "#111827"
        self.light_text = "#6B7280"

        self.success = "#16A34A"
        self.danger = "#DC2626"

        # ======================================
        # FONTS
        # ======================================

        self.title_font = (
            "Segoe UI",
            27,
            "bold"
        )

        self.subtitle_font = (
            "Segoe UI",
            13
        )

        self.label_font = (
            "Segoe UI",
            13,
            "bold"
        )

        self.entry_font = (
            "Segoe UI",
            13
        )

        self.button_font = (
            "Segoe UI",
            14,
            "bold"
        )

        # ======================================
        # MAIN BACKGROUND
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
        # TOP BLUE HEADER
        # ======================================

        self.header = ctk.CTkFrame(
            self.main_frame,
            height=90,
            fg_color=self.primary,
            corner_radius=0
        )

        self.header.pack(
            fill="x"
        )

        self.header.pack_propagate(False)

        ctk.CTkLabel(
            self.header,
            text="🎓  Student Management System ERP",
            font=("Segoe UI", 24, "bold"),
            text_color="white"
        ).pack(
            side="left",
            padx=30
        )

        ctk.CTkLabel(
            self.header,
            text="Create Account",
            font=("Segoe UI", 14),
            text_color="#DBEAFE"
        ).pack(
            side="right",
            padx=30
        )

        # ======================================
        # REGISTER CARD
        # ======================================

        self.card = ctk.CTkFrame(
            self.main_frame,
            width=500,
            height=570,
            fg_color=self.card_bg,
            corner_radius=20,
            border_width=1,
            border_color="#DBEAFE"
        )

        self.card.place(
            relx=0.5,
            rely=0.54,
            anchor="center"
        )

        # ======================================
        # LOGO
        # ======================================

        ctk.CTkLabel(
            self.card,
            text="👤",
            font=("Segoe UI Emoji", 45)
        ).pack(
            pady=(20, 3)
        )

        # ======================================
        # TITLE
        # ======================================

        ctk.CTkLabel(
            self.card,
            text="Create New Account",
            font=self.title_font,
            text_color=self.text
        ).pack()

        # ======================================
        # SUBTITLE
        # ======================================

        ctk.CTkLabel(
            self.card,
            text="Register a new administrator account",
            font=self.subtitle_font,
            text_color=self.light_text
        ).pack(
            pady=(3, 15)
        )

        # ======================================
        # FORM FRAME
        # ======================================

        form_frame = ctk.CTkFrame(
            self.card,
            fg_color="transparent"
        )

        form_frame.pack(
            fill="x",
            padx=55
        )

        # ======================================
        # FULL NAME
        # ======================================

        ctk.CTkLabel(
            form_frame,
            text="Full Name",
            font=self.label_font,
            text_color=self.text
        ).pack(
            anchor="w",
            pady=(2, 4)
        )

        self.full_name = ctk.CTkEntry(
            form_frame,
            width=390,
            height=42,
            corner_radius=8,
            border_width=1,
            border_color="#CBD5E1",
            placeholder_text="Enter full name",
            font=self.entry_font
        )

        self.full_name.pack(
            pady=(0, 8)
        )

        # ======================================
        # USERNAME
        # ======================================

        ctk.CTkLabel(
            form_frame,
            text="Username",
            font=self.label_font,
            text_color=self.text
        ).pack(
            anchor="w",
            pady=(2, 4)
        )

        self.username = ctk.CTkEntry(
            form_frame,
            width=390,
            height=42,
            corner_radius=8,
            border_width=1,
            border_color="#CBD5E1",
            placeholder_text="Enter username",
            font=self.entry_font
        )

        self.username.pack(
            pady=(0, 8)
        )

        # ======================================
        # MOBILE
        # ======================================

        ctk.CTkLabel(
            form_frame,
            text="Mobile Number",
            font=self.label_font,
            text_color=self.text
        ).pack(
            anchor="w",
            pady=(2, 4)
        )

        self.mobile = ctk.CTkEntry(
            form_frame,
            width=390,
            height=42,
            corner_radius=8,
            border_width=1,
            border_color="#CBD5E1",
            placeholder_text="Enter 10-digit mobile number",
            font=self.entry_font
        )

        self.mobile.pack(
            pady=(0, 8)
        )

        # ======================================
        # PASSWORD
        # ======================================

        ctk.CTkLabel(
            form_frame,
            text="Password",
            font=self.label_font,
            text_color=self.text
        ).pack(
            anchor="w",
            pady=(2, 4)
        )

        self.password = ctk.CTkEntry(
            form_frame,
            width=390,
            height=42,
            corner_radius=8,
            border_width=1,
            border_color="#CBD5E1",
            placeholder_text="Enter password",
            show="*",
            font=self.entry_font
        )

        self.password.pack(
            pady=(0, 8)
        )

        # ======================================
        # CONFIRM PASSWORD
        # ======================================

        ctk.CTkLabel(
            form_frame,
            text="Confirm Password",
            font=self.label_font,
            text_color=self.text
        ).pack(
            anchor="w",
            pady=(2, 4)
        )

        self.confirm_password = ctk.CTkEntry(
            form_frame,
            width=390,
            height=42,
            corner_radius=8,
            border_width=1,
            border_color="#CBD5E1",
            placeholder_text="Confirm your password",
            show="*",
            font=self.entry_font
        )

        self.confirm_password.pack(
            pady=(0, 12)
        )

        # ======================================
        # CREATE ACCOUNT BUTTON
        # ======================================

        self.register_btn = ctk.CTkButton(
            self.card,
            text="✓  Create Account",
            width=390,
            height=45,
            corner_radius=9,
            fg_color=self.primary,
            hover_color=self.primary_dark,
            font=self.button_font,
            command=self.register
        )

        self.register_btn.pack(
            pady=(2, 8)
        )

        # ======================================
        # BACK TO LOGIN
        # ======================================

        self.back_btn = ctk.CTkButton(
            self.card,
            text="←  Back to Login",
            width=390,
            height=40,
            corner_radius=9,
            fg_color="#64748B",
            hover_color="#475569",
            font=("Segoe UI", 13, "bold"),
            command=self.back_to_login
        )

        self.back_btn.pack(
            pady=(0, 10)
        )

        # ======================================
        # FOOTER
        # ======================================

        ctk.CTkLabel(
            self.card,
            text="© 2026 Student Management System ERP",
            font=("Segoe UI", 10),
            text_color=self.light_text
        ).pack(
            pady=(2, 8)
        )

        # ======================================
        # DEFAULT FOCUS
        # ======================================

        self.full_name.focus()

        # ======================================
        # ENTER KEY
        # ======================================

        self.root.bind(
            "<Return>",
            lambda event: self.register()
        )

    # ======================================
    # REGISTER
    # ======================================

    def register(self):

        full_name = self.full_name.get().strip()
        username = self.username.get().strip()
        mobile = self.mobile.get().strip()
        password = self.password.get().strip()
        confirm = self.confirm_password.get().strip()

        # ======================================
        # EMPTY VALIDATION
        # ======================================

        if (
            full_name == "" or
            username == "" or
            mobile == "" or
            password == "" or
            confirm == ""
        ):

            messagebox.showerror(
                "Registration Error",
                "Please fill all fields."
            )

            return

        # ======================================
        # MOBILE VALIDATION
        # ======================================

        if not mobile.isdigit() or len(mobile) != 10:

            messagebox.showerror(
                "Invalid Mobile",
                "Please enter a valid 10-digit mobile number."
            )

            self.mobile.focus()

            return

        # ======================================
        # PASSWORD LENGTH
        # ======================================

        if len(password) < 4:

            messagebox.showerror(
                "Invalid Password",
                "Password must be at least 4 characters."
            )

            self.password.focus()

            return

        # ======================================
        # PASSWORD MATCH
        # ======================================

        if password != confirm:

            messagebox.showerror(
                "Password Error",
                "Passwords do not match."
            )

            self.confirm_password.focus()

            return

        # ======================================
        # USERNAME EXISTS
        # ======================================

        if self.database.username_exists(username):

            messagebox.showerror(
                "Username Exists",
                "This username already exists.\nPlease choose another username."
            )

            self.username.focus()

            return

        # ======================================
        # REGISTER USER
        # ======================================

        try:

            success = self.database.register_admin(
                full_name,
                username,
                mobile,
                password
            )

            if success:

                messagebox.showinfo(
                    "Registration Successful",
                    "Account created successfully.\n\n"
                    "You can now login using your new account."
                )

                self.back_to_login()

            else:

                messagebox.showerror(
                    "Registration Failed",
                    "Unable to create account."
                )

        except Exception as e:

            messagebox.showerror(
                "Database Error",
                str(e)
            )

    # ======================================
    # BACK TO LOGIN
    # ======================================

    def back_to_login(self):

        from login import LoginWindow

        # Remove current widgets

        for widget in self.root.winfo_children():
            widget.destroy()

        # Open Login

        LoginWindow(
            self.root,
            self.database
        )


# ======================================
# RUN FILE FOR TESTING
# ======================================

if __name__ == "__main__":

    from database import Database

    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()

    root.title("Register")
    root.geometry("750x750")
    root.resizable(False, False)

    database = Database()

    RegisterWindow(
        root,
        database
    )

    root.mainloop()