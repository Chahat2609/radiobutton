l=[]
num=int(input("how many no u want to enter"))
for i in range(num):
    n=int(input("enter num"))
    l.append(n)
print(l)
l1=[]
#num1=int(input("how many no u want to enter"))
for i in range(num):
    n1=int(input("enter num"))
    l1.append(n1)
print(l1)
l3=[]
for i in range(num):
    l3.append(l[i]+l1[i])
print(l3)

