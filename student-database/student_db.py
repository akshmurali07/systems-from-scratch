import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        grade TEXT,
        cgpa REAL
    )
''')
conn.commit()

def add_student(name, age, grade, cgpa):
    cursor.execute("INSERT INTO students (name, age, grade, cgpa) VALUES (?, ?, ?, ?)",
                   (name, age, grade, cgpa))
    conn.commit()
    print(f"✅ Added: {name}")

def view_all():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    if not students:
        print("No students found.")
        return
    print("\n--- All Students ---")
    for s in students:
        print(f"ID: {s[0]} | Name: {s[1]} | Age: {s[2]} | Grade: {s[3]} | CGPA: {s[4]}")

def search(name):
    cursor.execute("SELECT * FROM students WHERE name LIKE ?", (f"%{name}%",))
    for s in cursor.fetchall():
        print(f"ID: {s[0]} | Name: {s[1]} | CGPA: {s[4]}")

def delete(student_id):
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    print(f"✅ Deleted ID: {student_id}")

def top_students():
    cursor.execute("SELECT * FROM students ORDER BY cgpa DESC LIMIT 3")
    print("\n--- Top 3 by CGPA ---")
    for s in cursor.fetchall():
        print(f"{s[1]} — CGPA: {s[4]}")

while True:
    print("\n=== Student Database ===")
    print("1. Add  2. View All  3. Search  4. Delete  5. Top 3  6. Exit")
    choice = input("Choose: ")

    if choice == "1":
        add_student(input("Name: "), int(input("Age: ")), input("Grade: "), float(input("CGPA: ")))
    elif choice == "2":
        view_all()
    elif choice == "3":
        search(input("Search name: "))
    elif choice == "4":
        delete(int(input("ID to delete: ")))
    elif choice == "5":
        top_students()
    elif choice == "6":
        break

conn.close()