from connection import create_connection


# 5 студентов с наибольшим средним баллом по всем предметам.

# select s.name, round(avg(m.mark), 2) as avg_mark
# from student_marks m
# left join students s on s.id = m.student_id
# group by s.id
# order by avg_mark desc
# limit 5;

def get_5_students_with_max_average_mark():
    with create_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT students.name, ROUND(AVG(student_marks.mark),2) AS average_mark
                FROM students
                JOIN student_marks ON students.id = student_marks.student_id
                GROUP BY students.name
                ORDER BY average_mark DESC
                LIMIT 5
                """
            )
            return cur.fetchall()


# 1 студент с наивысшим средним баллом по одному предмету.

def get_student_with_max_average_mark(subject_id):
    with create_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                    SELECT subj.name, s.name, ROUND(AVG(m.mark),2) AS average_mark
                    FROM student_marks m
                    LEFT JOIN students s ON s.id = m.student_id 
                    LEFT JOIN subjects subj ON subj.id = m.subject_id 
                    WHERE subj.id = %s
                    GROUP BY s.id, subj.id
                    ORDER BY average_mark DESC
                    LIMIT 1;
                """, (subject_id,)
            )
            return cur.fetchall()

# средний балл в группе по одному предмету.

# Средний балл в потоке.


# Какие курсы читает преподаватель.

# Список студентов в группе.

# Оценки студентов в группе по предмету.

# Оценки студентов в группе по предмету на последнем занятии.

# Список курсов, которые посещает студент.

# Список курсов, которые студенту читает преподаватель.

# Средний балл, который преподаватель ставит студенту.

# Средний балл, который ставит преподаватель.
