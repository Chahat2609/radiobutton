list=[]
num=int(input("how many no. u want to enter"))
for i in range(1,num+1):
    n=input("enter num")
    list.append(n)
print(list)
k=0
n2=int(input("enter the num u want to count"))
for j in list:
    if (j==n2):
        k=k+1
print(k)
    
   
