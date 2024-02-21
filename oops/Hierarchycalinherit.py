# Hierarchycal
# Single Parent and many childrens

class Mother:
    def __init__(self,mname,mlastName):
        self.firstName = mname
        self.lastName = mlastName

    def displayMName(self):
        print(self.firstName + self.lastName)

class Son(Mother):
    def __init__(self ,mname,mlastName, sname):
        super().__init__(mname,mlastName)
        self.sname = sname

    def displaySName(self):
        print(self.sname + self.lastName)


class Daughter(Mother):
    def __init__(self, mname, mlastName, dname):
        super().__init__(mname, mlastName)
        self.dname = dname

    def displayDName(self):
        print(self.dname + self.lastName)

#kanchan = Mother("kanchan","deshpande")

chinmay = Son("kanchan","deshpande","chinmay")
gauri = Daughter("kanchan","deshpande","gauri")


print(chinmay.sname)
print(chinmay.firstName)
print(chinmay.lastName)
chinmay.displayMName()
chinmay.displaySName()

print(gauri.dname)
print(gauri.firstName)
print(gauri.lastName)
gauri.displayMName()
gauri.displayDName()