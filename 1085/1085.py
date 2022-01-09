a = list(map(int,input().split()))
a.append(abs(a[0]-a[2]))
a.append(abs(a[1]-a[3]))
print(min(a))