from __future__ import division
import sys
from  decimal import *

check=0
cache={}
#inp = open('C:\\Users\\Vrashabh\\Desktop\\Contests\\inp.txt', 'r')

for line in sys.stdin.readline():
    if check==0:
        index=int(line)
        check = 1
    else:
        key = int(line)
        if key in cache:
            print cache[key]
        else:
            getcontext().rounding = ROUND_DOWN
            getcontext().prec = int(line)+1
            x = Decimal('103993')/Decimal('33102')
            print x
            cache[key] = x
                
    
