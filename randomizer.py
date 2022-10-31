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
    seed : Entier >= 2
    """
    S.fibo_seed = seed
    for i in range(FIBO_HISTORY_LENGHT):
        S.fibo_history[i] = (seed ** (i + 2) + (i + 17)**4 * seed) % RANDOM_MAX

def get_random_fibo():
    """
    Génère et renvoie le nombre suivant à partir des précedents et de la seed,
    dans [0 ; RANDOM_MAX[ selon Fibo.
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


def random_byte():
    """
    Entier aléatoire entre 0 et 255.
    Le générateur doit déjà avoir été initialisé avec init_fibo().
    """
    result = get_random_fibo()
    while result >= 256:
        result = get_random_fibo()
    return result


def random_integer_bits(nb_bits):
    """
    Génère un nombre entier sur nb_bits bits.
    Le générateur doit déjà avoir été initialisé avec init_fibo().
    """
    result = 0
    while nb_bits >= 8:
        result <<= 8
        result |= random_byte()
        nb_bits -= 8
    if nb_bits != 0:
        result <<= nb_bits
        result |= random_byte() & (0xFF >> (8-nb_bits))  # Les nb_bits premiers bits de l'octet aléatoire
    return result


# Script de test et de démo :
import matplotlib.pyplot as plt
NB_BITS = 1000
init_fibo(42)
h = [random_integer_bits(NB_BITS) for _ in range(10000)]
print("Couverture =", len(set(h)) / 2**NB_BITS * 100, "%")
# Matlplotlib ne sait pas gérer les nombres de plus de 64 bits,
# on affiche donc seulement le 64 bits de poids fort :
plt.hist([i >> (NB_BITS - 64) for i in h])
plt.show()
