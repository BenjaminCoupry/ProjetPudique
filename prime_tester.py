from time import time
import randomizer
import random

def puissance_rapide_modulaire(b, e, m):
    r = 1
    b = b % m
    if (b == 0):
         return 0
    while (e > 0) :
        if (e % 2) :
            r = (r * b) % m
        e = e >> 1
        b = (b ** 2) % m
    return r
    

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
    if n<=3 :
        return False
    s,d = first_decomp(n-1)
    for i in range(k):
        a = randomizer.get_random_range(2,n-1)
        if miller_indicator(n,s,d,a):
            return False
    return True

def generate_prime(nb_bits):
    u=0
    found = False
    N=0
    while not found:
        N+=1
        u = randomizer.random_integer_bits(nb_bits)
        found = miller_test(u)
    return u

randomizer.init_fibo(42)
print(generate_prime(3000))

