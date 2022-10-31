RANDOM_MAX = 1009

fibo_seed = 0
fibo_a = 0
fibo_b = 0
fibo_c = 0

def init_fibo(seed):
    """
    seed : Entier < RANDOM_MAX et > 0
    """
    global fibo_a
    global fibo_b
    global fibo_c
    global fibo_seed
    fibo_seed = seed
    fibo_a = seed
    fibo_b = (seed * 45 + 517) % seed
    fibo_c = (seed * 87 + 341) % (seed + 3)


def get_random_fibo():
    """
    Génère et renvoie le nombre suivant à partir de l'actuel, dans [0 ; RANDOM_MAX[ selo Fibo.
    """
    global fibo_a
    global fibo_b
    global fibo_c
    global fibo_seed
    fibo_a, fibo_b, fibo_c = fibo_b, fibo_c, ((fibo_seed+3) * fibo_a**3 + ((fibo_seed+2)**2) * fibo_b**2 + ((fibo_seed+1)**3 + 5) * fibo_c) % RANDOM_MAX
    return fibo_b

