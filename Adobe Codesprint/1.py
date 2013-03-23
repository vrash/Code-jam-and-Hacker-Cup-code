# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import sys

inputlist = []
check=0
x=0
prob=0
#inp = open ("C:\Users\PENG-LP-10\Desktop\\abc.txt","r")

for line in sys.stdin:
    for i in line.split():
        if check==0:
            p=float(i)
            check=1
        elif check==1:
            check=2
        else:
            n=float(i)
            if(n==1):
                print "%.4f" % p
            else:
               prob=(1-math.pow((1-2*p),n))/2
               print "%.4f" % prob
             
               
       
