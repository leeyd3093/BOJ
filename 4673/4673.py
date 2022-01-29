a=[]
n=0
b=set(range(0,10000))
def x(args):
    n=[int(_)for _ in str(args)] 
    n=sum(n)+int(args)
    return n
for i in range(10000) :
    a.append(x(i))
print(*sorted(b-set(a)))