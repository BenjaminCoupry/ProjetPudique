'''
Toutes les notations et noms de fonctions sont ceux de la page wikipédia
de SHA-2 : https://fr.wikipedia.org/wiki/SHA-2
'''
import sha_pitre as sp
 

def bourrage(data):
    '''
    data : Tableau d'octets (des entiers).
    Renvoie les octets de bourrage à ajouter, calculés de la manière idoine.
    '''
    l = len(data) * 8
    if l % 512 == 0 and l != 0:
        return []
    k = (448 - l - 1) % 512
    padding = [0b1000000]
    padding += ((k-7) // 8) * [0x00]
    mask = 0xFF << 56
    for i in range(8):
        padding.append( (l & mask) >> 8 * (7-i) )
        mask >>= 8
    return padding
