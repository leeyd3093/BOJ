a = list(input())
t = 0
for _ in a :
    t += 1
    t += (ord(_)-59)//3
    if ord(_) == 83 :
        t -= 1
    if ord(_) == 86 :
        t -= 1
    if ord(_) >= 89 :
        t -= 1
print(t)