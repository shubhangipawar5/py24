# inherit multiple base classes in the child class.
'''
class Base1:
    <class-suite>

class Base2:
    <class-suite>
.
.
.
class BaseN:
    <class-suite>

class Derived(Base1, Base2, ...... BaseN):
    <class-suite>
'''


class father():
    def __init__(self,fnm,snm):
        self.fnm=fnm
        self.sirnm=snm

    def dispFatherinfo(self):
        print(f'father name is  {self.fnm} And paternal sirname is {self.sirnm}')

class mother():
    def __init__(self,mnm,matsnm):
        self.mothernm=mnm
        self.maternalsirnm=matsnm

    def dispmotherinfo(self):
        print(f'mother name is {self.mothernm} and maternal sirname is {self.maternalsirnm}')


class child(father,mother):   #left side paent will be aacessed first always
    def __init__(self,fnm,snm,mnm,matsnm,chnm):
        father.__init__(self,fnm,snm)
        mother.__init__(self,mnm,matsnm)

        self.childnm=chnm
    def dispChildInfo(self):
        print(f'child name is : {self.childnm}')



co=child("som","pawar","shubh","Bhosale","Aayu")
co.dispFatherinfo()
co.dispmotherinfo()
co.dispChildInfo()


'''OR

class FatherA():
    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName =ln

    def displayPName(self):
        print("I am from father class")
        print(self.firstName + self.lastName)

class MotherA():
    def __init__(self, fn, ln):
        self.firstName = fn
        self.lastName = ln

    def displayPName(self):
        print("I am from mother class")
        print(self.firstName + self.lastName)

class SonA(FatherA,MotherA):  #left side paent will be aacessed first always
    def __init__(self,pn, ln ,sn):
        super().__init__(pn,ln)
        self.sname = sn

    def displaySn(self):
        print(self.sname+ self.lastName)

chinmay = SonA("kanchan","deshpande","chinmay")
chinmay.displayPName()
'''


