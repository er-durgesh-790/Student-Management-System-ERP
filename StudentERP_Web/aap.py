import sys
import os

from flask import (
    Flask,
    render_template,
    request,
    redirect,
    session
)

# =========================================================
# PROJECT PATH
# =========================================================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from database import Database


# =========================================================
# FLASK APP
# =========================================================

app = Flask(__name__)

app.secret_key = os.environ.get(
    "SECRET_KEY",
    "dev-only-change-this-secret"
)

# Production cookie settings
app.config.update(
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE="Lax",
    SESSION_COOKIE_SECURE=os.environ.get(
        "SESSION_COOKIE_SECURE",
        "false"
    ).lower() == "true"
)


# =========================================================
# DATABASE
# =========================================================

def get_database():
    return Database()


# =========================================================
# HOME
# =========================================================

@app.route("/")
def home():

    # Agar student already logged in hai
    if "student_id" in session:
        return redirect("/student-dashboard")

    # Agar admin already logged in hai
    if "admin_username" in session:
        return redirect("/dashboard")

    return render_template("login.html")


# =========================================================
# COMMON ADMIN CHECK
# =========================================================

def admin_required():

    return "admin_username" in session


# =========================================================
# ADMIN / GENERAL LOGIN
# =========================================================

@app.route("/login", methods=["POST"])
def login():

    user_type = request.form.get(
        "user_type",
        ""
    ).strip()

    username = request.form.get(
        "username",
        ""
    ).strip()

    password = request.form.get(
        "password",
        ""
    ).strip()

    if not username or not password:

        return render_template(
            "login.html",
            error="Please enter username and password."
        )

    database = get_database()

    # -----------------------------------------------------
    # ADMIN LOGIN
    # -----------------------------------------------------

    if user_type == "admin":

        admin = database.check_login(
            username,
            password
        )

        if admin:

            session.clear()

            session["admin_username"] = username

            return redirect("/dashboard")

        return render_template(
            "login.html",
            error="Invalid Admin Username or Password"
        )

    # -----------------------------------------------------
    # STUDENT LOGIN
    # -----------------------------------------------------

    elif user_type == "student":

        student = database.check_student_login(
            username,
            password
        )

        if student:

            session.clear()

            session["student_id"] = username

            return redirect(
                "/student-dashboard"
            )

        return render_template(
            "login.html",
            error="Invalid Student ID or Password"
        )

    return render_template(
        "login.html",
        error="Please select a valid login type."
    )


# =========================================================
# ADMIN DASHBOARD
# =========================================================

@app.route("/dashboard")
def dashboard():

    if not admin_required():
        return redirect("/")

    database = get_database()

    student_count = database.count_students()
    teacher_count = database.count_teachers()
    course_count = database.count_courses()
    exam_count = database.count_exams()

    return render_template(
        "dashboard.html",
        student_count=student_count,
        teacher_count=teacher_count,
        course_count=course_count,
        exam_count=exam_count
    )


# =========================================================
# STUDENT MANAGEMENT
# =========================================================

@app.route("/students")
def students():

    if not admin_required():
        return redirect("/")

    database = get_database()

    search = request.args.get(
        "search",
        ""
    ).strip()

    if search:

        students_data = database.search_students(
            search
        )

    else:

        students_data = database.fetch_students()

    return render_template(
        "students.html",
        students=students_data,
        search=search
    )


# =========================================================
# ADD STUDENT
# =========================================================

@app.route(
    "/students/add",
    methods=["POST"]
)
def add_student():

    if not admin_required():
        return redirect("/")

    student_id = request.form.get(
        "student_id",
        ""
    ).strip()

    first_name = request.form.get(
        "first_name",
        ""
    ).strip()

    last_name = request.form.get(
        "last_name",
        ""
    ).strip()

    mobile = request.form.get(
        "mobile",
        ""
    ).strip()

    course = request.form.get(
        "course",
        ""
    ).strip()

    semester = request.form.get(
        "semester",
        ""
    ).strip()

    photo_path = request.form.get(
        "photo_path",
        ""
    ).strip()

    password = request.form.get(
        "password",
        ""
    ).strip()

    if not student_id or not first_name:

        return redirect("/students")

    database = get_database()

    try:

        database.add_student(
            student_id,
            first_name,
            last_name,
            mobile,
            course,
            semester,
            photo_path,
            password if password else None
        )

    except Exception as e:

        print(
            "Student Add Error:",
            e
        )

    return redirect("/students")


# =========================================================
# TEACHERS
# =========================================================

@app.route("/teachers")
def teachers():

    if not admin_required():
        return redirect("/")

    database = get_database()

    search = request.args.get(
        "search",
        ""
    ).strip()

    if search:

        teachers_data = database.search_teachers(
            search
        )

    else:

        teachers_data = database.fetch_teachers()

    return render_template(
        "teachers.html",
        teachers=teachers_data,
        search=search
    )


# =========================================================
# ADD TEACHER
# =========================================================

@app.route(
    "/teachers/add",
    methods=["POST"]
)
def add_teacher():

    if not admin_required():
        return redirect("/")

    teacher_id = request.form.get(
        "teacher_id",
        ""
    ).strip()

    teacher_name = request.form.get(
        "teacher_name",
        ""
    ).strip()

    mobile = request.form.get(
        "mobile",
        ""
    ).strip()

    subject = request.form.get(
        "subject",
        ""
    ).strip()

    qualification = request.form.get(
        "qualification",
        ""
    ).strip()

    photo_path = request.form.get(
        "photo_path",
        ""
    ).strip()

    if not teacher_id or not teacher_name:
        return redirect("/teachers")

    database = get_database()

    try:

        database.add_teacher(
            teacher_id,
            teacher_name,
            mobile,
            subject,
            qualification,
            photo_path
        )

    except Exception as e:

        print(
            "Teacher Add Error:",
            e
        )

    return redirect("/teachers")


# =========================================================
# COURSES
# =========================================================

@app.route("/courses")
def courses():

    if not admin_required():
        return redirect("/")

    database = get_database()

    search = request.args.get(
        "search",
        ""
    ).strip()

    if search:

        courses_data = database.search_courses(
            search
        )

    else:

        courses_data = database.fetch_courses()

    return render_template(
        "courses.html",
        courses=courses_data,
        search=search
    )


# =========================================================
# ADD COURSE
# =========================================================

@app.route(
    "/courses/add",
    methods=["POST"]
)
def add_course():

    if not admin_required():
        return redirect("/")

    course_id = request.form.get(
        "course_id",
        ""
    ).strip()

    course_name = request.form.get(
        "course_name",
        ""
    ).strip()

    duration = request.form.get(
        "duration",
        ""
    ).strip()

    fee = request.form.get(
        "fee",
        ""
    ).strip()

    if not course_id or not course_name:
        return redirect("/courses")

    database = get_database()

    try:

        database.add_course(
            course_id,
            course_name,
            duration,
            fee
        )

    except Exception as e:

        print(
            "Course Add Error:",
            e
        )

    return redirect("/courses")


# =========================================================
# FEES
# =========================================================

@app.route("/fees")
def fees():

    if not admin_required():
        return redirect("/")

    database = get_database()

    search = request.args.get(
        "search",
        ""
    ).strip()

    if search:

        fees_data = database.search_fees(
            search
        )

    else:

        fees_data = database.fetch_fees()

    return render_template(
        "fees.html",
        fees=fees_data,
        search=search
    )


# =========================================================
# ADD FEE
# =========================================================

@app.route(
    "/fees/add",
    methods=["POST"]
)
def add_fee():

    if not admin_required():
        return redirect("/")

    student_id = request.form.get(
        "student_id",
        ""
    ).strip()

    student_name = request.form.get(
        "student_name",
        ""
    ).strip()

    course = request.form.get(
        "course",
        ""
    ).strip()

    amount = request.form.get(
        "amount",
        ""
    ).strip()

    status = request.form.get(
        "status",
        "Pending"
    ).strip()

    if (
        not student_id
        or not student_name
        or not course
        or not amount
    ):
        return redirect("/fees")

    database = get_database()

    try:

        database.add_fee(
            student_id,
            student_name,
            course,
            amount,
            status
        )

    except Exception as e:

        print(
            "Fee Add Error:",
            e
        )

    return redirect("/fees")


# =========================================================
# ATTENDANCE STUDENT API
# =========================================================

@app.route(
    "/attendance/student/<student_id>"
)
def attendance_student(student_id):

    if not admin_required():

        return {
            "success": False,
            "message": "Unauthorized"
        }, 401

    database = get_database()

    student = database.get_student(
        student_id.strip()
    )

    if not student:

        return {
            "success": False,
            "message": "Student not found"
        }

    return {
        "success": True,
        "student_id": student[1],
        "first_name": student[2] or "",
        "last_name": student[3] or "",
        "course": student[5] or "",
        "semester": student[6] or ""
    }


# =========================================================
# ATTENDANCE
# =========================================================

@app.route("/attendance")
def attendance():

    if not admin_required():
        return redirect("/")

    database = get_database()

    search = request.args.get(
        "search",
        ""
    ).strip()

    if search:

        attendance_data = database.search_attendance(
            search
        )

    else:

        attendance_data = database.fetch_attendance()

    return render_template(
        "attendance.html",
        attendance_data=attendance_data,
        search=search
    )


# =========================================================
# ADD ATTENDANCE
# =========================================================

@app.route(
    "/attendance/add",
    methods=["POST"]
)
def add_attendance():

    if not admin_required():
        return redirect("/")

    student_id = request.form.get(
        "student_id",
        ""
    ).strip()

    student_name = request.form.get(
        "student_name",
        ""
    ).strip()

    course = request.form.get(
        "course",
        ""
    ).strip()

    attendance_date = request.form.get(
        "attendance_date",
        ""
    ).strip()

    status = request.form.get(
        "status",
        "Present"
    ).strip()

    if (
        not student_id
        or not student_name
        or not course
        or not attendance_date
    ):
        return redirect("/attendance")

    database = get_database()

    try:

        database.add_attendance(
            student_id,
            student_name,
            course,
            attendance_date,
            status
        )

    except Exception as e:

        print(
            "Attendance Add Error:",
            e
        )

    return redirect("/attendance")


# =========================================================
# EDIT ATTENDANCE
# =========================================================

@app.route(
    "/attendance/edit/<int:attendance_id>"
)
def edit_attendance(attendance_id):

    if not admin_required():
        return redirect("/")

    database = get_database()

    attendance_record = database.get_attendance(
        attendance_id
    )

    if not attendance_record:
        return redirect("/attendance")

    return render_template(
        "attendance_edit.html",
        attendance=attendance_record
    )


# =========================================================
# UPDATE ATTENDANCE
# =========================================================

@app.route(
    "/attendance/update/<int:attendance_id>",
    methods=["POST"]
)
def update_attendance(attendance_id):

    if not admin_required():
        return redirect("/")

    student_id = request.form.get(
        "student_id",
        ""
    ).strip()

    student_name = request.form.get(
        "student_name",
        ""
    ).strip()

    course = request.form.get(
        "course",
        ""
    ).strip()

    attendance_date = request.form.get(
        "attendance_date",
        ""
    ).strip()

    status = request.form.get(
        "status",
        ""
    ).strip()

    database = get_database()

    try:

        database.update_attendance_by_id(
            attendance_id,
            student_id,
            student_name,
            course,
            attendance_date,
            status
        )

    except Exception as e:

        print(
            "Attendance Update Error:",
            e
        )

    return redirect("/attendance")


# =========================================================
# DELETE ATTENDANCE
# =========================================================

@app.route(
    "/attendance/delete/<int:attendance_id>",
    methods=["POST"]
)
def delete_attendance(attendance_id):

    if not admin_required():
        return redirect("/")

    database = get_database()

    try:

        database.delete_attendance_by_id(
            attendance_id
        )

    except Exception as e:

        print(
            "Attendance Delete Error:",
            e
        )

    return redirect("/attendance")


# =========================================================
# EXAMS
# =========================================================

@app.route("/exams")
def exams():

    if not admin_required():
        return redirect("/")

    database = get_database()

    search = request.args.get(
        "search",
        ""
    ).strip()

    if search:

        exams_data = database.search_exams(
            search
        )

    else:

        exams_data = database.fetch_exams()

    return render_template(
        "exams.html",
        exams=exams_data,
        search=search
    )


# =========================================================
# ADD EXAM
# =========================================================

@app.route(
    "/exams/add",
    methods=["POST"]
)
def add_exam():

    if not admin_required():
        return redirect("/")

    exam_id = request.form.get(
        "exam_id",
        ""
    ).strip()

    exam_name = request.form.get(
        "exam_name",
        ""
    ).strip()

    course = request.form.get(
        "course",
        ""
    ).strip()

    semester = request.form.get(
        "semester",
        ""
    ).strip()

    exam_date = request.form.get(
        "exam_date",
        ""
    ).strip()

    total_marks = request.form.get(
        "total_marks",
        ""
    ).strip()

    if not exam_id or not exam_name:
        return redirect("/exams")

    database = get_database()

    try:

        database.add_exam(
            exam_id,
            exam_name,
            course,
            semester,
            exam_date,
            total_marks
        )

    except Exception as e:

        print(
            "Exam Add Error:",
            e
        )

    return redirect("/exams")


# =========================================================
# EDIT EXAM
# =========================================================

@app.route(
    "/exams/edit/<int:exam_id>"
)
def edit_exam(exam_id):

    if not admin_required():
        return redirect("/")

    database = get_database()

    exam = database.get_exam(
        exam_id
    )

    if not exam:
        return redirect("/exams")

    return render_template(
        "exam_edit.html",
        exam=exam
    )


# =========================================================
# UPDATE EXAM
# =========================================================

@app.route(
    "/exams/update/<int:exam_id>",
    methods=["POST"]
)
def update_exam(exam_id):

    if not admin_required():
        return redirect("/")

    exam_id_value = request.form.get(
        "exam_id",
        ""
    ).strip()

    exam_name = request.form.get(
        "exam_name",
        ""
    ).strip()

    course = request.form.get(
        "course",
        ""
    ).strip()

    semester = request.form.get(
        "semester",
        ""
    ).strip()

    exam_date = request.form.get(
        "exam_date",
        ""
    ).strip()

    total_marks = request.form.get(
        "total_marks",
        ""
    ).strip()

    database = get_database()

    try:

        database.update_exam_by_id(
            exam_id,
            exam_id_value,
            exam_name,
            course,
            semester,
            exam_date,
            total_marks
        )

    except Exception as e:

        print(
            "Exam Update Error:",
            e
        )

    return redirect("/exams")


# =========================================================
# DELETE EXAM
# =========================================================

@app.route(
    "/exams/delete/<int:exam_id>",
    methods=["POST"]
)
def delete_exam(exam_id):

    if not admin_required():
        return redirect("/")

    database = get_database()

    try:

        database.delete_exam_by_id(
            exam_id
        )

    except Exception as e:

        print(
            "Exam Delete Error:",
            e
        )

    return redirect("/exams")


# =========================================================
# RESULTS
# =========================================================

@app.route("/results")
def results():

    if not admin_required():
        return redirect("/")

    database = get_database()

    search = request.args.get(
        "search",
        ""
    ).strip()

    if search:

        results_data = database.search_results(
            search
        )

    else:

        results_data = database.fetch_results()

    return render_template(
        "results.html",
        results=results_data,
        search=search
    )


# =========================================================
# ADD RESULT
# =========================================================

@app.route(
    "/results/add",
    methods=["POST"]
)
def add_result():

    if not admin_required():
        return redirect("/")

    student_id = request.form.get(
        "student_id",
        ""
    ).strip()

    student_name = request.form.get(
        "student_name",
        ""
    ).strip()

    course = request.form.get(
        "course",
        ""
    ).strip()

    subject = request.form.get(
        "subject",
        ""
    ).strip()

    marks = request.form.get(
        "marks",
        ""
    ).strip()

    grade = request.form.get(
        "grade",
        ""
    ).strip()

    percentage = request.form.get(
        "percentage",
        ""
    ).strip()

    status = request.form.get(
        "status",
        ""
    ).strip()

    if not student_id or not student_name:
        return redirect("/results")

    database = get_database()

    try:

        database.add_result(
            student_id,
            student_name,
            course,
            subject,
            marks,
            grade,
            percentage,
            status
        )

    except Exception as e:

        print(
            "Result Add Error:",
            e
        )

    return redirect("/results")


# =========================================================
# RESULT STUDENT API
# =========================================================

@app.route(
    "/results/student/<student_id>"
)
def result_student(student_id):

    if not admin_required():

        return {
            "success": False,
            "message": "Unauthorized"
        }, 401

    database = get_database()

    student = database.get_student(
        student_id.strip()
    )

    if not student:

        return {
            "success": False,
            "message": "Student not found"
        }

    return {
        "success": True,
        "student_id": student[1],
        "first_name": student[2] or "",
        "last_name": student[3] or "",
        "course": student[5] or "",
        "semester": student[6] or ""
    }


# =========================================================
# EDIT RESULT
# =========================================================

@app.route(
    "/results/edit/<int:result_id>"
)
def edit_result(result_id):

    if not admin_required():
        return redirect("/")

    database = get_database()

    result = database.get_result(
        result_id
    )

    if not result:
        return redirect("/results")

    return render_template(
        "result_edit.html",
        result=result
    )


# =========================================================
# UPDATE RESULT
# =========================================================

@app.route(
    "/results/update/<int:result_id>",
    methods=["POST"]
)
def update_result(result_id):

    if not admin_required():
        return redirect("/")

    student_id = request.form.get(
        "student_id",
        ""
    ).strip()

    student_name = request.form.get(
        "student_name",
        ""
    ).strip()

    course = request.form.get(
        "course",
        ""
    ).strip()

    subject = request.form.get(
        "subject",
        ""
    ).strip()

    marks = request.form.get(
        "marks",
        ""
    ).strip()

    grade = request.form.get(
        "grade",
        ""
    ).strip()

    percentage = request.form.get(
        "percentage",
        ""
    ).strip()

    status = request.form.get(
        "status",
        ""
    ).strip()

    database = get_database()

    try:

        database.update_result_by_id(
            result_id,
            student_id,
            student_name,
            course,
            subject,
            marks,
            grade,
            percentage,
            status
        )

    except Exception as e:

        print(
            "Result Update Error:",
            e
        )

    return redirect("/results")


# =========================================================
# DELETE RESULT
# =========================================================

@app.route(
    "/results/delete/<int:result_id>",
    methods=["POST"]
)
def delete_result(result_id):

    if not admin_required():
        return redirect("/")

    database = get_database()

    try:

        database.delete_result_by_id(
            result_id
        )

    except Exception as e:

        print(
            "Result Delete Error:",
            e
        )

    return redirect("/results")


# =========================================================
# STUDENT PORTAL LOGIN PAGE
# =========================================================

@app.route("/student-login")
def student_login():

    if "student_id" in session:
        return redirect("/student-dashboard")

    return render_template(
        "student_login.html"
    )


# =========================================================
# STUDENT PORTAL LOGIN
# =========================================================

@app.route(
    "/student-login",
    methods=["POST"]
)
def student_portal_login():

    student_id = request.form.get(
        "student_id",
        ""
    ).strip()

    password = request.form.get(
        "password",
        ""
    ).strip()

    if not student_id or not password:

        return render_template(
            "student_login.html",
            error="Please enter Student ID and Password."
        )

    database = get_database()

    try:

        student = database.check_student_login(
            student_id,
            password
        )

    except Exception as e:

        print(
            "Student Login Error:",
            e
        )

        return render_template(
            "student_login.html",
            error="Unable to process student login."
        )

    if student:

        session.clear()

        session["student_id"] = student_id

        return redirect(
            "/student-dashboard"
        )

    return render_template(
        "student_login.html",
        error="Invalid Student ID or Password."
    )


# =========================================================
# STUDENT DASHBOARD
# =========================================================

@app.route("/student-dashboard")
def student_dashboard():

    if "student_id" not in session:
        return redirect("/student-login")

    student_id = session["student_id"]

    database = get_database()

    try:

        dashboard_data = (
            database.get_student_dashboard_data(
                student_id
            )
        )

    except Exception as e:

        print(
            "Student Dashboard Error:",
            e
        )

        return redirect("/student-login")

    if not dashboard_data:

        session.clear()

        return render_template(
            "student_login.html",
            error="Student account not found."
        )

    student = dashboard_data["student"]

    return render_template(
        "student_dashboard.html",

        student=student,

        attendance=dashboard_data[
            "attendance"
        ],

        results=dashboard_data[
            "results"
        ],

        fees=dashboard_data[
            "fees"
        ],

        exams=dashboard_data[
            "exams"
        ],

        fee_summary=dashboard_data[
            "fee_summary"
        ],

        result_count=dashboard_data[
            "result_count"
        ],

        fee_count=dashboard_data[
            "fee_count"
        ],

        exam_count=dashboard_data[
            "exam_count"
        ]
    )


# =========================================================
# STUDENT PROFILE
# =========================================================

@app.route("/student-profile")
def student_profile():

    if "student_id" not in session:
        return redirect("/student-login")

    student_id = session["student_id"]

    database = get_database()

    student = database.get_student_profile(
        student_id
    )

    if not student:

        session.clear()

        return redirect("/student-login")

    return render_template(
        "student_profile.html",
        student=student
    )


# =========================================================
# STUDENT RESULTS
# =========================================================

@app.route("/student-results")
def student_results():

    if "student_id" not in session:
        return redirect("/student-login")

    student_id = session["student_id"]

    database = get_database()

    results_data = database.get_student_results(
        student_id
    )

    return render_template(
        "student_results.html",
        results=results_data
    )


# =========================================================
# STUDENT ATTENDANCE
# =========================================================

@app.route("/student-attendance")
def student_attendance():

    if "student_id" not in session:
        return redirect("/student-login")

    student_id = session["student_id"]

    database = get_database()

    attendance_data = database.get_student_attendance(
        student_id
    )

    attendance_summary = (
        database.get_student_attendance_summary(
            student_id
        )
    )

    return render_template(
        "student_attendance.html",
        attendance=attendance_data,
        summary=attendance_summary
    )


# =========================================================
# STUDENT FEES
# =========================================================

@app.route("/student-fees")
def student_fees():

    if "student_id" not in session:
        return redirect("/student-login")

    student_id = session["student_id"]

    database = get_database()

    fees_data = database.get_student_fees(
        student_id
    )

    fee_summary = (
        database.get_student_fee_summary(
            student_id
        )
    )

    return render_template(
        "student_fees.html",
        fees=fees_data,
        summary=fee_summary
    )


# =========================================================
# STUDENT EXAMS
# =========================================================

@app.route("/student-exams")
def student_exams():

    if "student_id" not in session:
        return redirect("/student-login")

    student_id = session["student_id"]

    database = get_database()

    student = database.get_student(
        student_id
    )

    if not student:

        session.clear()

        return redirect("/student-login")

    course = student[5]
    semester = student[6]

    exams_data = database.get_student_exams(
        course,
        semester
    )

    return render_template(
        "student_exams.html",
        exams=exams_data
    )


# =========================================================
# STUDENT CHANGE PASSWORD
# =========================================================

@app.route("/student-change-password")
def student_change_password_page():

    if "student_id" not in session:
        return redirect("/student-login")

    return render_template(
        "student_change_password.html"
    )


# =========================================================
# UPDATE STUDENT PASSWORD
# =========================================================

@app.route(
    "/student-change-password",
    methods=["POST"]
)
def student_change_password():

    if "student_id" not in session:
        return redirect("/student-login")

    student_id = session["student_id"]

    old_password = request.form.get(
        "old_password",
        ""
    ).strip()

    new_password = request.form.get(
        "new_password",
        ""
    ).strip()

    confirm_password = request.form.get(
        "confirm_password",
        ""
    ).strip()

    if (
        not old_password
        or not new_password
        or not confirm_password
    ):

        return render_template(
            "student_change_password.html",
            error="Please fill all fields."
        )

    if new_password != confirm_password:

        return render_template(
            "student_change_password.html",
            error="New passwords do not match."
        )

    if len(new_password) < 4:

        return render_template(
            "student_change_password.html",
            error="Password must contain at least 4 characters."
        )

    database = get_database()

    success = database.change_student_password(
        student_id,
        old_password,
        new_password
    )

    if success:

        return render_template(
            "student_change_password.html",
            success="Password changed successfully."
        )

    return render_template(
        "student_change_password.html",
        error="Current password is incorrect."
    )


# =========================================================
# STUDENT LOGOUT
# =========================================================

@app.route("/student-logout")
def student_logout():

    session.pop(
        "student_id",
        None
    )

    return redirect("/student-login")


# =========================================================
# ADMIN LOGOUT
# =========================================================

@app.route("/admin-logout")
def admin_logout():

    session.pop(
        "admin_username",
        None
    )

    return redirect("/")


# =========================================================
# GENERAL LOGOUT
# =========================================================

@app.route("/logout")
def logout():

    session.clear()

    return redirect("/")


# =========================================================
# HEALTH CHECK
# =========================================================

@app.route("/health")
def health():
    return {
        "status": "ok",
        "application": "Student Management System ERP"
    }, 200


# =========================================================
# ERROR HANDLERS
# =========================================================

@app.errorhandler(404)
def page_not_found(error):

    return """
    <h1>404 - Page Not Found</h1>
    <p>The requested page does not exist.</p>
    """, 404


@app.errorhandler(500)
def internal_server_error(error):

    print(
        "Internal Server Error:",
        error
    )

    return """
    <h1>500 - Internal Server Error</h1>
    <p>Something went wrong on the server.</p>
    """, 500


# =========================================================
# START SERVER
# =========================================================

if __name__ == "__main__":

    print("=" * 60)
    print("Student Management System ERP")
    print("Flask Server Starting...")
    host = os.environ.get("HOST", "127.0.0.1")
    port = int(os.environ.get("PORT", "5002"))
    debug = os.environ.get(
        "FLASK_DEBUG",
        "false"
    ).lower() == "true"

    print("Student Management System ERP")
    print(f"Flask Server Starting on {host}:{port}")
    print("=" * 60)

    app.run(
        host=host,
        port=port,
        debug=debug
    )