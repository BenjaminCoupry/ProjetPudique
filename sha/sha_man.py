'''
Toutes les notations et noms de fonctions sont ceux de la page wikipédia
de SHA-2 : https://fr.wikipedia.org/wiki/SHA-2
'''
from . import sha_pitre as sp
 

def bourrage(data):
    '''
    data : Tableau d'octets (des entiers).
    Renvoie les octets de bourrage à ajouter, calculés de la manière idoine.
    '''
    l = len(data) * 8
    if l % 512 == 0 and l != 0:
        return []
    k = (448 - l - 1) % 512
    padding = [0b10000000]
    padding += ((k-7) // 8) * [0x00]
    mask = 0xFF << 56
    for i in range(8):
        padding.append( (l & mask) >> 8 * (7-i) )
        mask >>= 8
    return padding


def build_W(block):
    '''
    Renvoie le tableau W construit à partir du bloc.
    block : Un bloc, 64 octets dans un tableau.
    '''
    W = [ block[i]*256**3 + block[i+1]*256**2 + block[i+2]*256 + block[i+3] for i in range(0, 64, 4) ]
    for t in range(16, 64):
        t1 = sp.small_sigma_1_256(W[t-2])
        t2 =  W[t-7]
        t3 =  sp.small_sigma_0_256(W[t-15])
        t4 =  W[t-16]
        sum = (t1+t2+t3+t4)% (sp.U32_MAX+1)
        W.append(sum )
    return W


def compute_intermediate_hashes(W, H):
    '''
    Calcule les hashs intermédiaires pour le W donné et le H du bloc précédent.
    Renvoie a, b, c, d, e, f, g, h sous forme de tuple
    '''
    a, b, c, d, e, f, g, h = H
    for t in range(64):
        t1 = h + sp.big_sigma_1_256(e) + sp.ch(e, f, g) + sp.K_256[t] + W[t]
        t2 = sp.big_sigma_0_256(a) + sp.maj(a, b, c)
        h, g, f, e, d, c, b, a = g, f, e, (d+t1) % (sp.U32_MAX+1), c, b, a, (t1+t2) % (sp.U32_MAX+1)
    return a, b, c, d, e, f, g, h


def sha_256_sum(data):
    '''
    Renvoie le hash SHA-256 des données (tableau d'octets)
    data : tableau d'octets (entiers).
    '''
    H = [h for h in sp.H_0]
    padded_data = data + bourrage(data)
    for i in range(len(padded_data) // 64):
        block = padded_data[i*64:(i+1)*64]
        W = build_W(block)
        intermediate_H = compute_intermediate_hashes(W, H)
        H = [ (h + ih) % (sp.U32_MAX+1) for h, ih in zip(H,intermediate_H) ]
    return [ item for subl in map(lambda h : ((0xFF000000 & h) >> 24, (0xFF0000 & h) >> 16, (0xFF00 & h) >> 8, 0xFF & h) , H ) for item in subl ]

