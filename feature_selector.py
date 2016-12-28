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
    print df.keys();
    
    i=0;
    f1=0
    arr=df.keys();
    temp_df=pd.DataFrame();
    df=df[(df.Title.str.find('*')==-1)]
    df=df[(df.Title.str.find('?')==-1)]
    df=df[(df.Title.str.find('(')==-1)]
    for i in df.index:
        if(pd.isnull(df.loc[i]).any()):
            df=df.drop(i)
    df=df.drop('Song_hotness',axis=1);
    
    billboard_presence=df['Presence']
    df=df.drop('Danceability',axis=1);
    df=df.drop('energy',axis=1);
    df=df.drop('Presence',axis=1)
    df=df.drop('Title',axis=1)
    from sklearn import preprocessing
    le = preprocessing.LabelEncoder()
    le.fit(df['Artist_Name']);
    artists=le.transform(df['Artist_Name'])
    
    df=df.drop('Artist_Name',axis=1);
    df['Artists']=artists
    print artists
    for i in df.keys():
        features[x]=i;
        x+=1;
    i=0
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(df,billboard_presence, test_size=0.25,random_state=12)
    #print len(df.keys())
    i=0
    X_tr=pd.DataFrame()
    X_te=pd.DataFrame()
    '''
    while(i<pow(len(features),len(features))):
        #for i in range(pow(len(df.keys()),len(df.keys()))):
        temp_df=pd.DataFrame();
        X_tr=pd.DataFrame()
        X_te=pd.DataFrame()
        
        for j in range(len(features)):
            X_tr[features[(i/(len(features)**j))%len(features)]]=X_train[features[(i/(len(features)**j))%len(features)]]
            X_te[features[(i/(len(features)**j))%len(features)]]=X_test[features[(i/(len(features)**j))%len(features)]]
            #temp_df[features[(i/(len(features)**j)%len(features))]]=df[features[(i/(len(features)**j))%len(features)]]
        print X_tr.keys()
        z=Rating_Predictor.predictor(X_tr, X_te, y_train, y_test);
        print z
        if(z>f1):
            f1=z;
            arr=X_tr.keys()
        i+=1
    '''
    x=time.time()
    print x
    from sklearn.model_selection import train_test_split
    for i1 in range(len(features)):
        for i2 in range(i1+1,len(features)):
            for i3 in range(i2+1,len(features)):
                for i4 in range(i3+1,len(features)):
                    for i5 in range(i4+1,len(features)):
                        for i6 in range(i5+1,len(features)):
                            for i7 in range(i6,len(features)):
                                for i8 in range(i7+1,len(features)):
                                    for i9 in range(i8,len(features)):
                                        for i10 in range(i9,len(features)):
                                            for i11 in range(i10+1,len(features)):
                                                for i12 in range(i11,len(features)):
                                                    for i13 in range(i12,len(features)):
                                                        for i14 in range(i13,len(features)):
                                                            for i15 in range(i14,len(features)):
                                                                for i16 in range(i15,len(features)):
                                                                    for i17 in range(i16,len(features)):
                                                            
                                                                        X_tr=pd.DataFrame()
                                                                        X_te=pd.DataFrame()
                                                                        X_tr[features[i1]]=X_train[features[i1]]
                                                                        X_tr[features[i2]]=X_train[features[i2]]
                                                                        X_tr[features[i3]]=X_train[features[i3]]
                                                                        X_tr[features[i4]]=X_train[features[i4]]
                                                                        X_tr[features[i5]]=X_train[features[i5]]
                                                                        X_tr[features[i6]]=X_train[features[i6]]
                                                                        X_tr[features[i7]]=X_train[features[i7]]
                                                                        X_tr[features[i8]]=X_train[features[i8]]
                                                                        X_tr[features[i9]]=X_train[features[i9]]
                                                                        X_tr[features[i10]]=X_train[features[i10]]
                                                                        X_tr[features[i11]]=X_train[features[i11]]
                                                                        X_tr[features[i12]]=X_train[features[i12]]
                                                                        X_tr[features[i13]]=X_train[features[i13]]
                                                                        X_tr[features[i14]]=X_train[features[i14]]
                                                                        X_tr[features[i15]]=X_train[features[i15]]
                                                                        X_tr[features[i16]]=X_train[features[i16]]
                                                                        X_tr[features[i17]]=X_train[features[i17]]
                                                                        
                                                                        
                                                                        X_te[features[i1]]=X_test[features[i1]]
                                                                        X_te[features[i2]]=X_test[features[i2]]
                                                                        X_te[features[i3]]=X_test[features[i3]]
                                                                        X_te[features[i4]]=X_test[features[i4]]
                                                                        X_te[features[i5]]=X_test[features[i5]]
                                                                        X_te[features[i6]]=X_test[features[i6]]
                                                                        X_te[features[i7]]=X_test[features[i7]]
                                                                        X_te[features[i8]]=X_test[features[i8]]
                                                                        X_te[features[i9]]=X_test[features[i9]]
                                                                        X_te[features[i10]]=X_test[features[i10]]
                                                                        X_te[features[i11]]=X_test[features[i11]]
                                                                        X_te[features[i12]]=X_test[features[i12]]
                                                                        X_te[features[i13]]=X_test[features[i13]]
                                                                        X_te[features[i14]]=X_test[features[i14]]
                                                                        X_te[features[i15]]=X_test[features[i15]]
                                                                        X_te[features[i16]]=X_test[features[i16]]
                                                                        X_te[features[i17]]=X_test[features[i17]]
                                                                        z=Rating_Predictor.predictor(X_tr, X_te, y_train, y_test);
                                                                        
                                                                        if(z>f1):
                                                                            f1=z;
                                                                            arr=X_tr.keys()
                                                                            print "z=",z
                                        print i1
                                        print time.time()-x
    
    print "IMPORTANT FEATURES : ", arr
    print "F1 SCORE = ", f1
if __name__=='__main__':
    import Features_data_creator
    df=Features_data_creator.get_all_files('E:\Udacity\Machine Learning\MillionSongSubset\data')
    df=pd.read_csv('data.csv',index_col=0)
    feature_selector(df)
