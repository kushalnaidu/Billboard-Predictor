# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 11:39:04 2016

@author: Kushal
"""

 
    
def predictor(X_train, X_test, y_train, y_test):
    from sklearn import svm
    from sklearn.model_selection import GridSearchCV
    from sklearn.metrics import accuracy_score
    from sklearn.ensemble import AdaBoostClassifier
    from sklearn.naive_bayes import GaussianNB
    
    clf1=GaussianNB()
    
    abc=AdaBoostClassifier(clf1)
    
    parameters={ 'n_estimators':range(10,50),'learning_rate':(0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1)}
    clf = GridSearchCV(abc, parameters)
    clf.fit(X_train, y_train)
    y_pred=clf.predict(X_test)
    
    print "The optimal parameters which yielded the best results are: ",
    print clf.best_params_
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
    print "Length of the test set:", 
    print len(y)
    print "Total number of songs present on the billboard:", 
    print zz
    print "Total number of songs present on the billboard, predicted accurately:", 
    print z1
    print 
    print "Accuracy Score = ",
    print accuracy_score(y_test, y_pred)
    