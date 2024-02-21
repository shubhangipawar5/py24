class Bank:
    def __init__(self,fn,ac,bal):
        self.fullname=fn
        self.account=ac
        self.balance=bal
        self.transactions=[]

        # Deposit method
    def deposit(self,amount):
        self.balance= self.balance + amount
        self.transactions.append(amount)
        return self.balance

#          withdrwal
    def withdrwal(self,amount):
        if (self.balance > amount):
            self.balance=self.balance - amount
            self.transactions.append( amount )
            return  self.balance
        else:
            print("insufficient balance")
# last 5 transactions

    def lastFiveTrans(self):
        print(self.transactions[-5:])



o1 = Bank("shubh",123,1000)
o1.deposit(100)
o1.withdrwal(50)
o1.lastFiveTrans()

o2 = Bank("aayu",234,2000)
o3 = Bank("som",387,10000)
o4 = Bank("anu",227,9000)

acList = [o1,o2,o3,o4]

for acc in acList:
    print(acc.balance)
    print(acc.fullname)
    acc.deposit(200)
    acc.withdrwal(100)
    acc.lastFiveTrans()



# import matplotlib.pyplot as plt
# print(matplotlib._get_version())     #3.7.2