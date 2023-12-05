import math
import random
import hashlib
from message import msg

p = 1224044258753416041925895309159625872242386338688850896477366740793360824790684832261551354504153328578363016656594486263853412477531796319224903539512461748863320425046859839113746228973809745210494074134763797075891709498375684498405313392521817549712790057198238367462015698124946175180452358837860500213174243973058911653874755655148217917757541318217574067573468475915570655852016429323173415969928516356191581557363743966176782880260098462210976044834162741
q = 1603489397753847388402709107239861521140641439606904067315297969727988048259024301634811621537441871433475648371453117878949966150611686604420553413146307951667695216668661021796431720137228520550128365952526656087056665494317359186869215087952595111010641385596091874322946498022792650415668922690339480469827022211417221680497845409207073717616323903618200962081205906037347970760478862317837460429630828061497356622645000033976182281460647486429544084982249713

class RSASignatureScheme:
    def __init__(self, p: int, q: int):
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
        return (self.e, self.n)

    def get_private_key(self):
        self.d = pow(self.e, -1, self.phi_n)
        return (self.d, self.n)

    def get_signature(self, message: str):
        hash_object = hashlib.sha3_224(message.encode())
        hex_dig = hash_object.hexdigest()
        S = pow(int(hex_dig, 16), self.d, self.n)
        return S
    
    def verify_signature(self, signature, message):
        H_1 = pow(signature, self.e, self.n)

        hash_object = hashlib.sha3_224(message.encode())
        hex_dig = hash_object.hexdigest()
        H_2 = int(hex_dig, 16) % self.n
        
        print(f"H_1 = {H_1}\n")
        print(f"H_2 = {H_2}\n")
        
        return H_1 == H_2


def main():
    print("Plaintext:")
    print(f"m = {msg}\n")

    rsa_sig = RSASignatureScheme(p, q)
    
    e, n_1 = rsa_sig.get_public_key()
    d, n_2 = rsa_sig.get_private_key()
    print(f"Public key (e, n):")
    print(f"e = {e}\n")
    print(f"n = {n_1}\n")
    print(f"Private key (d, n):")
    print(f"d = {d}\n")
    print(f"n = {n_2}\n")
    
    print("Signature:")
    sig = rsa_sig.get_signature(msg)
    print(f"S = {sig}\n")

    is_sig_valid = rsa_sig.verify_signature(sig, msg)
    print("Is signature valid?")
    print("YES" if is_sig_valid else "NO", "\n")

if __name__ == "__main__":
    main()