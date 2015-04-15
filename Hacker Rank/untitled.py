#!/bin/python
import sys

#inp = open ("C:\Users\Vrashabh\Desktop\\abc.txt","r")
check=0
inputlist =[]
x=0
interlist=[]

def productOfList(num_list, index=0, value=1):
    if index == len(num_list):
        return value
    return productOfList(num_list, index+1, value*num_list[index])


for line in sys.stdin:
#for line in inp.readlines():
    for i in line.split():
        if check==0:
            n=int(i)
            check=1
        else:
          inputlist.append(int(i))

m=sum(1 for z in inputlist if z)
prod=productOfList(inputlist)

if ((prod == 0) and (n-m) >= 2):
    while(x!=n):
        print 0
        x=x+1

elif ((prod == 0) and (n-m) == 1):
    if n==1:
        print 0
    else:
        
        while(x!=n):
            if(inputlist[x]==0):
                interlist=list(inputlist)
                interlist.pop(x)
                print productOfList(interlist)
            else:
                print 0
            x=x+1

else:
    while(x!=n):
        print prod/inputlist[x]
        x=x+1