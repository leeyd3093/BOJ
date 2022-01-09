cycle = int(0)
checkn = qusn = int(input())
while True :
    qusn = ((qusn%10)*10)+((qusn//10)+(qusn%10))%10
    cycle += 1
    if qusn==checkn : 
        break
print(cycle)