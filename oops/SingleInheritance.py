# Parents class has constructor and No constructor in child class
# Child can access parent class
#MRO#   https://www.youtube.com/watch?v=oBPwPPuf6Nw&list=PLI4OVrCFuY56E57FdYzFNSWcEDS-ZKK26&index=21
'''
class Parentcls():
    def __init__(self,pnm,snm,adhNum):
        self.parName=pnm
        self.sirName=snm
        self.adharnum=adhNum

    def dispParinfo(self):
        print(f'My parents Name is : {self.parName}  {self.sirName} and adharnum is {self.adharnum}')


class Childcls(Parentcls):    #childcls inherits parentcls
       childnm= "Aayush"

       def dispChildInfo(self):
           print(f'child name is : {self.childnm} {self.parName} {self.sirName}')


# Creating Object

o1=Childcls("som","Pawar",123)

print(o1.parName)
print(o1.sirName)
o1.dispParinfo()
print(o1.childnm)
o1.dispChildInfo()


'''


# constructor in parent as well as in child

class Parentcls():
    def __init__(self,pnm,snm,adhNum):
        self.parName=pnm
        self.sirName=snm
        self.adharnum=adhNum

    def dispParinfo(self):
        print(f'My parents Name is : {self.parName}  {self.sirName} and adharnum is {self.adharnum}')


class Childcls(Parentcls):    #childcls inherits parentcls
    def __init__(self,pnm,snm,adhNum,childNm):
      super().__init__(pnm,snm,adhNum)
      self.childName = childNm



    def dispChildInfo(self):
       print( f'child name is : {self.childName} {self.parName} {self.sirName}' )

        #child cls initiats parentcls constructor args first and then own args
             #childcls first calls the parent cls construcctor which is immediately passed in the child cls


c1=Childcls("Somnath","Pawar",12345,"Aayushi")

print(c1.parName)
print(c1.sirName)
c1.dispParinfo()

print(c1.childName)
c1.dispChildInfo()


'''
Python built-in class functions
The built-in functions defined in the class are described in the following table.

SN	Function	Description
1	getattr(obj,name,default)	-> It is used to access the attribute of the object.
2	setattr(obj, name,value)	-> It is used to set a particular value to the specific attribute of an object.
3	delattr(obj, name)	-> It is used to delete a specific attribute.
4	hasattr(obj, name)	-> It returns true if the object contains some specific attribute.


# Example

class Student:  
    def __init__(self, name, id, age):  
        self.name = name  
        self.id = id  
        self.age = age  
  
    # create the object of the class Student  
s = Student("John", 101, 22)  
  
# prints the attribute name of the object s  
print(getattr(s, 'name'))  
  
# reset the value of attribute age to 23   of object s
setattr(s, "age", 23)  
  
# prints the modified value of age  
print(getattr(s, 'age'))  
  
# prints true if the student contains the attribute with name id  
  
print(hasattr(s, 'id'))  
# deletes the attribute age  
delattr(s, 'age')  
'''









