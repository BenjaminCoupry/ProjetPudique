import prime_tester
import euclide
import randomizer

def generate_coprime(f):
    '''
    random number < f and prime with f
    '''
    e = randomizer.get_random_range(0,f)
    while euclide.extended_euclide(e,f)[0] != 1:
        e = randomizer.get_random_range(0,f)
    return e

def generate_prime_combination(nb_bits):
    '''
    genere n et phi aleatoires avec n mesurant environ nb_bits
    '''
    p = prime_tester.generate_prime(nb_bits//2)
    q = prime_tester.generate_prime(nb_bits//2)
    while q==p:
        q = prime_tester.generate_prime(nb_bits//2)
    n = p*q
    phi = (p-1)*(q-1)
    return n,phi

def generate_key(nb_bits, nb_bits_min):
    '''
    genere une clef entre nb_bits_min et nb_bits
    format clef chiffrement / dechiffrement
    '''
    pad = 2**nb_bits_min
    n,phi = generate_prime_combination(nb_bits)
    while n < pad:
        n,phi = generate_prime_combination(nb_bits)
    e = generate_coprime(phi)
    d = euclide.extended_euclide(e,phi)[1]
    return (n,e),(n,d)