import hashlib

# Constants
PC1 = [i - 1 for i in [
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7,
    56, 48, 40, 32, 24, 16, 8, 0,
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6
]]

PC2 = [i - 1 for i in [
    13, 16, 10, 23, 0, 4,
    2, 27, 14, 5, 20, 9,
    22, 18, 11, 3, 25, 7,
    15, 6, 26, 19, 12, 1,
    40, 51, 30, 36, 46, 54,
    29, 39, 50, 44, 32, 47,
    43, 48, 38, 55, 33, 52,
    45, 41, 49, 35, 28, 31
]]

SHIFT = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]


def hash_string_to_64bit_key(s):
    """Hashes string to 64-bit key"""
    return int(hashlib.sha256(s.encode()).hexdigest()[:16], 16)


def apply_permutation(input_bits, permutation):
    return [input_bits[x] for x in permutation]


def left_shift(bits, n):
    return bits[n:] + bits[:n]


def generate_round_keys(key_64bit, PC1, SHIFT, PC2):
    key_bits = [int(bit) for bit in format(key_64bit, '064b')]
    print(f"\nInitial 64-bit Key in Binary: {''.join(map(str, key_bits))}")

    key_56bit = apply_permutation(key_bits, PC1)
    C, D = key_56bit[:28], key_56bit[28:]
    round_keys = []

    for i in range(len(SHIFT)):
        C, D = left_shift(C, SHIFT[i]), left_shift(D, SHIFT[i])
        combined = C + D
        round_key = apply_permutation(combined, PC2)
        round_keys.append(round_key)

        print(f"\nRound {i + 1} Keys Generation:")
        print(f"C{i + 1}: {''.join(map(str, C))}")
        print(f"D{i + 1}: {''.join(map(str, D))}")
        print(f"K{i + 1}: {''.join(map(str, round_key))}")

    return round_keys


def main():
    user_input = input("Enter a text to generate a 64-bit DES key: ")
    key_64bit = hash_string_to_64bit_key(user_input)
    print(f"\nGenerated 64-bit DES key in Hex: {key_64bit:016X}")

    round_keys = generate_round_keys(key_64bit, PC1, SHIFT, PC2)

    print("\nGenerated Round Keys:")
    for i, round_key in enumerate(round_keys):
        print(f"Round {i + 1} key: {''.join(map(str, round_key))}")


if __name__ == "__main__":
    main()
