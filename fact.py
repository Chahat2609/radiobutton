import sys
sys.setrecursionlimit(3500)
def fact(b):
    if(b<=1):
        return b
    else:
        return b*fact(b-1)
a=int(input("enter num"))
fact1=fact(a)
print(fact1)
