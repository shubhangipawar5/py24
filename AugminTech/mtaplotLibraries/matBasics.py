import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
'''
x=np.array([1,7])
y=np.array([2,10])

# plt.plot(x,y)
plt.plot(x,y,'*')    #star is a marker point, it will not draw a line only * will be shown
plt.show()
'''
'''
xp=np.array([1,7,5,9,3])
yp=np.array([2,10,7,4,8])
plt.plot(yp)
plt.show()
'''

# Matplotlib Markers
# yp=np.array([1,2,3,4,5])
# plt.plot(yp,marker='o')
# plt.show()


# variations of colors and markers
'''
yp=np.array([1,2,3,4,5])
plt.plot(yp,'or')  #'o is marker of 'r' red color\
plt.plot(yp,'*k')
plt.plot(yp,'og')
plt.plot(yp,'+c')
plt.plot(yp,'-r')
plt.show()
'''

# change the size of markers
'''
x1=np.array([3,5,6,7,6])
# plt.plot(x1,marker='*',ms=25.5)
#ms is a marker size
plt.plot(x1,marker='*',mec='r')     #edge color-outline
#plot with line
plt.plot(x1,marker='*',mfc='g',ms=10)   #fase color -inner color

plt.show()

'''


'''change line style

x2=np.array([3,6,1,7,5])
# plt.plot(x2,ls='--')
plt.plot(x2,ls='dotted')
plt.show()
# plt.plot(x2,linestyle='--')

'''


'''line color

x2=np.array([3,6,2,7,5])

# plt.plot(x2,ls='dotted',color='r')
# plt.plot(x2,ls='dotted',color='m')


# https://redketchup.io/color-picker
plt.plot(x2,ls='dotted',color='#FF6F00')
plt.show()
'''


'''line width


x2=np.array([3,6,2,7,5])
plt.plot(x2,marker='o',color='r',lw=10,mec='k',mfc='m',ls='--')    #lw is line width->thicker line will show  , k is a black coor
plt.show()

'''


'''Ploting multiple lines


x3=np.array([1,4,2,6])
y3=np.array([3,7,4,9])
x4=np.array([1,9,2,3])
y4=np.array([8,7,2,9])

plt.plot(x3,y3,x4,y4,marker='o',mec='r')
plt.show()

'''

'''  labeling

x3=np.array([1,4,2,6])
y3=np.array([3,7,4,9])
font1={'family':'serif','color':'red','size':20}
font2={'family':'serif','color':'blue','size':20}
font3={'family':'serif','color':'m','size':25}
plt.xlabel('sales',fontdict=font1)
plt.ylabel('products',fontdict=font2)
# plt.title('inventory')   #centered location of titlte
plt.title( 'inventory' ,loc='left',fontdict=font3)     #left title location
plt.plot(x3,y3)
plt.show()

'''