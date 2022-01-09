a=list(map(int,input().split()))
a = [_ **2 for _ in a]
print(sum(a)%10)