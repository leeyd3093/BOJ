import sys
n = int(sys.stdin.readline())
a = [int(sys.stdin.readline()) for i in range (n)]
a.sort()
for i in a :
    print(i)