
import customtkinter as ctk
from tkinter import messagebox


class StudentPortal:

    def __init__(self, root, database, student):

        self.root = root
        self.database = database
        self.student = student

        # =====================================================
        # STUDENT DATA
        # =====================================================

        self.student_id = student[1]
        self.first_name = student[2] or ""
        self.last_name = student[3] or ""
        self.mobile = student[4] or ""
        self.course = student[5] or ""
        self.semester = student[6] or ""
        self.photo_path = student[7] or ""

        self.student_name = (
            f"{self.first_name} {self.last_name}"
        ).strip()

        # =====================================================
        # COLORS
        # =====================================================

        self.bg = "#F4F7FB"
        self.sidebar = "#1E3A8A"
        self.blue = "#2563EB"
        self.dark_blue = "#1D4ED8"

        self.green = "#16A34A"
        self.red = "#DC2626"
        self.orange = "#EA580C"

        self.white = "#FFFFFF"
        self.text = "#111827"
        self.gray = "#6B7280"
        self.border = "#E5E7EB"

        # =====================================================
        # WINDOW
        # =====================================================

        self.root.title(
            "Student Management System ERP - Student Portal"
        )

        self.root.geometry(
            "1200x700"
        )

        self.root.minsize(
            1000,
            600
        )

        self.root.configure(
            fg_color=self.bg
        )

        # =====================================================
        # MAIN FRAME
        # =====================================================

        self.main_frame = ctk.CTkFrame(
            self.root,
            fg_color=self.bg,
            corner_radius=0
        )

        self.main_frame.pack(
            fill="both",
            expand=True
        )

        # =====================================================
        # SIDEBAR
        # =====================================================

        self.sidebar_frame = ctk.CTkFrame(
            self.main_frame,
            width=250,
            fg_color=self.sidebar,
            corner_radius=0
        )

        self.sidebar_frame.pack(
            side="left",
            fill="y"
        )

        self.sidebar_frame.pack_propagate(False)

        # =====================================================
        # SIDEBAR LOGO
        # =====================================================

        ctk.CTkLabel(
            self.sidebar_frame,
            text="🎓",
            font=("Segoe UI Emoji", 55)
        ).pack(
            pady=(35, 5)
        )

        ctk.CTkLabel(
            self.sidebar_frame,
            text="STUDENT\nPORTAL",
            font=("Segoe UI", 24, "bold"),
            text_color=self.white,
            justify="center"
        ).pack()

        ctk.CTkLabel(
            self.sidebar_frame,
            text="Student Management ERP",
            font=("Segoe UI", 11),
            text_color="#BFDBFE"
        ).pack(
            pady=(5, 25)
        )

        # =====================================================
        # STUDENT NAME
        # =====================================================

        ctk.CTkLabel(
            self.sidebar_frame,
            text=self.student_name,
            font=("Segoe UI", 15, "bold"),
            text_color=self.white,
            wraplength=210
        ).pack(
            pady=(0, 3)
        )

        ctk.CTkLabel(
            self.sidebar_frame,
            text=f"ID: {self.student_id}",
            font=("Segoe UI", 11),
            text_color="#BFDBFE"
        ).pack(
            pady=(0, 25)
        )

        # =====================================================
        # SIDEBAR BUTTONS
        # =====================================================

        self.create_sidebar_button(
            "🏠  Dashboard",
            self.show_dashboard
        )

        self.create_sidebar_button(
            "👤  My Profile",
            self.show_profile
        )

        self.create_sidebar_button(
            "📅  Attendance",
            self.show_attendance
        )

        self.create_sidebar_button(
            "📊  Results",
            self.show_results
        )

        self.create_sidebar_button(
            "💰  Fees",
            self.show_fees
        )

        self.create_sidebar_button(
            "📝  Exams",
            self.show_exams
        )

        # =====================================================
        # BOTTOM BUTTONS
        # =====================================================

        ctk.CTkButton(
            self.sidebar_frame,
            text="🔐  Change Password",
            height=40,
            corner_radius=10,
            fg_color="#1D4ED8",
            hover_color="#2563EB",
            text_color=self.white,
            font=("Segoe UI", 12, "bold"),
            command=self.change_password
        ).pack(
            side="bottom",
            padx=20,
            pady=(5, 10),
            fill="x"
        )

        ctk.CTkButton(
            self.sidebar_frame,
            text="🚪  Logout",
            height=40,
            corner_radius=10,
            fg_color=self.red,
            hover_color="#B91C1C",
            text_color=self.white,
            font=("Segoe UI", 12, "bold"),
            command=self.logout
        ).pack(
            side="bottom",
            padx=20,
            pady=10,
            fill="x"
        )

        # =====================================================
        # CONTENT AREA
        # =====================================================

        self.content_frame = ctk.CTkFrame(
            self.main_frame,
            fg_color=self.bg,
            corner_radius=0
        )

        self.content_frame.pack(
            side="right",
            fill="both",
            expand=True
        )

        # =====================================================
        # SHOW DASHBOARD
        # =====================================================

        self.show_dashboard()

    # =========================================================
    # SIDEBAR BUTTON
    # =========================================================

    def create_sidebar_button(
        self,
        text,
        command
    ):

        button = ctk.CTkButton(
            self.sidebar_frame,
            text=text,
            height=44,
            corner_radius=10,
            fg_color="transparent",
            hover_color="#2563EB",
            text_color=self.white,
            font=("Segoe UI", 13, "bold"),
            anchor="w",
            command=command
        )

        button.pack(
            padx=15,
            pady=4,
            fill="x"
        )

    # =========================================================
    # CLEAR CONTENT
    # =========================================================

    def clear_content(self):

        for widget in self.content_frame.winfo_children():

            widget.destroy()

    # =========================================================
    # HEADER
    # =========================================================

    def create_header(
        self,
        title,
        subtitle=""
    ):

        header = ctk.CTkFrame(
            self.content_frame,
            fg_color=self.white,
            corner_radius=15,
            border_width=1,
            border_color=self.border
        )

        header.pack(
            padx=25,
            pady=(25, 15),
            fill="x"
        )

        ctk.CTkLabel(
            header,
            text=title,
            font=("Segoe UI", 25, "bold"),
            text_color=self.text
        ).pack(
            anchor="w",
            padx=20,
            pady=(15, 2)
        )

        if subtitle:

            ctk.CTkLabel(
                header,
                text=subtitle,
                font=("Segoe UI", 12),
                text_color=self.gray
            ).pack(
                anchor="w",
                padx=20,
                pady=(0, 15)
            )

    # =========================================================
    # DASHBOARD
    # =========================================================

    def show_dashboard(self):

        self.clear_content()

        self.create_header(
            "Welcome, " + self.student_name + " 👋",
            "Here you can view your complete academic information."
        )

        # =====================================================
        # INFO CARDS
        # =====================================================

        cards_frame = ctk.CTkFrame(
            self.content_frame,
            fg_color="transparent"
        )

        cards_frame.pack(
            padx=25,
            fill="x"
        )

        cards_frame.grid_columnconfigure(
            (0, 1, 2, 3),
            weight=1
        )

        # Get data

        attendance = self.database.get_student_attendance(
            self.student_id
        )

        results = self.database.get_student_results(
            self.student_id
        )

        fees = self.database.get_student_fees(
            self.student_id
        )

        exams = self.database.get_student_exams(
            self.course,
            self.semester
        )

        attendance_percentage = self.calculate_attendance_percentage(
            attendance
        )

        # Cards

        self.create_info_card(
            cards_frame,
            0,
            "📅",
            "Attendance",
            f"{attendance_percentage:.1f}%",
            self.green
        )

        self.create_info_card(
            cards_frame,
            1,
            "📊",
            "Results",
            str(len(results)),
            self.blue
        )

        self.create_info_card(
            cards_frame,
            2,
            "💰",
            "Fee Records",
            str(len(fees)),
            self.orange
        )

        self.create_info_card(
            cards_frame,
            3,
            "📝",
            "Upcoming Exams",
            str(len(exams)),
            "#7C3AED"
        )

        # =====================================================
        # PROFILE CARD
        # =====================================================

        profile_card = ctk.CTkFrame(
            self.content_frame,
            fg_color=self.white,
            corner_radius=15,
            border_width=1,
            border_color=self.border
        )

        profile_card.pack(
            padx=25,
            pady=25,
            fill="x"
        )

        ctk.CTkLabel(
            profile_card,
            text="👤  My Academic Profile",
            font=("Segoe UI", 19, "bold"),
            text_color=self.text
        ).pack(
            anchor="w",
            padx=20,
            pady=(18, 12)
        )

        self.create_profile_row(
            profile_card,
            "Student ID",
            self.student_id
        )

        self.create_profile_row(
            profile_card,
            "Student Name",
            self.student_name
        )

        self.create_profile_row(
            profile_card,
            "Mobile",
            self.mobile
        )

        self.create_profile_row(
            profile_card,
            "Course",
            self.course
        )

        self.create_profile_row(
            profile_card,
            "Semester",
            self.semester
        )

    # =========================================================
    # INFO CARD
    # =========================================================

    def create_info_card(
        self,
        parent,
        column,
        icon,
        title,
        value,
        color
    ):

        card = ctk.CTkFrame(
            parent,
            fg_color=self.white,
            corner_radius=15,
            border_width=1,
            border_color=self.border
        )

        card.grid(
            row=0,
            column=column,
            padx=6,
            pady=5,
            sticky="nsew"
        )

        ctk.CTkLabel(
            card,
            text=icon,
            font=("Segoe UI Emoji", 28)
        ).pack(
            pady=(15, 3)
        )

        ctk.CTkLabel(
            card,
            text=title,
            font=("Segoe UI", 12),
            text_color=self.gray
        ).pack()

        ctk.CTkLabel(
            card,
            text=value,
            font=("Segoe UI", 22, "bold"),
            text_color=color
        ).pack(
            pady=(2, 15)
        )

    # =========================================================
    # PROFILE
    # =========================================================

    def show_profile(self):

        self.clear_content()

        self.create_header(
            "My Profile 👤",
            "Your personal and academic information."
        )

        profile_card = ctk.CTkFrame(
            self.content_frame,
            fg_color=self.white,
            corner_radius=15,
            border_width=1,
            border_color=self.border
        )

        profile_card.pack(
            padx=25,
            pady=5,
            fill="x"
        )

        self.create_profile_row(
            profile_card,
            "Student ID",
            self.student_id
        )

        self.create_profile_row(
            profile_card,
            "First Name",
            self.first_name
        )

        self.create_profile_row(
            profile_card,
            "Last Name",
            self.last_name
        )

        self.create_profile_row(
            profile_card,
            "Mobile",
            self.mobile
        )

        self.create_profile_row(
            profile_card,
            "Course",
            self.course
        )

        self.create_profile_row(
            profile_card,
            "Semester",
            self.semester
        )

        ctk.CTkButton(
            self.content_frame,
            text="🔐 Change Password",
            width=220,
            height=45,
            corner_radius=10,
            fg_color=self.blue,
            hover_color=self.dark_blue,
            font=("Segoe UI", 13, "bold"),
            command=self.change_password
        ).pack(
            pady=20
        )

    # =========================================================
    # PROFILE ROW
    # =========================================================

    def create_profile_row(
        self,
        parent,
        label,
        value
    ):

        row = ctk.CTkFrame(
            parent,
            fg_color="#F9FAFB",
            corner_radius=8
        )

        row.pack(
            padx=20,
            pady=5,
            fill="x"
        )

        ctk.CTkLabel(
            row,
            text=label,
            width=150,
            anchor="w",
            font=("Segoe UI", 12, "bold"),
            text_color=self.gray
        ).pack(
            side="left",
            padx=15,
            pady=10
        )

        ctk.CTkLabel(
            row,
            text=str(value) if value else "-",
            anchor="w",
            font=("Segoe UI", 12),
            text_color=self.text
        ).pack(
            side="left",
            padx=15,
            pady=10
        )

    # =========================================================
    # ATTENDANCE
    # =========================================================

    def show_attendance(self):

        self.clear_content()

        attendance = self.database.get_student_attendance(
            self.student_id
        )

        percentage = self.calculate_attendance_percentage(
            attendance
        )

        self.create_header(
            "My Attendance 📅",
            f"Overall Attendance: {percentage:.1f}%"
        )

        # =====================================================
        # SUMMARY
        # =====================================================

        total = len(attendance)

        present = sum(
            1
            for row in attendance
            if str(row[5]).lower() == "present"
        )

        absent = sum(
            1
            for row in attendance
            if str(row[5]).lower() == "absent"
        )

        summary = ctk.CTkFrame(
            self.content_frame,
            fg_color="transparent"
        )

        summary.pack(
            padx=25,
            fill="x"
        )

        summary.grid_columnconfigure(
            (0, 1, 2),
            weight=1
        )

        self.create_info_card(
            summary,
            0,
            "📚",
            "Total Classes",
            str(total),
            self.blue
        )

        self.create_info_card(
            summary,
            1,
            "✅",
            "Present",
            str(present),
            self.green
        )

        self.create_info_card(
            summary,
            2,
            "❌",
            "Absent",
            str(absent),
            self.red
        )

        # =====================================================
        # TABLE
        # =====================================================

        table = ctk.CTkScrollableFrame(
            self.content_frame,
            fg_color=self.white,
            corner_radius=15
        )

        table.pack(
            padx=25,
            pady=20,
            fill="both",
            expand=True
        )

        headers = [
            "Date",
            "Course",
            "Status"
        ]

        for col, header in enumerate(headers):

            ctk.CTkLabel(
                table,
                text=header,
                font=("Segoe UI", 12, "bold"),
                text_color=self.text
            ).grid(
                row=0,
                column=col,
                padx=15,
                pady=10,
                sticky="w"
            )

        for row_index, record in enumerate(
            attendance,
            start=1
        ):

            date = record[4]
            course = record[3]
            status = record[5]

            color = (
                self.green
                if str(status).lower() == "present"
                else self.red
            )

            values = [
                date,
                course,
                status
            ]

            for col, value in enumerate(values):

                ctk.CTkLabel(
                    table,
                    text=str(value),
                    font=("Segoe UI", 11),
                    text_color=color if col == 2 else self.text
                ).grid(
                    row=row_index,
                    column=col,
                    padx=15,
                    pady=8,
                    sticky="w"
                )

    # =========================================================
    # CALCULATE ATTENDANCE
    # =========================================================

    def calculate_attendance_percentage(
        self,
        attendance
    ):

        if not attendance:

            return 0.0

        present = sum(
            1
            for row in attendance
            if str(row[5]).lower() == "present"
        )

        total = len(attendance)

        return (
            present / total
        ) * 100

    # =========================================================
    # RESULTS
    # =========================================================

    def show_results(self):

        self.clear_content()

        results = self.database.get_student_results(
            self.student_id
        )

        self.create_header(
            "My Results 📊",
            "Your marks, grades and result status."
        )

        table = ctk.CTkScrollableFrame(
            self.content_frame,
            fg_color=self.white,
            corner_radius=15
        )

        table.pack(
            padx=25,
            pady=5,
            fill="both",
            expand=True
        )

        headers = [
            "Subject",
            "Marks",
            "Grade",
            "Percentage",
            "Status"
        ]

        for col, header in enumerate(headers):

            ctk.CTkLabel(
                table,
                text=header,
                font=("Segoe UI", 12, "bold"),
                text_color=self.text
            ).grid(
                row=0,
                column=col,
                padx=15,
                pady=12,
                sticky="w"
            )

        if not results:

            ctk.CTkLabel(
                table,
                text="No result records available.",
                font=("Segoe UI", 13),
                text_color=self.gray
            ).grid(
                row=1,
                column=0,
                columnspan=5,
                pady=30
            )

            return

        for row_index, record in enumerate(
            results,
            start=1
        ):

            subject = record[4]
            marks = record[5]
            grade = record[6]
            percentage = record[7]
            status = record[8]

            values = [
                subject,
                marks,
                grade,
                percentage,
                status
            ]

            for col, value in enumerate(values):

                color = self.text

                if col == 4:

                    color = (
                        self.green
                        if str(status).lower()
                        in ["pass", "passed"]
                        else self.red
                    )

                ctk.CTkLabel(
                    table,
                    text=str(value),
                    font=("Segoe UI", 11),
                    text_color=color
                ).grid(
                    row=row_index,
                    column=col,
                    padx=15,
                    pady=9,
                    sticky="w"
                )

    # =========================================================
    # FEES
    # =========================================================

    def show_fees(self):

        self.clear_content()

        fees = self.database.get_student_fees(
            self.student_id
        )

        self.create_header(
            "My Fees 💰",
            "Your fee records and payment status."
        )

        table = ctk.CTkScrollableFrame(
            self.content_frame,
            fg_color=self.white,
            corner_radius=15
        )

        table.pack(
            padx=25,
            pady=5,
            fill="both",
            expand=True
        )

        headers = [
            "Course",
            "Amount",
            "Status"
        ]

        for col, header in enumerate(headers):

            ctk.CTkLabel(
                table,
                text=header,
                font=("Segoe UI", 12, "bold"),
                text_color=self.text
            ).grid(
                row=0,
                column=col,
                padx=20,
                pady=12,
                sticky="w"
            )

        if not fees:

            ctk.CTkLabel(
                table,
                text="No fee records available.",
                font=("Segoe UI", 13),
                text_color=self.gray
            ).grid(
                row=1,
                column=0,
                columnspan=3,
                pady=30
            )

            return

        for row_index, record in enumerate(
            fees,
            start=1
        ):

            course = record[3]
            amount = record[4]
            status = record[5]

            color = (
                self.green
                if str(status).lower()
                in ["paid", "complete", "completed"]
                else self.orange
            )

            values = [
                course,
                amount,
                status
            ]

            for col, value in enumerate(values):

                ctk.CTkLabel(
                    table,
                    text=str(value),
                    font=("Segoe UI", 11),
                    text_color=color if col == 2 else self.text
                ).grid(
                    row=row_index,
                    column=col,
                    padx=20,
                    pady=9,
                    sticky="w"
                )

    # =========================================================
    # EXAMS
    # =========================================================

    def show_exams(self):

        self.clear_content()

        exams = self.database.get_student_exams(
            self.course,
            self.semester
        )

        self.create_header(
            "My Exams 📝",
            f"Exam schedule for {self.course} - Semester {self.semester}"
        )

        table = ctk.CTkScrollableFrame(
            self.content_frame,
            fg_color=self.white,
            corner_radius=15
        )

        table.pack(
            padx=25,
            pady=5,
            fill="both",
            expand=True
        )

        headers = [
            "Exam ID",
            "Exam Name",
            "Course",
            "Semester",
            "Exam Date",
            "Total Marks"
        ]

        for col, header in enumerate(headers):

            ctk.CTkLabel(
                table,
                text=header,
                font=("Segoe UI", 12, "bold"),
                text_color=self.text
            ).grid(
                row=0,
                column=col,
                padx=12,
                pady=12,
                sticky="w"
            )

        if not exams:

            ctk.CTkLabel(
                table,
                text="No exam schedule available.",
                font=("Segoe UI", 13),
                text_color=self.gray
            ).grid(
                row=1,
                column=0,
                columnspan=6,
                pady=30
            )

            return

        for row_index, record in enumerate(
            exams,
            start=1
        ):

            values = [
                record[1],
                record[2],
                record[3],
                record[4],
                record[5],
                record[6]
            ]

            for col, value in enumerate(values):

                ctk.CTkLabel(
                    table,
                    text=str(value),
                    font=("Segoe UI", 11),
                    text_color=self.text
                ).grid(
                    row=row_index,
                    column=col,
                    padx=12,
                    pady=9,
                    sticky="w"
                )

    # =========================================================
    # CHANGE PASSWORD
    # =========================================================

    def change_password(self):

        dialog = ctk.CTkToplevel(
            self.root
        )

        dialog.title(
            "Change Student Password"
        )

        dialog.geometry(
            "430x400"
        )

        dialog.resizable(
            False,
            False
        )

        dialog.configure(
            fg_color=self.bg
        )

        dialog.grab_set()

        # =====================================================
        # CARD
        # =====================================================

        card = ctk.CTkFrame(
            dialog,
            fg_color=self.white,
            corner_radius=20
        )

        card.pack(
            padx=25,
            pady=25,
            fill="both",
            expand=True
        )

        ctk.CTkLabel(
            card,
            text="🔐",
            font=("Segoe UI Emoji", 40)
        ).pack(
            pady=(20, 5)
        )

        ctk.CTkLabel(
            card,
            text="Change Password",
            font=("Segoe UI", 22, "bold"),
            text_color=self.text
        ).pack()

        old_password = ctk.CTkEntry(
            card,
            width=300,
            height=42,
            placeholder_text="Current Password",
            show="*"
        )

        old_password.pack(
            pady=(20, 8)
        )

        new_password = ctk.CTkEntry(
            card,
            width=300,
            height=42,
            placeholder_text="New Password",
            show="*"
        )

        new_password.pack(
            pady=8
        )

        confirm_password = ctk.CTkEntry(
            card,
            width=300,
            height=42,
            placeholder_text="Confirm New Password",
            show="*"
        )

        confirm_password.pack(
            pady=8
        )

        def save_password():

            old = old_password.get().strip()
            new = new_password.get().strip()
            confirm = confirm_password.get().strip()

            if not old or not new or not confirm:

                messagebox.showerror(
                    "Error",
                    "Please fill all password fields.",
                    parent=dialog
                )

                return

            if new != confirm:

                messagebox.showerror(
                    "Error",
                    "New passwords do not match.",
                    parent=dialog
                )

                return

            if len(new) < 4:

                messagebox.showerror(
                    "Error",
                    "Password must contain at least 4 characters.",
                    parent=dialog
                )

                return

            success = self.verify_and_change_password(
                old,
                new
            )

            if success:

                messagebox.showinfo(
                    "Success",
                    "Password changed successfully.",
                    parent=dialog
                )

                dialog.destroy()

            else:

                messagebox.showerror(
                    "Error",
                    "Current password is incorrect.",
                    parent=dialog
                )

        ctk.CTkButton(
            card,
            text="Update Password",
            width=300,
            height=44,
            corner_radius=10,
            fg_color=self.blue,
            hover_color=self.dark_blue,
            font=("Segoe UI", 13, "bold"),
            command=save_password
        ).pack(
            pady=15
        )

    # =========================================================
    # VERIFY + CHANGE PASSWORD
    # =========================================================

    def verify_and_change_password(
        self,
        old_password,
        new_password
    ):

        student = self.database.check_student_login(
            self.student_id,
            old_password
        )

        if not student:

            return False

        self.database.update_student_password(
            self.student_id,
            new_password
        )

        return True

    # =========================================================
    # LOGOUT
    # =========================================================

    def logout(self):

        answer = messagebox.askyesno(
            "Logout",
            "Are you sure you want to logout?"
        )

        if not answer:
            return

        try:
            from login import StudentLogin

            for widget in self.root.winfo_children():
                widget.destroy()

            StudentLogin(
                self.root,
                self.database
            )

        except Exception as e:

            print("Logout Error:", e)

            messagebox.showerror(
                "Logout Error",
                f"Unable to return to login screen.\n\n{e}"
            )

            # =====================================================
            # IMPORT LOGIN
            # =====================================================

            from login import LoginWindow

            for widget in self.root.winfo_children():
                widget.destroy()

            LoginWindow(
                self.root,
                self.database
            )


# =============================================================
# TESTING
# =============================================================

if __name__ == "__main__":

    print(
        "Student Portal module loaded successfully."
    )
