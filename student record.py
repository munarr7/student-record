import mysql.connector

# Connect to MySQL Server
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="friedrice",      # Replace with your MySQL password
    use_pure=True
)
cursor = mydb.cursor()
# Create Database
cursor.execute("CREATE DATABASE IF NOT EXISTS student_management")
cursor.execute("USE student_management")
# Create Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    student_id VARCHAR(20) PRIMARY KEY,
    student_name VARCHAR(100) NOT NULL,
    cgpa FLOAT NOT NULL
)
""")
def add_students():
    try:
        n = int(input("\nHow many student records do you want to enter? "))
        for i in range(n):
            print(f"\nEnter details for Student {i+1}")

            student_id = input("Student ID: ")
            student_name = input("Student Name: ")
            while True:
                try:
                    cgpa = float(input("CGPA (0 - 5): "))
                    if 0 <= cgpa <= 5:
                        break
                    else:
                        print("CGPA must be between 0 and 5.")
                except ValueError:
                    print("Invalid CGPA.")
            sql = """
            INSERT INTO students(student_id, student_name, cgpa)
            VALUES(%s,%s,%s)
            """
            values = (student_id, student_name, cgpa)
            try:
                cursor.execute(sql, values)
            except mysql.connector.Error:
                print("Student ID already exists!")
        mydb.commit()
        print("\nStudent record(s) added successfully.")
        print(f"Number of student records enetered: {n}")
    except ValueError:
        print("Invalid number.")
# VIEW STUDENTS
def view_students():
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()
    if len(records) == 0:
        print("\nNo student records found.")
        return
    print("\n---------------- STUDENT RECORDS ----------------")
    print("{:<15}{:<25}{:<10}".format("Student ID", "Student Name", "CGPA"))
    print("-" * 50)
    for record in records:
        print("{:<15}{:<25}{:<10}".format(record[0], record[1], record[2]))
def update_student():
    sid = input("\nEnter Student ID to update: ")
    cursor.execute(
        "SELECT * FROM students WHERE student_id=%s",
        (sid,)
    )
    record = cursor.fetchone()
    if record is None:
        print("Student not found.")
        return
    new_name = input("Enter new student name: ")
    while True:
        try:
            new_cgpa = float(input("Enter new CGPA: "))
            if 0 <= new_cgpa <= 5:
                break
            else:
                print("CGPA must be between 0 and 5.")
        except ValueError:
            print("Invalid CGPA.")
    cursor.execute("""
    UPDATE students
    SET student_name=%s,
        cgpa=%s
    WHERE student_id=%s
    """, (new_name, new_cgpa, sid))
    mydb.commit()
    print("Student record updated successfully.")
# DELETE STUDENT
def delete_student():
    sid = input("\nEnter Student ID to delete: ")
    cursor.execute(
        "SELECT * FROM students WHERE student_id=%s",
        (sid,)
    )
    if cursor.fetchone() is None:
        print("Student not found.")
        return
    confirm = input("Are you sure? (Y/N): ")
    if confirm.upper() == "Y":
        cursor.execute(
            "DELETE FROM students WHERE student_id=%s",
            (sid,)
        )
        mydb.commit()
        print("Student record deleted successfully.")
    else:
        print("Delete cancelled.")
while True:
    print("\n====== STUDENT RECORD MANAGEMENT SYSTEM ======")
    print("1. Add Student Record(s)")
    print("2. View Student Records")
    print("3. Update Student Record")
    print("4. Delete Student Record")
    print("5. Exit")
    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_students()

    elif choice == "2":
        view_students()

    elif choice == "3":
        update_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("\nThank you for using the system.")
        break

    else:
        print("Invalid choice.")

cursor.close()
mydb.close()