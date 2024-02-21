#a file where we store an organized data

#syntax of open file
#f=open('fileNmae','mode')
#w - mode - write mode- everytime it writes with new contents
#r - read mode
# a - append to file with previous contents
# x - exclusive file creation mode, if it is not available it will create new otherwise refres same available file to read it


#binary file
#rb-read binary
#wb- write binary
#ab=append binary


'''   WRITE FILE
f=open('myfile.txt','w')   #if file is not available it will create new file
content = input('enter text:')
f.write(content)
f.close()

'''

"""    READ FILE
f=open('myfile.txt','r') 

res=f.read()
# f.readline()   #to read single line
# f.readlines()   #to read all the file contents
f.close()
 """

"""APPEND in A FILE 
f=open('appendMyfile.txt','a')
content = input('enter text:')
f.write('\n')
f.write(content)
f.close()
"""


"""write multiple lines in a file

f=open('multiLineFile.txt','w')
print('enter text and press # when u are done')
s=''
while s!= '#':
    s = input()
    f.write('\n')
    f.write(s)
f.close()

"""


""" COPY content of 1 file to other file /// red from 1 file and writ to other file

f1=open('appendMyfile.txt','r')
f2=open('copytofile.txt','w')
for i in f1:
    f2.write(i)
"""

"""CHECK file is existing or Not
1.import OS module


import os

try:
    if os.path.isfile('copytofile.txt'):
        f=open('copytofile.txt','w')
        f.write('file is copied')
except:
    print('file does not exist')

"""




















