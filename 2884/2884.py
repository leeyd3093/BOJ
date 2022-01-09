a, b = map(int,input().split())
if b < 45 :
    a, b = a-1, b+15
    if a < 0 :
        a += 24 
else :
    b -= 45
print(a, b)