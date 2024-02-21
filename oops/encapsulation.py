#https://www.youtube.com/watch?v=_0SGomLTW0k&list=PLI4OVrCFuY56E57FdYzFNSWcEDS-ZKK26&index=22
#encapsulation can be acheived making variables private and access them with methods/getters-setters.
#private var is creataed with double underscore (__) and protected with single(_)

#example 1
'''

'''
class Person:
    def __init__(self):
        self.__password=12345      #made this var as private with __

    def display(self):
        print(f'password is: {self.__password}')


    #make method also as private

    def __dispInfo(self):
        print(f'password is: {self.__password}')


o1 =Person()
print(o1.__dict__)    #o/p-> {'_Person__password': 12345}


# print(o1.__password)   #AttributeError: 'Person' object has no attribute '__password'
#because it is private var

#we can access this var with method
o1.display()     #password is: 12345
o1.__password=98768      #this will only change for the object
print(o1._Person__password)     #op- 12345
print(o1.__dict__)    #o/p-   {'_Person__password': 12345, '__password': 98768}

'''
#Name mangling
#__password can be tretaedd as  ->    _Person__password
print(o1._Person__password)  
'''
