from decimal import Decimal
import sys
import math

inp = open('C:\\Users\\Vrashabh\\Desktop\\inp.txt', 'r')
out = open('C:\\Users\\Vrashabh\\Desktop\\out.txt', 'w')

check =0
cache = {}
start = ()
case = 1
lengths = [2, 4, 8, 10, 14, 18, 20, 24, 30, 38, 40]
digit = [1, 4, 5, 6, 9]

def test(x):
    if(is_square(x)):
        y = math.sqrt(x)
        if(ispalindrome(x) and ispalindrome(int(y))):
            cache[x] = y
            return 1
        else:
            return 0
    return 0

def ispalindrome(x):
    z = str(x)
    l=len(z)//2  
    if (len(str(x))==1 or z[:l]==z[-l:][::-1]):  
        return 1  
    return 0  

def is_square(n):
    return math.sqrt(n).is_integer()

def checkprecondition(start,end,case):
    count = 0
    for x in range(start,end+1):
        print (x)
        print (count)
        if(len(str(x)) not in lengths and x%10 in digit):
            if(x not in cache):
                if(test(x) == 1):
                    count = count + 1
            else:
                count = count + 1
    output = "Case #"+str(case)+": "+str(count)
    print (output)
    out.writelines("%s\n" % output)


    
for line in inp.readlines():
    if check==0:
        count = line
        check = 1
    else:
        start,end = line.split()
        checkprecondition(int(start),int(end),case)
        case = case + 1
out.flush()
out.close()
inp.close()
        
                
    
