# Loops using range() on String, Tuple, and List

my_list = [10, 20, 30]
my_tuple = (40, 50, 60)
my_string = "Govind"

# using in range()
for i in range(len(my_list)):
    print(my_list[i], end=" ")
print()   # New line

for i in range(len(my_tuple)):
    print(my_tuple[i],end=" ")
print()   # New line

for i in range(len(my_string)):
    print(my_string[i],end=" ")
print()   # New line


#### Using for in  #####
for ch in my_list:
    print(ch,end=" ")
print()   # New line

for i in my_tuple:
    print(i,end=" ")
print()   # New line 

for ch in my_string:
    print(ch,end=" ")
print()    # New line 
