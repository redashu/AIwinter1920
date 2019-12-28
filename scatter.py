#!/usr/bin/python3

import  numpy  as np
import matplotlib.pyplot  as plt

#  now creating  data
x=np.arange(0,100,5)
x1=np.arange(0,100,4)
y=[i for i in  range(len(x))]
y1=[i for i in  range(len(x1))]

plt.xlabel("random x")
plt.ylabel("random y")
plt.xlim(0,100)  #  here we are setting the limit of x and y axis numbers
plt.ylim(0,30)
plt.scatter(x,y,label="normal way",marker="x")
plt.scatter(x1,y1,label="danger way",marker="^",s=500)
plt.legend()
plt.grid(color='g')
plt.show()

