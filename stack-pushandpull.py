'''Q.  Sanjana has created a dictionary containing ProdName and Price as the Key Value pair of 8 Products. Write a program with separate user defined function to perform the following operations:
• Push the Keys (ProdName) of the dictionary into a Stack, where corresponding Price range is 5000-25000 (inclusive of both values).
• Pop and display the content of Stack.'''

Stack=[]
Student={"TV":20000,"Mobile":19999,"Camera":4999,"Printer":5999, "Mouse":499,"Keyboard":600,"AC":45000}

def push():
    for i in Student: 
        if Student[i]>=5000 and Student[i]<=25000:
            Stack.append(i)
    print("Stack filled succesfully")

def pop():
    if Stack==[]:
        print('Underflow')
    else:
        print(Stack)
        while Stack!=[]:
            Stack.pop()


while True:
    ch=int(input('''
    MENU
    1. Push
    2. Pop
    3. Exit
    '''))
    if ch==1:
        push()
    elif ch==2:
        pop()
    elif ch==3:
        break
