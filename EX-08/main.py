import psycopg2
from contextlib import contextmanager
from faker import Faker
import random

fake = Faker()


@contextmanager
def create_connection():
    conn = None
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="university",
            user="postgres",
            password="postgres",
        )
        print("Connection established")
        yield conn
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(e)
    finally:
        conn.close()


def create_table():
    with create_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS courses (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(50) NOT NULL
                )
                """
            )

            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS students (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(50) NOT NULL,
                    course_id INTEGER NOT NULL,
                    FOREIGN KEY (course_id) REFERENCES courses (id)
                )
                """
            )

            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS teachers (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(50) NOT NULL
                )
                """
            )

            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS subjects (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(50) NOT NULL,
                    teacher_id INTEGER NOT NULL,
                    FOREIGN KEY (teacher_id) REFERENCES teachers (id)
                )
                """
            )

            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS student_marks (
                    id SERIAL PRIMARY KEY,
                    student_id INTEGER NOT NULL,
                    subject_id INTEGER NOT NULL,
                    mark INTEGER NOT NULL,
                    date DATE NOT NULL,
                    FOREIGN KEY (student_id) REFERENCES students (id),
                    FOREIGN KEY (subject_id) REFERENCES subjects (id)
                )
                """
            )


def insert_data():
    with create_connection() as conn:
        with conn.cursor() as cur:
            for i in range(3):
                cur.execute('INSERT INTO courses (name) VALUES (%s)',
                            (fake.lexify(text='Course: ??????????', letters='ABCDE'),))

            cur.execute('SELECT id FROM courses')
            courses_ids = cur.fetchall()
            conn.commit()

            # print(random.choice(student_courses)[0])

            for i in range(30):
                cur.execute('INSERT INTO students (name, course_id) VALUES (%s, %s)',
                            (fake.name(), random.choice(courses_ids)[0]))

            cur.execute('SELECT id FROM students')
            student_ids = cur.fetchall()
            conn.commit()

            for i in range(3):
                cur.execute('INSERT INTO teachers (name) VALUES (%s)',
                            (fake.name(),))

            cur.execute('SELECT id FROM teachers')
            teacher_ids = cur.fetchall()
            conn.commit()

            # print('teacher_ids', random.choice(teacher_ids)[0])

            for subject in ['Math', 'Physics', 'Chemistry', 'Biology', 'English']:
                cur.execute('INSERT INTO subjects (name, teacher_id) VALUES (%s, %s)',
                            (subject, random.choice(teacher_ids)[0]))

            cur.execute('SELECT id FROM subjects')
            subject_ids = cur.fetchall()
            conn.commit()
            # print('subject_ids', random.choice(subject_ids)[0])

            for i in range(20):
                cur.execute('INSERT INTO student_marks (student_id, subject_id, mark, date) VALUES (%s, %s, %s, %s)',
                            (random.choice(student_ids)[0], random.choice(subject_ids)[0], random.randint(1, 5),
                             fake.date_this_year()))


if __name__ == '__main__':
    # create_table()
    print('Table created')
    # insert_data()
