from random import randint

p = 32317006071311007300153513477825163362488057133489075174588434139269806834136210002792056362640164685458556357935330816928829023080573472625273554742461245741026202527916572972862706300325263428213145766931414223654220941111348629991657478268034230553086349050635557712219187890332729569696129743856241741236237225197346402691855797767976823014625397933058015226858730761197532436467475855460715043896844940366130497697812854295958659597567051283852132784468522925504568272879113720098931873959143374175837826000278034973198552060607533234122603254684088120031105907484281003994966956119696956248629032338072839127039
alpha = 2

class ElGamal:
    def __init__(self, p, alpha):
        self.p = p
        self.alpha = alpha

    def generate_key(self):
        k_pr = randint(2, self.p - 2)
        k_pub = pow(self.alpha, k_pr, self.p)

        self.d = k_pr
        self.beta = k_pub

        return (p, self.alpha, k_pub)
    
    def encrypt(self, message):
        i = randint(2, self.p - 2)
        k_E = pow(self.alpha, i, self.p)
        k_M = pow(self.beta, i, self.p)
        
        plaintext_numbers = [ord(char) for char in message]
        ciphertext = [(x * k_M) % p for x in plaintext_numbers]
        
        return (k_E, ciphertext)

    def decrypt(self, k_E, ciphertext):
        k_M = pow(k_E, self.d, self.p)
        k_M_inverse = pow(k_M, -1, self.p)
        
        plaintext_numbers = [(y * k_M_inverse) % self.p for y in ciphertext]
        plaintext = ''.join(chr(num) for num in plaintext_numbers)
        
        return plaintext

def main():
    m = "Cojocari-Goncear Maxim"
    print("Plaintext:")
    print(f"m = {m}\n")

    elg = ElGamal(p, alpha)
    
    k_pub = elg.generate_key()
    print(f"Public key (p, α, β):\n{k_pub}\n")
    
    print("Ciphertext (k_E, y):")
    c = elg.encrypt(m)
    print(f"c = {c}\n")

    k_E, y = c
    print("Deciphered c:")
    c_dec = elg.decrypt(k_E, y)
    print(c_dec, "\n")

if __name__ == "__main__":
    main()
