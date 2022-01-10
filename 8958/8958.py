for _ in range(int(input())):
    a = list(map(str,input()))
    b = [0]*(len(a)+1)
    for _ in range(len(a)):
        if a[_]=="O":
            b[_+1]+=1+b[_]
    print(sum(b))