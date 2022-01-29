input = input().upper()
mem_n = 0
for _ in set(input) :
    c = input.count(_)
    if mem_n<c :
        mem_n = c
        ans = _
    elif mem_n==c :
        ans="?"
print(ans)