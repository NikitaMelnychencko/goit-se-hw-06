import sqlite3


def select_top_5_students_by_average_grade(cur: sqlite3.Cursor):
    """
    Query top 5 students by average grade
    :param cur: the Connection object
    :return: rows top 5 students by average grade
    """
    rows = None
    try:
        cur.execute("""SELECT ROUND(AVG(g.grade), 2) as avggrade, s.fullname
                        FROM grades as g
                        LEFT JOIN students as s ON s.id = g.student_id
                        GROUP BY g.student_id
                        ORDER BY ROUND(AVG(g.grade), 2) DESC
                        LIMIT 5""")
        rows = cur.fetchall()
    except sqlite3.Error as e:
        print(e)
    finally:
        cur.close()
    return rows

def select_students_with_top_grade_in_subject(cur: sqlite3.Cursor, subject_id: int):
    """
    Query students with top grade in subject
    :param cur: the Connection object
    :param subject_id: subject id
    :return: rows students with top grade in subject
    """
    rows = None
    try:
        cur.execute("""SELECT s.fullname, g.grade
                        FROM grades as g
                        LEFT JOIN students as s ON s.id = g.student_id
                        WHERE g.subject_id = ?
                        ORDER BY g.grade DESC
                        LIMIT 1""", (subject_id,))
        rows = cur.fetchall()
    except sqlite3.Error as e:
        print(e)
    finally:
        cur.close()
    return rows

def select_average_grade_in_subject_by_group(cur: sqlite3.Cursor, subject_id: int):
    """
    Query average grade in subject by group
    :param cur: the Connection object
    :param subject_id: subject id
    :return: rows average grade in subject
    """
    rows = None
    try:
        cur.execute("""SELECT
                        sub.name AS subject_name,
                        gr.name AS group_name,
                        ROUND(AVG(g.grade), 2) AS avg_grade
                        FROM grades AS g
                        JOIN students AS s ON s.id = g.student_id
                        JOIN groups AS gr ON gr.id = s.group_id
                        JOIN subjects AS sub ON sub.id = g.subject_id
                        WHERE g.subject_id = 3
                        GROUP BY sub.id, sub.name, gr.id, gr.name
                        ORDER BY avg_grade DESC;""", (subject_id,))
        rows = cur.fetchall()
    except sqlite3.Error as e:
        print(e)
    finally:
        cur.close()
    return rows

def select_average_grade_in_subject_by_group(cur: sqlite3.Cursor, subject_id: int):
    """
    Query average grade in subject by group
    :param cur: the Connection object
    :param subject_id: subject id
    :return: rows average grade in subject
    """
    rows = None
    try:
        cur.execute("""SELECT AVG(g.grade) as grade FROM grades as g;""")
        rows = cur.fetchall()
    except sqlite3.Error as e:
        print(e)
    finally:
        cur.close()
    return rows
def select_subject_by_teacher(cur: sqlite3.Cursor, teacher_id: int):
    """
    Query subject by teacher
    :param cur: the Connection object
    :param teacher_id: teacher id
    :return: rows subject by teacher
    """
    rows = None
    try:
        cur.execute("""SELECT s.name, t.fullname FROM subjects as s JOIN teachers as t ON t.id = s.teacher_id WHERE t.id = ? GROUP BY s.name, t.fullname;""", (teacher_id,))
        rows = cur.fetchall()
        rows = {
            "subject": [name for name, _ in rows],
            "teacher": rows[0][1] if rows else None,
        }
    except sqlite3.Error as e:
        print(e)
    finally:
        cur.close()
    return rows

def select_students_from_group(cur: sqlite3.Cursor, group_id: int):
    """
    Query students from group
    :param cur: the Connection object
    :param group_id: group id
    :return: rows students from group
    """
    rows = None
    try:
        cur.execute("""SELECT s.fullname FROM students as s JOIN groups as g ON g.id = s.group_id WHERE g.id = ?;""", (group_id,))
        rows = [row[0] for row in cur.fetchall()]
    except sqlite3.Error as e:
        print(e)
    finally:
        cur.close()
    return rows


def select_students_from_group_by_subject(cur: sqlite3.Cursor, group_id: int, subject_id: int):
    """
    Query students from group by subject
    :param cur: the Connection object
    :param group_id: group id
    :param subject_id: subject id
    :return: rows students from group by subject
    """
    rows = None
    try:
        cur.execute("""SELECT s.fullname, gr.grade, gr.student_id, gr.date
                        FROM students as s
                        JOIN groups as g ON g.id = s.group_id
                        LEFT JOIN grades as gr ON gr.student_id  = s.id
                        WHERE g.id = ? and gr.subject_id = ?""", (group_id, subject_id))
        rows = cur.fetchall()
    except sqlite3.Error as e:
        print(e)
    finally:
        cur.close()
    return rows

def select_average_grade_from_subject_by_teacher(cur: sqlite3.Cursor, teacher_id: int, subject_id: int):
    """
    Query average grade from subject by teacher
    :param cur: the Connection object
    :param teacher_id: teacher id
    :return: rows average grade from subject by teacher
    """
    rows = None
    try:
        cur.execute("""SELECT AVG(g.grade)as avg_grade, t.fullname  FROM grades as g
                        LEFT JOIN subjects as s ON s.id = g.subject_id
                        LEFT JOIN teachers as t ON t.id = s.teacher_id
                        WHERE t.id = ? AND s.id = ?""", (teacher_id, subject_id))
        rows = cur.fetchall()
    except sqlite3.Error as e:
        print(e)
    finally:
        cur.close()
    return rows


def select_subjects_by_student(cur: sqlite3.Cursor, student_email: str):
    """
    Query subjects by student
    :param cur: the Connection object
    :param student_id: student id
    :return: rows subject by student
    """
    rows = None
    try:
        cur.execute("""SELECT s.fullname, sub.name FROM students as s
                        LEFT JOIN groups AS g ON g.id = s.group_id
                        LEFT JOIN subjects AS sub ON sub.group_id = g.id
                        WHERE s.email = ?
                        GROUP BY s.fullname, sub.name;""", (student_email,))
        rows = cur.fetchall()
    except sqlite3.Error as e:
        print(e)
    finally:
        cur.close()
    return rows

def select_subjects_by_student_from_teacher(cur: sqlite3.Cursor, teacher_id: int, student_id: str):
    """
    Query subjects by student from teacher
    :param cur: the Connection object
    :param teacher_email: teacher id
    :param student_email: student id
    :return: rows subjects by student from teacher
    """
    rows = None
    try:
        cur.execute("""SELECT s.fullname, sub.name FROM students as s
                        LEFT JOIN groups AS g ON g.id = s.group_id
                        LEFT JOIN subjects AS sub ON sub.group_id = g.id
                        LEFT JOIN teachers AS t ON t.id = sub.teacher_id
                        WHERE t.id = ? AND s.id = ?
                        GROUP BY s.fullname, sub.name;""", (teacher_id, student_id))
        rows = cur.fetchall()
    except sqlite3.Error as e:
        print(e)
    finally:
        cur.close()
    return rows


## --- additional queries ---

def select_average_grade_from_subject_by_student_form_teacher(cur: sqlite3.Cursor, teacher_id: int, student_id: int):
    """
    Query average grade from subject by student from teacher
    :param cur: the Connection object
    :param teacher_id: teacher id
    :param student_id: student id
    :return: rows average grade from subject by student from teacher
    """
    rows = None
    try:
        cur.execute("""SELECT AVG(g.grade)as avg_grade, s.fullname as studentname, t.fullname as teachername  FROM grades as g
                        LEFT JOIN subjects as sub ON sub.id = g.subject_id
                        LEFT JOIN teachers as t ON t.id = sub.teacher_id
                        LEFT JOIN students as s ON s.id = g.student_id
                        WHERE t.id = ? AND s.id = ?
                        GROUP BY t.fullname, s.fullname;""", (teacher_id, student_id))
        rows = cur.fetchall()
    except sqlite3.Error as e:
        print(e)
    finally:
        cur.close()
    return rows


def select_grades_from_group_by_subject_on_last_class(cur: sqlite3.Cursor, group_id: int, subject_id: int):
    """
    Query grades of students in a group for a subject on the last class
    :param cur: the Connection object
    :param group_id: group id
    :param subject_id: subject id
    :return: rows grades from group by subject on last class
    """
    rows = None
    try:
        cur.execute("""SELECT s.fullname, g.grade, g.date
                        FROM grades AS g
                        JOIN students AS s ON s.id = g.student_id
                        WHERE s.group_id = ?
                          AND g.subject_id = ?
                          AND g.date = (
                              SELECT MAX(g2.date)
                              FROM grades AS g2
                              JOIN students AS s2 ON s2.id = g2.student_id
                              WHERE s2.group_id = ?
                                AND g2.subject_id = ?
                          );""", (group_id, subject_id, group_id, subject_id))
        rows = cur.fetchall()
    except sqlite3.Error as e:
        print(e)
    finally:
        cur.close()
    return rows

if __name__ == "__main__":
    with sqlite3.connect("school.db") as con:
        cur = con.cursor()
        # print("top 5 students by average grade:")
        # top_5_students_by_average_grade = select_top_5_students_by_average_grade(cur)
        # print(top_5_students_by_average_grade)
        # print("students with top grade in subject:")
        # students_with_top_grade_in_subject = select_students_with_top_grade_in_subject(cur, 2)
        # print(students_with_top_grade_in_subject)
        # print("average grade in subject by group:")
        # average_grade_in_subject_by_group = select_average_grade_in_subject_by_group(cur, 2)
        # print(average_grade_in_subject_by_group)
        # print("average grade in subject:")
        # average_grade_in_subject = select_average_grade_in_subject(cur)
        # print(average_grade_in_subject)
        # print("subject by teacher:")
        # subject_by_teacher = select_subject_by_teacher(cur, 1)
        # print(subject_by_teacher)
        # print("students from group:")
        # students_from_group = select_students_from_group(cur, 2)
        # print(students_from_group)
        # print("students from group by subject:")
        # students_from_group_by_subject = select_students_from_group_by_subject(cur, 1, 1)
        # print(students_from_group_by_subject)
        # print("average grade from subject by teacher:")
        # average_grade_from_subject_by_teacher = select_average_grade_from_subject_by_teacher(cur, 1, 1)
        # print(average_grade_from_subject_by_teacher)
        # print("subject by student:")
        # subject_by_student = select_subject_by_student(cur, 1)
        # print(subject_by_student)
        # print("subjects by student:")
        # subjects_by_student = select_subjects_by_student(cur, "uhernandez@example.net")
        # print(subjects_by_student)
        # print("subjects by student from teacher:")
        # subjects_by_student_from_teacher = select_subjects_by_student_from_teacher(cur, 1, 1)
        # print(subjects_by_student_from_teacher)

        # print("average grade from subject by student from teacher:")
        # average_grade_from_subject_by_student_from_teacher = select_average_grade_from_subject_by_student_form_teacher(cur, 1, 1)
        # print(average_grade_from_subject_by_student_from_teacher)
        # print("grades from group by subject on last class:")
        # grades_from_group_by_subject_on_last_class = select_grades_from_group_by_subject_on_last_class(cur, 1, 1)
        # print(grades_from_group_by_subject_on_last_class)