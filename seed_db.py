import sqlite3

conn = sqlite3.connect("employee.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS employee (
    id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    role TEXT,
    salary INTEGER,
    joining_date TEXT
)
''')

cursor.execute("DELETE FROM employee")

sample_data = [
    (1, "Alice", "HR", "Manager", 75000, "2019-05-01"),
    (2, "Bob", "Engineering", "Developer", 90000, "2020-08-15"),
    (3, "Charlie", "Marketing", "Executive", 60000, "2021-01-10"),
    (4, "Dan", "Finance", "Manager", 97000, "2022-03-12"),
    (5, "Flora", "Marketing", "Manager", 82000, "2021-04-10"),
    (6, "George", "Sales", "Executive", 65000, "2021-01-10"),
    (7, "Harry", "Finance", "Executive", 80000, "2025-01-10"),
    (8, "Indu", "Engineering", "Tester", 85000, "2024-03-23"),
    (9, "Jack", "Sales", "Manager", 95000, "2024-01-10"),
    (10, "Katie", "Marketing", "Executive", 60000, "2021-01-10")
]

cursor.executemany("INSERT INTO employee VALUES (?, ?, ?, ?, ?, ?)", sample_data)
conn.commit()
conn.close()
