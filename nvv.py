str=input("enter any string")
v=0
for s in str:
    if(s=='a'or s=='e'or s=='i'or s=='o'or s=='u' or s=='A'or s=='E'or s=='I' or s=='O'or s=='U'):
        v=v+1   
print(v)
str1=str.replace("a,e,,I,O,U","@")
print(str1)
