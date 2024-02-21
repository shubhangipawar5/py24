# Tupple are immutable and allows duplictae and hetrogeneous/many data types

t1=(1,1,2,'s','f')
print(t1)

# Methods
"""
count
freq of the element

print(list_fruits.count('apple'))


index
position of the element's 1st occurance 

print(list_fruits.index('apple'))

/////IMP Note///
var1 = ("hello")
print(type(var1))  # <class 'str'>

# Creating a tuple having one element
var2 = ("hello",)
print(type(var2))  # <class 'tuple'>

# Parentheses is optional
var3 = "hello",
print(type(var3))  # <class 'tuple'>
"""

# accessing tuple elements using indexing
letters = ("p", "r", "o", "g", "r", "a", "m", "i", "z")
print(letters[0])
print(letters[:5])
print(letters[-1])
print(letters[-1:-2])  #empty ()
print(letters[::-1])   #reversed tupple -> ('z', 'i', 'm', 'a', 'r', 'g', 'o', 'r', 'p')


#count
print(letters.count('r'))

#index -first occurence indx

print(letters.index('r'))

# Creating a nested tuple
nested_tuple = ("Python", {4: 5, 6: 2, 8:2}, (51, 31, 51, 61),['s','h'])
print("A nested tuple: ", nested_tuple)
print(nested_tuple[0])

print(nested_tuple[2][1])
print(nested_tuple[3][0].upper())
dict = nested_tuple[1]
for i in dict.items():
    print(i)
    print(type(i))   #<class 'tuple'>


# CHANGING a tupple -> it is immutable but we can convert it to LIST -> change and againg bach to tupple

t2 = ('nashhik','pune','mumbai','goa')

# Now change 'goa'-> 'kolkata'
l1 = list(t2)
print(l1)
l1[3]='kolkata'
print(l1)
print('***********convert to tupple again**********')
t2=tuple(l1)
print(t2)


# loop
# for i in t2:
#     print(i)

for i in range(len(t2)):
    print(i, t2[i])


"""
**Unpacking concept

cities = ("pune","banglore","kolkalata","chennai")
x1,x2,x3,x4 = cities
print(x1,x2,x3,x4 )


*////
cities = ["pune","banglore","kolkalata","chennai"]

x1,x2,x3,x4 = cities
print(x1,x2,x3,x4 )
"""


