import hashlib
import random
import math

# Provided hash
hashed_message_hex = "c28e45180241a2a03128cb71aa45dd8815378c598dbf37f4ff7edf82"
hashed_message = int(hashed_message_hex, 16)

p = 32317006071311007300153513477825163362488057133489075174588434139269806834136210002792056362640164685458556357935330816928829023080573472625273554742461245741026202527916572972862706300325263428213145766931414223654220941111348629991657478268034230553086349050635557712219187890332729569696129743856241741236237225197346402691855797767976823014625397933058015226858730761197532436467475855460715043896844940366130497697812854295958659597567051283852132784468522925504568272879113720098931873959143374175837826000278034973198552060607533234122603254684088120031105907484281003994966956119696956248629032338072839127039
g = 2

# ElGamal parameters
a = random.randint(1, p - 2)
b = pow(g, a, p)

def hash_message(message):
    # Use a secure hash function, like SHA-256 or SHA-512
    return int(hashlib.sha512(message.encode()).hexdigest(), 16)

def sign_elgamal(hashed_message, a, p, g):
    while True:
        k = random.randint(1, p - 2)
        gcd_value = math.gcd(k, p - 1)

        if gcd_value == 1:
            r = pow(g, k, p)
            s = (pow(k, -1, p - 1) * (hashed_message - a * r)) % (p - 1)
            signature = (r, s)
            return signature

def verify_elgamal(hashed_message, signature, b, p, g):
    r, s = signature

    v1 = pow(g, hashed_message, p)
    v2 = (pow(b, r, p) * pow(r, s, p)) % p

    return v1 == v2

# Sign the provided hashed message using ElGamal
elgamal_signature = sign_elgamal(hashed_message, a, p, g)
print("ElGamal Signature:", elgamal_signature)

# Verify the signature using ElGamal
is_verified = verify_elgamal(hashed_message, elgamal_signature, b, p, g)
if is_verified:
    print("ElGamal Signature is valid.")
else:
    print("ElGamal Signature is not valid.")
