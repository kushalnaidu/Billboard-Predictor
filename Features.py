# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 12:56:24 2016

@author: Kushal
"""
'''
GET SEGMENTS TIMBRE IS 2d FIX IT!'''
import Web_Scraper as ws
import pandas as pd
import hdf5_getters
import numpy as np
f='TRAXLZU12903D05F94.h5'
f1='TRAAADZ128F9348C2E.h5'
h5 = hdf5_getters.open_h5_file_read(f)
h51=hdf5_getters.open_h5_file_read(f1)
'''
title.append(hdf5_getters.get_title(h5))

df=pd.DataFrame(title,columns=['Title'])
print hdf5_getters.get_num_songs(h5)
'''

#Creating lists to append columns in the database:

title=[]
familiarity=[]#get_artist_familiarity()
artist_hotness=[]#get_artist_hotttnesss
print len(hdf5_getters.get_segments_start(h5))
name=[]#get_artist_name
print len(hdf5_getters.get_segments_start(h51))
print np.mean(hdf5_getters.get_bars_confidence((h51)))
#print (hdf5_getters.get_segments_loudness_max(h51))
print np.mean(hdf5_getters.get_tatums_confidence(h5))
name=[]#get_artist_name`
title=[]#get_title()
familiarity=[]#get_artist_familiarity()
artist_hotness=[]#get_artist_hotttnesss
song_hotness=[]# get_song_hotttnesss
danceability=[]#get_danceability
energy=[]#get_energy
loudness=[]#get_loudness
tempo=[]#get_tempo
mode_confidence=[]#get_mode_confidence()
time_sig_confidence=[]#get_time_signature_confidence()
no_segments=[]#len(get_segments_start())
avg_segment_confidence=[]#np.mean(hdf5_getters.get_segments_confidence(h5))
avg_segment_pitches=[]#np.mean(hdf5_getters.get_segments_pitches(h51))
no_sections=[]#len(hdf5_getters.get_sections_start())
avg_sections_confidence=[]#np.mean(hdf5_getters.get_sections_confidence(h51))
no_beats_start=[]#len(hdf5_getters.get_beats_start(h51))
avg_beats_confidence=[]#np.mean(hdf5_getters.get_beats_confidence(h51))
no_bars=[]#len(hdf5_getters.get_bars_start(h5))
avg_bar_confidence=[]#np.mean(hdf5_getters.get_bars_confidence((h51))
no_tatums_start=[]#len(hdf5_getters.get_tatums_start(h5))
avg_tatums_start=[]#np.mean(get_tatums_confidence())
billboard_presence=[]#returned value from web scraper
#MAY NOT BE NECESSARY
end_of_fade_in=[]# get_end_of_fade_in
key_confidence=[]#get_key_confidence
mode_confidence=[]#get_mode_confidence
time_signature_confidence=[]#get_time_signature_confidence
'''
#IS NOT NECESSARY:
get_start_of_fade_out ONLY INDICATES LENGTH OF THE SONG. dOES NOTMATTER
'''