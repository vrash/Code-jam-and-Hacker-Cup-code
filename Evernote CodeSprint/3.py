from string import punctuation
from operator import itemgetter
import sys
from collections import Counter

N = 0
words = {}
#inp = open ("C:\Users\Vrashabh\Desktop\\abc.txt","r")
check=0
inputlist =[]
i=0
inc = {}

for line in sys.stdin:
#for line in inp.readlines():
    for i in line.split():
        if check==0:
            n=int(i)
            check=1
        else:
          inputlist.append(i)
          
N=int(inputlist.pop(-1))
words_gen = (word.strip(punctuation).lower() for word in inputlist)
inputlist = set(inputlist)

for a in inputlist:
    inc[a.strip(punctuation).lower()] = a

for word in words_gen:
    words[word] = words.get(word, 0) + 1

top_words = sorted(sorted(words.iteritems()), key=itemgetter(1), reverse=True)[:N]

for word, frequency in (top_words):
    print "%s" % inc[word]

