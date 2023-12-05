from Crypto.Util.number import getPrime, inverse

p1 = getPrime(1024)
p2 = getPrime(1024)
print(f"p1 = {p1}")
print(f"p2 = {p2}")

n = p1 * p2
print(f"modulus n = {n}")

phi_n = (p1 - 1) * (p2 - 1)
print(f"Euler's totient function phi(n) = {phi_n}")

e = 65537
print(f"public exponent e = {e}")

while phi_n % e == 0:
    p1 = getPrime(1024)
    p2 = getPrime(1024)
    n = p1 * p2
    phi_n = (p1 - 1) * (p2 - 1)

d = inverse(e, phi_n)
print(f"private exponent d = {d}")

message = "Procopii Maria"
print(f"Original Message: {message}")
m = int.from_bytes(message.encode(), byteorder='big')
print(f"Converted m to ASCII = {m}")

c = pow(m, e, n)
print(f"Encrypted message = {c}")

decrypted_message = pow(c, d, n)
decrypted_message_str = decrypted_message.to_bytes((decrypted_message.bit_length() + 7) // 8, byteorder='big').decode()
print(f"Decrypted Message: {decrypted_message_str}")
