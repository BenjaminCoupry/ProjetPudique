

def first_decomp(n):
    d=n
    s=0
    while d%2==0:
        d=d//2
        s+=1
    return s,d

def miller_indicator(n,a):
    s,d = first_decomp(n-1)
    x=1
    for i in range(d):
        x = (x*a)%n
    if x==1 or x==n-1:
        return False
    else:
        for i in range(s-1):
            x = (x*x)%n
            if x == n-1:
                return False
    return True

def miller_test(n,k):
    for i in range(k):
        a = n-2 #random between 2 and n-2
        if miller_indicator(n,a):
            return False
    return True
