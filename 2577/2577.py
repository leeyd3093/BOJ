a = 1
a *= int(input())
a *= int(input())
a *= int(input())
n = list(str(a))
for _ in range(10) :
    print(n.count(str(_)))