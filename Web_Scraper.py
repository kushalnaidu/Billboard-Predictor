# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 13:57:04 2016

@author: Kushal
"""

import urllib2
from bs4 import BeautifulSoup
import pandas as pd
import re
def billboard(songname,artist):#put parameter as song name, artist
    songlink=re.sub('[^A-Za-z0-9 ]+','',songname)
    songlink=re.sub('[ ]+','%20', songlink)
    print "came here 1"
    page=urllib2.urlopen('http://www.umdmusic.com/default.asp?Lang=English&Chart=D&ChDay=&ChMonth=&ChYear=&ChBand=&ChSong='+songlink)
    print "came here 2"    
    soup=BeautifulSoup(page);
    print type(soup)
    all_tables=soup.find_all('table')
    req_table=None
    for req_table in all_tables:
        None;
    #'i' is now storing the required table in which the data is present.
    print "came here 2"
    p=0
    #print req_table
    name=re.findall(r'<td style="font-size:10pt;font-family:Arial;padding-left:0.1in"><b>'+songname+'(.*?)</td>',str(req_table))
    ranks=re.findall(r'<td align="center" style="font-size:10pt;font-family:Arial">(\d\d|\d)',str(req_table))
    print name, ranks
    chart_true=0
    for x in name:
        ans=x.strip(' ');
        
        ans=ans.strip('</b><br/>');
        if(ans not in artist.upper()):
            p+=1;
        else:
            chart_true=1
            break;
    print "came here 4"
    if(chart_true==0):
        return 0,0,0;
    else:
        peak_position=int(ranks[p+1])
        weeks_on_billboard=int(ranks[p+2])
        print "FOUND!!!!!!!!"
        print peak_position,weeks_on_billboard
        return chart_true,peak_position,weeks_on_billboard;

if __name__ == "__main__":
    print billboard('Out Of The Woods','TAYLOR SWIFT');
