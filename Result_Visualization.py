# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 18:21:00 2017

@author: Kushal
"""

#Result visualization
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df=pd.read_csv('data.csv')
temp_df=pd.DataFrame()
def visualization(index, y_pred):
    from pylab import rcParams
    rcParams['figure.figsize'] = 15,10
    temp_df=df.Artist_Name.iloc[index]
    presence=df.Presence.iloc[index]
    x=temp_df
    unq=list(x.unique())
    x=list(x)
    names=[]
    ids=[]
    lnt=[]
    sum=0
    count=[]
    c=0
    for i in unq:
        if(x.count(i)>1):
            names.append(i)
    graph_names=[]
    ids=[]
    for j in names:
        ids=[]
        idx=temp_df.str.find(j)  
        
        for a,b in enumerate(idx):
            if(b==0):
                ids.append(a)
        c=0
        if(presence.iloc[ids].any()==1):
            lnt.append(len(ids))
            graph_names.append(j.split(' ',1)[0])
            for k in ids:
                
                if(y_pred[k]==presence.iloc[k]):
                    c+=1;
            count.append(c)
    
    fig, ax = plt.subplots()
    width = 0.35 
    ind=np.arange(len(lnt))
    rects1 = ax.bar(ind+width, count, width, color='r')
    
    rects2 = ax.bar(ind, lnt, width, color='y')
    ax.set_ylabel('No. Of Songs')
    ax.set_xlabel('Artist\'s Name')
    ax.legend((rects2[0], rects1[0]), ('Songs Sung by an Artist', 'Songs Accurately predicted'))
    ax.set_xticks(ind + width)
    ax.set_xticklabels(graph_names)
    plt.show()
    names=[]
    for i in unq:
        if(x.count(i)>2):
            names.append(i)
    ids=[]
    count=[]
    ids=[]
    lnt=[]
    for j in names:
        ids=[]
        idx=temp_df.str.find(j)  
        
        for a,b in enumerate(idx):
            if(b==0):
                ids.append(a)
        
        c=0
        lnt.append(len(ids))
        for k in ids:
            
            if(y_pred[k]==presence.iloc[k]):
                c+=1;
        count.append(c)
    ind=np.arange(len(lnt))
    fig, ax = plt.subplots()
    rects1 = ax.bar(ind+width, count, width, color='r')
    rects2 = ax.bar(ind, lnt, width, color='y') 
    ax.set_ylabel('No. Of Songs')
    ax.set_xlabel('Artist\'s ID')
    ax.legend((rects2[0], rects1[0]), ('Songs Sung by an Artist', 'Songs Accurately predicted'))
    
    width = 0.35 
    ind=np.arange(len(ids))
    
    