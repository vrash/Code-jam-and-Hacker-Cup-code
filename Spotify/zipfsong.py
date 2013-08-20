#zipfsong - Vrashabh

from __future__ import division
import sys
from operator import itemgetter
from collections import defaultdict

#inp = open ("C:\Users\slartibartfast\Desktop\\abc.txt","r")

#set the counters
counters = sys.stdin.readline().split(" ")
numberofselect = int(counters[1])

songsdict = defaultdict(list)#default dict for song list
bestsongsdict = {} #best song dict filter

#enumerate through
for x, line in enumerate(sys.stdin, start=1):
    songvalues = line.split()
    val = float(songvalues[0]) * x # val = f/z and z = 1/x => val = f*x
    bestsongsdict[songvalues[1]] = val
    songsdict[val].append(songvalues[1])

items = songsdict.items()
items.sort(key=itemgetter(0), reverse=True)
count = 0
for key, value in items:
    for element in value:
        if count < numberofselect:
            print element
            count += 1

