# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 09:42:20 2016

@author: Kushal
"""
import time
import pandas as pd
import Rating_Predictor
from random import randint
from sklearn.metrics import accuracy_score
def feature_selector(df):
    z=0
    features={}
    x=0

    i=0;
    f1=0
    '''
    print "Printing a few examples"
    print
    print "1."
    print df.loc[(randint(0,len(df)))]
    print
    print "2."
    print df.loc[(randint(0,len(df)))]
    print
    print "3."
    print df.loc[(randint(0,len(df)))]
    '''
    df=df[(df.Title.str.find('*')==-1)]
    df=df[(df.Title.str.find('?')==-1)]
    df=df[(df.Title.str.find('(')==-1)]
    df=df.drop('Song_hotness',axis=1);
    df=df.drop('Title',axis=1)
    df=df.drop('energy',axis=1);
    df=df.drop('Danceability',axis=1);
    z=len(df)
    

    from sklearn import preprocessing
    le = preprocessing.LabelEncoder()
    le.fit(df['Artist_Name']);
    artists=le.transform(df['Artist_Name'])
    df1=pd.DataFrame()
    df1=df['Artist_Name']
    df=df.drop('Artist_Name',axis=1);
    df['Artists']=artists
    for i in df.index:
        if(pd.isnull(df.loc[i]).any()):
            df=df.drop(i)
           
    billboard_presence=df['Presence']
    df=df.drop('Presence',axis=1)
    for i in df.keys():
        features[x]=i;
        x+=1;
    i=0
    print "Number of valid songs considered for the model:",
    print len(df)
    print 
    print max(df.index)
    
    
    from sklearn.model_selection import train_test_split
    
    # 0 4 
    #8 + for presence!
    def ml_algo(i):
        X_train, X_test, y_train, y_test = train_test_split(df,billboard_presence, test_size=0.20,random_state=i)
        '''
        df_array=df.as_matrix()
        from sklearn.model_selection import StratifiedKFold
        skf = StratifiedKFold(n_splits=3)
        skf.get_n_splits(df, billboard_presence)
        X_train, X_test, y_train, y_test =0,0,0,0    
        for train_index, test_index in skf.split(df_array,billboard_presence):
           print("TRAIN:", train_index, "TEST:", test_index)
           print max(train_index)
           print max(test_index)
           X_train, X_test = df_array[train_index], df_array[test_index]
           y_train, y_test = billboard_presence[train_index], billboard_presence[test_index]
        '''
        from sklearn.dummy import DummyClassifier
        clf=DummyClassifier(random_state=i)
        clf.fit(X_train, y_train)
        y_pred=clf.predict(X_test)
        z=0
        z1=0
        y=[]
        #Printing the values for getting more insight into the accuracy score:
        for i in y_test:
            y.append(i);
        zz=0 
        for i in range(len(y)):
            if(y[i]==1):
                zz+=1
            if(y[i]==y_pred[i]):
                if(y[i]==0):
                    z+=1
                if(y[i]==1):
                    z1+=1
        test_index=max(X_test.index)
        
        print "Length of the test set:", 
        print len(y)
        print "Total number of songs present on the billboard:", 
        print zz
        print "Total number of songs present on the billboard, predicted accurately:", 
        print z1
        print z
        print "Accuracy Score = ",
        print accuracy_score(y_test, y_pred)
        
        
        print "Number of features considered for the model:", 
        print len(features)
        print 
        pred=Rating_Predictor.predictor(X_train, X_test, y_train, y_test);
        return X_test,pred
    print "1. Random_State=0"
    _,_=ml_algo(0)
    print "1. Random_State=2"
    X_test,pred=ml_algo(2)
    print "1. Random_State=4"
    _,_=ml_algo(4)
    import Result_Visualization as rv
    #pred=y_pred
    rv.visualization(X_test.index, pred)

if __name__=='__main__':
    import Features_data_creator
    df=Features_data_creator.get_all_files('E:\Udacity\Machine Learning\MillionSongSubset\data')
    df=pd.read_csv('data.csv',index_col=0)
    feature_selector(df)
