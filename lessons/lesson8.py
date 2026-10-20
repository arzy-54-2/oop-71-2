import sqlite3

connect = sqlite3.connect("grade.db")

cursor =connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(50) NOT NULL,
        age INTEGER NOT NULL,
        hobby TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS grades(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        subject VARCHAR (100) NOT NULL,
        grade INTEGER NOT NULL,
        student_id INTEGER NOT NULL,
        FOREIGN KEY(student_id) REFERENCES students(id)
    )
''')
connect.commit()


def create_students():
    cursor.executemany(
        'INSERT INTO students(name, age, hobby) VALUES(?,?,?)',
        [
            ("Ardager", 27,"спать"),
            ("Олег", 13,"спать"),
            ("Слава", 10,"спать"),
            ("John", 22,"спать"),
        ]
    )
    connect.commit()
    print("Студенты созданы")

# create_students()

def create_grades():
    cursor.executemany(
        'INSERT INTO grades(subject, grade, student_id) VALUES(?,?,?)',
        [
            ("Алгебра", 5, 3),
            ("ИЗО", 2, 1),
            ("Химия", 5, 99),
            ("ФИЗРА", 5, 2),
        ]
    )
    connect.commit()
    print("Оценки добавлены")

# create_grades()

def get_student_grade():

    cursor.execute('''
        SELECT students.name, grades.subject, grades.grade
        FROM students FULL OUTER JOIN grades ON students.id = grades.student_id
    ''')

    data = cursor.fetchall()
    # print(data)
    for i in data:
        print(f"NAME: {i[0]} SUBJECT: {i[1]} GRADE: {i[2]}")

# get_student_grade()

# def get_best_student():
#
#     cursor.execute('''
#         SELECT name FROM students WHERE id IN (
#                 SELECT student_id FROM grades
#                 WHERE grade = 5
#             )
#     ''')
#     data = cursor.fetchall()
#     print(data)

# get_best_student()

# def create_my_view():
#     cursor.execute('''
#     CREATE VIEW IF NOT EXISTS best_student AS
#         SELECT name FROM students WHERE id IN (
#                 SELECT student_id FROM grades
#                 WHERE grade = 5
#             )
#     ''')
#     connect.commit()
#     print('View created')

# create_my_view()

def get_best_student_2():
    cursor.execute('SELECT * FROM best_student')
    data = cursor.fetchall()
    print(data)

get_best_student_2()