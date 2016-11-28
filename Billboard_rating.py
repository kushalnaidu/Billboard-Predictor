# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 13:22:29 2016

@author: Kushal
"""

import Web_Scraper as ws
import pandas as pd
import hdf5_getters
import numpy as np
f="TRAXLZU12903D05F94.h5"
'''
h5=hdf5_getters.open_h5_file_read(f)
print h5
print h5.root.metadata.songs.cols.title[0]'''

import os
import glob
import re
import hdf5_getters
def get_all_titles(basedir,ext='.h5') :
    for root, dirs, files in os.walk(basedir):
        files = glob.glob(os.path.join(root,'*'+ext))
        for f in files:
            h5 = hdf5_getters.open_h5_file_read(f)
            title=(hdf5_getters.get_title(h5))
            title=re.sub('[^A-Za-z0-9 ]+','', title)
            
            name=hdf5_getters.get_artist_name(h5)
            h5.close()
            x,_,_=ws.billboard(title,name)
            print title,x;

songs=get_all_titles("..\MillionSongSubset\data")
