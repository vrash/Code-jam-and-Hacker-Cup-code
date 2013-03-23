#Vrashabh Irde- GCJ 2012
#Prints to both File and STDOUT
#For use the paths to the input\output file need to be changed as required

import string

inputlist = []
a=[]
answerset=[]
# Input file has to be in C drive
inp = open ("C:\\Users\\peng-lp-10\\Desktop\\GCJ 2012\\A-small-attempt0.in","r")
outputfile = open ("C:\\Users\\peng-lp-10\\Desktop\\GCJ 2012\\A-small-attempt.out","w")
check =0
count =0
numberoflett = 0
answerset1=[]

def translateit(inputlist,count):
    rotrandom = string.maketrans(
    "abcdefghijklmnopqrstuvwxyz",
    "yhesocvxduiglbkrztnwjpfmaq")
    a=' '.join(inputlist)
    answer = string.translate(a, rotrandom)
    stringer = "Case #"+str(count)+":"
    stringer = stringer + " "+answer.translate(None,"'")
    answerset.append(stringer)

#read line into array 
for line in inp.readlines():
    inputlist = []
    for i in line.split():
        if check!=0:
            inputlist.append(i)
        else:
            index=int(i)
            check=1
    if check!=0 and inputlist:
        count=count+1
        translateit(inputlist,count)
        
for item in answerset:
   outputfile.writelines("%s\n" % item)
print answerset
outputfile.flush()
outputfile.close
inp.close
