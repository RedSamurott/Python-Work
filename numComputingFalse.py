import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x - np.cos(x)

x_domain = np.linspace(-1.5, 1.5, 100) # first two numbers are the domain of the functions and how much the plt will show, use any numbers for ease

plt.plot(x_domain,f(x_domain)) # blue is y=f(x)

x0 = 0 # mess around with this for each question
x1 = 1.57
x = x1
xn = 30
count = 2

while abs(f(xn)) > 10**-5 :
    xn = x - ((f(x)*(x-x0))/(f(x)-f(x0)))

    m = (f(x)-f(x0))/(x-x0)
    b = f(x) - m*x

    plt.plot(x_domain, (m*x_domain)+b, color = 'red')
    print(f"Iteration: {count}   x_{count-2} {x0}   x_{count-1} {x}   x_{count} {xn}   f(x_{count-1}) {f(x)}   f(x_{count-2}) {f(x0)}   Secant Line: {m}*x+{b}")

    if f(xn) * f(x0) < 0:
        x = xn

    elif f(xn) * f(x) < 0:
        x0 = xn
    count+=1

    
print(f'The root was found at {xn} with error {abs(f(xn))}')
plt.axhline(y=0, color = 'black')
plt.axvline(x=0, color = 'black')
plt.show()#if you want to see the secant lines generate one at a time, throw this in the loop alongside the intial declaration of the plot on line 9