from sys import stdin
input = stdin.readline
ans = [0]*10001
for _ in range (int(input())) :
    ans[int(input())] += 1
for __ in range (10001) :     
    for i in range (int(ans[__])) :
        print(__)