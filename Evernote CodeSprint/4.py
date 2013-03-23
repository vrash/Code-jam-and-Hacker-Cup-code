import sys
import heapq

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
          inputlist.append(int(i))
          
topn = heapq.nlargest(4, inputlist)
for a in topn:
    print "%d" %a

