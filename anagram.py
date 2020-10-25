#************************************Anagrams************************************************************

import collections

while 1==1:
    s1=list(input("s1"))
    s2=list(input("s2"))
    c = collections.Counter(s2)-collections.Counter(s1)
    k1 = ''.join(c.elements())
    c1 = len(k1)
    d=0
    m=len(s1)+len(s2)
    l1=set(s1).intersection(set(s2))
    l2=len(l1)
    for i in l1:
        d=d+min(s1.count(i),s2.count(i))
    print("remove {}".format(m-2*d-c1)," characters from '"+''.join(s1)+"' and {}".format(c1)+" characters from '"+"".join(s2)+"'")
    if m-2*d==0:
        print("they are anagrams")
        break
        
#********************************************************************************************************
