from itertools import count


a = input()
print(len(a))
c = 0
for _ in range (len(a)) :
    if "c="or"c-"or"dz="or"d-"or"lj"or"nj"or"s="or"z=" in a :
        c += 1
print(c)