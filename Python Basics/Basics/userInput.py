# User input in python
a=input("enter a  number ")
print(a)

s=input("enter your name ")
print(s)

#input in list 
#l=[int(x) for x in input().strip().split("")]
l = [int(x) for x in input().split()]
for i in l :
    print(i)

