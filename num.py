k=0
num=int(input("enter num"))
for i in range(num):
    for  j in range((num-i)-1):
        print("",end=" ")
    for j in range(2*i-1,0,-1):
        k=k+1
        print(k,end="")
    for k in range (i,0,-1):
       #k+=k
        k=k-1

        print(k,end=" ")
    print()
