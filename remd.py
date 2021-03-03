str=input("enter any string")
i=0
s1=""
for x in str:
    if str.index(x)==i:
    
        s1+=x
    i+=1
print(s1)
