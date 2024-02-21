from abc import ABC, abstractmethod
# Abstract class worldBank
class world(ABC):

    @abstractmethod
    def loanRoi(self):
        pass

    @abstractmethod
    def save(self):
        pass


# we can't make an object of abstract class
# Child classes  below which inherits parents abstarct class
# child class should always implement rules/metods of abstract class

class sbi(world):

    def loanRoi(self):
        print("ROI is 9%")

    def save(self):
        print("I am save from SBI")

class icici(world):

    def loanRoi(self):
        print( "ROI is 10%" )

    def save(self):
        print("I am save from ICICI")

    def myOwnMethod(self):
        print("I am from my own Method")

s1 = sbi()
s1.loanRoi()
s1.save()

I1 = icici()
I1.loanRoi()
I1.save()
I1.myOwnMethod()


