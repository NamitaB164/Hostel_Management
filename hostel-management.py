import mysql.connector as m
def database():
con=m.connect(host="localhost",user="root",passwd="student",database="hostel")
cur=con.cursor()
cur.execute("create database hostel;")
con.close()
#database()
def admin():
con=m.connect(host="localhost",user="root",passwd="student",database="hostel")
cur=con.cursor()
cur.execute("create table admin\
(Admno varchar(3) not null primary key,\
Aname varchar(15),\
Password varchar(5))")
con.close()
#admin()
def insertadmin():
con=m.connect(host="localhost",user="root",passwd="student",database="hostel")
cur=con.cursor()
while True:
    adno=input("Enter Admin No.:")
    aname=input("Enter Aname:")
    pa=input("Enter Password:")
    qry="insert into admin values ('{}','{}','{}')"
    cur.execute(qry.format(adno,aname,pa))
    x=input("Do you want to enter more?Y/N:")
    if x in "nN":
        break
con.commit()
#insertadmin()
def createhostel():
    con=m.connect(host="localhost",user="root",passwd="student",database="hostel")
    cur=con.cursor()
    cur.execute("create table hostel\
        (hid int(3) not null primary key,\
        name varchar(15),\
        phone int(10),\
        roomtype varchar(20),\
        amount int(5),\
        DateofArrival date,\
        DateofExit date)")
    con.close()
#createhostel()
con=m.connect(host="localhost",user="root",passwd="student",database="hostel")
cur=con.cursor()
from tabulate import tabulate
def adminlogin():
while True:
    print("-"*148,"\n","\t"*27,"ADMIN LOGIN","\t"*27,"\n")
    print("-"*148)
    name=input("Enter name:")
    p=input("Enter Password:")
    q="select*from admin where aname='{}' and password='{}';"
    cur.execute(q.format(name,p))
    rs=cur.fetchall()
    h=["Admno","Aname","Password"]
    print(tabulate(rs,headers=h,tablefmt="fancy_grid"),"\n")
    X=input("do you want to continue?y/n:")
    if X in "nN":
        break
print("\n","-"*8,"LOGGED IN","-"*8,"\n")
con.commit()
def insert():
    print("*"*148,"\t"*27,"ENTER HOSTELER DATA","\t"*27)
    print("*"*148)
    while True:
        hid=int(input("Enter Hostel id :"))
    name=input("Enter Name:")
    phone=int(input("Enter Phone No.:"))
    roomtype=input("Enter Roomtype:")
    amt=int(input("Enter Amount:"))
    da=input("Enter Date of Arrival(yyyy-mm-dd):")
    do=input("Enter Date of Exit(yyyy-mm-dd):")
    qry="insert into hostel values ({},'{}',{},'{}',{},'{}','{}')"
    cur.execute(qry.format(hid,name,phone,roomtype,amt,da,do))
    x=input("Do you want to insert more records?Y/N:")
    if x in "nN":
        break
print("\n","-"*20,"REGISTERED","-"*20)
con.commit()
print("\n")
from tabulate import tabulate
def display():
    print("\n",'-'*70,"HOSTEL",'-'*69,"\n")
    cur.execute("select*from hostel;" )
    rs=cur.fetchall()
    h=["hid","name","phone","roomtype","amount","DateofArrival","DateofExit"]
    print("\n")
    print(tabulate(rs,headers=h,tablefmt="fancy_grid"))
    print("\n")
def delete():
while True:
    i=int(input("Enter Hostel id to be deleted:"))
    q='delete from hostel where hid={}'
    cur.execute(q.format(i))
    print("\n","-"*10,"RECORD DELETED","-"*10,"\n")
    z=input("Do you want to delete more records?y/n:")
    if z in "Nn":
        break
    print("\n")
con.commit()
def update():
    while True:
    name=input("Enter name to be updated:")
    hidn=int(input("Enter hid :"))
    q="select* from hostel where hid={} and name='{}'"
    cur.execute(q.format(hidn,name))
    rs=cur.fetchall()
    if rs:
        ph=int(input("Enter new Phone no. :"))
        q="update hostel set phone={} where name='{}'"
        cur.execute(q.format(ph,name))
        print("\n","-"*10,"PHONE NUMBER UPDATED","-"*10,"\n")
        c=input("Do you want change the Phone No. of more records?y/n:")
        if c in "nN":
            break
        con.commit()
    else:
    print("Record Not Found.")
    def update2():
    while True:
        print("\n","*"*20,"UPDATE DATE OF EXIT","*"*20,"\n")
        name=input("Enter name to be updated:")
        q="select*from hostel where name='{}'"
        cur.execute(q.format(name))
        rs=cur.fetchall()
        if rs:
            rd=input("Enter Date Of Exit :")
            q="update hostel set DateofExit='{}' where name='{}'"
            cur.execute(q.format(rd,name))
            print("\n","-"*10,"DATE OF EXIT UPDATED","-"*10,"\n")
            c=input("Do you want to change the Date of Exit of more records?y/n:")
            if c in "nN":
                break
            con.commit()
    else:
        print("Record Not Found.")
print("\n")
def modify():
    while True:
        print("\n","1.Update Phone no.","\n","\n","2. Update Date of Exit","\n")
        k=int(input("Enter your choice(1or 2): "))
        if k==1:
            update()
        elif k==2:
            update2()
        p=input("Do you want to update more records?y/n:")
        if p in "Nn":
            break
print("\n")
def search():
    nm=input("Enter name to be searched:")
    hidn=int(input("Enter hid :"))
    q="select* from hostel where hid={} and name='{}'"
    cur.execute(q.format(hidn,nm))
    rs=cur.fetchall()
    h=["hid","name","phone","roomtype","amount","DateofArrival","DateofExit"]
    print("\n",tabulate(rs,headers=h,tablefmt="grid"),"\n")
def code():
    print(":"*148,"\t"*27,"HOSTEL MANAGEMENT DATABASE","\t"*27)
    print(":"*148)
    print("\n")
    ch='y'
    while ch=='y':
        print('-'*70,"MAIN MENU",'-'*67,"\n")
        print("\n","1.Login","\n","2.Insert","\n","3.Search","\n","4.Modify","\n","5.Delete",
                "\n","6.Display","\n","7.Exit","\n")
        op=int(input("Enter Your Choice (1-7):"))
        if op==1:
            adminlogin()
        elif op==2:
            insert()
            print("-"*148)
        elif op==3:
            search()
            print("-"*148)
        elif op==4:
            modify()
            print("-"*148)
        elif op==5:
            delete()
            print("-"*148)
        elif op==6:
            display()
            print("-"*148)
        elif op==7:
            print("\n","-"*6,"EXITED","-"*6,"\n")
        else:
            print("Invalid choice.")
            print("-"*148)
            x=input("Do you want to continue the program?:Y/N")
            if x in "nN":
                break
code()
