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
import sys
import Web_Scraper as ws
name=[]
title=[]
presence=[]
peak=[]
weeks=[]
basedir='..\MillionSongSubset\data'
ext='.h5'
if os.path.isfile('./Billboard.csv'):
    df=pd.read_csv("Billboard.csv",index_col=0)
    name=df['Name'].values.tolist()
    title=df['Title'].values.tolist()
    presence=df['Presence'].values.tolist()
    peak=df['peak'].values.tolist()
    weeks=df['weeks'].values.tolist()
else:
    df=pd.DataFrame();
i=0;
for root, dirs, files in os.walk(basedir):
    files = glob.glob(os.path.join(root,'*'+ext))
    for f in files :
        
        i+=1
        if (i>9000 and i%50==0):
            df=pd.DataFrame();
            df['Name']=name
            df['Title']=title
            df['Presence']=presence
            df['peak']=peak;
            df['weeks']=weeks;
            #GO THROUGH ALL FILES 
            df.to_csv("Billboard.csv");
            print "created file"
            print i
            
        h5=hdf5_getters.open_h5_file_read(f)
        
        artst=hdf5_getters.get_artist_name(h5)
        songnme=hdf5_getters.get_title(h5)
        
        h5.close()
        if((artst in name) and (songnme in title)):
            None;
        else:
            print songnme
            print artst
            try:
                if('*' in songnme or '?' in songnme or '(' in songnme):
                    blbrdpr=0;
                    blbrdpk=0;
                    blbrdwk=0;
                else:
                    blbrdpr,blbrdpk,blbrdwk=ws.billboard(songnme,artst)
                name.append(artst)
                title.append(songnme)
                presence.append(blbrdpr)
                peak.append(blbrdpk)
                weeks.append(blbrdwk)
            except:
                print "Error thrown, Writing to file and ending abruptly. Please rerun the script to continue saving data."
                print "Error thrown, Writing to file and ending abruptly. Please rerun the script to continue saving data."
                df=pd.DataFrame();
                df['Name']=name
                df['Title']=title
                df['Presence']=presence
                df['peak']=peak;
                df['weeks']=weeks;
                #GO THROUGH ALL FILES 
                df.to_csv("Billboard.csv");
                print "created file"
                sys.exit();
                print "should exit"

df=pd.DataFrame();
df['Name']=name
df['Title']=title
df['Presence']=presence
df['peak']=peak;
df['weeks']=weeks;
#GO THROUGH ALL FILES 
df.to_csv("Billboard.csv");
print "created file"
sys.exit();
print "should exit"               