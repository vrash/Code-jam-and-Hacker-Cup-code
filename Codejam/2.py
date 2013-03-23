#Vrashabh Irde- GCJ 2012
#Prints to both File and STDOUT
#For use the paths to the input\output file need to be changed as required

import string
import math

# Input file has to be in C drive
inp = open ("C:\\Users\\peng-lp-10\\Desktop\\GCJ 2012\\B-large.in","r")
outputfile = open ("C:\\Users\\peng-lp-10\\Desktop\\GCJ 2012\\B-large-attempt.out","w")
data=[]
inputlist=[]
case=0
people=0
surprise=0
minimum=0
scores=[]
check=0
answerset=[]

def findcases(inputlist,case,people,surprise,minimum,scores):
    answer=0
    noofcases=0
    for a_score in scores:
        basecase = (int)(a_score/3)
        scoremod=a_score%3
        inter1=[]
        inter2=[]
        inter=[]
        if(scoremod==0):
            if(basecase>=minimum):
                noofcases=noofcases+1
            else:
                if(surprise>0 and basecase>0 and basecase+1>=minimum):
                    noofcases=noofcases+1
                    surprise=surprise-1
                 
        elif(scoremod==1):
            if(basecase>=minimum or basecase+1>=minimum):
                noofcases=noofcases+1
            else:
                if(surprise>0 and basecase+1>=minimum):
                    noofcases=noofcases+1
                    surprise=surprise-1
        elif(scoremod==2):
            if(basecase>=minimum or basecase+1>=minimum):
                noofcases=noofcases+1
            else:
                if(surprise>0 and basecase+2>=minimum):
                    noofcases=noofcases+1
                    surprise=surprise-1    
    stringer = "Case #"+str(case)+":"
    stringer = stringer + " "+str(noofcases)
    answerset.append(stringer)

#read line into array 
for line in inp.readlines():
    inputlist = []
    for i in line.split():
        if check!=0:
            inputlist.append((int)(i))
        else:
            index=int(i)
            check=1
    if check!=0 and inputlist:
        case=case+1
        people = inputlist[0]
        surprise=inputlist[1]
        minimum=inputlist[2]
        x = 3
        i=3
        scores=[]
        while(i<(x+people)):
            scores.append(inputlist[i])
            i=i+1
        findcases(inputlist,case,people,surprise,minimum,scores)
        
for item in answerset:
   outputfile.writelines("%s\n" % item)
outputfile.flush()
outputfile.close
inp.close
