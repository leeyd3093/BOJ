a,b,c=map(int,input().split())
x=-1
if b<c:
    x=a//(c-b)+1
print(x)