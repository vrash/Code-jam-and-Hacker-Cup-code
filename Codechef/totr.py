import sys

#inp = open('C:\\Users\\Vrashabh\\Desktop\\Contests\\inp.txt', 'r')
lang = {}
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
check =0

def getstring(string):
    a=""
    for items in list(string):
        a= a+ lang[items]
    print a
    
for line in sys.stdin:
    if check==0:
        index,string=line.split()
        lang=dict(zip(alphabet, string))
        lang.update(dict((k.upper(), v.upper()) for k,v in lang.iteritems()))
        lang['_'] = " "
        lang['!'] = "!"
        lang['.'] = "."
        lang['?'] = "?"
        lang[','] = ","
        check = 1
    else:
        getstring(line.rstrip('\n'))
                
    
