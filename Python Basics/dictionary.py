# Dictionary - key value pair  - same like java or c++ map
# key are immutable , only one None key is allowed 

#creat dictionay 
# d={ key1 : value1 , key2 : value2 , key3 : value3 ,  .....}

d={
    1 : "one",
    2 : "two",
    "name" : "Govind",
    "age " : 26,
    7:123,
    5 : "Five"
}
print(d)

# print value for specific key
print(d[1])
print (d["name"])

# add key value 
d['temp']=5555




#check whether pariticular key is present or not 
print(5 in d)
print(10 in d)

del d[7]       # del & pop 
print(d)
 
delval=d.pop("temp")    
print(delval)

# All keys & values access 
k=d.keys()      # return list having keys
print(k)

v=d.values()    # return list having values
print(v)

# Iterate Through Keys
for k in d:    # or for k in d.keys():
    print(k , end=" ")
print()

# Iterate Through Values
for v in d.values():
    print(v,end=" ")
print()







