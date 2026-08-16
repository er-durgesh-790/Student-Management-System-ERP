from database import Database


db = Database()

student_id = "0001"
password = "0001"


print("\n========== LOGIN TEST ==========")

student = db.check_student_login(
    student_id,
    password
)

print("\nLOGIN RESULT:")
print(student)

if student:

    print("\n✅ STUDENT LOGIN SUCCESSFUL")

    print("Student ID :", student[1])
    print("Name       :", student[2], student[3])
    print("Course     :", student[5])
    print("Semester   :", student[6])

else:

    print("\n❌ STUDENT LOGIN FAILED")


print("\n================================")

db.close()