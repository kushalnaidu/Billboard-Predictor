# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 13:57:04 2016

@author: Kushal
"""

import urllib2
from bs4 import BeautifulSoup
import pandas as pd
def billboard(songname,artist):#put parameter as song name, artist
    page=urllib2.urlopen('http://www.umdmusic.com/default.asp?Lang=English&Chart=D&ChDay=&ChMonth=&ChYear=&ChBand=&ChSong='+songname)
    soup=BeautifulSoup(page);
    all_tables=soup.find_all('table')
    i=None
    for req_table in all_tables:
        None;
    #'i' is now storing the required table in which the data is present.
    import re
    p=0
    name=re.findall(r'<td style="font-size:10pt;font-family:Arial;padding-left:0.1in"><b>'+songname+'(.*?)</td>',str(req_table))
    ranks=re.findall(r'<td align="center" style="font-size:10pt;font-family:Arial">(\d\d|\d)',str(req_table))
    chart_true=0
    for x in name:
        ans=x.strip(' ');
        
        ans=ans.strip('</b><br/>');
        if(ans!=artist.upper()):
            p+=1;
        else:
            chart_true=1
            break;
    if(chart_true==0):
        return 0,0,0;
    else:
        
        peak_position=int(ranks[p+1])
        weeks_on_billboard=int(ranks[p+2])
        print peak_position,weeks_on_billboard
        return chart_true,peak_position,weeks_on_billboard;
'''
if __name__ == "__main__":
    billboard('Hollow','Tori Kelly');
'''