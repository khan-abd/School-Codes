import pickle
d={}
with open("product.dat","wb")as f:
    ch='y'
    while ch=='y':
        code=input("Enter the product code")
        desc=input("Enter the product description")
        sto=input("Enter the stock")
        d["prod_code"]=code
        d["prod_desc"]=desc
        d["stock"]=sto
        pickle.dump(d,f)
        ch=input("Do u want to continue(y/n)?")
    f.close()
def prod():
   
    d={}
    found=False
    fin=open("product.dat","rb+")
    STO=input("Enter the code to be updated")
    ST=input("Enter the new stock")
    try:
        while True:
            rpos=fin.tell()
            d=pickle.load(fin)
            if d["stock"]==STO:
                d["stock"]=ST
                fin.seek(rpos)
                pickle.dump(d,fin)
                found=True
                break
    except EOFError:
        if found==False:
            print("Sorry stock not matched")
        else:
            print("Update successful")
        fin.close()

def readinfo():
    fout=open("product.dat","rb")
    try:
        while True:
            stu=pickle.load(fout)
            print(stu)
            found=True
    except EOFError:
        if found==False:
            print("Unsuccessful")
        else:
            print("Success")
    fout.close()
prod()
readinfo()
            
            
    
