RANDOM_MAX = 257
FIBO_HISTORY_LENGHT = 10

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
        result += (coeff * S.fibo_history[i] ** power) + S.fibo_history[2] + 3
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


def random_odd_bits(nb_bits):
    """
    Génère une nombre impair sur nb_bits.
    Le générateur doit déjà avoir été initialisé avec init_fibo().
    """
    result = 2 * random_integer_bits(nb_bits - 1) + 1
    while result >= 2 ** nb_bits:
        result = 2 * random_integer_bits(nb_bits - 1) + 1
    return result



def nb_bits_for_range(n):
    """
    Renvoie le nombre de bits nécessaires pour écrire n nombre différents.
    En gros c'est (int) log2(n) + 1 mais à mains nues.
    """
    nb_bits = 1
    limit = 2
    limit2 = limit * limit
    while limit2 <= n:
        nb_bits *= 2
        limit = limit2
        limit2 = limit * limit
    while limit < n:
        nb_bits += 1
        limit *= 2
    return nb_bits


def get_random_range(a,b):
    """
    Entier aléatoire : a inclus, b exclu. b > a.
    """
    size = b - a
    nb_bits = nb_bits_for_range(size)
    rand = random_integer_bits(nb_bits)
    while rand >= size:
        rand = random_integer_bits(nb_bits)
    return a + rand
