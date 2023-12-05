import hashlib
import math
from random import randint
from message import msg

p = 32317006071311007300153513477825163362488057133489075174588434139269806834136210002792056362640164685458556357935330816928829023080573472625273554742461245741026202527916572972862706300325263428213145766931414223654220941111348629991657478268034230553086349050635557712219187890332729569696129743856241741236237225197346402691855797767976823014625397933058015226858730761197532436467475855460715043896844940366130497697812854295958659597567051283852132784468522925504568272879113720098931873959143374175837826000278034973198552060607533234122603254684088120031105907484281003994966956119696956248629032338072839127039
alpha = 2

class ElGamalSignatureScheme:
    def __init__(self, p, alpha):
        self.p = p
        self.alpha = alpha

    def gen_keys(self):
        k_pr = randint(2, self.p - 2)
        beta = pow(self.alpha, k_pr, self.p)

        self.k_pub = (self.p, self.alpha, beta) # private key
        self.k_pr = k_pr

        return {"pub_key": self.k_pub, "pr_key": self.k_pr}
    
    def get_signature(self, message: str):
        k_E = 0

        while True:
            x = randint(2, self.p - 2)
            if math.gcd(x, self.p - 1) == 1:
                k_E = x
                break
        
        r = pow(self.alpha, k_E, self.p)
        k_E_inv = pow(k_E, -1, self.p - 1)

        hash_object = hashlib.sha512(message.encode())
        hex_dig = hash_object.hexdigest()

        S = (k_E_inv * (int(hex_dig, 16) - self.k_pr * r)) % (self.p - 1)
        
        return (r, S)

    def verify_signature(self, signature, pub_key, message):
        p, local_alpha, beta = pub_key
        r, S = signature
        if not (1 <= r and r <= p - 1):
            return False
        v_1 = (pow(beta, r, p) * pow(r, S, p)) % p

        hash_object = hashlib.sha512(message.encode())
        hex_dig = hash_object.hexdigest()
        v_2 = pow(local_alpha, int(hex_dig, 16), p)

        print(f"v_1 = {v_1}\n")
        print(f"v_2 = {v_2}\n")        
        
        return v_1 == v_2

def main():
    print("Plaintext:")
    print(f"m = {msg}\n")

    elg_sig = ElGamalSignatureScheme(p, alpha)
    
    keys = elg_sig.gen_keys()
    local_p, local_alpha, beta = keys['pub_key']
    print(f"Public key (p, α, β):")
    print(f"p = {local_p}\n")
    print(f"α = {local_alpha}\n")
    print(f"β = {beta}\n")
    print(f"Private key (d):")
    print(f"d = {keys['pr_key']}\n")
    
    print("Signature:")
    r, sig = elg_sig.get_signature(msg)
    print(f"r = {r}\n")
    print(f"s = {sig}\n")

    is_sig_valid = elg_sig.verify_signature((r, sig), keys['pub_key'], msg)
    print("Is signature valid?")
    print("YES" if is_sig_valid else "NO", "\n")

if __name__ == "__main__":
    main()
