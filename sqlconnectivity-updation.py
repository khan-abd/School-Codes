#Insertion, search and update
import mysql.connector as mys
mycon=mys.connect(host='localhost',user='root', passwd='mysql123', database='abd')
mycur=mycon.cursor()
def display():
    mycur.execute("Select * from guestlist")
    for i in mycur.fetchall():
        print(i)
def add():
    name=input("Enter name: ")
    passcode=input("Enter Passcode")
    paid=int(input("Enter Payment"))
    date=input("Enter date of paying")
    mycur.execute("Insert into guestlist values('{}','{}',{},'{}')".format(name, passcode, paid, date))
    mycon.commit()
    print("Successfully added")
def search():
    c=input("Enter PassCode for search: ")
    mycur.execute("Select * from guestlist where PassCode='{}'".format(c))
    print(mycur.fetchone())
def update():
    c=input("Enter PassCode for updation: ")
    mycur.execute("Select * from guestlist where PassCode='{}'".format(c))
    print(mycur.fetchone())
    cb=int(input("Enter different Payment: "))
    mycur.execute("Update guestlist set Paid={} where PassCode='{}'".format(cb,c))
    mycon.commit()
    print("Successfully updated")
    

while True:
    ch=int(input('''Menu
    1. Display
    2. Add
    3. Search
    4. Update
    5. Exit
    '''))
    if ch==1:
        display()
    elif ch==2:
        add()
    elif ch==3:
        search()
    elif ch==4:
        update()
    elif ch==5:
        break
    
