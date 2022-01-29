i=int
a=input()
if int(a)<100:
    print(a)
else:
    q=99
    for _ in range(100,int(a)+1):
        c=str(_)
        if(i(c[1])-i(c[0])==i(c[2])-i(c[1])):
            q+=1
    print(q)