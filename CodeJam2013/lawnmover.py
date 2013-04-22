import re
import sys

#inp = open('C:\\Users\\Vrashabh\\Desktop\\inp.txt', 'r')
#out = open('C:\\Users\\Vrashabh\\Desktop\\out.txt', 'w')

def lawncheck(lawn):
    maxrow = [max(x) for x in lawn]
    columns = [[lawn[i][j] for i in range(len(lawn))] for j in range(len(lawn[0]))]
    maxcol = [max(x) for x in columns]
    for i in range(len(lawn)):
        for j in range(len(lawn[i])):
            val = lawn[i][j]
            if val != maxrow[i] and val != maxcol[j]:
                return "NO"
    return "YES"
        
def read_matrix(f):
    splitVal = re.split(" ",f.readline())
    x,y = int(splitVal[1]), int(splitVal[0])    
    l = []
    for i in range(y):
        line = f.readline()
        dimension = [int(x.strip()) for x in re.split(" ",line)]
        l.append(dimension)
    return l

def main():
    output = []
    with open("C:\\Users\\Vrashabh\\Desktop\\inp.txt","r") as inputFile:
        getValues = inputFile.readline()
        for i in range(int(getValues.strip())):
            currentLawnState = read_matrix(inputFile)
            outlist = "Case #%d: %s" % (i+1, lawncheck(currentLawnState))
            output.append(outlist)
    with open("C:\\Users\\Vrashabh\\Desktop\\out.txt","w") as outputFile:
        outputFile.write("\n".join(output))
main()        

