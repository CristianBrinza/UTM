from hashlib import sha256
from random import randint

p = 32317006071311007300153513477825163362488057133489075174588434139269806834136210002792056362640164685458556357935330816928829023080573472625273554742461245741026202527916572972862706300325263428213145766931414223654220941111348629991657478268034230553086349050635557712219187890332729569696129743856241741236237225197346402691855797767976823014625397933058015226858730761197532436467475855460715043896844940366130497697812854295958659597567051283852132784468522925504568272879113720098931873959143374175837826000278034973198552060607533234122603254684088120031105907484281003994966956119696956248629032338072839127039
alpha = 2

# Diffie-Hellman Key Exchange
class DHKE:
    def __init__(self, p, alpha):
        self.p = p
        self.alpha = alpha

    def gen_private_key(self):
        self.k_pr = randint(2, self.p - 2)
        return self.k_pr
    
    def gen_public_key(self):
        return pow(self.alpha, self.k_pr, self.p)
    
    def get_joint_key(self, k_pub_shared):
        self.k_joint = pow(k_pub_shared, self.k_pr, self.p)
        return self.k_joint

def get_hashed_key(key: int):
    byte_length = (key.bit_length() + 7) // 8  # Calculate the required number of bytes
    shared_secret_bytes = key.to_bytes(byte_length, byteorder='big')
    return sha256(shared_secret_bytes).hexdigest()

def main():
    alice = DHKE(p, alpha)
    bob = DHKE(p, alpha)

    print("Alice")
    print(f"Private key:\n{alice.gen_private_key()}")
    k_pub_alice = alice.gen_public_key()
    print(f"Public key:\n{k_pub_alice}\n")

    print("Bob")
    print(f"Private key:\n{bob.gen_private_key()}")
    k_pub_bob = bob.gen_public_key()
    print(f"Public key:\n{k_pub_bob}\n")

    print("Joint key (256 bit, hashed)")
    print(f"Alice:\t{get_hashed_key(alice.get_joint_key(k_pub_bob))}")
    print(f"Bob:\t{get_hashed_key(bob.get_joint_key(k_pub_alice))}")

if __name__ == "__main__":
    main()
