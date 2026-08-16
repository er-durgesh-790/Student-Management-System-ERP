
import customtkinter as ctk
from tkinter import messagebox, filedialog
import shutil
import os


class SettingsModule:

    def __init__(self, parent, database):

        self.parent = parent
        self.database = database

        self.logo_path = ""

        # ==============================
        # Colors
        # ==============================

        self.primary = "#2563EB"
        self.primary_hover = "#1D4ED8"

        self.success = "#16A34A"
        self.success_hover = "#15803D"

        self.warning = "#F59E0B"
        self.warning_hover = "#D97706"

        self.danger = "#DC2626"
        self.danger_hover = "#B91C1C"

        self.purple = "#7C3AED"
        self.purple_hover = "#6D28D9"

        self.bg = "#F8FAFC"
        self.card = "#FFFFFF"

        self.text = "#111827"
        self.secondary_text = "#64748B"

        # ==============================
        # Main Frame
        # ==============================

        self.main_frame = ctk.CTkFrame(
            parent,
            fg_color=self.bg,
            corner_radius=0
        )

        self.main_frame.pack(
            fill="both",
            expand=True
        )

        self.create_ui()

    # ==========================================================
    # CREATE UI
    # ==========================================================

    def create_ui(self):

        # ==============================
        # Header
        # ==============================

        header = ctk.CTkFrame(
            self.main_frame,
            fg_color=self.primary,
            height=80,
            corner_radius=0
        )

        header.pack(
            fill="x"
        )

        header.pack_propagate(False)

        ctk.CTkLabel(
            header,
            text="⚙  Settings",
            font=("Segoe UI", 28, "bold"),
            text_color="white"
        ).pack(
            side="left",
            padx=30
        )

        ctk.CTkLabel(
            header,
            text="Manage your ERP system",
            font=("Segoe UI", 14),
            text_color="#DBEAFE"
        ).pack(
            side="right",
            padx=30
        )

        # ==============================
        # Scrollable Content
        # ==============================

        content = ctk.CTkScrollableFrame(
            self.main_frame,
            fg_color=self.bg,
            corner_radius=0
        )

        content.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        # ======================================================
        # INSTITUTE INFORMATION
        # ======================================================

        info_card = ctk.CTkFrame(
            content,
            fg_color=self.card,
            corner_radius=15
        )

        info_card.pack(
            fill="x",
            pady=(0, 20)
        )

        ctk.CTkLabel(
            info_card,
            text="🏫  Institute Information",
            font=("Segoe UI", 20, "bold"),
            text_color=self.text
        ).pack(
            anchor="w",
            padx=25,
            pady=(20, 5)
        )

        ctk.CTkLabel(
            info_card,
            text="Update institute details used by the ERP system.",
            font=("Segoe UI", 13),
            text_color=self.secondary_text
        ).pack(
            anchor="w",
            padx=25,
            pady=(0, 20)
        )

        form = ctk.CTkFrame(
            info_card,
            fg_color="transparent"
        )

        form.pack(
            fill="x",
            padx=25,
            pady=(0, 20)
        )

        form.grid_columnconfigure(1, weight=1)

        # Institute Name

        ctk.CTkLabel(
            form,
            text="Institute Name",
            font=("Segoe UI", 14, "bold"),
            text_color=self.text
        ).grid(
            row=0,
            column=0,
            sticky="w",
            padx=(0, 20),
            pady=10
        )

        self.institute_name = ctk.CTkEntry(
            form,
            height=42,
            placeholder_text="Enter institute name"
        )

        self.institute_name.grid(
            row=0,
            column=1,
            sticky="ew",
            pady=10
        )

        # Address

        ctk.CTkLabel(
            form,
            text="Address",
            font=("Segoe UI", 14, "bold"),
            text_color=self.text
        ).grid(
            row=1,
            column=0,
            sticky="w",
            padx=(0, 20),
            pady=10
        )

        self.address = ctk.CTkEntry(
            form,
            height=42,
            placeholder_text="Enter institute address"
        )

        self.address.grid(
            row=1,
            column=1,
            sticky="ew",
            pady=10
        )

        # Phone

        ctk.CTkLabel(
            form,
            text="Phone",
            font=("Segoe UI", 14, "bold"),
            text_color=self.text
        ).grid(
            row=2,
            column=0,
            sticky="w",
            padx=(0, 20),
            pady=10
        )

        self.phone = ctk.CTkEntry(
            form,
            height=42,
            placeholder_text="Enter phone number"
        )

        self.phone.grid(
            row=2,
            column=1,
            sticky="ew",
            pady=10
        )

        # Email

        ctk.CTkLabel(
            form,
            text="Email",
            font=("Segoe UI", 14, "bold"),
            text_color=self.text
        ).grid(
            row=3,
            column=0,
            sticky="w",
            padx=(0, 20),
            pady=10
        )

        self.email = ctk.CTkEntry(
            form,
            height=42,
            placeholder_text="Enter email address"
        )

        self.email.grid(
            row=3,
            column=1,
            sticky="ew",
            pady=10
        )

        # Save Button

        ctk.CTkButton(
            info_card,
            text="💾  Save Settings",
            width=180,
            height=42,
            corner_radius=10,
            fg_color=self.primary,
            hover_color=self.primary_hover,
            font=("Segoe UI", 14, "bold"),
            command=self.save_settings
        ).pack(
            anchor="w",
            padx=25,
            pady=(0, 25)
        )

        # ======================================================
        # LOGO
        # ======================================================

        logo_card = ctk.CTkFrame(
            content,
            fg_color=self.card,
            corner_radius=15
        )

        logo_card.pack(
            fill="x",
            pady=(0, 20)
        )

        ctk.CTkLabel(
            logo_card,
            text="🖼️  Institute Logo",
            font=("Segoe UI", 20, "bold"),
            text_color=self.text
        ).pack(
            anchor="w",
            padx=25,
            pady=(20, 5)
        )

        ctk.CTkLabel(
            logo_card,
            text="Select a logo image for your institute.",
            font=("Segoe UI", 13),
            text_color=self.secondary_text
        ).pack(
            anchor="w",
            padx=25,
            pady=(0, 15)
        )

        logo_area = ctk.CTkFrame(
            logo_card,
            fg_color="transparent"
        )

        logo_area.pack(
            fill="x",
            padx=25,
            pady=(0, 25)
        )

        self.logo_preview = ctk.CTkLabel(
            logo_area,
            text="🏫\nNo Logo Selected",
            width=150,
            height=120,
            fg_color="#EEF2FF",
            corner_radius=12,
            font=("Segoe UI", 14, "bold"),
            text_color=self.secondary_text
        )

        self.logo_preview.pack(
            side="left",
            padx=(0, 25)
        )

        ctk.CTkButton(
            logo_area,
            text="📁  Choose Logo",
            width=170,
            height=42,
            fg_color=self.purple,
            hover_color=self.purple_hover,
            font=("Segoe UI", 14, "bold"),
            command=self.choose_logo
        ).pack(
            side="left"
        )

        # ======================================================
        # APPEARANCE
        # ======================================================

        theme_card = ctk.CTkFrame(
            content,
            fg_color=self.card,
            corner_radius=15
        )

        theme_card.pack(
            fill="x",
            pady=(0, 20)
        )

        ctk.CTkLabel(
            theme_card,
            text="🎨  Appearance",
            font=("Segoe UI", 20, "bold"),
            text_color=self.text
        ).pack(
            anchor="w",
            padx=25,
            pady=(20, 5)
        )

        ctk.CTkLabel(
            theme_card,
            text="Choose the appearance mode of the ERP.",
            font=("Segoe UI", 13),
            text_color=self.secondary_text
        ).pack(
            anchor="w",
            padx=25,
            pady=(0, 15)
        )

        theme_row = ctk.CTkFrame(
            theme_card,
            fg_color="transparent"
        )

        theme_row.pack(
            fill="x",
            padx=25,
            pady=(0, 25)
        )

        self.theme = ctk.CTkComboBox(
            theme_row,
            values=["Light", "Dark", "System"],
            width=180,
            height=40
        )

        self.theme.set("Light")

        self.theme.pack(
            side="left"
        )

        ctk.CTkButton(
            theme_row,
            text="🎨  Apply Theme",
            width=170,
            height=40,
            fg_color=self.warning,
            hover_color=self.warning_hover,
            text_color="white",
            font=("Segoe UI", 14, "bold"),
            command=self.change_theme
        ).pack(
            side="left",
            padx=15
        )

        # ======================================================
        # DATABASE
        # ======================================================

        database_card = ctk.CTkFrame(
            content,
            fg_color=self.card,
            corner_radius=15
        )

        database_card.pack(
            fill="x",
            pady=(0, 20)
        )

        ctk.CTkLabel(
            database_card,
            text="💾  Database Management",
            font=("Segoe UI", 20, "bold"),
            text_color=self.text
        ).pack(
            anchor="w",
            padx=25,
            pady=(20, 5)
        )

        ctk.CTkLabel(
            database_card,
            text="Create a backup or restore an existing database.",
            font=("Segoe UI", 13),
            text_color=self.secondary_text
        ).pack(
            anchor="w",
            padx=25,
            pady=(0, 15)
        )

        database_buttons = ctk.CTkFrame(
            database_card,
            fg_color="transparent"
        )

        database_buttons.pack(
            anchor="w",
            padx=25,
            pady=(0, 25)
        )

        ctk.CTkButton(
            database_buttons,
            text="⬇  Backup Database",
            width=190,
            height=42,
            fg_color=self.success,
            hover_color=self.success_hover,
            font=("Segoe UI", 14, "bold"),
            command=self.backup_database
        ).pack(
            side="left"
        )

        ctk.CTkButton(
            database_buttons,
            text="⬆  Restore Database",
            width=190,
            height=42,
            fg_color=self.danger,
            hover_color=self.danger_hover,
            font=("Segoe UI", 14, "bold"),
            command=self.restore_database
        ).pack(
            side="left",
            padx=15
        )

        # ======================================================
        # PASSWORD
        # ======================================================

        password_card = ctk.CTkFrame(
            content,
            fg_color=self.card,
            corner_radius=15
        )

        password_card.pack(
            fill="x",
            pady=(0, 20)
        )

        ctk.CTkLabel(
            password_card,
            text="🔐  Security",
            font=("Segoe UI", 20, "bold"),
            text_color=self.text
        ).pack(
            anchor="w",
            padx=25,
            pady=(20, 5)
        )

        ctk.CTkLabel(
            password_card,
            text="Change the administrator password.",
            font=("Segoe UI", 13),
            text_color=self.secondary_text
        ).pack(
            anchor="w",
            padx=25,
            pady=(0, 15)
        )

        password_row = ctk.CTkFrame(
            password_card,
            fg_color="transparent"
        )

        password_row.pack(
            fill="x",
            padx=25,
            pady=(0, 25)
        )

        self.new_password = ctk.CTkEntry(
            password_row,
            width=300,
            height=42,
            show="*",
            placeholder_text="Enter new password"
        )

        self.new_password.pack(
            side="left"
        )

        ctk.CTkButton(
            password_row,
            text="🔑  Change Password",
            width=190,
            height=42,
            fg_color=self.danger,
            hover_color=self.danger_hover,
            font=("Segoe UI", 14, "bold"),
            command=self.change_password
        ).pack(
            side="left",
            padx=15
        )

        # ======================================================
        # FOOTER
        # ======================================================

        ctk.CTkLabel(
            content,
            text="© 2026 Student Management System ERP | Developed by Durgesh Gupta",
            font=("Segoe UI", 12),
            text_color="gray"
        ).pack(
            pady=15
        )

    # ==========================================================
    # SAVE SETTINGS
    # ==========================================================

    def save_settings(self):

        institute = self.institute_name.get().strip()

        if institute == "":
            messagebox.showwarning(
                "Required",
                "Please enter Institute Name."
            )
            return

        messagebox.showinfo(
            "Success",
            "Settings Saved Successfully."
        )

    # ==========================================================
    # CHOOSE LOGO
    # ==========================================================

    def choose_logo(self):

        file = filedialog.askopenfilename(
            title="Select Institute Logo",
            filetypes=[
                ("Image Files", "*.png *.jpg *.jpeg")
            ]
        )

        if not file:
            return

        try:

            if not os.path.exists("logos"):
                os.makedirs("logos")

            filename = os.path.basename(file)

            destination = os.path.join(
                "logos",
                filename
            )

            shutil.copy2(
                file,
                destination
            )

            self.logo_path = destination

            # Preview
            image = ctk.CTkImage(
                light_image=None,
                dark_image=None,
                size=(100, 100)
            )

            try:

                from PIL import Image

                pil_image = Image.open(
                    self.logo_path
                )

                self.logo_image = ctk.CTkImage(
                    light_image=pil_image,
                    dark_image=pil_image,
                    size=(100, 100)
                )

                self.logo_preview.configure(
                    image=self.logo_image,
                    text=""
                )

            except Exception:

                self.logo_preview.configure(
                    text="✓\nLogo Selected"
                )

            messagebox.showinfo(
                "Success",
                "Logo Selected Successfully."
            )

        except Exception as e:

            messagebox.showerror(
                "Error",
                f"Unable to select logo.\n\n{e}"
            )

    # ==========================================================
    # CHANGE THEME
    # ==========================================================

    def change_theme(self):

        mode = self.theme.get()

        if mode == "Light":

            ctk.set_appearance_mode("light")

        elif mode == "Dark":

            ctk.set_appearance_mode("dark")

        else:

            ctk.set_appearance_mode("system")

        messagebox.showinfo(
            "Theme",
            f"{mode} Theme Applied Successfully."
        )

    # ==========================================================
    # BACKUP DATABASE
    # ==========================================================

    def backup_database(self):

        file = filedialog.asksaveasfilename(
            defaultextension=".db",
            filetypes=[
                ("Database File", "*.db")
            ],
            title="Save Database Backup"
        )

        if not file:
            return

        try:

            self.database.conn.commit()

            db_path = self.database.conn.execute(
                "PRAGMA database_list"
            ).fetchone()[2]

            shutil.copy2(
                db_path,
                file
            )

            messagebox.showinfo(
                "Backup Complete",
                "Database Backup Created Successfully."
            )

        except Exception as e:

            messagebox.showerror(
                "Backup Error",
                str(e)
            )

    # ==========================================================
    # RESTORE DATABASE
    # ==========================================================

    def restore_database(self):

        file = filedialog.askopenfilename(
            title="Select Backup Database",
            filetypes=[
                ("Database File", "*.db")
            ]
        )

        if not file:
            return

        answer = messagebox.askyesno(
            "Confirm Restore",
            "Restoring the database will replace the current database.\n\n"
            "Are you sure you want to continue?"
        )

        if not answer:
            return

        try:

            db_path = self.database.conn.execute(
                "PRAGMA database_list"
            ).fetchone()[2]

            self.database.conn.close()

            shutil.copy2(
                file,
                db_path
            )

            messagebox.showinfo(
                "Restore Complete",
                "Database Restored Successfully.\n\n"
                "Please restart the application."
            )

        except Exception as e:

            messagebox.showerror(
                "Restore Error",
                str(e)
            )

    # ==========================================================
    # CHANGE PASSWORD
    # ==========================================================

    def change_password(self):

        password = self.new_password.get().strip()

        if password == "":

            messagebox.showwarning(
                "Required",
                "Please Enter New Password."
            )

            return

        if len(password) < 4:

            messagebox.showwarning(
                "Invalid Password",
                "Password must contain at least 4 characters."
            )

            return

        try:

            self.database.cursor.execute(
                """
                UPDATE users
                SET password=?
                WHERE username='admin'
                """,
                (password,)
            )

            self.database.conn.commit()

            self.new_password.delete(
                0,
                "end"
            )

            messagebox.showinfo(
                "Success",
                "Password Changed Successfully."
            )

        except Exception as e:

            messagebox.showerror(
                "Password Error",
                str(e)
            )