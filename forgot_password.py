
import customtkinter as ctk
from tkinter import messagebox


class ForgotPasswordWindow:

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

        self.root.title("Reset Password - Student Management System ERP")
        self.root.geometry("1100x650")
        self.root.minsize(950, 580)
        self.root.resizable(True, True)

        # ======================================
        # COLORS
        # ======================================

        self.blue = "#2563EB"
        self.dark_blue = "#1D4ED8"
        self.green = "#16A34A"
        self.dark_green = "#15803D"

        self.bg = "#F4F7FB"
        self.card = "#FFFFFF"
        self.text = "#111827"
        self.gray = "#6B7280"

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
        # LEFT BRAND PANEL
        # ======================================

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
            text="🔐",
            font=("Segoe UI Emoji", 85)
        ).pack(
            pady=(90, 10)
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
                "Secure account recovery\n"
                "and password management\n"
                "for your ERP system."
            ),
            font=("Segoe UI", 15),
            text_color="#DBEAFE",
            justify="center"
        ).pack(
            pady=15
        )

        # Security Box

        security_frame = ctk.CTkFrame(
            self.left_frame,
            fg_color="#1D4ED8",
            corner_radius=15
        )

        security_frame.pack(
            padx=45,
            pady=25,
            fill="x"
        )

        ctk.CTkLabel(
            security_frame,
            text=(
                "✓  Verify Username\n"
                "✓  Verify Mobile Number\n"
                "✓  Create New Password"
            ),
            font=("Segoe UI", 13, "bold"),
            text_color="white",
            justify="left"
        ).pack(
            padx=20,
            pady=15
        )

        # ======================================
        # DEVELOPER NAME
        # ======================================

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

        # ======================================
        # RIGHT PANEL
        # ======================================

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

        # ======================================
        # RESET PASSWORD CARD
        # ======================================

        self.card = ctk.CTkFrame(
            self.right_frame,
            width=450,
            height=535,
            fg_color=self.card,
            corner_radius=25,
            border_width=1,
            border_color="#E5E7EB"
        )

        self.card.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        self.card.pack_propagate(False)

        # ======================================
        # ICON
        # ======================================

        ctk.CTkLabel(
            self.card,
            text="🔑",
            font=("Segoe UI Emoji", 45)
        ).pack(
            pady=(22, 5)
        )

        # ======================================
        # TITLE
        # ======================================

        ctk.CTkLabel(
            self.card,
            text="Reset Password",
            font=("Segoe UI", 28, "bold"),
            text_color=self.text
        ).pack(
            pady=(5, 2)
        )

        ctk.CTkLabel(
            self.card,
            text="Verify your account to create a new password",
            font=("Segoe UI", 13),
            text_color=self.gray
        ).pack(
            pady=(0, 20)
        )

        # ======================================
        # USERNAME
        # ======================================

        self.username = ctk.CTkEntry(
            self.card,
            width=320,
            height=46,
            corner_radius=12,
            placeholder_text="👤  Username",
            font=("Segoe UI", 14),
            border_width=1,
            border_color="#D1D5DB"
        )

        self.username.pack(
            pady=7
        )

        # ======================================
        # MOBILE
        # ======================================

        self.mobile = ctk.CTkEntry(
            self.card,
            width=320,
            height=46,
            corner_radius=12,
            placeholder_text="📱  Mobile Number",
            font=("Segoe UI", 14),
            border_width=1,
            border_color="#D1D5DB"
        )

        self.mobile.pack(
            pady=7
        )

        # ======================================
        # NEW PASSWORD
        # ======================================

        self.password = ctk.CTkEntry(
            self.card,
            width=320,
            height=46,
            corner_radius=12,
            placeholder_text="🔒  New Password",
            show="*",
            font=("Segoe UI", 14),
            border_width=1,
            border_color="#D1D5DB"
        )

        self.password.pack(
            pady=7
        )

        # ======================================
        # CONFIRM PASSWORD
        # ======================================

        self.confirm_password = ctk.CTkEntry(
            self.card,
            width=320,
            height=46,
            corner_radius=12,
            placeholder_text="🔒  Confirm Password",
            show="*",
            font=("Segoe UI", 14),
            border_width=1,
            border_color="#D1D5DB"
        )

        self.confirm_password.pack(
            pady=7
        )

        # ======================================
        # SHOW PASSWORD
        # ======================================

        self.show_password = ctk.BooleanVar(
            value=False
        )

        ctk.CTkCheckBox(
            self.card,
            text="Show Password",
            variable=self.show_password,
            command=self.toggle_password,
            font=("Segoe UI", 12),
            text_color=self.gray,
            fg_color=self.blue,
            hover_color=self.dark_blue
        ).pack(
            anchor="w",
            padx=65,
            pady=(5, 8)
        )

        # ======================================
        # UPDATE PASSWORD BUTTON
        # ======================================

        ctk.CTkButton(
            self.card,
            text="UPDATE PASSWORD",
            width=320,
            height=46,
            corner_radius=12,
            fg_color=self.blue,
            hover_color=self.dark_blue,
            font=("Segoe UI", 14, "bold"),
            command=self.update_password
        ).pack(
            pady=(10, 8)
        )

        # ======================================
        # BACK TO LOGIN
        # ======================================

        ctk.CTkButton(
            self.card,
            text="←  Back to Login",
            width=320,
            height=42,
            corner_radius=12,
            fg_color="#6B7280",
            hover_color="#4B5563",
            font=("Segoe UI", 13, "bold"),
            command=self.back_to_login
        ).pack(
            pady=5
        )

        # ======================================
        # FOOTER
        # ======================================

        ctk.CTkLabel(
            self.card,
            text="© 2026 Student Management System ERP",
            font=("Segoe UI", 10),
            text_color="#9CA3AF"
        ).pack(
            side="bottom",
            pady=12
        )

        # ======================================
        # FOCUS
        # ======================================

        self.username.focus()

        # ======================================
        # ENTER KEY
        # ======================================

        self.root.bind(
            "<Return>",
            lambda event: self.update_password()
        )

    # ======================================
    # SHOW / HIDE PASSWORD
    # ======================================

    def toggle_password(self):

        if self.show_password.get():

            self.password.configure(
                show=""
            )

            self.confirm_password.configure(
                show=""
            )

        else:

            self.password.configure(
                show="*"
            )

            self.confirm_password.configure(
                show="*"
            )

    # ======================================
    # UPDATE PASSWORD
    # ======================================

    def update_password(self):

        username = self.username.get().strip()
        mobile = self.mobile.get().strip()

        new_password = self.password.get().strip()
        confirm_password = self.confirm_password.get().strip()

        # ======================================
        # EMPTY VALIDATION
        # ======================================

        if (
            username == "" or
            mobile == "" or
            new_password == "" or
            confirm_password == ""
        ):

            messagebox.showerror(
                "Error",
                "Please fill all fields."
            )

            return

        # ======================================
        # MOBILE VALIDATION
        # ======================================

        if not mobile.isdigit() or len(mobile) != 10:

            messagebox.showerror(
                "Invalid Mobile",
                "Enter a valid 10-digit mobile number."
            )

            return

        # ======================================
        # PASSWORD LENGTH
        # ======================================

        if len(new_password) < 4:

            messagebox.showerror(
                "Invalid Password",
                "Password must be at least 4 characters."
            )

            return

        # ======================================
        # PASSWORD MATCH
        # ======================================

        if new_password != confirm_password:

            messagebox.showerror(
                "Password Error",
                "Passwords do not match."
            )

            return

        # ======================================
        # VERIFY USER
        # ======================================

        try:

            user = self.database.verify_admin(
                username,
                mobile
            )

            if not user:

                messagebox.showerror(
                    "Verification Failed",
                    "Username or Mobile Number is incorrect."
                )

                return

            # ======================================
            # UPDATE PASSWORD
            # ======================================

            success = self.database.update_admin_password(
                username,
                new_password
            )

            if success:

                messagebox.showinfo(
                    "Success",
                    "Password updated successfully."
                )

                self.root.unbind("<Return>")

                self.back_to_login()

            else:

                messagebox.showerror(
                    "Error",
                    "Unable to update password."
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

        self.root.unbind("<Return>")

        for widget in self.root.winfo_children():
            widget.destroy()

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

    root.title("Forgot Password")
    root.geometry("1100x650")
    root.minsize(950, 580)

    database = Database()

    ForgotPasswordWindow(
        root,
        database
    )

    root.mainloop()