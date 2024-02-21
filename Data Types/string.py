"""
SST->str,set,tupples=Immutable
DL->Dict,List=Mutable
Set & Dict-> No Duplicate values, created with {}
List,Tupple,Dict,SET-> Hetrogeneous/any data type
tupple created->()
list created->[]
all are ordered except SET
"""




# in nested string method , if the return type is string then only string methods work in nested string/'
# In Python, strings are immutable. That means the characters of a string cannot be changed.
# string1 = "Python programming"
#
# # Accessing string
# print(string1[0])   #P
#
# for i in string1:
#      print(i)

print("*******************")

# Methods
# 1.length
#         0123456
greet =  "WELCOME to minskole"

print(len(greet))

# 2.slicing
print(greet[0:3])   #n-1 indexx will work
print(greet[0:-1])    #till last index -1
print((greet[0::]))   #default first to last
print((greet[0:]))     #default last from first
print((greet[:-1]))    #default first till last

print(greet[-3:])     #return 3 characters from last // upto last -3 index

# negative Indexing
print(greet[-2])

# slicing with jump values   # n-1 jump
print((greet[0::1]))   #WELCOME to minskole
print((greet[0::2]))    #WLOEt isoe

# Compare Two Strings
str1 = "Hello, world!"
str2 = "I love Python."
str3 = "Hello, world!"

# compare str1 and str2
print(str1 == str2)

# Join Two or More Strings
print(str1 + str2)
str1.join(str3)
# Membership test -returns boolean
print('a' in str1)  #False

print('a' not in str1)   #True

# 3.lower , upper, title
print(str1.upper()) #all upper
print(str1.lower()) #all lower
print(str1.title()) # 1st character of every word in the string


# 4. strip , lstrip,rstrip  // remooves extra spaces leading and trailing
fav = "  i Love Pune "
print(fav.strip())
print(fav.lstrip())
print(fav.rstrip())
#  CASEFOLD is similar to Lower method
# The casefold() method is similar to the lower() method but it is more aggressive.
# it converts other languages to lower case
text = 'groß'

# convert text to lowercase using casefold()
print('Using casefold():', text.casefold()) #o/p- gross


# 5.split
# split()			Splits the string at the specified separator, and returns a list

s = "Today is weekend"
print(s.split(" "))

email = "minskole@gmail.com"
print(email.split("@"))

print(type(s))
print(type(email.split("@"))) #'list'

# isascii()		Returns True if all characters in the string are ascii characters

# isdecimal()		Returns True if all characters in the string are decimals
# isdigit()		Returns True if all characters in the string are digits

# islower()		Returns True if all characters in the string are lower case
# isnumeric()		Returns True if all characters in the string are numeric
# isspace()		Returns True if all characters in the string are whitespaces
# istitle()		Returns True if the string follows the rules of a title
# isupper()		Returns True if all characters in the string are upper case


# 6.startswith()	Returns true if the string starts with the specified value
# Dynamicaaly typed - lower and upper case matters in string
strname = "Hello this is data science cource"

print(strname.startswith('H'))

# # 6. startswith()	Returns true if the string ends with the specified value
print(strname.endswith('e'))

# 7. index()  - returns index of substring
print(strname.index('H'))
print(strname.index('data'))

# 8. find()	returns the index of first occurrence of substring
print(strname.find('s'))   #9 index
print(strname.find('s',10))   #12 index  (here we have given 10 as start point, we can also give third arg. as end point
# )

# 9.replace()	replaces substring inside
print(strname)
print(strname.replace('data','info'))   #does not change the original string  / only temporarily replaces
print(strname)

# 10. Count -gives count of specified substring in the string
print(strname.count('s'))

# 11. Format
txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'm {1}".format("John",36)
txt3 = "My name is {}, I'm {}".format("John",36)

# 12. capitalize-  first letter of string to capital
nm = "hello shubh"
print(nm.capitalize())


#  13. contains- returns boolean if specified value contains in the string
print(nm.__contains__('o'))


names = " this is aayu is smart boy is good looking is"
a = names.find('is')
print(a)
strind = a
countt = names.count('is')
print(countt)
sub = len('is')

a = names.find('is')
i=a
strind = a

# reverse string
str = "shubhangi"

str1= ''.join(reversed(str))
print(str1)  #ignahbuhs
print(str[::-1])  #ignahbuhs




print('*****Reverse the string**********')

mystr='shubhangi'
revstr=''
for i in range(len(mystr)):
    revstr = mystr[i] + revstr

print(revstr)

#reverse below string

mystr1="shubhangi somnath pawar"
rev=''
spstr=mystr1.split(' ')
empl=[]
print(spstr)

for i in spstr:
    for j in range(len(i)):
        rev= i[j] + rev
    empl.append(rev)
    rev=''
print(empl)    #['ignahbuhs', 'htanmos', 'rawap']


print('//')
for i in empl:
    rev = i + rev
    rev = rev + ' '
print(rev)       #rawap htanmos ignahbuhs




# count the repeated chars in list/string
mystr='shubhangi'
chars = ['h','s','h','u','s','b','h','a','n','g','i',1,1,1,1,'h',2,3]
dict={}
l=len(chars)
count = 0
for i in range(l):
        for j in range(l):
          if (chars[i] == chars[j]):
            count = count + 1
            dict[chars[i]] = count


        count=0



print(dict)
