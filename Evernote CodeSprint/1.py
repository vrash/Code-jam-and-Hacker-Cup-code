#!/bin/python
import sys
import collections

#inp = open ("C:\Users\Vrashabh\Desktop\\abc.txt","r")
check=0
inputlist =[]
x=0
interlist=[]


for line in sys.stdin.readlines():
    newline=line.strip()
    if check==0:
        n=int(newline)
        check=1
    else:
        inputlist.append(newline)
      
if n==0:
    print "None"
else:  
    dq = collections.deque(maxlen=n)

while(x!=len(inputlist)):
    if (inputlist[x]== 'Q'):
        os._exit(1)
       
    elif(inputlist[x]== 'L'):
            for element in dq:
                    print element
            x=x+1
           
    else:
        appenRem,count = inputlist[x].split(' ')
        if(appenRem[0]== 'A'):
            y=x+1
            while(y!=x+int(count)+1):
                dq.append(inputlist[y])
                y=y+1
            x=x+int(count)+1
        else:
            z=1
            while(z<=int(count)):
                    dq.popleft()
                    z=z+1
            x=x+1
