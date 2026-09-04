import mysql.connector

# Connect to MySQL Database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="friedrice",   # Replace with your MySQL password
    database="student_management",
    use_pure=True
)

cursor = mydb.cursor()

# Retrieve student records
cursor.execute("SELECT student_id, student_name, cgpa FROM students")
records = cursor.fetchall()

# Sort records by Student ID
records = sorted(records, key=lambda x: x[0])

# ==========================
# BINARY SEARCH FUNCTION
# ==========================
def binary_search(records, target):

    low = 0
    high = len(records) - 1

    while low <= high:

        mid = (low + high) // 2

        if records[mid][0] == target:
            return records[mid]

        elif records[mid][0] < target:
            low = mid + 1

        else:
            high = mid - 1

    return None

# ==========================
# SEARCH STUDENT
# ==========================
student_id = input("Enter Student ID to search: ")

student = binary_search(records, student_id)

# ==========================
# DISPLAY RESULT
# ==========================
if student:

    print("\nStudent Found!")
    print("----------------------------")
    print("Student ID   :", student[0])
    print("Student Name :", student[1])
    print("CGPA         :", student[2])

else:

    print("\nStudent record not found.")

cursor.close()
mydb.close()