class Person:
    def __init__(self,nm,age,ln):
        self.firstname=nm
        self.age=age
        self.lastname=ln

    #setters

    def setFirstname(self,fn):
        self.firstname=fn

    def setAge(self, dob):
        self.age = dob

    def setLastName(self, lsn):
        self.lastname = lsn

    #getters

    def getFirstname(self):
        return self.firstname

    def getAge(self):
        return self.age


    def getLastName(self):
        return self.lastname


o1 = Person("Aayu",5,"Pawar")
print(o1.getFirstname())    #Aayu
o1.setFirstname("shubh")
print(o1.getFirstname())     #shubh

o2 =Person("Aayu",5,"Pawar")     #if you have to set the arguments outside the class with setters then do not pass argument in the construstor while creating it
o2.setAge(7)
o2.setLastName("xyz")
o2.setFirstname("abc")

print(o2.getAge())
print(o2.getFirstname())
print(o2.getLastName())
