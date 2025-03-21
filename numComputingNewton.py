import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 2*(x**4) + 24*(x**3) + 61*(x**2) - 16*(x) + 1
"""
For ease of putting in each function:
1. return 2*(x**4) + 24*(x**3) + 61*(x**2) - 16*(x) + 1
2. return (x**3) + 94*(x**2) - 389*x + 294
3. return 0.5 + .25*(x**2) - x*(math.sin(x)) - 0.5*(math.cos(2*x))
4. return 230*(x**4) + 18*(x**3) + 9*(x**2) - 221*(x) - 6
"""
    
def df(x):
    return 8*(x**3) + 72*(x**2) + 122*(x) - 16
"""
For ease of putting in each function:
1. return 8*(x**3) + 72*(x**2) + 122*(x) - 16
2. return 3*(x**2) + 188*x - 389
3. return 0.5*x + math.sin(2*x) - x*(math.cos(x)) - math.sin(x)
4. return 920*(x**3) + 54*(x**2) + 18*(x) - 221
"""

x_domain = np.linspace(-1, 1, 100) # first two numbers are the domain of the functions and how much the plt will show, use any numbers for ease
"""
For best results when showing graphs for each problem given, reminder that there is a zoom in feature to see the tangent lines:
1. x_domain = np.linspace(-1, 1, 100)
2. x_domain = np.linspace(0, 5, 100)
3. x_domain = np.linspace(-5, 5, 100)
4. x_domain = np.linspace(-1, 1, 100)
"""
plt.plot(x_domain,f(x_domain),x_domain,df(x_domain)) # blue is y=f(x), orange is y=f'(x)

x0 = 0.1 # mess around with this for each question
x = x0
xn = 30
count = 1

while abs(f(xn)) > 10**-5 :
    xn = x - (f(x)/df(x))

    plt.plot(x_domain, df(x)*(x-x_domain)+f(x), color = 'red')
    print(f"Iteration: {count}   x_{count-1} {x}   x_{count} {xn}   f(x_{count-1}) {f(x)}   f'(x_{count-1}) {df(x)} Tangent Line: {df(x)}*(x-{x})+{f(x)}")
    x = xn
    count += 1

    
print(f'The root was found at {x} with error {abs(f(x))}')
plt.axhline(y=0, color = 'black')
plt.axvline(x=0, color = 'black')
plt.show()#if you want to see the tangent lines generate one at a time, throw this in the loop alongside the intial declaration of the plot on line 32