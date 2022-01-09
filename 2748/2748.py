n = int(input())
a = [0] + [1]
if (n>=1) : 
    for i in range(1,n-1) :
        a[0], a[1] = a[1], sum(a)
else :
    a= [0] + [0]
print(sum(a))