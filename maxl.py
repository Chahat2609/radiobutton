list=[]
num=int(input("how many no u want to enter"))
for i in range(num):
    n1=input("enter num")
    list.append(n1)
    print(list)
max=list[0]
for i in range(len(list)):
    if list[i]>max:
        max=list[i]
print(max)
    
