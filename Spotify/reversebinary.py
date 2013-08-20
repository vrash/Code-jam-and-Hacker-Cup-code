#Reversebinary - Vrashabh
import sys
import heapq

#inp = open ("C:\Users\slartibartfast\Desktop\\abc.txt","r")

for line in sys.stdin:
#for line in inp.readlines():
    print int(bin(int(line))[:1:-1], 2) #
