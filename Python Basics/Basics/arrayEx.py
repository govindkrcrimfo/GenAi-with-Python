
from array import array

# integer aarray 
arr=array('i',[1,5, 3,66,1,123,4,5])
for i in arr:
    print(i, end=" ")
print()

arr.append(1)
for i in arr:
    print(i, end=" ")
print()

arr.reverse()
for i in arr:
    print(i, end=" ")
print()

#float array
arr1=array('f',[1.2, 3.4, 5.6, 7.8])
for i in arr1:
    print(i, end=" ")
print()

#double array
arr2=array('d',[1.2, 3.4, 5.6, 7.8])
for i in arr2: 
    print(i, end=" ")
print()
