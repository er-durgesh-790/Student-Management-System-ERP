
import customtkinter as ctk
from tkinter import ttk
from tkinter import messagebox


class FeeModule:

    def __init__(self, root, database):

        self.root = root
        self.database = database

        self.create_ui()

    # =========================================================
    # CREATE UI
    # =========================================================

    def create_ui(self):

        self.main_frame = ctk.CTkFrame(
            self.root,
            fg_color="#F5F7FB",
            corner_radius=0
        )

        self.main_frame.pack(
            fill="both",
            expand=True
        )

        # =====================================================
        # HEADER
        # =====================================================

        header = ctk.CTkFrame(
            self.main_frame,
            height=80,
            fg_color="#2563EB",
            corner_radius=0
        )

        header.pack(
            fill="x"
        )

        header.pack_propagate(False)

        ctk.CTkLabel(
            header,
            text="💳  Fees Management",
            font=("Segoe UI", 27, "bold"),
            text_color="white"
        ).pack(
            side="left",
            padx=25
        )

        ctk.CTkLabel(
            header,
            text="Manage student fee records",
            font=("Segoe UI", 13),
            text_color="#DBEAFE"
        ).pack(
            side="right",
            padx=25
        )

        # =====================================================
        # FORM CARD
        # =====================================================

        form_card = ctk.CTkFrame(
            self.main_frame,
            fg_color="white",
            corner_radius=15
        )

        form_card.pack(
            fill="x",
            padx=25,
            pady=(20, 10)
        )

        ctk.CTkLabel(
            form_card,
            text="Fee Details",
            font=("Segoe UI", 18, "bold"),
            text_color="#111827"
        ).grid(
            row=0,
            column=0,
            columnspan=4,
            sticky="w",
            padx=20,
            pady=(15, 10)
        )

        # -----------------------------------------------------
        # Student ID
        # -----------------------------------------------------

        ctk.CTkLabel(
            form_card,
            text="Student ID",
            font=("Segoe UI", 13, "bold"),
            text_color="#374151"
        ).grid(
            row=1,
            column=0,
            padx=15,
            pady=8,
            sticky="w"
        )

        self.student_id = ctk.CTkEntry(
            form_card,
            width=220,
            height=40,
            placeholder_text="Enter Student ID"
        )

        self.student_id.grid(
            row=1,
            column=1,
            padx=15,
            pady=8
        )

        # -----------------------------------------------------
        # Student Name
        # -----------------------------------------------------

        ctk.CTkLabel(
            form_card,
            text="Student Name",
            font=("Segoe UI", 13, "bold"),
            text_color="#374151"
        ).grid(
            row=1,
            column=2,
            padx=15,
            pady=8,
            sticky="w"
        )

        self.student_name = ctk.CTkEntry(
            form_card,
            width=220,
            height=40,
            placeholder_text="Enter Student Name"
        )

        self.student_name.grid(
            row=1,
            column=3,
            padx=15,
            pady=8
        )

        # -----------------------------------------------------
        # Course
        # -----------------------------------------------------

        ctk.CTkLabel(
            form_card,
            text="Course",
            font=("Segoe UI", 13, "bold"),
            text_color="#374151"
        ).grid(
            row=2,
            column=0,
            padx=15,
            pady=8,
            sticky="w"
        )

        self.course = ctk.CTkEntry(
            form_card,
            width=220,
            height=40,
            placeholder_text="Enter Course"
        )

        self.course.grid(
            row=2,
            column=1,
            padx=15,
            pady=8
        )

        # -----------------------------------------------------
        # Amount
        # -----------------------------------------------------

        ctk.CTkLabel(
            form_card,
            text="Amount (₹)",
            font=("Segoe UI", 13, "bold"),
            text_color="#374151"
        ).grid(
            row=2,
            column=2,
            padx=15,
            pady=8,
            sticky="w"
        )

        self.amount = ctk.CTkEntry(
            form_card,
            width=220,
            height=40,
            placeholder_text="Enter Fee Amount"
        )

        self.amount.grid(
            row=2,
            column=3,
            padx=15,
            pady=8
        )

        # -----------------------------------------------------
        # Status
        # -----------------------------------------------------

        ctk.CTkLabel(
            form_card,
            text="Payment Status",
            font=("Segoe UI", 13, "bold"),
            text_color="#374151"
        ).grid(
            row=3,
            column=0,
            padx=15,
            pady=8,
            sticky="w"
        )

        self.status = ctk.CTkComboBox(
            form_card,
            values=[
                "Paid",
                "Pending"
            ],
            width=220,
            height=40,
            button_color="#2563EB",
            button_hover_color="#1D4ED8"
        )

        self.status.grid(
            row=3,
            column=1,
            padx=15,
            pady=(8, 18)
        )

        self.status.set("Pending")

        # =====================================================
        # BUTTON CARD
        # =====================================================

        button_frame = ctk.CTkFrame(
            self.main_frame,
            fg_color="white",
            corner_radius=15
        )

        button_frame.pack(
            fill="x",
            padx=25,
            pady=10
        )

        ctk.CTkLabel(
            button_frame,
            text="Actions",
            font=("Segoe UI", 16, "bold"),
            text_color="#111827"
        ).pack(
            side="left",
            padx=(20, 15)
        )

        # Add

        ctk.CTkButton(
            button_frame,
            text="➕ Add Fee",
            width=130,
            height=38,
            corner_radius=8,
            fg_color="#16A34A",
            hover_color="#15803D",
            font=("Segoe UI", 13, "bold"),
            command=self.add_fee
        ).pack(
            side="left",
            padx=5,
            pady=12
        )

        # Update

        ctk.CTkButton(
            button_frame,
            text="✏ Update",
            width=130,
            height=38,
            corner_radius=8,
            fg_color="#2563EB",
            hover_color="#1D4ED8",
            font=("Segoe UI", 13, "bold"),
            command=self.update_fee
        ).pack(
            side="left",
            padx=5
        )

        # Delete

        ctk.CTkButton(
            button_frame,
            text="🗑 Delete",
            width=130,
            height=38,
            corner_radius=8,
            fg_color="#DC2626",
            hover_color="#B91C1C",
            font=("Segoe UI", 13, "bold"),
            command=self.delete_fee
        ).pack(
            side="left",
            padx=5
        )

        # Clear

        ctk.CTkButton(
            button_frame,
            text="🧹 Clear",
            width=130,
            height=38,
            corner_radius=8,
            fg_color="#6B7280",
            hover_color="#4B5563",
            font=("Segoe UI", 13, "bold"),
            command=self.clear_fields
        ).pack(
            side="left",
            padx=5
        )

        # =====================================================
        # SEARCH CARD
        # =====================================================

        search_frame = ctk.CTkFrame(
            self.main_frame,
            fg_color="white",
            corner_radius=15
        )

        search_frame.pack(
            fill="x",
            padx=25,
            pady=10
        )

        ctk.CTkLabel(
            search_frame,
            text="🔍 Search Fees",
            font=("Segoe UI", 16, "bold"),
            text_color="#111827"
        ).pack(
            side="left",
            padx=(20, 10)
        )

        self.search_entry = ctk.CTkEntry(
            search_frame,
            width=300,
            height=38,
            placeholder_text="Student ID / Student Name"
        )

        self.search_entry.pack(
            side="left",
            padx=10,
            pady=12
        )

        ctk.CTkButton(
            search_frame,
            text="Search",
            width=110,
            height=38,
            corner_radius=8,
            fg_color="#2563EB",
            hover_color="#1D4ED8",
            command=self.search_fee
        ).pack(
            side="left",
            padx=5
        )

        ctk.CTkButton(
            search_frame,
            text="Show All",
            width=110,
            height=38,
            corner_radius=8,
            fg_color="#64748B",
            hover_color="#475569",
            command=self.load_fees
        ).pack(
            side="left",
            padx=5
        )

        # =====================================================
        # TABLE CARD
        # =====================================================

        table_card = ctk.CTkFrame(
            self.main_frame,
            fg_color="white",
            corner_radius=15
        )

        table_card.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=(5, 20)
        )

        ctk.CTkLabel(
            table_card,
            text="Fee Records",
            font=("Segoe UI", 17, "bold"),
            text_color="#111827"
        ).pack(
            anchor="w",
            padx=20,
            pady=(15, 5)
        )

        # =====================================================
        # TREEVIEW STYLE
        # =====================================================

        style = ttk.Style()

        try:
            style.theme_use("clam")
        except:
            pass

        style.configure(
            "Fee.Treeview",
            background="white",
            foreground="#1F2937",
            rowheight=38,
            fieldbackground="white",
            font=("Segoe UI", 11)
        )

        style.configure(
            "Fee.Treeview.Heading",
            background="#2563EB",
            foreground="white",
            font=("Segoe UI", 11, "bold"),
            padding=8
        )

        style.map(
            "Fee.Treeview",
            background=[
                ("selected", "#DBEAFE")
            ],
            foreground=[
                ("selected", "#111827")
            ]
        )

        # =====================================================
        # TABLE
        # =====================================================

        table_frame = ctk.CTkFrame(
            table_card,
            fg_color="white"
        )

        table_frame.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=10
        )

        columns = (
            "Student ID",
            "Student Name",
            "Course",
            "Amount",
            "Status"
        )

        self.fee_table = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            height=10,
            style="Fee.Treeview"
        )

        for col in columns:

            self.fee_table.heading(
                col,
                text=col
            )

            self.fee_table.column(
                col,
                width=170,
                anchor="center"
            )

        scrollbar = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=self.fee_table.yview
        )

        self.fee_table.configure(
            yscrollcommand=scrollbar.set
        )

        self.fee_table.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        self.fee_table.bind(
            "<<TreeviewSelect>>",
            self.select_fee
        )

        # Load Data

        self.load_fees()

    # =========================================================
    # ADD FEE
    # =========================================================

    def add_fee(self):

        student_id = self.student_id.get().strip()
        student_name = self.student_name.get().strip()
        course = self.course.get().strip()
        amount = self.amount.get().strip()
        status = self.status.get()

        if (
            student_id == "" or
            student_name == "" or
            course == "" or
            amount == ""
        ):

            messagebox.showerror(
                "Required Fields",
                "Please fill all required fields."
            )

            return

        try:
            amount_value = float(amount)

            if amount_value < 0:
                raise ValueError

        except ValueError:

            messagebox.showerror(
                "Invalid Amount",
                "Please enter a valid fee amount."
            )

            return

        try:

            success = self.database.add_fee(
                student_id,
                student_name,
                course,
                amount,
                status
            )

            if not success:
                messagebox.showerror(
                    "Error",
                    "Fee could not be added."
                )
                return

            self.load_fees()
            self.clear_fields()

            messagebox.showinfo(
                "Success",
                "Fee Added Successfully."
            )

        except Exception as e:

            messagebox.showerror(
                "Database Error",
                str(e)
            )

    # =========================================================
    # LOAD FEES
    # =========================================================

    def load_fees(self):

        for item in self.fee_table.get_children():
            self.fee_table.delete(item)

        try:

            fees = self.database.fetch_fees()

            for fee in fees:

                self.fee_table.insert(
                    "",
                    "end",
                    values=(
                        fee[1],
                        fee[2],
                        fee[3],
                        fee[4],
                        fee[5]
                    )
                )

        except Exception as e:

            messagebox.showerror(
                "Database Error",
                str(e)
            )

    # =========================================================
    # SELECT FEE
    # =========================================================

    def select_fee(self, event):

        selected = self.fee_table.focus()

        if not selected:
            return

        data = self.fee_table.item(
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

        self.amount.delete(0, "end")
        self.amount.insert(0, data[3])

        self.status.set(data[4])

    # =========================================================
    # UPDATE FEE
    # =========================================================

    def update_fee(self):

        student_id = self.student_id.get().strip()

        if student_id == "":

            messagebox.showerror(
                "Error",
                "Please select a fee record first."
            )

            return

        try:

            self.database.update_fee(
                self.student_id.get().strip(),
                self.student_name.get().strip(),
                self.course.get().strip(),
                self.amount.get().strip(),
                self.status.get()
            )

            self.load_fees()
            self.clear_fields()

            messagebox.showinfo(
                "Success",
                "Fee Updated Successfully."
            )

        except Exception as e:

            messagebox.showerror(
                "Database Error",
                str(e)
            )

    # =========================================================
    # DELETE FEE
    # =========================================================

    def delete_fee(self):

        student_id = self.student_id.get().strip()

        if student_id == "":

            messagebox.showerror(
                "Error",
                "Please select a fee record first."
            )

            return

        confirm = messagebox.askyesno(
            "Confirm Delete",
            "Are you sure you want to delete this fee record?"
        )

        if not confirm:
            return

        try:

            self.database.delete_fee(
                student_id
            )

            self.load_fees()
            self.clear_fields()

            messagebox.showinfo(
                "Success",
                "Fee Deleted Successfully."
            )

        except Exception as e:

            messagebox.showerror(
                "Database Error",
                str(e)
            )

    # =========================================================
    # SEARCH FEE
    # =========================================================

    def search_fee(self):

        keyword = self.search_entry.get().strip()

        if keyword == "":
            self.load_fees()
            return

        for item in self.fee_table.get_children():
            self.fee_table.delete(item)

        try:

            fees = self.database.search_fees(
                keyword
            )

            for fee in fees:

                self.fee_table.insert(
                    "",
                    "end",
                    values=(
                        fee[1],
                        fee[2],
                        fee[3],
                        fee[4],
                        fee[5]
                    )
                )

        except Exception as e:

            messagebox.showerror(
                "Database Error",
                str(e)
            )

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

        self.amount.delete(
            0,
            "end"
        )

        self.status.set(
            "Pending"
        )

        # Remove table selection

        try:
            self.fee_table.selection_remove(
                self.fee_table.selection()
            )
        except:
            pass
