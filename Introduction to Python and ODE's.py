#!/usr/bin/env python
# coding: utf-8

# In[6]:


#This Jupyter Notebook serves as an introduction to Python and Solving ODE's Numerically for new research students. 
#For any readers with extensive experience with either, a more rigorous notebook would likely be more useful. 
#Welcome new students! There is quite a lot of work for you to be doing, and no doubt there is a lot that has you a little bit worried. 
#If this document does its job then we should quiet a few of those fears by the end. 
#For this code we will be walking through the very first of the problems found in "The Structure of White Dwarf and Neutron Stars."
#A module by David G. Robertson that was provided by Dr. Nielson. 
#We will use the Euler Method of Approximation as detailed by that document. 

#When starting to code in Python, it is important to recognize a few things. First, a line that begins with a # is a comment!
#This means that the code will ignore the rest of the line when it runs.
#It is a good idea to leave comments when you feel it is necessary to explain what a code is doing. 

#When beginning a code, you first need to import some libraries. These come with prepackaged code that you can reference and use.
#This allows you to use complicated functions without being required to figure out how to write the code yourself. 
#It is important to do this first so that we can make use of these libraries throughout our code. Python compiles line by line,
#which results in us only being able to reference backwards when we need to do reference other parts of our code. 
import math
import numpy as np
import matplotlib.pyplot as plt

#The reason we imported some code with "as '_____'" written after them will become clearer as we continue. 

#getting Python to output text recquires a simple print command
print("Hello World!")
print("Exercise 1 using Euler's Method")

x = np.linspace(0, 4, 100)
y = np.exp(-1/2*x**2)
plt.plot(x,y)


#In order to create functions in python, we use a "def" command and then give it a name. 
def Eulergraph(input1, input2):
    Xvalues = []
    Yvalues = []
    Y0 = input1
    x = 0
    Yvalues.append(Y0)
    Xvalues.append(x)
    e = input2
    while x < 3:
        x = x+e
        Y = Y0 - e*x*Y0
        Y0 = Y
        Yvalues.append(Y0)
        Xvalues.append(x)
        
    plt.plot(Xvalues, Yvalues)
    

Eulergraph(1,1)

Eulergraph(1,.5)
    
Eulergraph(1,.1)


# In[ ]:




