# Ordered -> Elements maintain insertion order
# Immutable -> Cannot modify elements after creation
# Can store different data types

t=(1,"abcd",2.10)
print(t)
print(len(t))

t1=("efg", 25)
print(t+t1)     #concatination

print(t[0:2])   #slicing

# check present or not in tuple
if "abcd" in t:
    print("Element found")
else:
    print("Element not found")