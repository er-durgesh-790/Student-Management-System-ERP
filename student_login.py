import customtkinter as ctk
from tkinter import messagebox


class StudentLogin:

    # =========================================================
    # INITIALIZATION
    # =========================================================

    def __init__(self, root, database, on_login_success=None):

        self.root = root
        self.database = database
        self.on_login_success = on_login_success

        self.login_closing = False

        # =====================================================
        # WINDOW SETTINGS
        # =====================================================

        self.root.title("Student Portal - Login")
        self.root.geometry("1100x700")
        self.root.minsize(900, 600)
        self.root.resizable(True, True)

        # =====================================================
        # COLORS
        # =====================================================

        self.bg_color = "#0F172A"
        self.card_color = "#1E293B"
        self.input_color = "#0F172A"

        self.primary_color = "#2563EB"
        self.primary_hover = "#1D4ED8"

        self.text_color = "#F8FAFC"
        self.secondary_text = "#94A3B8"

        self.success_color = "#22C55E"
        self.error_color = "#EF4444"

        # =====================================================
        # ROOT BACKGROUND
        # =====================================================

        self.root.configure(
            fg_color=self.bg_color
        )

        # =====================================================
        # CLEAR OLD WINDOW
        # =====================================================

        self.clear_window()

        # =====================================================
        # CREATE LOGIN SCREEN
        # =====================================================

        self.create_login_screen()

        # =====================================================
        # KEYBOARD EVENTS
        # =====================================================

        self.root.bind(
            "<Return>",
            self.handle_enter
        )

        self.root.bind(
            "<Escape>",
            self.handle_escape
        )

    # =========================================================
    # CLEAR WINDOW
    # =========================================================

    def clear_window(self):

        try:

            for widget in self.root.winfo_children():

                try:
                    widget.destroy()

                except Exception:
                    pass

        except Exception as e:

            print(
                "Clear Window Error:",
                e
            )

    # =========================================================
    # CREATE LOGIN SCREEN
    # =========================================================

    def create_login_screen(self):

        # =====================================================
        # MAIN CONTAINER
        # =====================================================

        self.main_container = ctk.CTkFrame(
            self.root,
            fg_color=self.bg_color,
            corner_radius=0
        )

        self.main_container.pack(
            fill="both",
            expand=True
        )

        # =====================================================
        # LEFT BRAND PANEL
        # =====================================================

        self.left_panel = ctk.CTkFrame(
            self.main_container,
            fg_color=self.primary_color,
            corner_radius=0,
            width=500
        )

        self.left_panel.pack(
            side="left",
            fill="both",
            expand=True
        )

        self.left_panel.pack_propagate(False)

        # =====================================================
        # BRAND CONTENT
        # =====================================================

        self.brand_frame = ctk.CTkFrame(
            self.left_panel,
            fg_color="transparent"
        )

        self.brand_frame.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        # Logo

        ctk.CTkLabel(
            self.brand_frame,
            text="🎓",
            font=("Arial", 72)
        ).pack(
            pady=(0, 15)
        )

        # Title

        ctk.CTkLabel(
            self.brand_frame,
            text="STUDENT PORTAL",
            font=("Arial", 30, "bold"),
            text_color="white"
        ).pack(
            pady=5
        )

        # Subtitle

        ctk.CTkLabel(
            self.brand_frame,
            text="Student Management System",
            font=("Arial", 16),
            text_color="#DBEAFE"
        ).pack(
            pady=(0, 30)
        )

        # Description

        ctk.CTkLabel(
            self.brand_frame,
            text=(
                "Access your academic information\n"
                "from one secure portal."
            ),
            font=("Arial", 15),
            text_color="#E0E7FF",
            justify="center"
        ).pack(
            pady=10
        )

        # =====================================================
        # RIGHT LOGIN PANEL
        # =====================================================

        self.right_panel = ctk.CTkFrame(
            self.main_container,
            fg_color=self.bg_color,
            corner_radius=0
        )

        self.right_panel.pack(
            side="right",
            fill="both",
            expand=True
        )

        # =====================================================
        # LOGIN CARD
        # =====================================================

        self.login_card = ctk.CTkFrame(
            self.right_panel,
            fg_color=self.card_color,
            corner_radius=20,
            border_width=1,
            border_color="#334155"
        )

        self.login_card.place(
            relx=0.5,
            rely=0.5,
            anchor="center",
            relwidth=0.78,
            relheight=0.80
        )

        # =====================================================
        # HEADER
        # =====================================================

        self.header_frame = ctk.CTkFrame(
            self.login_card,
            fg_color="transparent"
        )

        self.header_frame.pack(
            fill="x",
            padx=45,
            pady=(35, 5)
        )

        ctk.CTkLabel(
            self.header_frame,
            text="Welcome Back!",
            font=("Arial", 28, "bold"),
            text_color=self.text_color
        ).pack(
            anchor="w"
        )

        ctk.CTkLabel(
            self.header_frame,
            text="Login to continue to your student account",
            font=("Arial", 13),
            text_color=self.secondary_text
        ).pack(
            anchor="w",
            pady=(5, 0)
        )

        # =====================================================
        # FORM
        # =====================================================

        self.form_frame = ctk.CTkFrame(
            self.login_card,
            fg_color="transparent"
        )

        self.form_frame.pack(
            fill="both",
            expand=True,
            padx=45,
            pady=25
        )

        # =====================================================
        # STUDENT ID LABEL
        # =====================================================

        ctk.CTkLabel(
            self.form_frame,
            text="Student ID",
            font=("Arial", 13, "bold"),
            text_color=self.text_color
        ).pack(
            anchor="w",
            pady=(5, 7)
        )

        # =====================================================
        # STUDENT ID ENTRY
        # =====================================================

        self.student_id_entry = ctk.CTkEntry(
            self.form_frame,
            height=46,
            corner_radius=10,
            border_width=1,
            border_color="#475569",
            fg_color=self.input_color,
            text_color=self.text_color,
            placeholder_text="Enter your Student ID",
            placeholder_text_color="#64748B",
            font=("Arial", 14)
        )

        self.student_id_entry.pack(
            fill="x",
            pady=(0, 18)
        )

        # =====================================================
        # PASSWORD LABEL
        # =====================================================

        ctk.CTkLabel(
            self.form_frame,
            text="Password",
            font=("Arial", 13, "bold"),
            text_color=self.text_color
        ).pack(
            anchor="w",
            pady=(0, 7)
        )

        # =====================================================
        # PASSWORD FRAME
        # =====================================================

        self.password_frame = ctk.CTkFrame(
            self.form_frame,
            fg_color=self.input_color,
            corner_radius=10,
            border_width=1,
            border_color="#475569"
        )

        self.password_frame.pack(
            fill="x",
            pady=(0, 8)
        )

        # =====================================================
        # PASSWORD ENTRY
        # =====================================================

        self.password_entry = ctk.CTkEntry(
            self.password_frame,
            height=44,
            corner_radius=10,
            border_width=0,
            fg_color="transparent",
            text_color=self.text_color,
            placeholder_text="Enter your password",
            placeholder_text_color="#64748B",
            show="*",
            font=("Arial", 14)
        )

        self.password_entry.pack(
            side="left",
            fill="x",
            expand=True,
            padx=(10, 0)
        )

        # =====================================================
        # SHOW PASSWORD BUTTON
        # =====================================================

        self.show_password_button = ctk.CTkButton(
            self.password_frame,
            text="👁",
            width=45,
            height=38,
            corner_radius=8,
            fg_color="transparent",
            hover_color="#334155",
            text_color=self.secondary_text,
            command=self.toggle_password
        )

        self.show_password_button.pack(
            side="right",
            padx=4
        )

        # =====================================================
        # INFO FRAME
        # =====================================================

        self.info_frame = ctk.CTkFrame(
            self.form_frame,
            fg_color="transparent"
        )

        self.info_frame.pack(
            fill="x",
            pady=(0, 20)
        )

        self.show_password_var = ctk.BooleanVar(
            value=False
        )

        self.show_password_checkbox = ctk.CTkCheckBox(
            self.info_frame,
            text="Show password",
            variable=self.show_password_var,
            command=self.toggle_password,
            font=("Arial", 12),
            text_color=self.secondary_text,
            hover_color=self.primary_color,
            fg_color=self.primary_color
        )

        self.show_password_checkbox.pack(
            side="left"
        )

        # =====================================================
        # LOGIN BUTTON
        # =====================================================

        self.login_button = ctk.CTkButton(
            self.form_frame,
            text="LOGIN",
            height=48,
            corner_radius=10,
            fg_color=self.primary_color,
            hover_color=self.primary_hover,
            text_color="white",
            font=("Arial", 15, "bold"),
            command=self.login
        )

        self.login_button.pack(
            fill="x",
            pady=(5, 15)
        )

        # =====================================================
        # STATUS LABEL
        # =====================================================

        self.status_label = ctk.CTkLabel(
            self.form_frame,
            text="",
            font=("Arial", 12),
            text_color=self.secondary_text
        )

        self.status_label.pack(
            pady=(0, 10)
        )

        # =====================================================
        # FIRST LOGIN INFORMATION
        # =====================================================

        self.first_login_frame = ctk.CTkFrame(
            self.form_frame,
            fg_color="#172554",
            corner_radius=10
        )

        self.first_login_frame.pack(
            fill="x",
            pady=(5, 15)
        )

        ctk.CTkLabel(
            self.first_login_frame,
            text="🔐 First Login",
            font=("Arial", 12, "bold"),
            text_color="#BFDBFE"
        ).pack(
            anchor="w",
            padx=15,
            pady=(10, 2)
        )

        ctk.CTkLabel(
            self.first_login_frame,
            text="Default password is your Student ID.",
            font=("Arial", 11),
            text_color="#93C5FD"
        ).pack(
            anchor="w",
            padx=15,
            pady=(0, 10)
        )

        # =====================================================
        # FOOTER
        # =====================================================

        ctk.CTkLabel(
            self.login_card,
            text=(
                "Student Management System • "
                "Secure Student Access"
            ),
            font=("Arial", 10),
            text_color="#64748B"
        ).pack(
            pady=(0, 15)
        )

        # =====================================================
        # IMPORTANT
        # =====================================================
        # Yahan direct focus() nahi kar rahe.
        # Isi se pending focus_set error avoid hota hai.
        # =====================================================

    # =========================================================
    # SAFE FOCUS STUDENT ID
    # =========================================================

    def focus_student_id(self):

        if self.login_closing:
            return

        try:

            if (
                hasattr(self, "student_id_entry")
                and self.student_id_entry.winfo_exists()
            ):

                self.student_id_entry.focus_set()

        except Exception:
            pass

    # =========================================================
    # TOGGLE PASSWORD
    # =========================================================

    def toggle_password(self):

        if self.login_closing:
            return

        try:

            if self.show_password_var.get():

                self.password_entry.configure(
                    show=""
                )

                self.show_password_button.configure(
                    text="🙈"
                )

            else:

                self.password_entry.configure(
                    show="*"
                )

                self.show_password_button.configure(
                    text="👁"
                )

        except Exception as e:

            print(
                "Toggle Password Error:",
                e
            )

    # =========================================================
    # LOGIN
    # =========================================================

    def login(self):

        if self.login_closing:
            return

        try:

            student_id = (
                self.student_id_entry
                .get()
                .strip()
            )

            password = (
                self.password_entry
                .get()
                .strip()
            )

        except Exception:

            return

        # =====================================================
        # VALIDATION
        # =====================================================

        if not student_id:

            self.show_status(
                "Please enter your Student ID.",
                self.error_color
            )

            self.safe_focus(
                self.student_id_entry
            )

            return

        if not password:

            self.show_status(
                "Please enter your password.",
                self.error_color
            )

            self.safe_focus(
                self.password_entry
            )

            return

        # =====================================================
        # DISABLE LOGIN BUTTON
        # =====================================================

        try:

            self.login_button.configure(
                state="disabled",
                text="LOGGING IN..."
            )

            self.show_status(
                "Verifying your credentials...",
                self.secondary_text
            )

            self.root.update_idletasks()

        except Exception:
            return

        # =====================================================
        # DATABASE VERIFICATION
        # =====================================================

        try:

            student = self.database.check_student_login(
                student_id,
                password
            )

            # =================================================
            # LOGIN SUCCESS
            # =================================================

            if student:

                self.show_status(
                    "Login successful. Opening portal...",
                    self.success_color
                )

                self.root.update_idletasks()

                # ---------------------------------------------
                # Mark login screen as closing
                # ---------------------------------------------

                self.login_closing = True

                # ---------------------------------------------
                # Remove keyboard bindings
                # ---------------------------------------------

                try:

                    self.root.unbind(
                        "<Return>"
                    )

                    self.root.unbind(
                        "<Escape>"
                    )

                except Exception:
                    pass

                # ---------------------------------------------
                # Disable login button completely
                # ---------------------------------------------

                try:

                    self.login_button.configure(
                        state="disabled"
                    )

                except Exception:
                    pass

                # ---------------------------------------------
                # Open portal after short delay
                #
                # Delay gives Tkinter time to finish
                # current button/focus events.
                # ---------------------------------------------

                self.root.after(
                    600,
                    lambda student_data=student:
                        self.open_portal_safe(
                            student_data
                        )
                )

                return

            # =================================================
            # LOGIN FAILED
            # =================================================

            self.show_status(
                "Invalid Student ID or Password.",
                self.error_color
            )

            self.login_button.configure(
                state="normal",
                text="LOGIN"
            )

            self.password_entry.delete(
                0,
                "end"
            )

            self.safe_focus(
                self.password_entry
            )

        except Exception as e:

            print(
                "Student Login Error:",
                e
            )

            self.show_status(
                "Unable to connect to database.",
                self.error_color
            )

            try:

                self.login_button.configure(
                    state="normal",
                    text="LOGIN"
                )

            except Exception:
                pass

            messagebox.showerror(
                "Login Error",
                f"An unexpected error occurred.\n\n{e}"
            )

    # =========================================================
    # SAFE OPEN PORTAL
    # =========================================================

    def open_portal_safe(
        self,
        student
    ):

        try:

            # ---------------------------------------------
            # If callback is still valid
            # ---------------------------------------------

            if not self.root.winfo_exists():

                return

            # ---------------------------------------------
            # Use callback if main.py provided one
            # ---------------------------------------------

            if self.on_login_success:

                self.on_login_success(
                    student
                )

                return

            # ---------------------------------------------
            # Otherwise open Student Portal directly
            # ---------------------------------------------

            from student_portal import StudentPortal

            # Remove old login widgets

            self.destroy_login_screen()

            # Open portal

            StudentPortal(
                self.root,
                self.database,
                student
            )

        except ImportError:

            self.login_closing = False

            messagebox.showerror(
                "Student Portal",
                "student_portal.py नहीं मिला।"
            )

            try:

                self.login_button.configure(
                    state="normal",
                    text="LOGIN"
                )

            except Exception:
                pass

        except Exception as e:

            print(
                "Student Portal Error:",
                e
            )

            messagebox.showerror(
                "Student Portal Error",
                f"Unable to open Student Portal.\n\n{e}"
            )

    # =========================================================
    # DESTROY LOGIN SCREEN
    # =========================================================

    def destroy_login_screen(self):

        try:

            self.root.unbind(
                "<Return>"
            )

            self.root.unbind(
                "<Escape>"
            )

        except Exception:
            pass

        try:

            if hasattr(
                self,
                "main_container"
            ):

                if self.main_container.winfo_exists():

                    self.main_container.destroy()

                return

        except Exception as e:

            print(
                "Login Screen Destroy Error:",
                e
            )

        # Fallback

        self.clear_window()

    # =========================================================
    # SAFE FOCUS
    # =========================================================

    def safe_focus(
        self,
        widget
    ):

        if self.login_closing:
            return

        try:

            if widget.winfo_exists():

                widget.focus_set()

        except Exception:
            pass

    # =========================================================
    # STATUS MESSAGE
    # =========================================================

    def show_status(
        self,
        message,
        color
    ):

        if self.login_closing:
            return

        try:

            if self.status_label.winfo_exists():

                self.status_label.configure(
                    text=message,
                    text_color=color
                )

        except Exception:
            pass

    # =========================================================
    # ENTER KEY
    # =========================================================

    def handle_enter(
        self,
        event=None
    ):

        if self.login_closing:
            return "break"

        self.login()

        return "break"

    # =========================================================
    # ESCAPE KEY
    # =========================================================

    def handle_escape(
        self,
        event=None
    ):

        if self.login_closing:
            return "break"

        self.clear_form()

        return "break"

    # =========================================================
    # CLEAR FORM
    # =========================================================

    def clear_form(self):

        if self.login_closing:
            return

        try:

            self.student_id_entry.delete(
                0,
                "end"
            )

            self.password_entry.delete(
                0,
                "end"
            )

            self.show_password_var.set(
                False
            )

            self.password_entry.configure(
                show="*"
            )

            self.show_password_button.configure(
                text="👁"
            )

            self.show_status(
                "",
                self.secondary_text
            )

            self.safe_focus(
                self.student_id_entry
            )

        except Exception as e:

            print(
                "Clear Form Error:",
                e
            )

    # =========================================================
    # DESTROY
    # =========================================================

    def destroy(self):

        self.login_closing = True

        try:

            self.root.unbind(
                "<Return>"
            )

            self.root.unbind(
                "<Escape>"
            )

        except Exception:
            pass

        try:

            if hasattr(
                self,
                "main_container"
            ):

                if self.main_container.winfo_exists():

                    self.main_container.destroy()

        except Exception as e:

            print(
                "Student Login Destroy Error:",
                e
            )


# =============================================================
# TESTING
# =============================================================

if __name__ == "__main__":

    ctk.set_appearance_mode(
        "dark"
    )

    ctk.set_default_color_theme(
        "blue"
    )

    root = ctk.CTk()

    root.title(
        "Student Portal - Login"
    )

    root.geometry(
        "1100x700"
    )

    root.minsize(
        900,
        600
    )

    print(
        "StudentLogin standalone testing mode."
    )

    root.mainloop()