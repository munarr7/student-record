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

# Retrieve all student records
cursor.execute("SELECT student_id, student_name, cgpa FROM students")
records = cursor.fetchall()

# QUICK SORT FUNCTION
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2][0]
    left = [x for x in arr if x[0] < pivot]
    middle = [x for x in arr if x[0] == pivot]
    right = [x for x in arr if x[0] > pivot]

    return quick_sort(left) + middle + quick_sort(right)

# Sort the records
sorted_records = quick_sort(records)

# Display the sorted records
print("\n====== STUDENT RECORDS SORTED BY STUDENT ID ======")

if len(sorted_records) == 0:
    print("No student records found.")
else:
    print("{:<15}{:<25}{:<10}".format("Student ID", "Student Name", "CGPA"))
    print("-" * 55)

    for student in sorted_records:
        print("{:<15}{:<25}{:<10}".format(
            student[0],
            student[1],
            student[2]
        ))

cursor.close()
mydb.close()