# overloading


# class Cal:
#     def add(self ,x,y):
#         print(x+y)
#
#     def add(self,x,y,z):
#         print(x+y+z)
#
#     def add(self,x,y,z,a):
#         print(x+y+z+a)
#
# a = Cal()    #it will consider last add method only here
# a.add(12,45,4,5)



# in python scripting overloading is not possible so we use below way


class Cal:
    def add(self , a = None , b = None , c = None , d = None):
        if(a != None and b != None  and c != None and d != None):
            print(a+b+c+d)
        elif(a != None and b != None and c != None):
            print(a+b+c)
        elif(a != None and b != None):
            print(a + b)

a = Cal()
a.add(12,14,4,5)
a.add(12,14,4)
a.add(12,14)

"""
Overriding
"""

class WorldB():
    def __init__(self, city):
        self.city = city

    def loan(self):
        print("loan implemented from world")
    def save(self):
        print("save implement from world bank")

class SBI(WorldB):
    def loan(self):
        print("I am loan from SBI bank")
    def save(self):
        print("I am save from SBI bank")
    def save(self,p):
        print("I am save from SBI bank")
        print(p)

class PNB(WorldB):
    pass
    # def loan(self):
    #     print("I am loan from PNB bank")
    # def save(self):
    #     print("I am save from PNB bank")

pune  = SBI("pune")
print(pune.city)
pune.save(1)
pune.loan()


goa = PNB("goa")
goa.loan()
goa.save()
###################

class GrandFather():
    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName  = ln

    def displayName(self):
        print(self.firstName+self.lastName)
class Father(GrandFather):
    def __init__(self, fn, ln, ffn):
       super().__init__(fn,ln)
       self.fname = ffn

    def displayName(self):
        print(self.fname + self.lastName)
        super().displayName()

class Son(Father):

    def __init__(self, fn, ln, ffn,ssn):
       super().__init__(fn,ln,ffn)
       self.sname = ssn
    def displayName(self):
        print(self.sname + self.lastName)
        # super().displayName()


chinmay  = Son("manohar","deshpande","shirish","chinmay")
chinmay.displayName()
