# List - Ordered and mutable collection of elements
#      - elements may have different data type


#Creating list 

l=[1,2,"abc",4,2.10,"g"]
print(l[1])     # print at specific index

a=list()       #list 

#list function
a.append(1)
a.append(10)
a.append(2)
print(a)

a.insert(0,5)
a.insert(5,10)
print(a)

a.remove(2)

print(a)

#sort
a.sort()
print(a)

#reverse 
a.reverse()
print(a)


# 0 to 10 number in list
a2 = [i for  i in range(10)]
print(a2)


# square of 0 to 10
a3 =[i*i for i in range(10)]
print(a3)

