
"""
class person:
    name = "shubhangi"
    age = 10
    skills = ["python","java","cypress"]

    def numOdskills(self):
        print(len(self.skills))

    def fullName(self):
        print(self.name)


obj1 = person()

print(obj1.skills)
print(obj1.name)
print(obj1.age)

# update properties values

obj1.name="aayush"
print(obj1.name)     #aayush

obj2 = person()
print(obj2.name)     #shubhangi
obj2.name= "som"
print(obj2.name)      #som
"""
# all above values are hardcoded ; not a good practice

# To have dynamic values we use constructor

class person2:

    def __init__(self,fn,a,sk):
        self.fullname=fn
        self.age=a
        self.skills=sk


    def dispplaynm(self):
        print(self.fullname)

    def dispSkills(self):
        print(self.skills)


shubh = person2("shubhangi",30,["cypress","java"])

shubh.dispplaynm()
shubh.dispSkills()


#creating many object with list
listofObj = [
    person2("aayu",5,["math","eng"]),
    person2("anu",7,["math","eng","hindi"]),
    person2("som",35,["mba","market"]),
    person2("sadu",25,["aws","sql"])
]

for item in listofObj:
    # print(item)    # i is a object here
    item.dispSkills()
    item.dispplaynm()

print("*********************")
for item in range(len(listofObj)):
    listofObj[item].dispplaynm()
    listofObj[item].dispSkills()


# creating many objects with dictionary

studentss = {
    "student1": person2("aayu",5,["math","eng"]),
    "student2": person2("aayu",5,["math","eng"]),
    "student3": person2("aayu",5,["math","eng"]),


}

for k in studentss.keys():
    # print(k)    #gives key only
     print(studentss[k])       #gives object  (whichh is the value of key)
     studentss[k].dispplaynm()    #gives the method
     print(studentss.get(k))    #gives values of key
     studentss.get(k).dispSkills()
     studentss.get(k).dispplaynm()

#
for k,v in studentss.items():
    print(k,v)
    v.dispplaynm()
    v.dispSkills()


for v in studentss.values():
    print(v)         #gives values only
    v.dispSkills()
    v.dispplaynm()


for k in studentss:
    # print(k)                #keys
    print(studentss[k])       #values

