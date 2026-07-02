import math 
import numpy as np
import matplotlib.pyplot as plt

#cost function
def f(x):
    return 3*x**2 - 4*x + 5
print(f(9))
xs=np.arange(-5,5,0.25)
ys=f(xs)
print(ys)
(plt.plot(xs,ys))
#plt.show()
h=0.01
x=3.0
#this is the derivative of the function f(x) at x=3.0 means how mych function is changing when we twick the x value it is derivative slope 
#the sign tells the diection where we are movving in a grapg by twicking the x value 
#DIVIDEBY H IOS DELL X NUMERATOR IS CHANGE IN Y BUT HOW MUCH AND WWRT TO WHOME DENOMINATOR TELL THAT 
print((f(x+h)-f(x))/h)
a=2
b=-3
c=10
h=0.01 
d=a*b+c
d1=(a+h)*b+c
print((d1-d)/h)