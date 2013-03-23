#Vrashabh Irde- Facebook Hacker Cup 2013 Problem 1-problem1.TXT- Text Format
#Prints to both File and STDOUT
#For use, the paths to the input\output file need to be changed as required

from collections import Counter
import operator

check=0
count=0
abc={}
beautysum=1
case_count =1

# Input file has to be in C drive
inp = open ("C:\Users\pradeep\Desktop\Facebook Hacker Cup\\abcd.txt","r")
outputfile = open ("C:\Users\pradeep\Desktop\Facebook Hacker Cup\\fboutput1.txt","w")

def calc_beauty(abc,case_count):
    beauty_count = 27
    runningsum = 0
    for k, v in sorted(abc.iteritems(), key=operator.itemgetter(1), reverse=True):
        beauty_count=beauty_count-1
        beautysum=(beauty_count)*v
        runningsum=runningsum+beautysum
    outputfile.writelines("Case #%d: %d\n" % (case_count,runningsum))
    
for line in inp.readlines():
    if check!=0:
        abc = Counter(c for c in line.rstrip('\n').upper() if c.isalpha())
        calc_beauty(abc,case_count)
        case_count = case_count +1
    else:
        count=int(line)
        check=1
        
outputfile.close()
inp.close()


