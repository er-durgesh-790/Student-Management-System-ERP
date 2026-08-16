import customtkinter as ctk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import csv

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


class ReportsModule:

    def __init__(self, parent, database):

        self.parent = parent
        self.database = database

        # ==========================
        # COLORS
        # ==========================

        self.primary = "#2563EB"
        self.primary_dark = "#1D4ED8"
        self.success = "#16A34A"
        self.danger = "#DC2626"
        self.warning = "#F59E0B"

        self.bg = "#F8FAFC"
        self.card_bg = "#FFFFFF"
        self.text = "#111827"
        self.light_text = "#6B7280"

        self.main_frame = None
        self.report_table = None
        self.report_type = None
        self.record_label = None

        self.create_ui()

    # ====================================================
    # CREATE UI
    # ====================================================

    def create_ui(self):

        # ==========================
        # MAIN FRAME
        # ==========================

        self.main_frame = ctk.CTkFrame(
            self.parent,
            fg_color=self.bg,
            corner_radius=0
        )

        self.main_frame.pack(
            fill="both",
            expand=True
        )

        # ==========================
        # HEADER
        # ==========================

        header = ctk.CTkFrame(
            self.main_frame,
            height=80,
            fg_color=self.primary,
            corner_radius=0
        )

        header.pack(
            fill="x"
        )

        header.pack_propagate(False)

        ctk.CTkLabel(
            header,
            text="📊  Reports Management",
            font=("Segoe UI", 28, "bold"),
            text_color="white"
        ).pack(
            side="left",
            padx=25,
            pady=20
        )

        ctk.CTkLabel(
            header,
            text="Generate • View • Export Reports",
            font=("Segoe UI", 14),
            text_color="#DBEAFE"
        ).pack(
            side="right",
            padx=25
        )

        # ==========================
        # REPORT CONTROL CARD
        # ==========================

        control_card = ctk.CTkFrame(
            self.main_frame,
            fg_color=self.card_bg,
            corner_radius=15
        )

        control_card.pack(
            fill="x",
            padx=20,
            pady=(20, 10)
        )

        ctk.CTkLabel(
            control_card,
            text="📋 Report Controls",
            font=("Segoe UI", 20, "bold"),
            text_color=self.text
        ).pack(
            anchor="w",
            padx=20,
            pady=(15, 10)
        )

        control_frame = ctk.CTkFrame(
            control_card,
            fg_color="transparent"
        )

        control_frame.pack(
            fill="x",
            padx=20,
            pady=(0, 20)
        )

        # Report Type

        ctk.CTkLabel(
            control_frame,
            text="Report Type",
            font=("Segoe UI", 14, "bold"),
            text_color=self.text
        ).pack(
            side="left",
            padx=(0, 10)
        )

        self.report_type = ctk.CTkComboBox(
            control_frame,
            values=[
                "Students",
                "Teachers",
                "Courses",
                "Fees",
                "Attendance",
                "Exams"
            ],
            width=200,
            height=40,
            corner_radius=8,
            border_color=self.primary,
            button_color=self.primary,
            button_hover_color=self.primary_dark,
            font=("Segoe UI", 13)
        )

        self.report_type.pack(
            side="left",
            padx=10
        )

        self.report_type.set("Students")

        # Load Report

        ctk.CTkButton(
            control_frame,
            text="📊 Load Report",
            width=150,
            height=40,
            corner_radius=8,
            fg_color=self.primary,
            hover_color=self.primary_dark,
            font=("Segoe UI", 13, "bold"),
            command=self.load_report
        ).pack(
            side="left",
            padx=8
        )

        # CSV Export

        ctk.CTkButton(
            control_frame,
            text="📗 Export CSV",
            width=150,
            height=40,
            corner_radius=8,
            fg_color=self.success,
            hover_color="#15803D",
            font=("Segoe UI", 13, "bold"),
            command=self.export_excel
        ).pack(
            side="left",
            padx=8
        )

        # PDF Export

        ctk.CTkButton(
            control_frame,
            text="📕 Export PDF",
            width=150,
            height=40,
            corner_radius=8,
            fg_color=self.danger,
            hover_color="#B91C1C",
            font=("Segoe UI", 13, "bold"),
            command=self.export_pdf
        ).pack(
            side="left",
            padx=8
        )

        # ==========================
        # STATUS CARD
        # ==========================

        status_card = ctk.CTkFrame(
            self.main_frame,
            fg_color="#EFF6FF",
            corner_radius=10,
            height=50
        )

        status_card.pack(
            fill="x",
            padx=20,
            pady=5
        )

        status_card.pack_propagate(False)

        self.record_label = ctk.CTkLabel(
            status_card,
            text="📊 Records: 0",
            font=("Segoe UI", 14, "bold"),
            text_color=self.primary
        )

        self.record_label.pack(
            side="left",
            padx=20
        )

        ctk.CTkLabel(
            status_card,
            text="Select a report type and click Load Report",
            font=("Segoe UI", 13),
            text_color=self.light_text
        ).pack(
            side="right",
            padx=20
        )

        # ==========================
        # TABLE CARD
        # ==========================

        table_card = ctk.CTkFrame(
            self.main_frame,
            fg_color=self.card_bg,
            corner_radius=15
        )

        table_card.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        ctk.CTkLabel(
            table_card,
            text="📑 Report Data",
            font=("Segoe UI", 20, "bold"),
            text_color=self.text
        ).pack(
            anchor="w",
            padx=20,
            pady=(15, 10)
        )

        # ==========================
        # TREEVIEW STYLE
        # ==========================

        style = ttk.Style()

        try:
            style.theme_use("clam")
        except:
            pass

        style.configure(
            "Reports.Treeview",
            background="#FFFFFF",
            foreground="#111827",
            rowheight=38,
            fieldbackground="#FFFFFF",
            font=("Segoe UI", 11),
            borderwidth=0
        )

        style.configure(
            "Reports.Treeview.Heading",
            background=self.primary,
            foreground="white",
            font=("Segoe UI", 11, "bold"),
            padding=10
        )

        style.map(
            "Reports.Treeview",
            background=[
                ("selected", "#DBEAFE")
            ],
            foreground=[
                ("selected", "#111827")
            ]
        )

        # ==========================
        # TABLE FRAME
        # ==========================

        table_frame = ctk.CTkFrame(
            table_card,
            fg_color="transparent"
        )

        table_frame.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=(0, 15)
        )

        self.report_table = ttk.Treeview(
            table_frame,
            style="Reports.Treeview",
            show="headings"
        )

        # Vertical Scrollbar

        scrollbar_y = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=self.report_table.yview
        )

        # Horizontal Scrollbar

        scrollbar_x = ttk.Scrollbar(
            table_frame,
            orient="horizontal",
            command=self.report_table.xview
        )

        self.report_table.configure(
            yscrollcommand=scrollbar_y.set,
            xscrollcommand=scrollbar_x.set
        )

        self.report_table.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        scrollbar_y.grid(
            row=0,
            column=1,
            sticky="ns"
        )

        scrollbar_x.grid(
            row=1,
            column=0,
            sticky="ew"
        )

        table_frame.grid_rowconfigure(
            0,
            weight=1
        )

        table_frame.grid_columnconfigure(
            0,
            weight=1
        )

        # Double click event

        self.report_table.bind(
            "<Double-1>",
            self.table_double_click
        )

        # Initial report

        self.load_report()

    # ====================================================
    # LOAD REPORT
    # ====================================================

    def load_report(self):

        report = self.report_type.get()

        # Clear old data

        for item in self.report_table.get_children():
            self.report_table.delete(item)

        self.report_table["columns"] = ()

        # ==========================
        # STUDENTS
        # ==========================

        if report == "Students":

            columns = (
                "Student ID",
                "First Name",
                "Last Name",
                "Mobile",
                "Course",
                "Semester"
            )

            self.setup_columns(columns)

            students = self.database.fetch_students()

            for row in students:

                self.report_table.insert(
                    "",
                    "end",
                    values=(
                        row[1],
                        row[2],
                        row[3],
                        row[4],
                        row[5],
                        row[6]
                    )
                )

        # ==========================
        # TEACHERS
        # ==========================

        elif report == "Teachers":

            columns = (
                "Teacher ID",
                "Teacher Name",
                "Mobile",
                "Subject",
                "Qualification"
            )

            self.setup_columns(columns)

            teachers = self.database.fetch_teachers()

            for row in teachers:

                self.report_table.insert(
                    "",
                    "end",
                    values=(
                        row[1],
                        row[2],
                        row[3],
                        row[4],
                        row[5]
                    )
                )

        # ==========================
        # COURSES
        # ==========================

        elif report == "Courses":

            columns = (
                "Course ID",
                "Course Name",
                "Duration",
                "Fee"
            )

            self.setup_columns(columns)

            courses = self.database.fetch_courses()

            for row in courses:

                self.report_table.insert(
                    "",
                    "end",
                    values=(
                        row[1],
                        row[2],
                        row[3],
                        row[4]
                    )
                )

        # ==========================
        # FEES
        # ==========================

        elif report == "Fees":

            columns = (
                "Student ID",
                "Student Name",
                "Course",
                "Amount",
                "Status"
            )

            self.setup_columns(columns)

            fees = self.database.fetch_fees()

            for row in fees:

                self.report_table.insert(
                    "",
                    "end",
                    values=(
                        row[1],
                        row[2],
                        row[3],
                        row[4],
                        row[5]
                    )
                )

        # ==========================
        # ATTENDANCE
        # ==========================

        elif report == "Attendance":

            columns = (
                "Student ID",
                "Student Name",
                "Course",
                "Date",
                "Status"
            )

            self.setup_columns(columns)

            attendance = self.database.fetch_attendance()

            for row in attendance:

                self.report_table.insert(
                    "",
                    "end",
                    values=(
                        row[1],
                        row[2],
                        row[3],
                        row[4],
                        row[5]
                    )
                )

        # ==========================
        # EXAMS
        # ==========================

        elif report == "Exams":

            columns = (
                "Exam ID",
                "Exam Name",
                "Course",
                "Semester",
                "Exam Date",
                "Total Marks"
            )

            self.setup_columns(columns)

            exams = self.database.fetch_exams()

            for row in exams:

                self.report_table.insert(
                    "",
                    "end",
                    values=(
                        row[1],
                        row[2],
                        row[3],
                        row[4],
                        row[5],
                        row[6]
                    )
                )

        # Update record count

        count = len(
            self.report_table.get_children()
        )

        self.record_label.configure(
            text=f"📊 Records: {count}"
        )

    # ====================================================
    # SETUP TABLE COLUMNS
    # ====================================================

    def setup_columns(self, columns):

        self.report_table["columns"] = columns

        self.report_table["show"] = "headings"

        for col in columns:

            self.report_table.heading(
                col,
                text=col
            )

            self.report_table.column(
                col,
                width=160,
                minwidth=100,
                anchor="center"
            )

    # ====================================================
    # TABLE DOUBLE CLICK
    # ====================================================

    def table_double_click(self, event):

        selected = self.report_table.focus()

        if not selected:
            return

        values = self.report_table.item(
            selected
        )["values"]

        if values:

            messagebox.showinfo(
                "Record Information",
                "\n".join(
                    f"{column}: {value}"
                    for column, value in zip(
                        self.report_table["columns"],
                        values
                    )
                )
            )

    # ====================================================
    # EXPORT CSV
    # ====================================================

    def export_excel(self):

        if not self.report_table["columns"]:

            messagebox.showwarning(
                "No Report",
                "Please load a report first."
            )

            return

        file = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[
                ("CSV File", "*.csv")
            ],
            title="Export Report"
        )

        if not file:
            return

        try:

            with open(
                file,
                "w",
                newline="",
                encoding="utf-8"
            ) as f:

                writer = csv.writer(f)

                columns = self.report_table["columns"]

                writer.writerow(columns)

                for item in self.report_table.get_children():

                    writer.writerow(
                        self.report_table.item(
                            item
                        )["values"]
                    )

            messagebox.showinfo(
                "Export Successful",
                "Report exported successfully."
            )

        except Exception as e:

            messagebox.showerror(
                "Export Error",
                str(e)
            )

    # ====================================================
    # EXPORT PDF
    # ====================================================

    def export_pdf(self):

        if not self.report_table["columns"]:

            messagebox.showwarning(
                "No Report",
                "Please load a report first."
            )

            return

        file = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[
                ("PDF File", "*.pdf")
            ],
            title="Export PDF Report"
        )

        if not file:
            return

        try:

            pdf = canvas.Canvas(
                file,
                pagesize=letter
            )

            width, height = letter

            y = height - 50

            # ==========================
            # PDF TITLE
            # ==========================

            pdf.setFont(
                "Helvetica-Bold",
                18
            )

            pdf.drawString(
                40,
                y,
                f"{self.report_type.get()} Report"
            )

            y -= 25

            pdf.setFont(
                "Helvetica",
                9
            )

            pdf.drawString(
                40,
                y,
                "Student Management System ERP"
            )

            y -= 25

            # ==========================
            # TABLE HEADER
            # ==========================

            columns = self.report_table["columns"]

            pdf.setFont(
                "Helvetica-Bold",
                7
            )

            header_text = " | ".join(
                str(col)
                for col in columns
            )

            pdf.drawString(
                40,
                y,
                header_text[:110]
            )

            y -= 15

            # ==========================
            # TABLE DATA
            # ==========================

            pdf.setFont(
                "Helvetica",
                7
            )

            for item in self.report_table.get_children():

                row = self.report_table.item(
                    item
                )["values"]

                row_text = " | ".join(
                    map(str, row)
                )

                pdf.drawString(
                    40,
                    y,
                    row_text[:110]
                )

                y -= 15

                # New Page

                if y < 50:

                    pdf.showPage()

                    y = height - 50

                    pdf.setFont(
                        "Helvetica",
                        7
                    )

            pdf.save()

            messagebox.showinfo(
                "Export Successful",
                "PDF report exported successfully."
            )

        except Exception as e:

            messagebox.showerror(
                "PDF Export Error",
                str(e)
            )