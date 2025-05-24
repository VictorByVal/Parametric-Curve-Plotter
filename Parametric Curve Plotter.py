# Library Imports 
import numpy as np 
import matplotlib.pyplot as plt 
import numpy as np # This will be used to create arrays and for functions with sin, cos and related operators and constants. 
import pandas as pd # This will be used to create a DataFrame with the values of the parametric equations.
import tkinter as tk 

## This function will create a range of numbers from start to end with a given step. it is used to plot the parametric curve with a given float step. 
def my_range(start, end, step):
    while start <= end:
        yield start
        start += step

# Functions to evaluate the parametric equations.
def f(t): 
    x = 2.3*(t-np.sin(t)) 
    return x 
def g(t): 
    y = 2.3*(1-np.cos(t)) 
    return y

# Lists to store the values of the parametric equations
x = list()
y = list()
tvalue = list() 

# Varaibles to store the limits of the plot and the step 
ilimit = -20
flimit = 20
step = .1

for t in my_range(ilimit, flimit, step): 
    tvalue.append(t) 

for value in tvalue: 
    x.append(f(value))
    y.append(g(value))

# Creating a Matrix with numpy to later use it to create a DataFrame 

values = np.array([tvalue, x, y]) 

values = np.transpose(values)

# Creating the DataFrame  
df = pd.DataFrame(values, columns=['t','f(t)', 'g(t)']) 

# Creating the Plot 
df.plot(x='f(t)', y='g(t)', grid = True, color = 'black', figsize=(15,8), xlabel='f(t)', ylabel='g(t)', title = 'Movemet of the functions f(t) arount time t')