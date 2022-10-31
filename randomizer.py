RANDOM_MAX = 257
FIBO_HISTORY_LENGHT = 5

class S:
    """
    Classe contenant des variables statiques puisque
    c'est le seul moyen de le faire en Python.
    """
    fibo_seed = 0
    fibo_history = FIBO_HISTORY_LENGHT * [0]  # Le plus récent à la fin


def init_fibo(seed):
    """
    seed : Entier < RANDOM_MAX et > 0
    """
    S.fibo_seed = seed
    for i in range(FIBO_HISTORY_LENGHT):
        S.fibo_history[i] = (seed ** (i + 2) + (i + 17)**4 * seed) % RANDOM_MAX

def get_random_fibo():
    """
    Génère et renvoie le nombre suivant à partir de l'actuel, dans [0 ; RANDOM_MAX[ selo Fibo.
    """
    result = 0;
    for i in range(FIBO_HISTORY_LENGHT):
        coeff = (i*S.fibo_seed + S.fibo_history[0]) % 5
        power = (i + S.fibo_seed + S.fibo_history[1] % 2) % 53
        result += coeff * S.fibo_history[i] ** power
        result %= RANDOM_MAX
    S.fibo_history.append(result)
    del S.fibo_history[0]
    return result


# Script de test et de démo :
import matplotlib.pyplot as plt
import random
init_fibo(42)
h = [get_random_fibo() for _ in range(1000000)]
n = [h.count(i) for i in range(RANDOM_MAX)]
print("Couverture =", len(set(h)) / RANDOM_MAX * 100, "%")
plt.hist(h)
plt.show()
plt.plot(n)
plt.show()
