num=int(input("enter num"))
for i in range(num ):
    for j in range((num-i)-1):
        print(end=" ")
    for j in range(0,i):
        print("*",end=" ")
    print()
for i in range((num-1),0,-1):
    for j in range((num-i)-1):
        print(end=" ")
    for j in range(0,i):
        print("*",end=" ")
    print()
        
