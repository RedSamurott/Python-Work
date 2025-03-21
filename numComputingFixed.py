import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return (x**3) - 3*x + 3 # change function as needed
"""
For ease of putting in each function:
1. return (x**3) - 6*(x**2) + 10*x - 4
2. return (x**3) - 2.4*x + 2.4
3. return (x**3) - 2.9*x + 2.9
4. return (x**3) - 3*x + 3
"""

def df(x):
    return 3*(x**2) - 3 # change derivative of function as needed
"""
For ease of putting in each function:
1. return 3*(x**2) - 12*x + 10
2. return 3*(x**2) - 2.4
3. return 3*(x**2) - 2.9
4. return 3*(x**2) - 3
"""

x = np.linspace(-1, 3, 100) # first two numbers are the domain of the functions and how much the plt will show, use any numbers for ease
"""
For best results when showing graphs for each problem given, reminder that there is a zoom in feature to see the convergence lines:
1. x = np.linspace(-1, 5, 100)
2. x = np.linspace(-1, 3, 100)
3. x = np.linspace(-1, 3, 100)
4. x = np.linspace(-1, 3, 100)
"""
plt.plot(x,x,x,f(x),x,df(x)) # blue is y=x, orange is y=f(x), green is y=f'(x)

xplot = np.ndarray(3)
yplot = np.ndarray(3)

x0 = 1.1
count = 1

while count <= 50: #mess with this value to go for lower/higher iterations
    xold = x0
    xplot[0] = x0
    yplot[0] = x0
    xplot[1] = x0
    yplot[1] = f(x0)
    xn = f(x0)
    xplot[2] = xn
    yplot[2] = xn
    x0 = xn

    plt.plot(xplot,yplot, color = 'red')

    print(f"Iteration: {count}   x_{count-1} {xold}   x_{count} {xn}   f(x_{count}) {f(xn)}   f'(x_{count}) {df(xn)}")
    
    count += 1


plt.axhline(y=0, color = 'black')
plt.axvline(x=0, color = 'black')
plt.show() #if you want to see the convergence lines generate one at a time, throw this in the loop alongside the intial declaration of the plot on line 32