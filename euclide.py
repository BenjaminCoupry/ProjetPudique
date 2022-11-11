
def init_vars(a,b):
    r1 = b
    r2 = a
    u1 = 0
    v1 = 1
    u2 = 1
    v2 = 0
    return r1,r2,u1,v1,u2,v2

def extended_euclide(a,b):
    r1,r2,u1,v1,u2,v2 = init_vars(a,b)
    while r2 !=0:
        q = r1//r2
        r1,u1,v1,r2,u2,v2 = r2,u2,v2,r1-q*r2,u1-q*u2,v1-q*v2
    return r1,u1,v1