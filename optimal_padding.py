from sha import sha_man
import randomizer

RANDOM_SIZE = 9


def get_sha_bytes(x,nb_bytes):
    full = nb_bytes//32
    hashed = []
    last = x
    for _ in range(full):
        hs = sha_man.sha_256_sum(last)
        hashed += hs
        last = hs
    rest = nb_bytes%32
    hashed += sha_man.sha_256_sum(last)[0:rest]
    return hashed

def bytesxor(b1,b2):
    return [a1^a2 for a1,a2 in zip(b1,b2)]

def padd_data(message,goal_size):
    """
    message : liste d'octets <= goal_size-2-RANDOM_SIZE
    """
    hash_size = goal_size - RANDOM_SIZE
    bsize = [len(message)&0xFF00,len(message)&0xFF]
    pd_block =bsize + message + [0]*(hash_size-len(message)-2)
    rd = [randomizer.random_byte() for _ in range(RANDOM_SIZE)]
    G = get_sha_bytes(rd,hash_size)
    X = bytesxor(G,pd_block)
    H = get_sha_bytes(X,RANDOM_SIZE)
    Y = bytesxor(H,rd)
    return X+Y

def unpadd_data(padded_block):
    """
    padded_block : liste d'octets, 32 + RANDOM_SIZE octets
    """
    nX = len(padded_block)-RANDOM_SIZE
    X = padded_block[0:nX]
    Y = padded_block[nX:]
    H =  get_sha_bytes(X,RANDOM_SIZE)
    rd = bytesxor(H,Y)
    G = get_sha_bytes(rd,nX)
    block = bytesxor(X,G)
    szinfo = (block[0]<<8) + block[1]
    message = block[2:szinfo+2]
    return message

def get_max_message_bytes(goal_size):
    return goal_size-2-RANDOM_SIZE


randomizer.init_fibo(43)
message = [randomizer.random_byte() for _ in range(25)]

padded = padd_data(message,20)
depadded = unpadd_data(padded)

print(message)
print(padded)
print(depadded)

