rev=0
n=int(input("enter num"))
temp=n
while(n!=0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
print(rev)
if(temp==rev):
    print("palindrome")
else:
    print("not palindrome")


