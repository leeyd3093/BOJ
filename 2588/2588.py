def triple(x,a,b,c):
    x_ = int(a+b+c)
    print(int(x)*x_)
x,y,z = input()
a,b,c = input()
triple(c,x,y,z)
triple(b,x,y,z)
triple(a,x,y,z)
triple(a+b+c,x,y,z)