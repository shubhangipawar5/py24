'''  Using Assertion you can give any description of error which you want \/ try and catch already custom error msg are provided


num=int(input('enter an Even number'))

assert num%2 ==0, "You have entered an odd Number"
print("Entered number is: " , num)
print("After Assertion"

'''


#Handle assertion Error

try:
    num = int( input( 'enter an Even number' ) )

    assert num % 2 == 0, "You have entered an odd or an invalid Number"
    print( "Entered number is: ", num )
except AssertionError as msg:
    print(msg)


# Raise an User defined exceptions

a=-1
if a<0:
    raise Exception('Number is less than zero')
else:
    print("valid number")



'''
def cal_age(year_born):
    current_year = 2023
    if current_year<year_born:
        raise Exception("Invalid  year of birth")
    else:
        age = current_year - year_born
        print(age)
cal_age(2030)

try:        
    cal_age(2090)
except:
    print("Invalid  year of birth")
'''







