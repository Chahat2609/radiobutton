l=[]
num=int(input("how many no u want to enter"))
for i in range(num):
    n=int(input("enter num"))
    l.append(n)
print(l)
length=len(l)
n1=int(input("enter the element to found"))
for i in range(length):
    if(n1==l[i]):
        print("element is found at loc",i)
        break
    else:
        print("element is  not found at loc")
    
    
