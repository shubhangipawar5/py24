# Values can be of any type, including integer, list, and tuple.   , Mutable, uses Key and values

employee = {
            "Name": "Johnny",
            "Age": 32,
            "salary":26000,
            "Company":"^TCS",
            "found":["india","bangladesh"]
            }
#retrive values
print(employee["Name"])

# change value os key
employee["Name"]="AAyush"
print(employee["Name"])

# Add key
employee["DOB"]=20
print(employee["DOB"])
print(employee)
print(len(employee))

# del employee["DOB"]
# print(employee["DOB"])   #KeyError: 'DOB'

# del employee
# print(employee)   #removes from memory -  name 'employee' is not defined

"""
pop()	Remove the item with the specified key.
update()	Add or change dictionary items.
clear()	Remove all the items from the dictionary.
keys()	Returns all the dictionary's keys.
values()	Returns all the dictionary's values.
get()	Returns the value of the specified key.
popitem()	Returns the last inserted key and value as a tuple.
copy()	Returns a copy of the dictionary.
"""
print(employee.pop("DOB"))
print(employee)

print(employee.popitem())
print(employee)

e2 = employee.copy()
print(e2)
print(employee)
e2["color"]='red'
print(employee)  #{'Name': 'AAyush', 'Age': 32, 'salary': 26000, 'Company': '^TCS'}
print(e2)   #{'Name': 'AAyush', 'Age': 32, 'salary': 26000, 'Company': '^TCS', 'color': 'red'}   //changes memory

print(e2.get("color"))


print("####################")
# Looping

# for prop in employee:   #only keys
#     print(prop)
#
# for val in employee:  #only values
#     print(employee[val])
#
# for i in employee.items():   #both key,val
#     print(i)
#
# for i,j in employee.items():
#     print(i,j,sep=':')    #like this- Name:AAyush

# employee.update({"likes":"pizza","dislikes":"banana"})   #updates with other dict
# print(employee)
# employee.clear()   #empty {}
# print(employee)