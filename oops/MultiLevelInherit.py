# Multi-level inheritance

'''

class class1:
    <class-suite>
class class2(class1):
    <class suite>
class class3(class2):
    <class suite>
'''

class grandfather:
      def __init__(self,gfnm,snm):
          self.gfname=gfnm
          self.sirname=snm

       
      def displayGfInfo(self):
          print(f'My grandfather name i s: {self.gfname}  {self.sirname}')
          
class fater(grandfather):
    
      def __init__(self,gfnm,snm,fnm):
          super().__init__(gfnm,snm)
          self.fathernm=fnm


      def dispfatherInfo(self):
          print(f'my father name is : {self.fathernm}  {self.sirname}')


class child(fater):
    def __init__(self,gfnm,snm,fnm,chNm):
        super().__init__(gfnm,snm,fnm)
        self.childNm=chNm

    def displayChildInfo(self):
        print(f'chiuld name is :  {self.childNm}  {self.fathernm}   {self.sirname}')


c1=child("chhaya","Pawar","Somnath","Aayush")

print(c1.sirname)
print(c1.gfname)
print(c1.fathernm)
print(c1.childNm)
c1.displayGfInfo()
c1.dispfatherInfo()
c1.displayChildInfo()
