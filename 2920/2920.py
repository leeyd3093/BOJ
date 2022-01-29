a=list(map(int,input().split()))
if a==sorted(a,reverse=1):
    print("descending")
elif a==sorted(a):
    print("ascending")
else:
    print("mixed")