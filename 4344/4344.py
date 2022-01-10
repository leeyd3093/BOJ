for _ in range(int(input())):
    a=list(map(int,input().split()))
    a.remove(a[0])
    count=int()
    for _ in(a):
        if _>sum(a)/len(a):
            count+=1
    print('%0.3f'%(round(count/len(a),5)*100),end="%\n")
    count=0