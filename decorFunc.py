'''DECORATORS
'''

def decor(func):
    def inner():
        result = func()
        return result*2
    return inner


'''way1 to connect with decorator function'''
def num():
    return 5
resultfunc=decor(num)
print(resultfunc())

'''way2
use of special character '@decoratorfunction name
'''

@decor
def num():
    return 25
print(num())