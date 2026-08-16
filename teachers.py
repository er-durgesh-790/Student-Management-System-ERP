
import customtkinter as ctk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import os
import shutil


class TeacherModule:

    # ==========================================================
    # CONSTRUCTOR
    # ==========================================================

    def __init__(self, root, database):

        self.root = root
        self.database = database

        self.photo_path = ""
        self.photo_image = None

        self.create_ui()
        self.load_teachers()

    # ==========================================================
    # CREATE UI
    # ==========================================================

    def create_ui(self):

        # ======================================================
        # COLORS
        # ======================================================

        self.bg_color = "#F8FAFC"
        self.card_color = "#FFFFFF"
        self.primary = "#2563EB"
        self.primary_hover = "#1D4ED8"
        self.success = "#16A34A"
        self.success_hover = "#15803D"
        self.danger = "#DC2626"
        self.danger_hover = "#B91C1C"
        self.warning = "#F59E0B"
        self.warning_hover = "#D97706"
        self.text_color = "#111827"
        self.secondary_text = "#64748B"
        self.border_color = "#E2E8F0"

        # ======================================================
        # MAIN FRAME
        # ======================================================

        self.main_frame = ctk.CTkFrame(
            self.root,
            fg_color=self.bg_color,
            corner_radius=0
        )

        self.main_frame.pack(
            fill="both",
            expand=True
        )

        # ======================================================
        # HEADER
        # ======================================================

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
            text="👨‍🏫  Teacher Management",
            font=("Segoe UI", 26, "bold"),
            text_color="white"
        ).pack(
            side="left",
            padx=25
        )

        ctk.CTkLabel(
            header,
            text="Manage teacher records",
            font=("Segoe UI", 13),
            text_color="#DBEAFE"
        ).pack(
            side="right",
            padx=25
        )

        # ======================================================
        # FORM CARD
        # ======================================================

        form_card = ctk.CTkFrame(
            self.main_frame,
            fg_color=self.card_color,
            corner_radius=15,
            border_width=1,
            border_color=self.border_color
        )

        form_card.pack(
            fill="x",
            padx=20,
            pady=(20, 10)
        )

        ctk.CTkLabel(
            form_card,
            text="Teacher Information",
            font=("Segoe UI", 19, "bold"),
            text_color=self.text_color
        ).grid(
            row=0,
            column=0,
            columnspan=4,
            padx=20,
            pady=(18, 15),
            sticky="w"
        )

        # ======================================================
        # FORM COLUMN CONFIGURATION
        # ======================================================

        form_card.grid_columnconfigure(1, weight=1)
        form_card.grid_columnconfigure(3, weight=1)

        # ======================================================
        # TEACHER ID
        # ======================================================

        ctk.CTkLabel(
            form_card,
            text="Teacher ID",
            font=("Segoe UI", 14, "bold"),
            text_color=self.text_color
        ).grid(
            row=1,
            column=0,
            padx=(20, 10),
            pady=8,
            sticky="w"
        )

        self.teacher_id = ctk.CTkEntry(
            form_card,
            width=260,
            height=40,
            placeholder_text="Enter Teacher ID"
        )

        self.teacher_id.grid(
            row=1,
            column=1,
            padx=10,
            pady=8,
            sticky="ew"
        )

        # ======================================================
        # TEACHER NAME
        # ======================================================

        ctk.CTkLabel(
            form_card,
            text="Teacher Name",
            font=("Segoe UI", 14, "bold"),
            text_color=self.text_color
        ).grid(
            row=1,
            column=2,
            padx=(20, 10),
            pady=8,
            sticky="w"
        )

        self.teacher_name = ctk.CTkEntry(
            form_card,
            width=260,
            height=40,
            placeholder_text="Enter Teacher Name"
        )

        self.teacher_name.grid(
            row=1,
            column=3,
            padx=10,
            pady=8,
            sticky="ew"
        )

        # ======================================================
        # MOBILE
        # ======================================================

        ctk.CTkLabel(
            form_card,
            text="Mobile",
            font=("Segoe UI", 14, "bold"),
            text_color=self.text_color
        ).grid(
            row=2,
            column=0,
            padx=(20, 10),
            pady=8,
            sticky="w"
        )

        self.mobile = ctk.CTkEntry(
            form_card,
            width=260,
            height=40,
            placeholder_text="Enter Mobile Number"
        )

        self.mobile.grid(
            row=2,
            column=1,
            padx=10,
            pady=8,
            sticky="ew"
        )

        # ======================================================
        # SUBJECT
        # ======================================================

        ctk.CTkLabel(
            form_card,
            text="Subject",
            font=("Segoe UI", 14, "bold"),
            text_color=self.text_color
        ).grid(
            row=2,
            column=2,
            padx=(20, 10),
            pady=8,
            sticky="w"
        )

        self.subject = ctk.CTkEntry(
            form_card,
            width=260,
            height=40,
            placeholder_text="Enter Subject"
        )

        self.subject.grid(
            row=2,
            column=3,
            padx=10,
            pady=8,
            sticky="ew"
        )

        # ======================================================
        # QUALIFICATION
        # ======================================================

        ctk.CTkLabel(
            form_card,
            text="Qualification",
            font=("Segoe UI", 14, "bold"),
            text_color=self.text_color
        ).grid(
            row=3,
            column=0,
            padx=(20, 10),
            pady=8,
            sticky="w"
        )

        self.qualification = ctk.CTkEntry(
            form_card,
            width=260,
            height=40,
            placeholder_text="e.g. M.Tech / B.Tech / M.Sc"
        )

        self.qualification.grid(
            row=3,
            column=1,
            padx=10,
            pady=8,
            sticky="ew"
        )

        # ======================================================
        # PHOTO AREA
        # ======================================================

        photo_area = ctk.CTkFrame(
            form_card,
            fg_color="transparent"
        )

        photo_area.grid(
            row=3,
            column=2,
            rowspan=2,
            columnspan=2,
            padx=20,
            pady=10,
            sticky="e"
        )

        self.photo_label = ctk.CTkLabel(
            photo_area,
            text="No Photo",
            width=120,
            height=120,
            fg_color="#F1F5F9",
            corner_radius=12,
            text_color=self.secondary_text
        )

        self.photo_label.pack(
            side="left",
            padx=(0, 15)
        )

        photo_buttons = ctk.CTkFrame(
            photo_area,
            fg_color="transparent"
        )

        photo_buttons.pack(
            side="left"
        )

        ctk.CTkLabel(
            photo_buttons,
            text="Teacher Photo",
            font=("Segoe UI", 14, "bold"),
            text_color=self.text_color
        ).pack(
            pady=(0, 8)
        )

        self.photo_btn = ctk.CTkButton(
            photo_buttons,
            text="📷 Choose Photo",
            width=160,
            height=40,
            fg_color=self.primary,
            hover_color=self.primary_hover,
            command=self.choose_photo
        )

        self.photo_btn.pack(
            pady=5
        )

        # ======================================================
        # BUTTON FRAME
        # ======================================================

        button_frame = ctk.CTkFrame(
            form_card,
            fg_color="transparent"
        )

        button_frame.grid(
            row=4,
            column=0,
            columnspan=2,
            padx=20,
            pady=(15, 20),
            sticky="w"
        )

        # ADD
        ctk.CTkButton(
            button_frame,
            text="➕ Add Teacher",
            width=145,
            height=42,
            fg_color=self.success,
            hover_color=self.success_hover,
            font=("Segoe UI", 13, "bold"),
            command=self.add_teacher
        ).pack(
            side="left",
            padx=(0, 8)
        )

        # UPDATE
        ctk.CTkButton(
            button_frame,
            text="✏ Update",
            width=120,
            height=42,
            fg_color=self.primary,
            hover_color=self.primary_hover,
            font=("Segoe UI", 13, "bold"),
            command=self.update_teacher
        ).pack(
            side="left",
            padx=8
        )

        # DELETE
        ctk.CTkButton(
            button_frame,
            text="🗑 Delete",
            width=120,
            height=42,
            fg_color=self.danger,
            hover_color=self.danger_hover,
            font=("Segoe UI", 13, "bold"),
            command=self.delete_teacher
        ).pack(
            side="left",
            padx=8
        )

        # CLEAR
        ctk.CTkButton(
            button_frame,
            text="↻ Clear",
            width=120,
            height=42,
            fg_color="#64748B",
            hover_color="#475569",
            font=("Segoe UI", 13, "bold"),
            command=self.clear_fields
        ).pack(
            side="left",
            padx=8
        )

        # ======================================================
        # SEARCH CARD
        # ======================================================

        search_card = ctk.CTkFrame(
            self.main_frame,
            fg_color=self.card_color,
            corner_radius=15,
            border_width=1,
            border_color=self.border_color
        )

        search_card.pack(
            fill="x",
            padx=20,
            pady=10
        )

        ctk.CTkLabel(
            search_card,
            text="🔎 Search Teacher",
            font=("Segoe UI", 17, "bold"),
            text_color=self.text_color
        ).pack(
            side="left",
            padx=(20, 10)
        )

        self.search_entry = ctk.CTkEntry(
            search_card,
            width=300,
            height=40,
            placeholder_text="Teacher ID / Name / Mobile"
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
            command=self.search_teacher
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
            command=self.load_teachers
        ).pack(
            side="left",
            padx=5
        )

        # ======================================================
        # TABLE CARD
        # ======================================================

        table_card = ctk.CTkFrame(
            self.main_frame,
            fg_color=self.card_color,
            corner_radius=15,
            border_width=1,
            border_color=self.border_color
        )

        table_card.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(10, 20)
        )

        ctk.CTkLabel(
            table_card,
            text="📋 Teacher Records",
            font=("Segoe UI", 18, "bold"),
            text_color=self.text_color
        ).pack(
            anchor="w",
            padx=20,
            pady=(15, 5)
        )

        # ======================================================
        # TREEVIEW STYLE
        # ======================================================

        style = ttk.Style()

        try:
            style.theme_use("clam")
        except Exception:
            pass

        style.configure(
            "Teacher.Treeview",
            background="#FFFFFF",
            foreground="#111827",
            rowheight=38,
            fieldbackground="#FFFFFF",
            font=("Segoe UI", 11)
        )

        style.configure(
            "Teacher.Treeview.Heading",
            background="#2563EB",
            foreground="white",
            font=("Segoe UI", 11, "bold"),
            relief="flat"
        )

        style.map(
            "Teacher.Treeview",
            background=[
                ("selected", "#DBEAFE")
            ],
            foreground=[
                ("selected", "#111827")
            ]
        )

        # ======================================================
        # TABLE FRAME
        # ======================================================

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

        columns = (
            "Teacher ID",
            "Teacher Name",
            "Mobile",
            "Subject",
            "Qualification"
        )

        self.teacher_table = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            style="Teacher.Treeview"
        )

        # ======================================================
        # TABLE HEADINGS
        # ======================================================

        for col in columns:

            self.teacher_table.heading(
                col,
                text=col
            )

        self.teacher_table.column(
            "Teacher ID",
            width=140,
            anchor="center"
        )

        self.teacher_table.column(
            "Teacher Name",
            width=220,
            anchor="w"
        )

        self.teacher_table.column(
            "Mobile",
            width=170,
            anchor="center"
        )

        self.teacher_table.column(
            "Subject",
            width=200,
            anchor="w"
        )

        self.teacher_table.column(
            "Qualification",
            width=220,
            anchor="w"
        )

        # ======================================================
        # SCROLLBAR
        # ======================================================

        scrollbar = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=self.teacher_table.yview
        )

        self.teacher_table.configure(
            yscrollcommand=scrollbar.set
        )

        self.teacher_table.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        # ======================================================
        # SELECT EVENT
        # ======================================================

        self.teacher_table.bind(
            "<<TreeviewSelect>>",
            self.select_teacher
        )

    # ==========================================================
    # ADD TEACHER
    # ==========================================================

    def add_teacher(self):

        teacher_id = self.teacher_id.get().strip()
        teacher_name = self.teacher_name.get().strip()
        mobile = self.mobile.get().strip()
        subject = self.subject.get().strip()
        qualification = self.qualification.get().strip()

        if teacher_id == "":
            messagebox.showwarning(
                "Required",
                "Please enter Teacher ID."
            )
            self.teacher_id.focus()
            return

        if teacher_name == "":
            messagebox.showwarning(
                "Required",
                "Please enter Teacher Name."
            )
            self.teacher_name.focus()
            return

        try:

            self.database.add_teacher(
                teacher_id,
                teacher_name,
                mobile,
                subject,
                qualification,
                photo_path=self.photo_path
            )

            messagebox.showinfo(
                "Success",
                "Teacher added successfully."
            )

            self.load_teachers()
            self.clear_fields()

        except Exception as e:

            messagebox.showerror(
                "Database Error",
                f"Unable to add teacher.\n\n{e}"
            )

    # ==========================================================
    # LOAD TEACHERS
    # ==========================================================

    def load_teachers(self):

        for item in self.teacher_table.get_children():
            self.teacher_table.delete(item)

        try:

            teachers = self.database.fetch_teachers()

            for teacher in teachers:

                self.teacher_table.insert(
                    "",
                    "end",
                    values=(
                        teacher[1],
                        teacher[2],
                        teacher[3],
                        teacher[4],
                        teacher[5]
                    )
                )

        except Exception as e:

            messagebox.showerror(
                "Database Error",
                f"Unable to load teachers.\n\n{e}"
            )

    # ==========================================================
    # SELECT TEACHER
    # ==========================================================

    def select_teacher(self, event=None):

        selected = self.teacher_table.focus()

        if not selected:
            return

        data = self.teacher_table.item(
            selected
        ).get("values", [])

        if len(data) < 5:
            return

        self.teacher_id.delete(
            0,
            "end"
        )

        self.teacher_id.insert(
            0,
            data[0]
        )

        self.teacher_name.delete(
            0,
            "end"
        )

        self.teacher_name.insert(
            0,
            data[1]
        )

        self.mobile.delete(
            0,
            "end"
        )

        self.mobile.insert(
            0,
            data[2]
        )

        self.subject.delete(
            0,
            "end"
        )

        self.subject.insert(
            0,
            data[3]
        )

        self.qualification.delete(
            0,
            "end"
        )

        self.qualification.insert(
            0,
            data[4]
        )

        # ======================================================
        # FIND PHOTO FROM DATABASE
        # ======================================================

        try:

            teachers = self.database.fetch_teachers()

            for teacher in teachers:

                if str(teacher[1]) == str(data[0]):

                    if len(teacher) > 6:

                        saved_photo = teacher[6]

                        if saved_photo:
                            self.load_photo(
                                saved_photo
                            )
                        else:
                            self.clear_photo_preview()

                    else:

                        self.clear_photo_preview()

                    break

        except Exception as e:

            print(
                "Photo Load Error:",
                e
            )

    # ==========================================================
    # LOAD PHOTO
    # ==========================================================

    def load_photo(self, photo_path):

        if not photo_path:
            self.clear_photo_preview()
            return

        # Convert relative path into absolute path
        if not os.path.isabs(photo_path):

            base_dir = os.path.dirname(
                os.path.abspath(__file__)
            )

            photo_path = os.path.join(
                base_dir,
                photo_path
            )

        if not os.path.exists(photo_path):

            print(
                "Photo not found:",
                photo_path
            )

            self.clear_photo_preview()
            return

        try:

            image = Image.open(
                photo_path
            )

            image = image.convert(
                "RGB"
            )

            image.thumbnail(
                (120, 120)
            )

            self.photo_image = ImageTk.PhotoImage(
                image
            )

            self.photo_label.configure(
                image=self.photo_image,
                text="",
                fg_color="#FFFFFF"
            )

            self.photo_path = photo_path

            self.photo_btn.configure(
                text="📷 Change Photo"
            )

        except Exception as e:

            print(
                "Photo Preview Error:",
                e
            )

            self.clear_photo_preview()

    # ==========================================================
    # CLEAR PHOTO PREVIEW
    # ==========================================================

    def clear_photo_preview(self):

        self.photo_image = None
        self.photo_path = ""

        self.photo_label.configure(
            image=None,
            text="No Photo",
            fg_color="#F1F5F9"
        )

        self.photo_btn.configure(
            text="📷 Choose Photo"
        )

    # ==========================================================
    # UPDATE TEACHER
    # ==========================================================

    def update_teacher(self):

        teacher_id = self.teacher_id.get().strip()

        teacher_name = self.teacher_name.get().strip()
        mobile = self.mobile.get().strip()
        subject = self.subject.get().strip()
        qualification = self.qualification.get().strip()

        if teacher_id == "":
            messagebox.showwarning(
                "Select Teacher",
                "Please select a teacher first."
            )
            return

        if teacher_name == "":
            messagebox.showwarning(
                "Required",
                "Teacher Name cannot be empty."
            )
            return

        try:

            self.database.update_teacher(
                teacher_id,
                teacher_name,
                mobile,
                subject,
                qualification,
                photo_path=self.photo_path
            )

            messagebox.showinfo(
                "Success",
                "Teacher updated successfully."
            )

            self.load_teachers()
            self.clear_fields()

        except Exception as e:

            messagebox.showerror(
                "Database Error",
                f"Unable to update teacher.\n\n{e}"
            )

    # ==========================================================
    # DELETE TEACHER
    # ==========================================================

    def delete_teacher(self):

        teacher_id = self.teacher_id.get().strip()

        if teacher_id == "":
            messagebox.showwarning(
                "Select Teacher",
                "Please select a teacher first."
            )
            return

        answer = messagebox.askyesno(
            "Confirm Delete",
            "Are you sure you want to delete this teacher?"
        )

        if not answer:
            return

        try:

            self.database.delete_teacher(
                teacher_id
            )

            messagebox.showinfo(
                "Deleted",
                "Teacher deleted successfully."
            )

            self.load_teachers()
            self.clear_fields()

        except Exception as e:

            messagebox.showerror(
                "Database Error",
                f"Unable to delete teacher.\n\n{e}"
            )

    # ==========================================================
    # CLEAR FIELDS
    # ==========================================================

    def clear_fields(self):

        self.teacher_id.delete(
            0,
            "end"
        )

        self.teacher_name.delete(
            0,
            "end"
        )

        self.mobile.delete(
            0,
            "end"
        )

        self.subject.delete(
            0,
            "end"
        )

        self.qualification.delete(
            0,
            "end"
        )

        self.clear_photo_preview()

        if hasattr(
            self,
            "search_entry"
        ):

            self.search_entry.delete(
                0,
                "end"
            )

        # Remove table selection
        if hasattr(
            self,
            "teacher_table"
        ):

            for item in self.teacher_table.selection():

                self.teacher_table.selection_remove(
                    item
                )

    # ==========================================================
    # CHOOSE PHOTO
    # ==========================================================

    def choose_photo(self):

        file = filedialog.askopenfilename(
            title="Select Teacher Photo",
            filetypes=[
                (
                    "Image Files",
                    "*.png *.jpg *.jpeg"
                )
            ]
        )

        if not file:
            return

        try:

            # ==================================================
            # PROJECT DIRECTORY
            # ==================================================

            base_dir = os.path.dirname(
                os.path.abspath(__file__)
            )

            # ==================================================
            # PHOTOS DIRECTORY
            # ==================================================

            photos_dir = os.path.join(
                base_dir,
                "photos"
            )

            os.makedirs(
                photos_dir,
                exist_ok=True
            )

            # ==================================================
            # CREATE UNIQUE FILE NAME
            # ==================================================

            original_name = os.path.basename(
                file
            )

            name, extension = os.path.splitext(
                original_name
            )

            teacher_id = self.teacher_id.get().strip()

            if teacher_id:

                filename = (
                    f"teacher_{teacher_id}"
                    f"{extension.lower()}"
                )

            else:

                filename = original_name

            destination = os.path.join(
                photos_dir,
                filename
            )

            # ==================================================
            # COPY PHOTO
            # ==================================================

            shutil.copy2(
                file,
                destination
            )

            # ==================================================
            # SAVE PATH
            # ==================================================

            self.photo_path = destination

            # ==================================================
            # PREVIEW
            # ==================================================

            self.load_photo(
                destination
            )

            self.photo_btn.configure(
                text="📷 Photo Selected"
            )

            print(
                "Teacher Photo Saved:",
                destination
            )

        except Exception as e:

            messagebox.showerror(
                "Photo Error",
                f"Unable to save photo.\n\n{e}"
            )

    # ==========================================================
    # SEARCH TEACHER
    # ==========================================================

    def search_teacher(self):

        keyword = self.search_entry.get().strip()

        if keyword == "":

            self.load_teachers()
            return

        try:

            teachers = self.database.search_teachers(
                keyword
            )

            for item in self.teacher_table.get_children():

                self.teacher_table.delete(
                    item
                )

            for teacher in teachers:

                self.teacher_table.insert(
                    "",
                    "end",
                    values=(
                        teacher[1],
                        teacher[2],
                        teacher[3],
                        teacher[4],
                        teacher[5]
                    )
                )

        except Exception as e:

            messagebox.showerror(
                "Search Error",
                f"Unable to search teachers.\n\n{e}"
            )
