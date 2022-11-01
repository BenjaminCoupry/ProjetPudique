import randomizer

def puissance_rapide_modulaire(x,n,m):
    xm = x%m
    k=xm
    while n>1:
        k2 = (k*k)%m
        if n%2==0:
            k = k2
            n = n//2
        else:
            k = (xm*k2)%m
            n= (n-1)//2
    return k
    

def first_decomp(n):
    d=n
    s=0
    while d%2==0:
        d=d//2
        s+=1
    return s,d

def miller_indicator(n,s,d,a):
    x=puissance_rapide_modulaire(a,d,n)
    if x==1 or x==n-1:
        return False
    else:
        for i in range(s-1):
            x = ((x%n)*(x%n))%n
            if x == n-1:
                return False
    return True

def miller_test(n,k=25):
    s,d = first_decomp(n-1)
    for i in range(k):
        a = randomizer.get_random_range(2,n-1)
        if miller_indicator(n,s,d,a):
            return False
    return True

randomizer.init_fibo(42)
for i in range(1000):
    u=randomizer.random_integer_bits(10)
    print(miller_test(u))
print(u)