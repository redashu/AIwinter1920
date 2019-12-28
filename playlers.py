#!/usr/bin/python3

import  numpy  as np
import matplotlib.pyplot  as plt

#  now creating  data
players=["virat","rohit","dhoni","jadeja"]
runs=[1200,800,700,500]
runs1=[1300,900,1000,800]

plt.xlabel("cricket players")
plt.ylabel("score")
plt.ylim(400,1300)
plt.bar(players,runs,label="performance in 2019")
#plt.bar(players,runs1,label="performance in 2030",color='r')
plt.bar(players,runs1,label="performance in 2020")
plt.grid(color='g')
plt.legend()
plt.show()

