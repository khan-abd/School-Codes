import csv

head=open("students.csv","w", newline='')
wob=csv.writer(head)
wob.writerow(['Name', 'Admno', 'Marks'])
head.close()

def add():
    with open ("students.csv", "a", newline='') as f:
        wob=csv.writer(f)
        name=input("Enter name: ")
        admno=int(input("Enter admno: "))
        marks=int(input("Enter marks: "))
        wob.writerow([name, admno, marks])
    
def search(searchid):
    with open ("students.csv", "r", newline='') as f1: 
        found=False
        rob=csv.reader(f1)
        for i in rob:
            if i[1].isalpha():
                pass
            elif int(i[1])==searchid:
                found=True
                print("Record:",i)
        else:
            if found==False:
                print("Record does not exist")


while True:
    menu=int(input('''
    1. Add
    2. Search
    3. Exit
    '''))

    if menu==1:
        add()
    elif menu==2:
        c=int(input("Enter admno, who's record has to be searched: "))
        search(c)
    elif menu==3:
        break

