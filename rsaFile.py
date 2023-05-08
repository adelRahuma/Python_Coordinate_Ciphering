import math
def rsa( num) :
    
    p = 3
    q = 7
    n = p*q
    #print("n =", n)
    phi = (p-1)*(q-1)
    e = 2
    while(e<phi):
        if (math.gcd(e, phi) == 1):
            break
        else:
            e += 1

    #print("e =", e)
    # step 5
    k = 2
    d = ((k*phi)+1)/e
    #print("d =", d)
    #print(f'Public key: {e, n}')
    #print(f'Private key: {d, n}')
    #msg = 11
    #print(f'Original message:{num}')
    C = pow(num, e)
    C = math.fmod(C, n)
    #print(f'Encrypted message: {C}')
    # decryption
    M = pow(C, d)
    M = math.fmod(M, n)
    return C
    #print(f'Decrypted message: {M}') 