import faker
from random import randint, choice
import sqlite3

NUMBER_STUDENTS = 50
NUMBER_TEACHERS = 10
NUMBER_GROUPS = 3
NUMBER_SUBJECTS = 9
NUMBER_GRADES = 20


def generate_fake_data():
    fake_teachers = []  # here we will store teachers
    fake_students = []  # here we will store students

    fake_data = faker.Faker()

    # Create users with unique emails
    fullnames = set()
    emails = set()
    for _ in range(NUMBER_STUDENTS):
        fullname = fake_data.name()
        email = fake_data.email()
        group_id = randint(1, NUMBER_GROUPS)
        if email not in emails:
            emails.add(email)
        if fullname not in fullnames:
            fullnames.add(fullname)

        fake_students.append((fullname, email, group_id))

    for _ in range(NUMBER_TEACHERS):
        fullname = fake_data.name()
        email = fake_data.email()
        if fullname not in fullnames:
            fullnames.add(fullname)
        if email not in emails:
            emails.add(email)
        fake_teachers.append((fullname, email))

    fake_subjects = []  # here we will store subjects
    fake_grades = []  # here we will store grades
    for_users = []

    for n in range(NUMBER_SUBJECTS):
        fullname = f"Subject {n+1}"
        teacher_id = randint(1, NUMBER_TEACHERS)
        group_id = randint(1, NUMBER_GROUPS)
        fake_subjects.append((fullname, teacher_id, group_id))


    return  fake_teachers, fake_students, fake_subjects


def fake_grades(subjects, students):
    fake_grades = []
    for student_id in range(NUMBER_STUDENTS):
        for _ in range(NUMBER_GRADES):
            current_student = students[student_id]
            current_subject = list(filter(lambda x: x[2] == current_student[2], subjects))
            subject_id = subjects.index(choice(current_subject)) + 1
            grade = randint(1, 100)
            fake_data = faker.Faker()
            date = fake_data.date()
            fake_grades.append((student_id + 1, subject_id, grade, date))
    return fake_grades

def insert_data_to_db(teachers, students, subjects, grades):
    # Create database connection
    with sqlite3.connect("school.db") as con:
        cur = con.cursor()
        try:
            # Insert users
            sql_to_students = """INSERT INTO students(fullname, email, group_id)
                            VALUES (?, ?, ?)"""
            cur.executemany(sql_to_students, students)

            # Insert teachers
            sql_to_teachers = """INSERT INTO teachers(fullname, email)
                            VALUES (?, ?)"""
            cur.executemany(sql_to_teachers, teachers)

            # Insert subjects
            sql_to_subjects = """INSERT INTO subjects(name, teacher_id, group_id)
                            VALUES (?, ?, ?)"""
            cur.executemany(sql_to_subjects, subjects)

            # Insert grades
            sql_to_grades = """INSERT INTO grades(student_id, subject_id, grade, date)
                            VALUES (?, ?, ?, ?)"""
            cur.executemany(sql_to_grades, grades)

                # Commit changes
            con.commit()
            print(f"Added {len(teachers)} teachers and {len(students)} students")
            print(f"Added {len(subjects)} subjects and {len(grades)} grades")
        except sqlite3.Error as e:
            print(f"Error: {e}")
            con.rollback()
        finally:
            con.close()


if __name__ == "__main__":
    teachers, students, subjects = generate_fake_data()
    grades = fake_grades(subjects, students)
    insert_data_to_db(teachers, students, subjects, grades)
