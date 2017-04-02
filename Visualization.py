import numpy as np
import pylab as plt

#
# Shows a plot of the number of songs songs sung by each artist, provided they have alteast 2 songs.
#

#
# 
#

import pandas as pd
df=pd.read_csv("data.csv")
x = df['Artist_Name'];
from pylab import rcParams
rcParams['figure.figsize'] = 15,10 # manually adjust the size of the graph.
a=list(x.unique())
x=list(x)
print len(a)
q=[]
names=[]
for i in a:
    if(x.count(i)>1):
        q.append(x.count(i))
        names.append(i)
print len(names)
#print q
plt.ylabel("Number of songs",fontsize=15)
plt.xlabel("Artist's ID",fontsize=15)
plt.plot(q)
plt.plot([len(names), len(names)], [2, max(q)], 'k-', lw=2)

#plt.xticks(q,names)

