k=0
num=int(input("enter num"))
for i in range(num):
    for j in range((num-i)):
        print(end="  ")
    for j in range(0,2*i-1):
        print(k,end=" ")
        k=k+1
    print()
