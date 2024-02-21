#Pickle - is a built in module used to serialize the files


class  myclass:
    def __init__(self,id,name,marks):
        self.id=id
        self.name=name
        self.marks=marks


    def display(self):
        print("my name is : " + "" + self.name)