# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 09:42:20 2016

@author: Kushal
"""
import time
import pandas as pd
def feature_selector(df):
    x=0
    features={}
    for i in df.keys():
        features[x]=i;
        x+=1;
    i=0;
    
    temp_df=pd.DataFrame();
    print len(df.keys())
    while(i<pow(len(df.keys()),len(df.keys()))):
    #for i in range(pow(len(df.keys()),len(df.keys()))):
        x=time.time()
        
        temp_df=pd.DataFrame();
        temp_df[features[i%len(df.keys())]]=df[features[i%len(df.keys())]]
        temp_df[features[(i/len(df.keys()))%len(df.keys())]]=df[features[(i/len(df.keys()))%len(df.keys())]]
        temp_df[features[(i/(len(df.keys())**2))%len(df.keys())]]=df[features[(i/(len(df.keys())**2))%len(df.keys())]]
        temp_df[features[(i/(len(df.keys())**3))%len(df.keys())]]=df[features[(i/(len(df.keys())**3))%len(df.keys())]]
        temp_df[features[(i/(len(df.keys())**4))%len(df.keys())]]=df[features[(i/(len(df.keys())**4))%len(df.keys())]]
        temp_df[features[(i/(len(df.keys())**5))%len(df.keys())]]=df[features[(i/(len(df.keys())**5))%len(df.keys())]]
        temp_df[features[(i/(len(df.keys())**6))%len(df.keys())]]=df[features[(i/(len(df.keys())**6))%len(df.keys())]]
        temp_df[features[(i/(len(df.keys())**7))%len(df.keys())]]=df[features[(i/(len(df.keys())**7))%len(df.keys())]]
        temp_df[features[(i/(len(df.keys())**8))%len(df.keys())]]=df[features[(i/(len(df.keys())**8))%len(df.keys())]]
        temp_df[features[(i/(len(df.keys())**9))%len(df.keys())]]=df[features[(i/(len(df.keys())**9))%len(df.keys())]]
        temp_df[features[(i/(len(df.keys())**10))%len(df.keys())]]=df[features[(i/(len(df.keys())**10))%len(df.keys())]]
        temp_df[features[(i/(len(df.keys())**11))%len(df.keys())]]=df[features[(i/(len(df.keys())**11))%len(df.keys())]]
        temp_df[features[(i/(len(df.keys())**12))%len(df.keys())]]=df[features[(i/(len(df.keys())**12))%len(df)]]
        temp_df[features[(i/(len(df)**13))%len(df)]]=df[features[(i/(len(df)**13))%len(df)]]
        temp_df[features[(i/(len(df)**14))%len(df)]]=df[features[(i/(len(df)**14))%len(df)]]
        temp_df[features[(i/(len(df)**15))%len(df)]]=df[features[(i/(len(df)**15))%len(df)]]
        temp_df[features[(i/(len(df)**16))%len(df)]]=df[features[(i/(len(df.keys())**16))%len(df.keys())]]
        temp_df[features[(i/(len(df.keys())**17))%len(df.keys())]]=df[features[(i/(len(df.keys())**17))%len(df.keys())]]
        temp_df[features[(i/(len(df.keys())**18))%len(df.keys())]]=df[features[(i/(len(df.keys())**18))%len(df.keys())]]
        temp_df[features[(i/(len(df.keys())**19))%len(df.keys())]]=df[features[(i/(len(df.keys())**19))%len(df.keys())]]
        temp_df[features[(i/(len(df.keys())**20))%len(df.keys())]]=df[features[(i/(len(df.keys())**20))%len(df.keys())]]
        temp_df[features[(i/(len(df.keys())**21))%len(df.keys())]]=df[features[(i/(len(df.keys())**21))%len(df.keys())]]
        temp_df[features[(i/(len(df.keys())**22))%len(df.keys())]]=df[features[(i/(len(df.keys())**22))%len(df.keys())]]
        temp_df[features[(i/(len(df.keys())**23))%len(df.keys())]]=df[features[(i/(len(df.keys())**23))%len(df.keys())]]
        print temp_df.keys()
        while((time.time()-x)<1):
           None;
        i+=1;
    
if __name__=='__main__':
    df=pd.read_csv('data.csv',index_col=0)
    feature_selector(df)
