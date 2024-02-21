# run time errors


'''
a=5
b=0



try:
    c=a/b
# code which raises th exception/error

except ZeroDivisionError:
    print("Division by zero is not allowed")

finally:
    print("After exception")

'''
# Name Error
'''
try:
    print( x )

except NameError:
    print("given var is not defined")

'''

# Files exceptiom
'''

y = 10
z = 0

try:
    f = open( 'newFile.txt', 'w' )
    res = y / z
    f.write( 'writing %d to file:' % res )
except ZeroDivisionError:
    print( "Division by zero is not allowed" )

finally:
    f.close()
    print( "file closed" )
'''

y = 10
z = 0

try:
    res=y/z
    print(res)
except Exception as e:
    print(e)
print("Here execution will not stop though gets error , it will catch thhe exception")

try:
    names=["aayu","pihu"]
    print(names[3])
except Exception as e:
    print(e)
print('this will excute after handling exception')
# more than 1 exception handling
try:
    print(10/0)
    names=["aayu","pihu"]
    print(names[3])
except ZeroDivisionError as e:
    print(e)
    print("enter non zero value")
except IndexError as er:
    print(er)
    print("hello")
except Exception as e:    #generic exception
    print(e)

# Day 2
# using else and finally
# using else in try..except
a = 100
try:

    b = 1
    print( type( b ) )
    c = a / b
    print( c )

except Exception as error:
    print( "Some error occured", error )
else:  # this will be exceuted if there is no exception
    print( "Code executed successfully , congrats !!! " )


# using finally
a = 100
try:

    b = 1
    print( type( b ) )
    c = a / b
    print( c )

except Exception as error:
    print( "Some error occured", error )
else:  # this will be exceuted if there is no exception
    print( "Code executed successfully , congrats !!! " )
finally:  # always get executed
    print( "This code will always get executed , irrespective of the execution status under try..except block" )
