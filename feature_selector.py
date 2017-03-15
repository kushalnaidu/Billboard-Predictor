# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 09:42:20 2016

@author: Kushal
"""
import time
import pandas as pd
import Rating_Predictor
def feature_selector(df):
    z=0
    features={}
    x=0

    i=0;
    f1=0
    
    df=df[(df.Title.str.find('*')==-1)]
    df=df[(df.Title.str.find('?')==-1)]
    df=df[(df.Title.str.find('(')==-1)]
    df=df.drop('Song_hotness',axis=1);
    df=df.drop('Title',axis=1)
    z=len(df)
    for i in df.index:
        if(pd.isnull(df.loc[i]).any()):
            df=df.drop(i)

    from sklearn import preprocessing
    le = preprocessing.LabelEncoder()
    le.fit(df['Artist_Name']);
    artists=le.transform(df['Artist_Name'])
    
    
    df=df.drop('Artist_Name',axis=1);
    df['Artists']=artists
    
    billboard_presence=df['Presence']
    df=df.drop('Presence',axis=1)
    for i in df.keys():
        features[x]=i;
        x+=1;
    i=0
    print "Number of valid songs considered for the model:",
    print len(df)
    print 
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(df,billboard_presence, test_size=0.20,random_state=2)
    
    print "Number of features considered for the model:", 
    print len(features)
    print 
    x=time.time()
    z=Rating_Predictor.predictor(X_train, X_test, y_train, y_test);

if __name__=='__main__':
    import Features_data_creator
    df=Features_data_creator.get_all_files('E:\Udacity\Machine Learning\MillionSongSubset\data')
    df=pd.read_csv('data.csv',index_col=0)
    feature_selector(df)
