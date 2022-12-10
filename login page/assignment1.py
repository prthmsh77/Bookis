def search_value(A,X):
    n=len(A)
    for i in range (n):
        if (A[i]==X):
            return 1
        else:
            return 0

def intersection(A,B):
    C=[]
    for i in range (len(A)):
        flag=search_value(B,A[i])
        if (flag==1):
            C.append(A[i])
    return C


def union(A,B):
    C=A.copy()
    for i in range(len(A)):
        C.append(A[i])
    for i in range(len(B)):
        flag = search_value(A,B[i])
        if(flag==0):
            C.append(B[i])
    return C

def diff(A,B):
    C=[]
    for i in range(len(A)):
        flag = search_value(B,A[i])
        if(flag==0):
            C.append(A[i])
    return C


def sym_diff(lst1,lst2):
    lst3=[]
    D1=diff(lst1,lst2)
    print("Difference between Cricket and Badminton (C-B) is : ", D1)
    D2=diff(lst2,lst1)
    print("Difference between Badminton and Cricket (B-C) is : ", D2)
    lst3=union(D1,D2)
    return lst3


def CB(lst1,lst2):
    lst3=intersection(lst1,lst2)
    print("\n\nList of students who play both cricket and badminton is : ", lst3)
    return len(lst3)


def eCeB(lst1,lst2):
    lst3=sym_diff(lst1,lst2)
    print("\nList of students who play either cricket or badminton but not both is : ",lst3)
    return len(lst3)



def nCnB(lst1,lst2,lst3):
    lst4=diff(lst1,union(lst2,lst3))
    print("\n\nList of students who play neither cricket nor badminton is : ",lst4)
    return len(lst4)



def CBnF(lst1,lst2,lst3):
    lst4=diff(intersection(lst1,lst2),lst3)
    print("\n\nList of students who play cricket and football but not badminton is : ",lst4)
    return len(lst4)



SEComp = []
n = int(input("\nEnter number of students in SE COMPUTER: "))
print("Enter the names of",n,"students  :")
for i in range(0, n):
    ele = input()
    SEComp.append(ele) 
print("Original list of students in SEComp : " + str(SEComp))



Cricket = []
n = int(input("\n\nEnter number of students who play cricket : "))
print("Enter the names of",n,"students who play cricket  :")
for i in range(0, n):
    ele = input()
    Cricket.append(ele)  
print("Original list of students playing cricket is :" +str(Cricket))



Football = []
n = int(input("\n\nEnter number of students who play football : "))
print("Enter the name of",n,"students who play football  :")
for i in range(0, n):
    ele = input()
    Football.append(ele)  
print("Original list of students playing football :" +str(Football))




Badminton = []
n = int(input("\n\nEnter number of students who play badminton : "))
print("Enter the name of",n,"students who play badminton  :")
for i in range(0, n):
    ele = input()
    Badminton.append(ele)  # adding the element
print("Original list of students playing badminton :" +str(Badminton))



while True:
    print("\n\n--------------------MENU BAR--------------------\n")
    print("1. List of students who play both cricket and badminton")
    print("2. List of students who play either cricket or badminton but not both")
    print("3. List of students who play neither cricket nor badminton")
    print("4. Number of students who play cricket and football but not badminton")
    print("5. Exit\n")
    ch=int(input("Enter your Choice (from 1 to 5) :"))

    if ch==1:
        print("Number of students who play both cricket and badminton : ", CB(Cricket,Badminton))
       

    elif ch==2:
        print("Number of students who play either cricket or badminton but not both : ", eCeB(Cricket, Badminton))
       

    elif ch==3:
        print("Number of students who play neither cricket nor badminton : ", nCnB(SEComp,Cricket,Badminton))
       

    elif ch==4:
        print("Number of students who play cricket and football but not badminton : ", CBnF(Cricket,Football,Badminton))
        

    elif ch==5:
       
        print("Thanks for using this program!")
        break

    else:
        print("Wrong Choice!! ")
    a = input("\n\nDo you want to continue (y/n) :")
    if(a=="y"):continue
    else:break

#NAME : Dipali shendge
#ROLL NO : SECO2223B017
#hello this is pratrhmesh nigade