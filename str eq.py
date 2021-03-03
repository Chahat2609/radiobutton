a=input("enter any string")
b=input("enter any string")
'''if (a==b):
    print("equal")
else:
    print("not")'''
c=set(a.split(' '))
d=set(b.split(' '))
if(c==d):
    print("equal")
else:
    print("not")
