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
import os
import sys
import glob
import time
'''
title.append(hdf5_getters.get_title(h5))

df=pd.DataFrame(title,columns=['Title'])
print hdf5_getters.get_num_songs(h5)
'''
'''
#Creating lists to append columns in the database:
print len(hdf5_getters.get_segments_start(h5))
print len(hdf5_getters.get_segments_start(h51))
print np.mean(hdf5_getters.get_bars_confidence((h51)))
#print (hdf5_getters.get_segments_loudness_max(h51))
print np.mean(hdf5_getters.get_tatums_confidence(h5))
'''

'''
#IS NOT NECESSARY:
get_start_of_fade_out ONLY INDICATES LENGTH OF THE SONG. dOES NOTMATTER
'''






def get_all_files(basedir,ext='.h5') :
    """
    From a root directory, go through all subdirectories
    and find all files with the given extension.
    Return all absolute paths in a list.
    """
    c=0
    title=[]#get_title(h5)
    name=[]#get_artist_name`
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
    key=[]
    duration=[]
    mode=[]
    target=pd.read_csv('Billboard.csv')
    j=0
    if(not(os.path.isfile('./data.csv'))):
        for root, dirs, files in os.walk(basedir):
            files = glob.glob(os.path.join(root,'*'+ext))
            for f in files :
                h5 = hdf5_getters.open_h5_file_read(f)
                songnme=hdf5_getters.get_title(h5)
                artst=hdf5_getters.get_artist_name(h5)
                for i in range(len(target)):
                    if(target.Title[i]==songnme and target.Name[i]==artst):
                        billboard_presence.append(target.Presence[i])
                        
                        title.append(songnme)
                        name.append(artst)
                        familiarity.append(hdf5_getters.get_artist_familiarity(h5))
                        artist_hotness.append(hdf5_getters.get_artist_hotttnesss(h5))
                        song_hotness.append(hdf5_getters. get_song_hotttnesss(h5))
                        danceability.append(hdf5_getters.get_danceability(h5))
                        key.append(hdf5_getters.get_key(h5))
                        duration.append(hdf5_getters.get_duration(h5))
                        mode.append(hdf5_getters.get_mode(h5))
                        energy.append(hdf5_getters.get_energy(h5))
                        loudness.append(hdf5_getters.get_loudness(h5))
                        tempo.append(hdf5_getters.get_tempo(h5))
                        mode_confidence.append(hdf5_getters.get_mode_confidence(h5))
                        time_sig_confidence.append(hdf5_getters.get_time_signature_confidence(h5))
                        
                        no_segments.append(len(hdf5_getters.get_segments_start(h5)))
                        avg_segment_confidence.append(np.mean(hdf5_getters.get_segments_confidence(h5)))
                        avg_segment_pitches.append(np.mean(hdf5_getters.get_segments_pitches(h5)))
                        no_sections.append(len(hdf5_getters.get_sections_start(h5)))
                        avg_sections_confidence.append(np.mean(hdf5_getters.get_sections_confidence(h5)))
                        no_beats_start.append(len(hdf5_getters.get_beats_start(h5)))
                        avg_beats_confidence.append(np.mean(hdf5_getters.get_beats_confidence(h5)))
                        no_bars.append(len(hdf5_getters.get_bars_start(h5)))
                        avg_bar_confidence.append(np.mean(hdf5_getters.get_bars_confidence(h5)))
                        no_tatums_start.append(len(hdf5_getters.get_tatums_start(h5)))
                        avg_tatums_start.append(np.mean(hdf5_getters.get_tatums_confidence(h5)))
                        
                        j+=1
                        print j #prints the index number of each song, to keep track of the song being saved to the database, and to identify errors.
                        break;
                        
                h5.close()
        print "Created Arrays"             
        df=pd.DataFrame(title,columns=['Title'])
        df['Artist_Name']=name
        df['Familiarity']=familiarity
        df['Hotness']=artist_hotness
        df['Song_hotness']=song_hotness
        df['Danceability']=danceability
        df['energy']=energy
        df['loudness']=loudness
        df['tempo']=tempo
        df['mode_confidence']=mode_confidence
        df['time_sig_confidence']=time_sig_confidence
        df['no_segments']=no_segments
        df['avg_segment_confidence']=avg_segment_confidence
        df['avg_segment_pitches']=avg_segment_pitches
        df['no_sections']=no_sections
        df['avg_sections_confidence']=avg_sections_confidence
        df['no_beats_start']=no_beats_start
        df['avg_beats_confidence']=avg_beats_confidence
        df['no_bars']=no_bars
        df['avg_bar_confidence']=avg_bar_confidence
        df['no_tatums_start']=no_tatums_start
        df['avg_tatums_start']=avg_tatums_start
        df['key']=key
        df['Mode']=mode
        df['duration']=duration
        df['Presence']=billboard_presence
        print df.head()
        print billboard_presence
        df.to_csv("data.csv")
    else:
        df=pd.read_csv('data.csv',index_col=0)
        print "Number of features in the created dataset:",
        print len(df.keys())
        print
    return df
if __name__=='__main__':
    get_all_files('E:\Udacity\Machine Learning\MillionSongSubset\data')

    