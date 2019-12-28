#!/usr/bin/python3

import  numpy  as np
import matplotlib.pyplot  as plt

#  now creating  data
players=["virat","rohit","dhoni","jadeja"]
runs=[1200,800,700,500]
runs1=[1300,900,1400,900]

'''
plt.xlabel("cricket players")
plt.ylabel("score")
plt.pie(runs,labels=players,autopct='%1.1f%%',explode=(0,0,0,0.2),shadow=True)
plt.legend()
plt.show()
'''
fig,ax=plt.subplots(2)
ax[0].pie(runs,labels=players,autopct='%1.1f%%',explode=(0,0,0,0.2),shadow=True)
ax[0].legend()
ax[1].pie(runs1,labels=players,autopct='%1.1f%%',explode=(0.2,0,0,0),shadow=True)
ax[1].legend()
plt.show()


