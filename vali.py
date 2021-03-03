import re
phno=input("enter number")
r="w(3)-\w(3)-w(4)"
if re.search(r,phno):
    print("correct")
else:
    print("not")
