from collections import *
py='YES';pn='NO'
l=[]

# storing all 3 digit ending number that are divisible by 8
for i in range(1000,2000,8):
    s1=Counter(str(i)[1:])
    l.append(s1)

#Special case for 1-2 digit 
ch = ['0','8','16','24','23','04','48','56','46','27','08','88','69']
for _ in range(input()):
    flag = 0
    n=raw_input()
    if len(n)<3:  #<3  
        t1 = list(n)
        t1.sort()
        for i in ch:
            b = list(i)
            if b == t1:
                print py
                flag = 1
                break
        if flag == 1:
            continue
        else:
            print pn
    else:
        string = Counter(n)    #Counter is a multiset in Python
        for i in l:
            flag = 0
            for j in i:
            #check if each possibility in l[] lies in string , i is a counter . i[j] returns count of j in i 
                if i[j]>string[j]:
                    flag = 1
                    break
            if flag == 0:
                print py
                break
        if flag == 1:
            print pn