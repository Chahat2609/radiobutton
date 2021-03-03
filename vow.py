str=input("enter any string")
c=v=w=n=s=0
for a in str:
    if(a=='a'or a=='e'or a=='i'or a=='o'or a=='u' or a=='A'or a=='E'or a=='I'or a=='O'or a=='U'):
        v=v+1
    elif(a==' '):
        w=w+1
    elif(a>='a' and a<='z' or a>='A' and a<='Z'):
        c=c+1
    elif(a>='0' and a<='9'):
        n=n+1
    else:
        s=s+1
print(v)
print(w)
print(c)
print(n)
print(s)
