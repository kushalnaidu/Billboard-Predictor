# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 11:39:04 2016

@author: Kushal
"""

 
    
def predictor(X_train, X_test, y_train, y_test):
    import pandas as pd
    #from sklearn.model_selection import train_test_split
    from sklearn.metrics import f1_score
    '''
    df=df[(df.Title.str.find('*')==-1)]
    df=df[(df.Title.str.find('?')==-1)]
    df=df[(df.Title.str.find('(')==-1)]
    for i in df.index:
        if(pd.isnull(df.loc[i]).any()):
            df=df.drop(i)
    df=df.drop('Artist_Name',axis=1);
    df=df.drop('Song_hotness',axis=1);
    
    df=df.drop('Danceability',axis=1);
    df=df.drop('energy',axis=1);
    #df = df.drop(df['*' in df.Title | '?' in df.Title | '(' in df.Title].index)
    
    #print df.head()
        
    
    df=df.drop('Title',axis=1)
    billboard_presence=df['Presence']
    
    df=df.drop('Presence',axis=1)

    #X_train, X_test, y_train, y_test = train_test_split(df,billboard_presence, test_size=0.25)
    '''
    from sklearn.naive_bayes import GaussianNB
    clf = GaussianNB()
    
    clf.fit(X_train, y_train)
    y_pred=clf.predict(X_test)
    return f1_score(y_test, y_pred)
    #print "f1 score =",
    '''
    from sklearn.ensemble import AdaBoostClassifier
    clf1=AdaBoostClassifier(base_estimator=clf)
    clf1.fit(X_train, y_train)
    y_pred=clf1.predict(X_test)
    print "f1 score =",f1_score(y_test, y_pred)
    from sklearn.svm import SVC
    clf2=SVC()
    from sklearn.ensemble import BaggingClassifier
    clf5=BaggingClassifier()
    from sklearn.neighbors import KNeighborsClassifier
    clf5=KNeighborsClassifier(n_neighbors=2,weights='distance')
    clf5.fit(X_train, y_train)
    y_pred=clf5.predict(X_test)
    print "f1score=",f1_score(y_test,y_pred)
    
    from sklearn.ensemble import BaggingClassifier
    clf6=BaggingClassifier()
    clf6.fit(X_train, y_train)
    y_pred=clf6.predict(X_test)
    print "f1score=",f1_score(y_test,y_pred)
    '''