t = int(input())
for i in range(t) :
    b=list(input())
    r, b = int(b[0]), b[2:]
    s = []
    for _ in b :
        print(_*r,end='')
    print()