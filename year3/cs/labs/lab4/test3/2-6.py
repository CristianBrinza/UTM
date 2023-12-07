import os
import random

EXPANSION_TABLE = [
    32,
    1,
    2,
    3,
    4,
    5,
    4,
    5,
    6,
    7,
    8,
    9,
    8,
    9,
    10,
    11,
    12,
    13,
    12,
    13,
    14,
    15,
    16,
    17,
    16,
    17,
    18,
    19,
    20,
    21,
    20,
    21,
    22,
    23,
    24,
    25,
    24,
    25,
    26,
    27,
    28,
    29,
    28,
    29,
    30,
    31,
    32,
    1,
]


def hex_to_binary(hex_string):
    binary_string = bin(int(hex_string, 16))[2:].zfill(4 * len(hex_string))
    print(f"Hexadecimal to binary conversion: {hex_string} -> {binary_string}")
    return binary_string


def apply_expansion(input_bits, expansion_table):
    expanded = "".join(input_bits[i - 1] for i in expansion_table)
    print(f"Applying expansion table on {input_bits} to get {expanded}")
    return expanded


def xor_bits(bit_string1, bit_string2):
    return "".join(str(int(b1) ^ int(b2)) for b1, b2 in zip(bit_string1, bit_string2))


def get_user_input():
    K_hex = input("Enter the 48-bit subkey (Ki) in hex: ")
    R_prev_hex = input("Enter the 32-bit block (Ri-1) from the previous round in hex: ")
    return K_hex, R_prev_hex


def generate_random_input():
    K_hex = os.urandom(6).hex()
    R_prev_hex = os.urandom(4).hex()
    print(f"Randomly generated 48-bit subkey (Ki) in hex: {K_hex}")
    print(f"Randomly generated 32-bit block (Ri-1) in hex: {R_prev_hex}")
    return K_hex, R_prev_hex


def main():
    choice = input(
        "Enter '1' to input your own values, or '2' to generate random values: "
    )

    if choice == "1":
        K_hex, R_prev_hex = get_user_input()
    elif choice == "2":
        K_hex, R_prev_hex = generate_random_input()
    else:
        print("Invalid choice. Exiting the program.")
        return

    K_bin = hex_to_binary(K_hex)
    R_prev_bin = hex_to_binary(R_prev_hex)

    print(f"\nDES Expansion Table: {EXPANSION_TABLE}")

    expanded_R = apply_expansion(R_prev_bin, EXPANSION_TABLE)

    xor_output = xor_bits(expanded_R, K_bin)
    print(f"\nResult of XOR between expanded R and K: {xor_output}")

    print("\n6-bit blocks after expansion and XOR (B1, B2, B3, B4, B5, B6, B7, B8):")
    for i in range(8):
        B = xor_output[i * 6 : (i + 1) * 6]
        print(f"B{i+1}: {B}")


if __name__ == "__main__":
    main()
