import pickle
with open ("emplo.dat", "wb") as f:
    pickle.dump(["name", "empid", "salary"], f)   
    while True:
        name=input("Enter name: ")
        empid=int(input("Enter id: "))
        salary=int(input("Enter salary: "))
        pickle.dump([name, empid, salary], f)
        ch=input("Continue? ")    
        if ch.lower()=="n":
            break
def search(searchid):
    found=False
    with open ("emplo.dat", "rb") as f1: 
        
        try:
            while True:
                x=pickle.load(f1)
                if x[1]==searchid:
                    found=True
                    print("Record required: ", x)

        except EOFError:
            if found==False:
                print("Record not found")

def update(updateid):
    found=False
    f2=open ("emplo.dat", "rb+")
    try:
        while True:
            rpos=f2.tell()
            x=pickle.load(f2)
            if list(x)[1]==updateid:
                found=True
                change=int(input("Enter new salary: "))
                x[2]=change
                f2.seek(rpos)
                pickle.dump(x, f2)
                print("Record updated!. See: ", x)

    except EOFError:
            if found==False:
                print("Record not found")

while True:
    menu=int(input('''
    1. Search
    2. Update
    3. Exit
    '''))

    if menu==1:
        c=int(input("Enter empid to be searched: "))
        search(c)
    elif menu==2:
        c=int(input("Enter empid to be updated: "))
        update(c)
    elif menu==3:
        break

