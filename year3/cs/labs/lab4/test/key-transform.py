RED = "\033[91m"
RESET = "\033[0m"
BLUE = "\033[94m"
GREEN = "\033[92m"

# Initial permutation for the 64-bit key
def initial_permutation(key):
    pc1 = [57, 49, 41, 33, 25, 17, 9,
           1, 58, 50, 42, 34, 26, 18,
           10, 2, 59, 51, 43, 35, 27,
           19, 11, 3, 60, 52, 44, 36,
           63, 55, 47, 39, 31, 23, 15,
           7, 62, 54, 46, 38, 30, 22,
           14, 6, 61, 53, 45, 37, 29,
           21, 13, 5, 28, 20, 12, 4]

    key_permuted = [key[pc1[i] - 1] for i in range(56)]
    return key_permuted

# Perform a left circular shift
def left_circular_shift(key, shift):
    return key[shift:] + key[:shift]

# Permuted Choice 2 (PC-2) for generating round keys
def pc2_permutation(key):
    pc2 = [14, 17, 11, 24, 1, 5, 3, 28,
           15, 6, 21, 10, 23, 19, 12, 4,
           26, 8, 16, 7, 27, 20, 13, 2,
           41, 52, 31, 37, 47, 55, 30, 40,
           51, 45, 33, 48, 44, 49, 39, 56,
           34, 53, 46, 42, 50, 36, 29, 32]

    round_key = [key[pc2[i] - 1] for i in range(48)]
    return round_key

# Generate all 16 round keys
def generate_round_keys(key):
    round_keys = []

    key = initial_permutation(key)
    print(f"Initial permutation ({len(key)}b):  {''.join(key)}          *split")

    C, D = key[:28], key[28:]
    print(f"Intial C and D ({len(C)}b):       {BLUE}{''.join(C)}{RESET}, {GREEN}{''.join(D)}{RESET}")
    print()

    for i in range(16):
        # Determine the number of positions to shift for this round
        shift = 2 if i in [0, 1, 8, 15] else 1

        print(f"Round - {i+1:2}, shift = {shift} @", " " * 69 ,"*C and D left-circular shift")

        # Perform left circular shifts on C and D
        C = left_circular_shift(C, shift)
        D = left_circular_shift(D, shift)
        
        print(f"   ~ Shifted C and D ({len(C)}b):   {BLUE}{''.join(C[:len(C)-shift])}{RESET}{RED}{''.join(C[len(C)-shift:])}{RESET}, {GREEN}{''.join(D[:len(D)-shift])}{RESET}{RED}{''.join(D[len(D)-shift:])}{RESET}      *concatenation")

        # Combine C and D and apply PC-2 permutation to get the round key
        combined_key = C + D
        round_key = pc2_permutation(combined_key)
        round_keys.append(round_key)

        print(f"   ~ Combined key ({len(combined_key)}b):      {BLUE}{''.join(combined_key[:28])}{RESET}{GREEN}{''.join(combined_key[28:])}{RESET}        *compression-perm. (PC-2)")
        print(f"   ~ Round key ({len(round_key)}b):         {''.join(round_key)}")
        print()

    return round_keys

# Example DES key (64 bits)
des_key = "0111101000010101010100011100110111101000010101010100011100110111"

print(f"Initial key ({len(des_key)}b):          {des_key}  *initial-perm. (PC-1)")

# Generate the 16 round keys
round_keys = generate_round_keys(des_key)

# Display the round keys
# for i, key in enumerate(round_keys, start=1):
#     print(f"Round {i:2}: {''.join(key)}")
