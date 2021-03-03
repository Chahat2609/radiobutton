str=input("enter any string")
str1=" "
for i in range(1,len(str)+1):
    str1+=str[-i]
print(str1)
