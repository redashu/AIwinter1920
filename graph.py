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
plt.plot(x,y,label="numpy data view")
plt.bar(x,y,label="numpy data view in bar ")
plt.plot(x1,y1,label="numpy data view format")
plt.bar(x1,y1,label="numpy data view format in bar")
plt.legend()
plt.grid(color='g')
plt.show()

