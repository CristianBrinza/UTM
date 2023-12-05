from Crypto.Util.number import getPrime, inverse


def generate_rsa_keypair():
    p1 = getPrime(1536)
    p2 = getPrime(1536)
    n = p1 * p2
    phi_n = (p1 - 1) * (p2 - 1)

    e = 65537

    while phi_n % e == 0:
        p1 = getPrime(1536)
        p2 = getPrime(1536)
        n = p1 * p2
        phi_n = (p1 - 1) * (p2 - 1)

    d = inverse(e, phi_n)

    return n, e, d


def sign_hash_with_rsa_private_key(hashed_message, d, n):
    m = int.from_bytes(hashed_message, byteorder='big')
    signature = pow(m, d, n)

    return signature


def verify_hash_signature_with_rsa_public_key(hashed_message, signature, e, n):
    m = int.from_bytes(hashed_message, byteorder='big')
    is_verified = pow(signature, e, n) == m

    return is_verified


if __name__ == "__main__":
    n, e, d = generate_rsa_keypair()
    hash = "c28e45180241a2a03128cb71aa45dd8815378c598dbf37f4ff7edf82"
    print(f"Public modulus n = {n}")
    print(f"Public exponent e = {e}")
    print(f"Private exponent d = {d}")
    print(f"Hash of the message = {hash}")


    provided_hashed_message = bytes.fromhex(hash)
    signature = sign_hash_with_rsa_private_key(provided_hashed_message, d, n)
    print(f"Signature: {signature}")

    is_verified = verify_hash_signature_with_rsa_public_key(provided_hashed_message, signature, e, n)
    if is_verified:
        print("Signature is valid.")
    else:
        print("Signature is not valid.")
