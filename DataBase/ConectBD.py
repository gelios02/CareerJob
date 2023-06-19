import sqlite3

# Создание базы данных и таблиц
connection = sqlite3.connect('competencies.db')
cursor = connection.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS courses (id INTEGER PRIMARY KEY AUTOINCREMENT, code TEXT, direction TEXT)')

cursor.execute(
    'CREATE TABLE IF NOT EXISTS competencies (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, course_id INTEGER, FOREIGN KEY (course_id) REFERENCES courses(id))')

# Пример заготовленных данных
courses = [
    ('06.001', 'Программист'),
    ('06.004', 'Специалист по тестированию в области информационных технологий'),
    ('06.011', 'Администратор баз данных'),
    ('06.015', 'Специалист по информационным системам'),
    ('06.016', 'Руководитель проектов в области информационных технологий'),
    ('06.019', 'Технический писатель'),
    ('06.022', 'Системный аналитик'),
    ('06.025', 'Специалист по дизайну графических и пользовательских интерфейсов'),
    ('06.026', 'Системный администратор информационно-коммуникационных систем'),
    ('06.028', 'Системный программист')
]

competencies = [
    ('C++', 1),
    ('Python', 1),
    ('Java', 1),
    ('JavaScript', 1),
    ('C#', 1),
    ('Ruby', 1),
    ('PHP', 1),
    ('SQL', 1),
    ('ООП', 1),
    ('CSS', 1),
    ('HTML', 1),
    ('Git', 1),
    ('Жизненный цикл ПО', 2),
    ('Selenium', 2),
    ('Postman', 2),
    ('JUnit', 2),
    ('TestNG', 2),
    ('Agile', 2),
    ('Scrum', 2),
    ('Waterfall', 2),
    ('Java', 2),
    ('Python', 2),
    ('HTML', 3),
    ('MySQL', 3),
    ('Oracle', 3),
    ('PostgreSQL', 3),
    ('SQL', 3),
    ('Java', 4),
    ('C#', 4),
    ('Python', 4),
    ('JavaScript', 4),
    ('SQL', 4),
    ('API', 4),
    ('Тестирование', 4),
    ('Управление проектами', 4),
    ('Управление проектами', 5),
    ('Agile', 5),
    ('Waterfall', 5),
    ('Kanban', 5),
    ('Коммуникация', 5),
    ('Планирование и оценка рисков', 5),
    ('Мониторинг и контроль', 5),
    ('Английский', 6),
    ('Exel', 6),
    ('Microsoft Word', 6),
    ('Adobe FrameMaker', 6),
    ('MadCap Flare', 6),
    ('Confluence', 6),
    ('Jira', 6),
    ('Умение работать в команде', 6),
    ('Моделирование бизнес-процессов', 7),
    ('Сбор и документирование требований', 7),
    ('Управление проектами', 7),
    ('Коммуникационные навыки', 7),
    ('Графический дизайн', 8),
    ('UI/UX', 8),
    ('Прототипирование и макетирование', 8),
    ('Adobe XD', 8),
    ('Sketch', 8),
    ('Figma', 8),
    ('Аналитическое мышление', 8),
    ('Администрирование серверов', 9),
    ('Сетевые навыки', 9),
    ('Резервное копирование и восстановление данных', 9),
    ('Техническая поддержка', 9),
    ('C++', 10),
    ('Java', 10),
    ('C#', 10),
    ('Python', 10),
    ('Windows', 10),
    ('Linux', 10),
    ('UNIX', 10),
    ('Разработка драйверов', 10)
]

# Вставка данных в таблицы
for course in courses:
    cursor.execute('INSERT INTO courses (code, direction) VALUES (?, ?)', course)

for competency in competencies:
    cursor.execute('INSERT INTO competencies (name, course_id) VALUES (?, ?)', competency)

# Сохранение изменений и закрытие соединения с базой данных
connection.commit()
connection.close()
