result=0
n=int(input("enter num"))
temp=n
while(n!=0):
    rem=n%10
    result=rem+(rem*rem*rem)
    n=n//10
print(result)
if(temp==result):
    print("armstrong")
else:
    print("not")


