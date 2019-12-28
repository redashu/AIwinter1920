#!/usr/bin/python3

import  numpy  as np
import matplotlib.pyplot  as plt

#  now creating  data
players=["virat","rohit","dhoni","jadeja"]
runs=[1200,800,700,500]
runs1=[1300,900,1000,800]
runs2=[1400,1900,12000,1800]


fig,ax=plt.subplots(3)
#  here subplots will give you two property
#  fig --will be for entire figure 
# ax will for individual attributes 
#  for graph1 2019
ax[0].bar(players,runs,color='g',label="2019")
ax[0].legend()
#ax[0].set_title("performance of 2019")
#  for graph2 2020
ax[1].bar(players,runs1,color='y',label="2020")
ax[1].legend()
ax[2].bar(players,runs2,color='r',label="2021")
ax[2].legend()
#ax[1].set_title("performance of 2020")
fig.suptitle("cricket performance graph")
plt.show()
