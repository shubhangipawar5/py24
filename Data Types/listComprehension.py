# [Expression for loop   if condition]
from functools import reduce

age=[4,18,19,20,25,7,98,4,3]

voters=[item for item in age if item >= 18]
print(voters)

# list comprehension

fruits = ["mango","banana","Kiwi","chikoo"]
newList = []

for item in fruits:
    newList.append(item)
print(newList)

# [expression for item in list if condition]
# program 2

q = [1,2,3,4,5,6,7,8,9,10]
sq = []
for item in q:
    sq.append(item*item)
print(sq)
q2 = [item * item for item in q]
print(q2)


# program 3
birthYear = [1990,1991,1992,1993]
q3=[2023 - item for item in birthYear]
print(q3)


# program 4
cities = ["kolkata","chennai","banglore","madras"]
q4 =[item.upper() for item in cities]
print(q4)

#program 5

names = ["kajal","poorva","mayuri","sarika","amol","ram"]
q5 = [item.upper() for item in names if len(item) >= 5]
print(q5)

# program 6
numbers = [11,22,44,55,22,33,44,55]
q6 = [item for item in numbers if item % 2 == 0]
print(q6)
# program 7
q7 = "books"
# q8 = {
#     "b":1,
#     "o":2,
#     "k":1,
#     "s":1
# }
dictA = {}
for char in q7:
    dictA[char]= dictA.get(char,0) + 1
print(dictA)





info  = {
    "firstName":"chinmay",
    "lastName":"deshpande"
}

print(info['firstName'])
info.get('firstName')
info['age'] = info.get('age',23)
print(info)



# program 1
numbers = [1,2,3,4,5,6,7,8,9,10]
newList = []
for item in numbers:
    newList.append(item * item)
print(newList)

# [expression for item in iterable if condition]
q2 = [item * item for item in numbers]
print(q2)

#program 2
names = ["amol","ram","rakesh","kajal","sarika","mayuri","chinmay","amol"]
q3 = [name.upper() for name in names]
print(q3)

#program3
q4 = [item.upper() for item in names if len(item) >= 5]
print(q4)

#program 4
q5 = [item * item * item for item in range(1,11)]
print(q5)

#program 5
students = [
    {'fullName':"chinmay deshpande",'age': 22},
    {'fullName':"sarang deshpande",'age': 30},
    {'fullName':"kanchan deshpande",'age': 50},
]

q5 = [student for student in students if student['age'] >= 30]
print(q5)



q5 = [student for student in students if student['age'] >= 30 and student['fullName'].startswith("k")]
print(q5)

#program 6

birthYear = [2001,1999,1998,1999,2000]
q6 = [2023 - year for year in birthYear ]
print(q6)

q7 = list(map(lambda year:2023 - year,birthYear))
print(q7)


q8 = list(filter(lambda student:student['age'] >= 30,students))
print(q8)

# list comprehension
#[1,2,3]
#
l=[1,2,3]
q8=reduce(lambda num1,num2:num1+num2,l)
print(q8)