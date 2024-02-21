import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# %matplotlib inline   #pip install matplotlib-inline

import warnings
warnings.filterwarnings('ignore')
'''
GRID

xp=np.array([80,85,90,95,100])
yp=np.array([10,15,20,25,30])
plt.plot(xp,yp)
plt.grid()
# plt.grid(color='red',ls='dotted',lw=1)    #customizing grids

# plt.grid(axis='x')    #only x axis grids
# plt.grid(axis='y')    #only y axis grids
plt.show()

'''


'''  multiple plots using subplots

# Way-1
x=np.array([0,1,2,3,4])
y=np.array([2,7,3,1,10])
plt.subplot(1,2,1)   #1 row, 2 colms,  plot no-1
plt.plot(x,y)



x=np.array([9,4,5,3,4])
y=np.array([2,7,3,1,10])
plt.subplot(1,2,2)
plt.plot(x,y)

plt.show()


# way 2 -> functional Methods

x=np.linspace(0,5,11)
y=x**2
# print(x)
# print(y)
plt.subplot(1,2,1)

plt.plot(x,y)
plt.title('Inventory')
plt.xlabel('sales')
plt.ylabel('Product')
x=np.array([9,4,5,3,4])
y=np.array([2,7,3,1,10])
plt.subplot(1,2,2)
plt.plot(x,y)
plt.show()
'''

# way 3-  OOP Method
'''
fig=plt.figure()
# # print(fig)      #object is created for  fig
# x=np.linspace(0,5,11)
# y=x**2
# axes=fig.add_axes([0.1,0.1,0.8,0.8])   #L,W,B,H
# axes.plot(x,y)
# axes.set_label('x axis')
# axes.set_ylabel('y axis')
# axes.title('Main title')
# # print(fig)

fig=plt.figure()
x=np.linspace(0,5,11)
y=x**2
axes1=fig.add_axes([0.1,0.1,0.8,0.8])
axes2=fig.add_axes([0.2,0.5,0.4,0.3])
#L,W,B,H
axes1.plot(x,y)
axes2.plot(x,y)          #axes2.plot(y,x)  also try it
plt.show()
'''

''' PIE CHART
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.axis('equal')
langs = ['C', 'C++', 'Java', 'Python', 'PHP']
students = [23,17,35,29,12]
ax.pie(students, labels = langs,autopct='%1.2f%%')
plt.show()
'''



'''Types of charts'''

'''BAR PLOT

x=np.array(['A','B','C','D','E'])
y=np.array([10,20,30,40,29])

plt.bar(x,y,color='m',width=0.2)
# plt.barh(x,y)              #only for horizontal bar graph
plt.show()

'''

'''Histograph   =->only vertically shown

x=np.random.normal([100,120,170,200])
plt.hist(x)
'''

'''Pie charts
x=np.array([10,20,56,78,67])

colorLabls=['Red','Blue','Green','Yellow','Pink']   #labeling with colors
plt.pie(x,startangle=90,labels=colorLabls,colors=colorLabls,autopct='%1f%%')  #autopct-> to convert into percentage
plt.legend(title="my colors")    #legends-> to show which thing is assigned with what color

'''

'''Scattered charts


x=np.array([9,4,5,3,4])
y=np.array([2,7,3,1,10])

plt.scatter(x,y,color='r',cmap='autumn')
plt.colorbar()
'''
                                                                    