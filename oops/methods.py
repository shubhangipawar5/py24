#No need to create objects for static method , we can casll with class name
class MathUtils:
    @staticmethod
    def add(x,y):
        return x + y

    @staticmethod
    def sub(x, y):
        return x - y


cal1 = MathUtils()
print(cal1.add(12,4))
print(cal1.sub(12,4))
print(MathUtils.add(12,3))
print(MathUtils.sub(12,3))

# program 2 count number of objects created from class
class MyClass:
    count = 0
    def __init__(self):
        MyClass.count =  MyClass.count + 1

    @staticmethod
    def get_object_count():
        return MyClass.count

a = MyClass()
b = MyClass()
c = MyClass()


print(MyClass.get_object_count())

# program 3


class Person:
    count = 0              #//static/class var
    country = 'INDIA'      #static/class var
    def __init__(self):
        Person.count += 1

    @classmethod
    def getObjCount(cls):
        return Person.count

    @classmethod
    def updateCountry(cls):
        cls.country = "india"

    @staticmethod
    def displayCoutry():
        return Person.country


a  = Person()
b  = Person()
print(b.getObjCount())
print(Person.getObjCount())