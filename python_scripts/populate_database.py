import random
from faker import Faker
from sqlalchemy import create_engine
import pandas as pd
from urllib.parse import quote_plus

# Faker object
fake = Faker()

# MySQL connection
username = "root"
password = quote_plus("YOUR_PASSWORD")

engine = create_engine(
    f"mysql+pymysql://{username}:{password}@localhost/student_performance"
)

# -----------------------------
# MASTER DATA
# -----------------------------

departments = {
    1: "CSE",
    2: "IT",
    3: "ECE",
    4: "MECH",
    5: "CIVIL"
}

subjects = {
    1: [1, 2],
    2: [3],
    3: [4],
    4: [5],
    5: [6]
}

# -----------------------------
# GENERATE STUDENTS
# -----------------------------

students_data = []

for i in range(1, 201):

    department_id = random.randint(1, 5)

    students_data.append({
        "roll_no": f"STU{i:03}",
        "student_name": fake.name(),
        "gender": random.choice(["M", "F"]),
        "email": f"student{i}@college.edu",
        "semester": random.randint(1, 8),
        "admission_year": random.randint(2021, 2025),
        "department_id": department_id
    })

students_df = pd.DataFrame(students_data)

students_df.to_sql(
    name="student",
    con=engine,
    if_exists="append",
    index=False
)

print("200 students inserted")

# -----------------------------
# FETCH STUDENT IDS
# -----------------------------

students = pd.read_sql(
    "SELECT student_id, department_id FROM student",
    con=engine
)

# -----------------------------
# ENROLLMENT DATA
# -----------------------------

enrollment_data = []

for _, row in students.iterrows():

    student_id = row["student_id"]
    department_id = row["department_id"]

    subject_list = subjects[department_id]

    for subject_id in subject_list:

        enrollment_data.append({
            "student_id": student_id,
            "subject_id": subject_id,
            "enrollment_date": fake.date_between(
                start_date='-1y',
                end_date='today'
            )
        })

enrollment_df = pd.DataFrame(enrollment_data)

enrollment_df.to_sql(
    name="enrollment",
    con=engine,
    if_exists="append",
    index=False
)

print("Enrollment data inserted")

# -----------------------------
# ATTENDANCE DATA
# -----------------------------

attendance_data = []

for _, row in students.iterrows():

    student_id = row["student_id"]
    department_id = row["department_id"]

    for subject_id in subjects[department_id]:

        attendance = random.randint(35, 100)

        if attendance >= 75:
            status = "Excellent"
        elif attendance >= 50:
            status = "Average"
        else:
            status = "Low"

        attendance_data.append({
            "student_id": student_id,
            "subject_id": subject_id,
            "attendance_percentage": attendance,
            "status": status,
            "recorded_date": fake.date_this_year()
        })

attendance_df = pd.DataFrame(attendance_data)

attendance_df.to_sql(
    name="attendance",
    con=engine,
    if_exists="append",
    index=False
)

print("Attendance data inserted")

# -----------------------------
# MARKS DATA
# -----------------------------

marks_data = []

for _, row in students.iterrows():

    student_id = row["student_id"]
    department_id = row["department_id"]

    for subject_id in subjects[department_id]:

        internal = random.randint(10, 30)
        external = random.randint(20, 70)

        total = internal + external

        if total >= 85:
            grade = "A"
        elif total >= 70:
            grade = "B"
        elif total >= 55:
            grade = "C"
        elif total >= 40:
            grade = "D"
        else:
            grade = "F"

        marks_data.append({
            "student_id": student_id,
            "subject_id": subject_id,
            "internal_marks": internal,
            "external_marks": external,
            "total_marks": total,
            "grade": grade
        })

marks_df = pd.DataFrame(marks_data)

marks_df.to_sql(
    name="marks",
    con=engine,
    if_exists="append",
    index=False
)

print("Marks data inserted")

# -----------------------------
# PERFORMANCE REPORT DATA
# -----------------------------

performance_data = []

for _, row in students.iterrows():

    student_id = row["student_id"]

    gpa = round(random.uniform(4.0, 9.8), 2)

    if gpa >= 8:
        performance = "Excellent"
    elif gpa >= 6:
        performance = "Good"
    elif gpa >= 5:
        performance = "Average"
    else:
        performance = "Poor"

    performance_data.append({
        "student_id": student_id,
        "semester": random.randint(1, 8),
        "gpa": gpa,
        "rank_position": random.randint(1, 200),
        "performance_status": performance,
        "generated_date": fake.date_this_year()
    })

performance_df = pd.DataFrame(performance_data)

performance_df.to_sql(
    name="performance_report",
    con=engine,  
    if_exists="append",
    index=False
)

print("Performance report inserted")

print("DATABASE POPULATION COMPLETED")
