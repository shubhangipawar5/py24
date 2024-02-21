'''
https://www.youtube.com/watch?v=t4qkpUZRkAA&list=PLI4OVrCFuY56E57FdYzFNSWcEDS-ZKK26&index=11
'''
'''
class level variable is same for all the object instance variables
though u change instance var , it will update for that instance of object only not for class
'''
class Person:
    # class level variable
    country = "india"
    def __init__(self,fn,ln,age):
        self.firstName = fn
        self.lastName = ln
        self.age = age

    def displayName(self):
        print(self.firstName + self.lastName)

    def displayCountry(self):
        print(self.country)
    @classmethod
    def getCountry(cls):
        print(Person.country)


    @classmethod
    def changeCourty(cls,newC):       #cls - is a new class level variable for reference here , newC is the argument
        cls.country = newC

Person.getCountry()        #o/p- india
print(Person.country)     #o/p- india
Person.changeCourty("UK")    #now it is chnagedd to UK for all objects and cls level
sarika  =  Person("sarika","pansare",23)
sarika.displayCountry()

poorva  =  Person("poorva","vyas",44)
poorva.displayCountry()

mayuri = Person("Mayuri","Rao",34)
mayuri.displayCountry()

poorva.country = "USA seattle"       #though u change instance var , it will update for that instance of object only not for class
poorva.displayCountry()
print(poorva.__dict__)  #o/p-{'firstName': 'poorva', 'lastName': 'vyas', 'age': 44, 'country': 'USA seattle'}
print(Person.country)    #o/p- UK