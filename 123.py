num=int(input("enter num"))
for i in range(0,6):
    print()
    for j in range(num-i):
        print(end="")
for j in range(0,2*i-1):
    print("*",end="")
    print()
