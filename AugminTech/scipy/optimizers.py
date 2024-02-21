from scipy.optimize import root
from math import cos
from scipy.optimize import minimize

# find root of an x+cos(X)


def eqn(x):
    return x + cos(x)
myroot=root(eqn,0)
print(myroot)





