lst=[1,3,2,1,21,1,1]
length=len(lst)
n=int(input("enter num"))
c=0
for i in range(0,length):
    if n==lst[i]:
        c+=1
if c==0:
    print(n,"not found")
else:
    print(n,"has frequency",c)
