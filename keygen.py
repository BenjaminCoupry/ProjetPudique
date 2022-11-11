import prime_tester
import euclide
import randomizer

def generate_coprime(f):
    e = randomizer.get_random_range(0,f)
    while euclide.extended_euclide(e,f)[0] != 1:
        e = randomizer.get_random_range(0,f)
    return e

def generate_key(nb_bits):
    p = prime_tester.generate_prime(nb_bits//2)
    q = prime_tester.generate_prime(nb_bits//2)
    while q==p:
        q = prime_tester.generate_prime(nb_bits//2)
    n = p*q
    phi = (p-1)*(q-1)
    e = generate_coprime(phi)
    d = euclide.extended_euclide(e,phi)[1]
    return (n,e),(n,d)