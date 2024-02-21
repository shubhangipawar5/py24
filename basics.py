# name = "shubhangi"
# print(name)
# # multiline text
# name1 = """Hi this is shubh
# from solapur
# and now in pune"""
# print(name1)

# Printing strings in diff. ways
# Escaping Single Quote
String1 = 'I\'m a "Geek"'
print("Ramesh,Rakesh,Ujjwal")
print("Ramesh")
print("Rakesh")
print("Ujjwal")
print(String1)
# Print to new line
print("Ramesh,\nRakesh,\nUjjwal")
# print with a tab space
print("Ramesh,\tRakesh,\tUjjwal")

# using raw string  --it will prnt the string as it is given raw
print(r'C:/Users/shubh/HomeWork/2023/PyByRahulSir_2023/pyB/yRahul/basics.py')

#string formatings
name = "Shital"
place = "Nagpur"
skill =  "Python"

print("i am {} from {} with skill {}".format(name,place,skill))
# i am Shital from Nagpur with skill Python

# with indexing --0,1,2....
print("i am {0} from {1} with skill {2}".format(name,place,skill))
# i am Shital from Nagpur with skill Python

print("my skills is{2} , i am from {1} and my name is {0}".format(name,place,skill))
# my skills isPython , i am from Nagpur and my name is Shital

# using f-string
print(f"my name is {name}, i am from {place} and skill is {skill}")

myName = "aayush"
print("my name is", (myName))


print('**********input from user*****************')
"""
a = input('enter any number')
print(a)
# in above case it can take any input str / int/float,etc . from user
# use "eval"/int to evaluate the expression so it will take int value on;y from user
b = eval(input('enter any number'))
print(b)
c = int(input('enter any number'))
print(c)
"""


"""

# Take multiple input from user
lst = [x for x in input("enter 3 numbers with space:").split()]
print(lst)    #['1', '2', '3'] it is in string
# to get in integers we have to use int
lst1 = [int(x) for x in input("enter 3 numbers with space:").split()]
print(lst1)    #['1', '2', '3'] it is in string


# use od end/ sep in loop
# range(start point,end breakpoint,step value)

for i in range(0,5):
    print(i,end=" ") #end evry loop value with space  #0 1 2 3 4


for i in range(5,10):
    print(i,end=",") #end evry loop value with ,  #4 5,6,7,8,9,
"""
# map(data type,input())
nm = list(map(int,input('enter many numbers').split()))
print(nm)   #

""""
use of separator"""

for i in range(5,10):
    print(i,sep=":") #end evry loop value : ,  #4:   #i==index
                                               # 5:

lst = [1,2,3,4,5]

for i in range(len(lst)):
    print(i,lst[i],sep=':')   #i = index,  lst[i]  valus at index place

