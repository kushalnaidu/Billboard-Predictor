# -*- coding: utf-8 -*-
"""
Created on Tue Dec 06 18:21:20 2016

@author: kusha
"""

#--> csv writing
import pandas as pd
import os
import hdf5_getters
import glob
import Web_Scraper as ws
name=[]
title=[]
presence=[]
peak=[]
weeks=[]
basedir='./'
ext='.h5'
if os.path.isfile('./Billboard.csv'):
    df=pd.read_csv("Billboard.csv",index_col=0)
else:
    df=pd.DataFrame();
    name=df['Name'].values.tolist()
    title=df['Title'].values.tolist()
    presence=df['Presence'].values.tolist()
    peak=df['peak'].values.tolist()
    weeks=df['weeks'].values.tolist()
i=0;
for root, dirs, files in os.walk(basedir):
    files = glob.glob(os.path.join(root,'*'+ext))
    for f in files :
        i+=1
        h5=hdf5_getters.open_h5_file_read(f)
        if(i>len(df)):
            artst=hdf5_getters.get_artist_name(h5)
            songnme=hdf5_getters.get_title(h5)    
            try:
                blbrdpr,blbrdpk,blbrdwk=ws.billboard(songnme,artst)
                name.append(artst)
                title.append(songnme)
                
                presence.append(blbrdpr)
                peak.append(blbrdpk)
                weeks.append(blbrdwk)
            except:
                df['Name']=name
                df['Title']=title
                df['Presence']=presence
                df['peak']=peak;
                df['weeks']=weeks;
                #GO THROUGH ALL FILES 
                df.to_csv("Billboard.csv");
                exit(0);
                