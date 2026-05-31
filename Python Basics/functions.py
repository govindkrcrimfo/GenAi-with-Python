#funcitons in python and its type

# without parameter 
def greet():
    print("hello Govind ")
greet()

# with parameter 
def sum(a, b):
    return a+b
print(sum(2,3))

# with default parameter -> if paramte passed it will take it else default one
def greeting(name="Govind"):
    print("Hello ",name)
print(greeting("kumar"))

# variable size input 
def sum(a,b,*more):
    ans=a+b
    for i in more :
        ans+=i
    return ans
print(sum(1,2,3,4,5))

# more than one return value
def dumm(a,b):
    return a+b, a-b, a*b       #return tuple of (a+b , a-b , a*b)
t=dumm(3,2)
print(t)

