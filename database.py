import sqlite3
from config import DATABASE_PATH


class Database:

    # =========================================================
    # DATABASE INITIALIZATION
    # =========================================================

    def __init__(self):
        self.conn = sqlite3.connect(
            DATABASE_PATH,
            check_same_thread=False
        )
        self.cursor = self.conn.cursor()

        self.create_tables()
        self.migrate_students_table()
        self.create_default_admin()

    # =========================================================
    # CREATE TABLES
    # =========================================================

    def create_tables(self):

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS students(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id TEXT UNIQUE,
            first_name TEXT,
            last_name TEXT,
            mobile TEXT,
            course TEXT,
            semester TEXT,
            photo_path TEXT,
            password TEXT
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS teachers(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            teacher_id TEXT UNIQUE,
            teacher_name TEXT,
            mobile TEXT,
            subject TEXT,
            qualification TEXT,
            photo_path TEXT
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS courses(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            course_id TEXT UNIQUE,
            course_name TEXT,
            duration TEXT,
            fee TEXT
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS fees(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id TEXT,
            student_name TEXT,
            course TEXT,
            amount TEXT,
            status TEXT
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS attendance(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id TEXT,
            student_name TEXT,
            course TEXT,
            attendance_date TEXT,
            status TEXT
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS exams(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            exam_id TEXT UNIQUE,
            exam_name TEXT,
            course TEXT,
            semester TEXT,
            exam_date TEXT,
            total_marks TEXT
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS results(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id TEXT,
            student_name TEXT,
            course TEXT,
            subject TEXT,
            marks TEXT,
            grade TEXT,
            percentage TEXT,
            status TEXT
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS admins(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT,
            username TEXT UNIQUE,
            mobile TEXT,
            password TEXT
        )
        """)

        # =====================================================
        # STUDENT PORTAL CONTENT
        # =====================================================

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS portal_notices(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            message TEXT NOT NULL,
            priority TEXT DEFAULT 'Normal',
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS academic_calendar(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            event_date TEXT NOT NULL,
            description TEXT DEFAULT ''
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS social_links(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            platform TEXT NOT NULL,
            url TEXT NOT NULL
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS chairman_profile(
            id INTEGER PRIMARY KEY CHECK (id = 1),
            name TEXT NOT NULL,
            title TEXT DEFAULT 'Chairman',
            message TEXT NOT NULL
        )
        """)

        self.conn.commit()
# =========================================================
# STUDENT TABLE MIGRATION
# =========================================================

    def migrate_students_table(self):

        try:
            # Current students table columns check karo
            self.cursor.execute("PRAGMA table_info(students)")

            columns = [
                row[1]
                for row in self.cursor.fetchall()
            ]

            print("Existing student columns:", columns)

            # =====================================================
            # PHOTO PATH
            # =====================================================

            if "photo_path" not in columns:

                self.cursor.execute("""
                    ALTER TABLE students
                    ADD COLUMN photo_path TEXT
                """)

                print("Added column: photo_path")

            # =====================================================
            # PASSWORD
            # =====================================================

            if "password" not in columns:

                self.cursor.execute("""
                    ALTER TABLE students
                    ADD COLUMN password TEXT
                """)

                print("Added column: password")

            # =====================================================
            # EXISTING STUDENTS PASSWORD
            # Student ID ko default password rakho
            # =====================================================

            self.cursor.execute("""
                UPDATE students
                SET password = student_id
                WHERE password IS NULL
                   OR password = ''
            """)

            self.conn.commit()

            print("Students table migration completed.")

        except Exception as e:

            print(
                "Students Table Migration Error:",
                e
            )
   

    # =========================================================
    # DEFAULT ADMIN
    # ===============================================# =========================================================


    def create_default_admin(self):

        try:
            self.cursor.execute("""
                SELECT *
                FROM admins
                WHERE username=?
            """, ("admin",))

            admin = self.cursor.fetchone()

            if admin is None:
                self.cursor.execute("""
                    INSERT INTO admins(
                        full_name,
                        username,
                        mobile,
                        password
                    )
                    VALUES(?,?,?,?)
                """, (
                    "Durgesh Gupta",
                    "admin",
                    "",
                    "admin123"
                ))

                self.conn.commit()
                print("Default admin created.")

            elif admin[1] in (None, "", "System Administrator"):
                self.cursor.execute("""
                    UPDATE admins
                    SET full_name=?
                    WHERE username=?
                """, ("Durgesh Gupta", "admin"))
                self.conn.commit()

        except Exception as e:
            print("Default Admin Error:", e)

    # =========================================================
    # ADMIN LOGIN
    # =========================================================

    def check_login(self, username, password):

        self.cursor.execute("""
            SELECT *
            FROM admins
            WHERE username=?
            AND password=?
        """, (username, password))

        return self.cursor.fetchone()

    # =========================================================
    # GET ADMIN PROFILE
    # =========================================================

    def get_admin(self, username):

        self.cursor.execute("""
            SELECT id, full_name, username, mobile
            FROM admins
            WHERE username=?
        """, (username,))

        return self.cursor.fetchone()

    # =========================================================
    # VERIFY ADMIN
    # =========================================================

    def verify_admin(self, username, mobile):

        self.cursor.execute("""
            SELECT *
            FROM admins
            WHERE username=?
            AND mobile=?
        """, (username, mobile))

        return self.cursor.fetchone()

    # =========================================================
    # UPDATE ADMIN PASSWORD
    # =========================================================

    def update_admin_password(self, username, password):

        try:
            self.cursor.execute("""
                UPDATE admins
                SET password=?
                WHERE username=?
            """, (password, username))

            self.conn.commit()
            return self.cursor.rowcount > 0

        except Exception as e:
            print("Password Update Error:", e)
            return False

    # =========================================================
    # CHECK ADMIN USERNAME
    # =========================================================

    def username_exists(self, username):

        self.cursor.execute("""
            SELECT *
            FROM admins
            WHERE username=?
        """, (username,))

        return self.cursor.fetchone()

    # =========================================================
    # REGISTER ADMIN
    # =========================================================

    def register_admin(
        self,
        full_name,
        username,
        mobile,
        password
    ):

        try:
            self.cursor.execute("""
                INSERT INTO admins(
                    full_name,
                    username,
                    mobile,
                    password
                )
                VALUES(?,?,?,?)
            """, (
                full_name,
                username,
                mobile,
                password
            ))

            self.conn.commit()
            return True

        except sqlite3.IntegrityError:
            print("Admin username already exists.")
            return False

        except Exception as e:
            print("Admin Registration Error:", e)
            return False

    # =========================================================
    # CHANGE ADMIN PASSWORD
    # =========================================================

    def change_password(
        self,
        username,
        old_password,
        new_password
    ):

        self.cursor.execute("""
            SELECT id
            FROM admins
            WHERE username=?
            AND password=?
        """, (username, old_password))

        user = self.cursor.fetchone()

        if not user:
            return False

        self.cursor.execute("""
            UPDATE admins
            SET password=?
            WHERE username=?
        """, (new_password, username))

        self.conn.commit()
        return True

    # =========================================================
    # ADD STUDENT
    # =========================================================

    def add_student(
        self,
        student_id,
        first_name,
        last_name,
        mobile,
        course,
        semester,
        photo_path,
        password=None
    ):

        try:
            if not password:
                password = student_id

            self.cursor.execute("""
                INSERT INTO students(
                    student_id,
                    first_name,
                    last_name,
                    mobile,
                    course,
                    semester,
                    photo_path,
                    password
                )
                VALUES(?,?,?,?,?,?,?,?)
            """, (
                student_id,
                first_name,
                last_name,
                mobile,
                course,
                semester,
                photo_path,
                password
            ))

            self.conn.commit()
            return True

        except sqlite3.IntegrityError:
            print("Student ID already exists.")
            return False

        except Exception as e:
            print("Add Student Error:", e)
            return False

    # =========================================================
    # FETCH STUDENTS
    # =========================================================

    def fetch_students(self):

        self.cursor.execute("""
            SELECT *
            FROM students
            ORDER BY id DESC
        """)

        return self.cursor.fetchall()

    # =========================================================
    # GET STUDENT
    # =========================================================

    def get_student(self, student_id):

        self.cursor.execute("""
            SELECT *
            FROM students
            WHERE student_id=?
        """, (student_id,))

        return self.cursor.fetchone()

    # =========================================================
    # CHECK STUDENT EXISTS
    # =========================================================

    def student_exists(self, student_id):

        self.cursor.execute("""
            SELECT id
            FROM students
            WHERE student_id=?
        """, (student_id,))

        return self.cursor.fetchone() is not None

    # =========================================================
    # VERIFY STUDENT IDENTITY
    # =========================================================

    def verify_student_identity(self, student_id, mobile):

        self.cursor.execute("""
            SELECT *
            FROM students
            WHERE student_id=?
            AND mobile=?
        """, (student_id, mobile))

        return self.cursor.fetchone()

    # =========================================================
    # STUDENT LOGIN
    # =========================================================

    def check_student_login(self, student_id, password):

        try:
            student_id = str(student_id).strip()
            password = str(password).strip()

            print("\n========== STUDENT LOGIN DEBUG ==========")
            print("Student ID:", repr(student_id))
            print("Password:", repr(password))

            self.cursor.execute("""
                SELECT
                    id,
                    student_id,
                    first_name,
                    last_name,
                    mobile,
                    course,
                    semester,
                    password
                FROM students
                WHERE student_id=?
            """, (student_id,))

            student = self.cursor.fetchone()

            if student is None:
                print("Student ID not found.")
                print("=========================================\n")
                return None

            print("Student Found")
            print("Database ID :", student[0])
            print("Student ID   :", student[1])
            print("Name         :", student[2], student[3])
            print("Mobile       :", student[4])
            print("Course       :", student[5])
            print("Semester     :", student[6])

            if student[7] == password:
                print("PASSWORD MATCH")
                print("STUDENT LOGIN SUCCESS")
                print("=========================================\n")
                return student

            print("PASSWORD DOES NOT MATCH")
            print("=========================================\n")
            return None

        except Exception as e:
            print("Student Login Database Error:", e)
            print("=========================================\n")
            return None

    # =========================================================
    # REGISTER STUDENT PASSWORD
    # =========================================================

    def register_student_password(
        self,
        student_id,
        mobile,
        new_password
    ):

        try:
            self.cursor.execute("""
                SELECT id
                FROM students
                WHERE student_id=?
                AND mobile=?
            """, (student_id, mobile))

            student = self.cursor.fetchone()

            if not student:
                return False

            self.cursor.execute("""
                UPDATE students
                SET password=?
                WHERE student_id=?
            """, (new_password, student_id))

            self.conn.commit()
            return True

        except Exception as e:
            print("Student Password Registration Error:", e)
            return False

    # =========================================================
    # UPDATE STUDENT PASSWORD
    # =========================================================

    def update_student_password(self, student_id, new_password):

        try:
            self.cursor.execute("""
                UPDATE students
                SET password=?
                WHERE student_id=?
            """, (new_password, student_id))

            self.conn.commit()
            return self.cursor.rowcount > 0

        except Exception as e:
            print("Student Password Update Error:", e)
            return False

    # =========================================================
    # CHANGE STUDENT PASSWORD
    # =========================================================

    def change_student_password(
        self,
        student_id,
        old_password,
        new_password
    ):

        self.cursor.execute("""
            SELECT id
            FROM students
            WHERE student_id=?
            AND password=?
        """, (student_id, old_password))

        student = self.cursor.fetchone()

        if not student:
            return False

        self.cursor.execute("""
            UPDATE students
            SET password=?
            WHERE student_id=?
        """, (new_password, student_id))

        self.conn.commit()
        return True

    # =========================================================
    # UPDATE STUDENT
    # =========================================================

    def update_student(
        self,
        student_id,
        first_name,
        last_name,
        mobile,
        course,
        semester
    ):

        self.cursor.execute("""
            UPDATE students
            SET
                first_name=?,
                last_name=?,
                mobile=?,
                course=?,
                semester=?
            WHERE student_id=?
        """, (
            first_name,
            last_name,
            mobile,
            course,
            semester,
            student_id
        ))

        self.conn.commit()
        return self.cursor.rowcount > 0

    # =========================================================
    # DELETE STUDENT
    # =========================================================

    def delete_student(self, student_id):

        self.cursor.execute("""
            DELETE FROM students
            WHERE student_id=?
        """, (student_id,))

        self.conn.commit()
        return self.cursor.rowcount > 0

    # =========================================================
    # SEARCH STUDENTS
    # =========================================================

    def search_students(self, keyword):

        search = f"%{keyword.strip()}%"

        self.cursor.execute("""
            SELECT *
            FROM students
            WHERE student_id LIKE ?
               OR first_name LIKE ?
               OR last_name LIKE ?
               OR mobile LIKE ?
               OR course LIKE ?
            ORDER BY id DESC
        """, (
            search,
            search,
            search,
            search,
            search
        ))

        return self.cursor.fetchall()

    # =========================================================
    # COUNT STUDENTS
    # =========================================================

    def count_students(self):

        self.cursor.execute("""
            SELECT COUNT(*)
            FROM students
        """)

        return self.cursor.fetchone()[0]

    # =========================================================
    # GET STUDENT PROFILE
    # =========================================================

    def get_student_profile(self, student_id):

        self.cursor.execute("""
            SELECT
                id,
                student_id,
                first_name,
                last_name,
                mobile,
                course,
                semester,
                photo_path
            FROM students
            WHERE student_id=?
        """, (student_id,))

        return self.cursor.fetchone()

    # =========================================================
    # ADD TEACHER
    # =========================================================

    def add_teacher(
        self,
        teacher_id,
        teacher_name,
        mobile,
        subject,
        qualification,
        photo_path
    ):

        try:
            self.cursor.execute("""
                INSERT INTO teachers(
                    teacher_id,
                    teacher_name,
                    mobile,
                    subject,
                    qualification,
                    photo_path
                )
                VALUES(?,?,?,?,?,?)
            """, (
                teacher_id,
                teacher_name,
                mobile,
                subject,
                qualification,
                photo_path
            ))

            self.conn.commit()
            return True

        except sqlite3.IntegrityError:
            print("Teacher ID already exists.")
            return False

        except Exception as e:
            print("Add Teacher Error:", e)
            return False

    # =========================================================
    # FETCH TEACHERS
    # =========================================================

    def fetch_teachers(self):

        self.cursor.execute("""
            SELECT *
            FROM teachers
            ORDER BY id DESC
        """)

        return self.cursor.fetchall()

    # =========================================================
    # UPDATE TEACHER
    # =========================================================

    def update_teacher(
        self,
        teacher_id,
        teacher_name,
        mobile,
        subject,
        qualification,
        photo_path
    ):

        self.cursor.execute("""
            UPDATE teachers
            SET
                teacher_name=?,
                mobile=?,
                subject=?,
                qualification=?,
                photo_path=?
            WHERE teacher_id=?
        """, (
            teacher_name,
            mobile,
            subject,
            qualification,
            photo_path,
            teacher_id
        ))

        self.conn.commit()
        return self.cursor.rowcount > 0

    # =========================================================
    # DELETE TEACHER
    # =========================================================

    def delete_teacher(self, teacher_id):

        self.cursor.execute("""
            DELETE FROM teachers
            WHERE teacher_id=?
        """, (teacher_id,))

        self.conn.commit()
        return self.cursor.rowcount > 0

    # =========================================================
    # SEARCH TEACHERS
    # =========================================================

    def search_teachers(self, keyword):

        search = f"%{keyword.strip()}%"

        self.cursor.execute("""
            SELECT *
            FROM teachers
            WHERE teacher_id LIKE ?
               OR teacher_name LIKE ?
               OR mobile LIKE ?
               OR subject LIKE ?
            ORDER BY id DESC
        """, (
            search,
            search,
            search,
            search
        ))

        return self.cursor.fetchall()

    # =========================================================
    # COUNT TEACHERS
    # =========================================================

    def count_teachers(self):

        self.cursor.execute("""
            SELECT COUNT(*)
            FROM teachers
        """)

        return self.cursor.fetchone()[0]

    # =========================================================
    # ADD COURSE
    # =========================================================

    def add_course(
        self,
        course_id,
        course_name,
        duration,
        fee
    ):

        try:
            self.cursor.execute("""
                INSERT INTO courses(
                    course_id,
                    course_name,
                    duration,
                    fee
                )
                VALUES(?,?,?,?)
            """, (
                course_id,
                course_name,
                duration,
                fee
            ))

            self.conn.commit()
            return True

        except sqlite3.IntegrityError:
            print("Course ID already exists.")
            return False

        except Exception as e:
            print("Add Course Error:", e)
            return False

    # =========================================================
    # FETCH COURSES
    # =========================================================

    def fetch_courses(self):

        self.cursor.execute("""
            SELECT *
            FROM courses
            ORDER BY id DESC
        """)

        return self.cursor.fetchall()

    # =========================================================
    # UPDATE COURSE
    # =========================================================

    def update_course(
        self,
        course_id,
        course_name,
        duration,
        fee
    ):

        self.cursor.execute("""
            UPDATE courses
            SET
                course_name=?,
                duration=?,
                fee=?
            WHERE course_id=?
        """, (
            course_name,
            duration,
            fee,
            course_id
        ))

        self.conn.commit()
        return self.cursor.rowcount > 0

    # =========================================================
    # DELETE COURSE
    # =========================================================

    def delete_course(self, course_id):

        self.cursor.execute("""
            DELETE FROM courses
            WHERE course_id=?
        """, (course_id,))

        self.conn.commit()
        return self.cursor.rowcount > 0

    # =========================================================
    # SEARCH COURSES
    # =========================================================

    def search_courses(self, keyword):

        search = f"%{keyword.strip()}%"

        self.cursor.execute("""
            SELECT *
            FROM courses
            WHERE course_id LIKE ?
               OR course_name LIKE ?
               OR duration LIKE ?
               OR fee LIKE ?
            ORDER BY id DESC
        """, (
            search,
            search,
            search,
            search
        ))

        return self.cursor.fetchall()

    # =========================================================
    # COUNT COURSES
    # =========================================================

    def count_courses(self):

        self.cursor.execute("""
            SELECT COUNT(*)
            FROM courses
        """)

        return self.cursor.fetchone()[0]

    # =========================================================
    # ADD FEE
    # =========================================================

    def add_fee(
        self,
        student_id,
        student_name,
        course,
        amount,
        status
    ):

        self.cursor.execute("""
            INSERT INTO fees(
                student_id,
                student_name,
                course,
                amount,
                status
            )
            VALUES(?,?,?,?,?)
        """, (
            student_id,
            student_name,
            course,
            amount,
            status
        ))

        self.conn.commit()
        return True

    # =========================================================
    # FETCH FEES
    # =========================================================

    def fetch_fees(self):

        self.cursor.execute("""
            SELECT *
            FROM fees
            ORDER BY id DESC
        """)

        return self.cursor.fetchall()

    # =========================================================
    # GET FEE BY ID
    # =========================================================

    def get_fee(self, fee_id):

        self.cursor.execute("""
            SELECT *
            FROM fees
            WHERE id=?
        """, (fee_id,))

        return self.cursor.fetchone()

    # =========================================================
    # UPDATE FEE
    # =========================================================

    def update_fee(
        self,
        student_id,
        student_name,
        course,
        amount,
        status
    ):

        self.cursor.execute("""
            UPDATE fees
            SET
                student_name=?,
                course=?,
                amount=?,
                status=?
            WHERE student_id=?
        """, (
            student_name,
            course,
            amount,
            status,
            student_id
        ))

        self.conn.commit()
        return self.cursor.rowcount > 0

    # =========================================================
    # DELETE FEE
    # =========================================================

    def delete_fee(self, student_id):

        self.cursor.execute("""
            DELETE FROM fees
            WHERE student_id=?
        """, (student_id,))

        self.conn.commit()
        return self.cursor.rowcount > 0

    # =========================================================
    # DELETE FEE BY ID
    # =========================================================

    def delete_fee_by_id(self, fee_id):

        self.cursor.execute("""
            DELETE FROM fees
            WHERE id=?
        """, (fee_id,))

        self.conn.commit()
        return self.cursor.rowcount > 0

    # =========================================================
    # SEARCH FEES
    # =========================================================

    def search_fees(self, keyword):

        search = f"%{keyword.strip()}%"

        self.cursor.execute("""
            SELECT *
            FROM fees
            WHERE student_id LIKE ?
               OR student_name LIKE ?
               OR course LIKE ?
               OR status LIKE ?
            ORDER BY id DESC
        """, (
            search,
            search,
            search,
            search
        ))

        return self.cursor.fetchall()

    # =========================================================
    # COUNT FEES
    # =========================================================

    def count_fees(self):

        self.cursor.execute("""
            SELECT COUNT(*)
            FROM fees
        """)

        return self.cursor.fetchone()[0]

    # =========================================================
    # ADD RESULT
    # =========================================================

    def add_result(
        self,
        student_id,
        student_name,
        course,
        subject,
        marks,
        grade,
        percentage,
        status
    ):

        self.cursor.execute("""
            INSERT INTO results(
                student_id,
                student_name,
                course,
                subject,
                marks,
                grade,
                percentage,
                status
            )
            VALUES(?,?,?,?,?,?,?,?)
        """, (
            student_id,
            student_name,
            course,
            subject,
            marks,
            grade,
            percentage,
            status
        ))

        self.conn.commit()
        return True

    # =========================================================
    # FETCH RESULTS
    # =========================================================

    def fetch_results(self):

        self.cursor.execute("""
            SELECT *
            FROM results
            ORDER BY id DESC
        """)

        return self.cursor.fetchall()

    # =========================================================
    # GET RESULT BY ID
    # =========================================================

    def get_result(self, result_id):

        self.cursor.execute("""
            SELECT *
            FROM results
            WHERE id=?
        """, (result_id,))

        return self.cursor.fetchone()

    # =========================================================
    # UPDATE RESULT BY ID
    # =========================================================

    def update_result_by_id(
        self,
        result_id,
        student_id,
        student_name,
        course,
        subject,
        marks,
        grade,
        percentage,
        status
    ):

        self.cursor.execute("""
            UPDATE results
            SET
                student_id=?,
                student_name=?,
                course=?,
                subject=?,
                marks=?,
                grade=?,
                percentage=?,
                status=?
            WHERE id=?
        """, (
            student_id,
            student_name,
            course,
            subject,
            marks,
            grade,
            percentage,
            status,
            result_id
        ))

        self.conn.commit()
        return self.cursor.rowcount > 0

    # =========================================================
    # UPDATE RESULT BY STUDENT ID
    # =========================================================

    def update_result(
        self,
        student_id,
        student_name,
        course,
        subject,
        marks,
        grade,
        percentage,
        status
    ):

        self.cursor.execute("""
            UPDATE results
            SET
                student_name=?,
                course=?,
                subject=?,
                marks=?,
                grade=?,
                percentage=?,
                status=?
            WHERE student_id=?
        """, (
            student_name,
            course,
            subject,
            marks,
            grade,
            percentage,
            status,
            student_id
        ))

        self.conn.commit()
        return self.cursor.rowcount > 0

    # =========================================================
    # DELETE RESULT BY ID
    # =========================================================

    def delete_result_by_id(self, result_id):

        self.cursor.execute("""
            DELETE FROM results
            WHERE id=?
        """, (result_id,))

        self.conn.commit()
        return self.cursor.rowcount > 0

    # =========================================================
    # DELETE RESULT BY STUDENT ID
    # =========================================================

    def delete_result(self, student_id):

        self.cursor.execute("""
            DELETE FROM results
            WHERE student_id=?
        """, (student_id,))

        self.conn.commit()
        return self.cursor.rowcount > 0

    # =========================================================
    # SEARCH RESULTS
    # =========================================================

    def search_results(self, keyword):

        search = f"%{keyword.strip()}%"

        self.cursor.execute("""
            SELECT *
            FROM results
            WHERE student_id LIKE ?
               OR student_name LIKE ?
               OR course LIKE ?
               OR subject LIKE ?
               OR status LIKE ?
            ORDER BY id DESC
        """, (
            search,
            search,
            search,
            search,
            search
        ))

        return self.cursor.fetchall()

    # =========================================================
    # COUNT RESULTS
    # =========================================================

    def count_results(self):

        self.cursor.execute("""
            SELECT COUNT(*)
            FROM results
        """)

        return self.cursor.fetchone()[0]

    # =========================================================
    # ADD ATTENDANCE
    # =========================================================

    def add_attendance(
        self,
        student_id,
        student_name,
        course,
        attendance_date,
        status
    ):

        self.cursor.execute("""
            INSERT INTO attendance(
                student_id,
                student_name,
                course,
                attendance_date,
                status
            )
            VALUES(?,?,?,?,?)
        """, (
            student_id,
            student_name,
            course,
            attendance_date,
            status
        ))

        self.conn.commit()
        return True

    # =========================================================
    # FETCH ATTENDANCE
    # =========================================================

    def fetch_attendance(self):

        self.cursor.execute("""
            SELECT *
            FROM attendance
            ORDER BY id DESC
        """)

        return self.cursor.fetchall()

    # =========================================================
    # GET ATTENDANCE BY ID
    # =========================================================

    def get_attendance(self, attendance_id):

        self.cursor.execute("""
            SELECT *
            FROM attendance
            WHERE id=?
        """, (attendance_id,))

        return self.cursor.fetchone()

    # =========================================================
    # UPDATE ATTENDANCE BY ID
    # =========================================================

    def update_attendance_by_id(
        self,
        attendance_id,
        student_id,
        student_name,
        course,
        attendance_date,
        status
    ):

        self.cursor.execute("""
            UPDATE attendance
            SET
                student_id=?,
                student_name=?,
                course=?,
                attendance_date=?,
                status=?
            WHERE id=?
        """, (
            student_id,
            student_name,
            course,
            attendance_date,
            status,
            attendance_id
        ))

        self.conn.commit()
        return self.cursor.rowcount > 0

    # =========================================================
    # UPDATE ATTENDANCE BY STUDENT ID
    # =========================================================

    def update_attendance(
        self,
        student_id,
        student_name,
        course,
        attendance_date,
        status
    ):

        self.cursor.execute("""
            UPDATE attendance
            SET
                student_name=?,
                course=?,
                attendance_date=?,
                status=?
            WHERE student_id=?
        """, (
            student_name,
            course,
            attendance_date,
            status,
            student_id
        ))

        self.conn.commit()
        return self.cursor.rowcount > 0

    # =========================================================
    # DELETE ATTENDANCE BY ID
    # =========================================================

    def delete_attendance_by_id(self, attendance_id):

        self.cursor.execute("""
            DELETE FROM attendance
            WHERE id=?
        """, (attendance_id,))

        self.conn.commit()
        return self.cursor.rowcount > 0

    # =========================================================
    # DELETE ATTENDANCE BY STUDENT ID
    # =========================================================

    def delete_attendance(self, student_id):

        self.cursor.execute("""
            DELETE FROM attendance
            WHERE student_id=?
        """, (student_id,))

        self.conn.commit()
        return self.cursor.rowcount > 0

    # =========================================================
    # SEARCH ATTENDANCE
    # =========================================================

    def search_attendance(self, keyword):

        search = f"%{keyword.strip()}%"

        self.cursor.execute("""
            SELECT *
            FROM attendance
            WHERE student_id LIKE ?
               OR student_name LIKE ?
               OR course LIKE ?
               OR attendance_date LIKE ?
               OR status LIKE ?
            ORDER BY id DESC
        """, (
            search,
            search,
            search,
            search,
            search
        ))

        return self.cursor.fetchall()

    # =========================================================
    # COUNT ATTENDANCE
    # =========================================================

    def count_attendance(self):

        self.cursor.execute("""
            SELECT COUNT(*)
            FROM attendance
        """)

        return self.cursor.fetchone()[0]

    # =========================================================
    # STUDENT ATTENDANCE SUMMARY
    # =========================================================

    def get_student_attendance_summary(self, student_id):

        self.cursor.execute("""
            SELECT
                COUNT(*) AS total_classes,
                SUM(
                    CASE
                        WHEN LOWER(TRIM(status))='present'
                        THEN 1
                        ELSE 0
                    END
                ) AS present_classes,
                SUM(
                    CASE
                        WHEN LOWER(TRIM(status))='absent'
                        THEN 1
                        ELSE 0
                    END
                ) AS absent_classes
            FROM attendance
            WHERE student_id=?
        """, (student_id,))

        row = self.cursor.fetchone()

        total_classes = row[0] or 0
        present_classes = row[1] or 0
        absent_classes = row[2] or 0

        percentage = 0

        if total_classes > 0:
            percentage = round(
                (present_classes / total_classes) * 100,
                2
            )

        return {
            "total_classes": total_classes,
            "present_classes": present_classes,
            "absent_classes": absent_classes,
            "attendance_percentage": percentage
        }

    # =========================================================
    # ADD EXAM
    # =========================================================

    def add_exam(
        self,
        exam_id,
        exam_name,
        course,
        semester,
        exam_date,
        total_marks
    ):

        try:
            self.cursor.execute("""
                INSERT INTO exams(
                    exam_id,
                    exam_name,
                    course,
                    semester,
                    exam_date,
                    total_marks
                )
                VALUES(?,?,?,?,?,?)
            """, (
                exam_id,
                exam_name,
                course,
                semester,
                exam_date,
                total_marks
            ))

            self.conn.commit()
            return True

        except sqlite3.IntegrityError:
            print("Exam ID already exists.")
            return False

        except Exception as e:
            print("Add Exam Error:", e)
            return False

    # =========================================================
    # FETCH EXAMS
    # =========================================================

    def fetch_exams(self):

        self.cursor.execute("""
            SELECT *
            FROM exams
            ORDER BY id DESC
        """)

        return self.cursor.fetchall()

    # =========================================================
    # GET EXAM BY DATABASE ID
    # =========================================================

    def get_exam(self, exam_database_id):

        self.cursor.execute("""
            SELECT *
            FROM exams
            WHERE id=?
        """, (exam_database_id,))

        return self.cursor.fetchone()

    # =========================================================
    # UPDATE EXAM BY EXAM ID
    # =========================================================

    def update_exam(
        self,
        exam_id,
        exam_name,
        course,
        semester,
        exam_date,
        total_marks
    ):

        self.cursor.execute("""
            UPDATE exams
            SET
                exam_name=?,
                course=?,
                semester=?,
                exam_date=?,
                total_marks=?
            WHERE exam_id=?
        """, (
            exam_name,
            course,
            semester,
            exam_date,
            total_marks,
            exam_id
        ))

        self.conn.commit()
        return self.cursor.rowcount > 0

    # =========================================================
    # UPDATE EXAM BY DATABASE ID
    # =========================================================

    def update_exam_by_id(
        self,
        database_id,
        exam_id,
        exam_name,
        course,
        semester,
        exam_date,
        total_marks
    ):

        self.cursor.execute("""
            UPDATE exams
            SET
                exam_id=?,
                exam_name=?,
                course=?,
                semester=?,
                exam_date=?,
                total_marks=?
            WHERE id=?
        """, (
            exam_id,
            exam_name,
            course,
            semester,
            exam_date,
            total_marks,
            database_id
        ))

        self.conn.commit()
        return self.cursor.rowcount > 0

    # =========================================================
    # DELETE EXAM BY EXAM ID
    # =========================================================

    def delete_exam(self, exam_id):

        self.cursor.execute("""
            DELETE FROM exams
            WHERE exam_id=?
        """, (exam_id,))

        self.conn.commit()
        return self.cursor.rowcount > 0

    # =========================================================
    # DELETE EXAM BY DATABASE ID
    # =========================================================

    def delete_exam_by_id(self, exam_database_id):

        self.cursor.execute("""
            DELETE FROM exams
            WHERE id=?
        """, (exam_database_id,))

        self.conn.commit()
        return self.cursor.rowcount > 0

    # =========================================================
    # SEARCH EXAMS
    # =========================================================

    def search_exams(self, keyword):

        search = f"%{keyword.strip()}%"

        self.cursor.execute("""
            SELECT *
            FROM exams
            WHERE exam_id LIKE ?
               OR exam_name LIKE ?
               OR course LIKE ?
               OR semester LIKE ?
            ORDER BY id DESC
        """, (
            search,
            search,
            search,
            search
        ))

        return self.cursor.fetchall()

    # =========================================================
    # COUNT EXAMS
    # =========================================================

    def count_exams(self):

        self.cursor.execute("""
            SELECT COUNT(*)
            FROM exams
        """)

        return self.cursor.fetchone()[0]

    # =========================================================
    # STUDENT PORTAL - RESULTS
    # =========================================================

    def get_student_results(self, student_id):

        self.cursor.execute("""
            SELECT *
            FROM results
            WHERE student_id=?
            ORDER BY id DESC
        """, (student_id,))

        return self.cursor.fetchall()

    # =========================================================
    # STUDENT PORTAL - RESULT COUNT
    # =========================================================

    def count_student_results(self, student_id):

        self.cursor.execute("""
            SELECT COUNT(*)
            FROM results
            WHERE student_id=?
        """, (student_id,))

        return self.cursor.fetchone()[0]

    # =========================================================
    # STUDENT PORTAL - ATTENDANCE
    # =========================================================

    def get_student_attendance(self, student_id):

        self.cursor.execute("""
            SELECT *
            FROM attendance
            WHERE student_id=?
            ORDER BY attendance_date DESC, id DESC
        """, (student_id,))

        return self.cursor.fetchall()

    # =========================================================
    # STUDENT PORTAL - FEES
    # =========================================================

    def get_student_fees(self, student_id):

        self.cursor.execute("""
            SELECT *
            FROM fees
            WHERE student_id=?
            ORDER BY id DESC
        """, (student_id,))

        return self.cursor.fetchall()

    # =========================================================
    # STUDENT PORTAL - EXAMS
    # =========================================================

    def get_student_exams(self, course, semester):

        self.cursor.execute("""
            SELECT *
            FROM exams
            WHERE course=?
            AND semester=?
            ORDER BY exam_date ASC
        """, (course, semester))

        return self.cursor.fetchall()

    # =========================================================
    # STUDENT PORTAL - FEE SUMMARY
    # =========================================================

    def get_student_fee_summary(self, student_id):

        self.cursor.execute("""
            SELECT COUNT(*)
            FROM fees
            WHERE student_id=?
        """, (student_id,))

        total_records = self.cursor.fetchone()[0]

        self.cursor.execute("""
            SELECT amount
            FROM fees
            WHERE student_id=?
        """, (student_id,))

        rows = self.cursor.fetchall()

        total_amount = 0.0

        for row in rows:
            try:
                total_amount += float(row[0] or 0)
            except (ValueError, TypeError):
                pass

        self.cursor.execute("""
            SELECT COUNT(*)
            FROM fees
            WHERE student_id=?
            AND LOWER(TRIM(status))='paid'
        """, (student_id,))

        paid_records = self.cursor.fetchone()[0]

        self.cursor.execute("""
            SELECT COUNT(*)
            FROM fees
            WHERE student_id=?
            AND LOWER(TRIM(status))='pending'
        """, (student_id,))

        pending_records = self.cursor.fetchone()[0]

        return {
            "total_records": total_records,
            "total_amount": total_amount,
            "paid_records": paid_records,
            "pending_records": pending_records
        }

    # =========================================================
    # STUDENT PORTAL - DASHBOARD DATA
    # =========================================================

    def get_student_dashboard_data(self, student_id):

        student = self.get_student(student_id)

        if not student:
            return None

        attendance_summary = self.get_student_attendance_summary(
            student_id
        )

        results = self.get_student_results(student_id)
        fees = self.get_student_fees(student_id)

        course = student[5]
        semester = student[6]

        exams = self.get_student_exams(
            course,
            semester
        )

        fee_summary = self.get_student_fee_summary(student_id)

        return {
            "student": student,
            "attendance": attendance_summary,
            "results": results,
            "fees": fees,
            "exams": exams,
            "fee_summary": fee_summary,
            "result_count": len(results),
            "fee_count": len(fees),
            "exam_count": len(exams)
        }

    # =========================================================
    # CLOSE DATABASE
    # =========================================================

    def close(self):

        try:
            if self.conn:
                self.conn.close()
                print("Database connection closed.")

        except Exception as e:
            print("Database Close Error:", e)

    # =========================================================
    # STUDENT PORTAL CONTENT / NOTICES / CALENDAR / SOCIAL
    # =========================================================

    def get_portal_notices(self, limit=6):
        try:
            self.cursor.execute("""
                SELECT id, title, message, priority, created_at
                FROM portal_notices
                ORDER BY id DESC
                LIMIT ?
            """, (limit,))
            return self.cursor.fetchall()
        except Exception as e:
            print("Portal Notices Error:", e)
            return []

    def add_portal_notice(self, title, message, priority="Normal"):
        try:
            self.cursor.execute("""
                INSERT INTO portal_notices(title, message, priority)
                VALUES (?, ?, ?)
            """, (title, message, priority))
            self.conn.commit()
            return True
        except Exception as e:
            print("Add Notice Error:", e)
            return False

    def delete_portal_notice(self, notice_id):
        try:
            self.cursor.execute(
                "DELETE FROM portal_notices WHERE id=?",
                (notice_id,)
            )
            self.conn.commit()
            return True
        except Exception as e:
            print("Delete Notice Error:", e)
            return False

    def get_calendar_events(self, limit=8):
        try:
            self.cursor.execute("""
                SELECT id, title, event_date, description
                FROM academic_calendar
                ORDER BY event_date ASC, id ASC
                LIMIT ?
            """, (limit,))
            return self.cursor.fetchall()
        except Exception as e:
            print("Calendar Error:", e)
            return []

    def add_calendar_event(self, title, event_date, description=""):
        try:
            self.cursor.execute("""
                INSERT INTO academic_calendar(title, event_date, description)
                VALUES (?, ?, ?)
            """, (title, event_date, description))
            self.conn.commit()
            return True
        except Exception as e:
            print("Add Calendar Error:", e)
            return False

    def delete_calendar_event(self, event_id):
        try:
            self.cursor.execute(
                "DELETE FROM academic_calendar WHERE id=?",
                (event_id,)
            )
            self.conn.commit()
            return True
        except Exception as e:
            print("Delete Calendar Error:", e)
            return False

    def get_social_links(self):
        try:
            self.cursor.execute("""
                SELECT id, platform, url
                FROM social_links
                ORDER BY platform ASC
            """)
            return self.cursor.fetchall()
        except Exception as e:
            print("Social Links Error:", e)
            return []

    def add_social_link(self, platform, url):
        try:
            self.cursor.execute(
                "INSERT INTO social_links(platform, url) VALUES (?, ?)",
                (platform, url)
            )
            self.conn.commit()
            return True
        except Exception as e:
            print("Add Social Link Error:", e)
            return False

    def delete_social_link(self, link_id):
        try:
            self.cursor.execute(
                "DELETE FROM social_links WHERE id=?",
                (link_id,)
            )
            self.conn.commit()
            return True
        except Exception as e:
            print("Delete Social Link Error:", e)
            return False

    def get_chairman_profile(self):
        try:
            self.cursor.execute("""
                SELECT id, name, title, message
                FROM chairman_profile
                WHERE id=1
            """)
            row = self.cursor.fetchone()
            if row:
                return row
            return (
                1,
                "Chairman",
                "Chairman",
                "Welcome to our Student Management System ERP. "
                "We wish every student success in academics and career."
            )
        except Exception as e:
            print("Chairman Profile Error:", e)
            return None

    def save_chairman_profile(self, name, title, message):
        try:
            self.cursor.execute("""
                INSERT INTO chairman_profile(id, name, title, message)
                VALUES (1, ?, ?, ?)
                ON CONFLICT(id) DO UPDATE SET
                    name=excluded.name,
                    title=excluded.title,
                    message=excluded.message
            """, (name, title, message))
            self.conn.commit()
            return True
        except Exception as e:
            print("Save Chairman Error:", e)
            return False

    def get_student_portal_content(self):
        return {
            "notices": self.get_portal_notices(),
            "calendar": self.get_calendar_events(),
            "social_links": self.get_social_links(),
            "chairman": self.get_chairman_profile()
        }
