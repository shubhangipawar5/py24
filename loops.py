# if - elseloop
# num = int(input("enter a number"))
# if(num >=0 ):
#     print("positive number")
# else:
#     print(f"{num} is negative")

marks = 67
if(marks > 90):
    print('Grade A')
elif(marks > 75):
    print('Grade B')
elif(marks >65):
    print('Grade C')
else:
    print('Fail .. please try again')


# FOR loop

sieName = "Pawar"
for i in sieName:
    print(i )
print("*****************")
# using range
length = len(sieName)
for item in range(length):
    print(sieName[item])





languages = ['Swift', 'Python', 'Go', 'JavaScript']

# run a loop for each item of the list
for language in languages:
    print(language)

i = 0
while(i < len( languages )):
     print(languages[i])
     i= i+1

#break
counter = 0

while counter < 3:
    # loop ends because of break
    # the else part is not executed
    if counter == 2:
        break

    print('Inside loop')
    counter = counter + 1


# program to find first 5 multiples of 6

i = 1

while i <= 10:
    print( '6 * ', (i), '=', 6 * i )

    if i >= 5:
        break

    i = i + 1

    # '''''pass acts as a placeholder. We can fill this place later on'''  //same as continue in js
sequence = ["Python", "c--", "Statement", "Placeholder"]
for value in sequence:
        if value == "Statement":
            pass  # leaving an empty if block using the pass keyword  // skip this blockk for this condition met  and continue other execution
        else:
            print( "Not reached pass keyword: ", value )











