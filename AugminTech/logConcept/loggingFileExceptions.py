import logging

logging.basicConfig(filename='file1.log',level=logging.ERROR)
f=open('myfile2.txt','w')
try:
    a=5
    b=0
    logging.info('Devision is in progress')
    c=a/b
    f.write('writing %d to file'%c)
except ZeroDivisionError:
    print('Devision by zero is not allowed')
    print('enter non zero number')
    logging.error('Devision by zero')   #will log logs into file1.log

finally:
    f.close()

