import mysql.connector
from tabulate import tabulate

con = mysql.connector.connect(host="localhost", user="root", password="root", database="hostel")
if con.is_connected():
    print("Successfully connected")
cursor = con.cursor()

def insertdata():
    r = int(input("Enter Roll Number: "))
    n = input("Enter Name: ")
    c = input("Enter Course: ")
    b = input("Enter Branch: ")
    h = input("Enter Hostel: ")
    f = int(input("Enter Hostel Fee: "))
    try:
        sql = "insert into student values(%s,%s,%s,%s,%s,%s)"
        val = (r, n, c, b, h, f)
        cursor.execute(sql, val)
        con.commit()
        print("Data Inserted Successfully")
    except:
        print("Data Insertion Failed")

def displaydata():
    sql = "select * from student"
    cursor.execute(sql)
    result = cursor.fetchall()
    print(tabulate(result, headers=["Roll No", "Name", "Course", "Branch", "Hostel", "Fees"], tablefmt="psql"))

def updatedata():
    r = int(input("Enter Roll Number to Update: "))
    f = int(input("Enter Updated Fees: "))
    sql = "update student set fees=%s where rollno=%s"
    val = (f, r)
    cursor.execute(sql, val)
    con.commit()
    print("Data Updated Successfully")

def deletedata():
    r = int(input("Enter Roll Number to Delete: "))
    sql = "delete from student where rollno=%s"
    val = (r,)
    cursor.execute(sql, val)
    con.commit()
    print("Data Deleted Successfully")

def searchdata():
    r = int(input("Enter Roll Number to Search: "))
    sql = "select * from student where rollno=%s"
    val = (r,)
    cursor.execute(sql, val)
    result = cursor.fetchall()
    if result:
        print(tabulate(result, headers=["Roll No", "Name", "Course", "Branch", "Hostel", "Fees"], tablefmt="psql"))
    else:
        print("No Record Found")

while True:
    print("""
    1. Insert Student Data
    2. Display All Students
    3. Update Student Fees
    4. Delete Student Record
    5. Search Student
    6. Exit
    """)
    ch = int(input("Enter your choice: "))
    if ch == 1:
        insertdata()
    elif ch == 2:
        displaydata()
    elif ch == 3:
        updatedata()
    elif ch == 4:
        deletedata()
    elif ch == 5:
        searchdata()
    elif ch == 6:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
