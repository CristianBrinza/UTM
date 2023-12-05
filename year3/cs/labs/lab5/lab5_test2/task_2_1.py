import math
import random

p = 560990425683049460916176277141816812094501381196269188639598220864499843982602591733517991401108350010235620685784602426919921463588790038130754558747388243459541741303980844537737995445176315205591934449056069159763973464292782268430269522289332855003358383430084901430925268327174740097780183229036929269158041
q = 598661283959070371094692740368970904385496940873920609271673815489517322507843171439835483784589681827046079473318141319633731978693338489842047319746942677796136389359291205418179874710892967509804688654060645708185735747158070174302159594643383087617257674621703987184208448033248957652269461489146544655934383

class RSA:
    def __init__(self, p, q):
        self.p = p
        self.q = q

    def get_public_key(self):
        n = self.p * self.q
        e = 1
        phi_n = (self.p - 1)*(self.q - 1)

        while True:
            x = random.randint(1, phi_n - 1)
            if math.gcd(x, phi_n) == 1:
                e = x
                break

        self.n = n
        self.e = e
        self.phi_n = phi_n
        
        return (n, e)

    def get_private_key(self):
        self.d = pow(self.e, -1, self.phi_n)
        return (self.n, self.d)

    def encrypt(self, message):        
        plaintext_numbers = [ord(char) for char in message]
        ciphertext = [pow(x, self.e, self.n) for x in plaintext_numbers]
        return ciphertext
    
    def decrypt(self, ciphertext):        
        plaintext_numbers = [pow(y, self.d, self.n) for y in ciphertext]
        plaintext = ''.join(chr(num) for num in plaintext_numbers)
        return plaintext


def main():
    m = "Cojocari-Goncear Maxim"
    print("Plaintext:")
    print(f"m = {m}\n")

    rsa = RSA(p, q)
    
    k_pub = rsa.get_public_key()
    k_pr = rsa.get_private_key()
    print(f"Public key (n, e):\n{k_pub}\n")
    print(f"Private key (n, d):\n{k_pr}\n")
    
    print("Ciphertext:")
    c = rsa.encrypt(m)
    print(f"c = {c}\n")

    print("Deciphered c:")
    c_dec = rsa.decrypt(c)
    print(c_dec, "\n")

if __name__ == "__main__":
    main()