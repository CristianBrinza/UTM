"""
    Implementation of task 11 for the laboratory nr. 4.
    Condition:
        La criptarea unui bloc în cifrul DES s-a obţinut
        L16 = ... (32 biți)
        R16 = ... (32 biți)
        Să se determine blocul criptat al mesajului reprezentat hexazecimal.
"""
import re


def final_permutation(L16, R16):
    """Final step in the encryption process."""

    table = [40, 8, 48, 16, 56, 24, 64, 32,
             39, 7, 47, 15, 55, 23, 63, 31,
             38, 6, 46, 14, 54, 22, 62, 30,
             37, 5, 45, 13, 53, 21, 61, 29,
             36, 4, 44, 12, 52, 20, 60, 28,
             35, 3, 43, 11, 51, 19, 59, 27,
             34, 2, 42, 10, 50, 18, 58, 26,
             33, 1, 41, 9, 49, 17, 57, 25]
    
    print("\tFinal permutation table:")
    for i in range(0, len(table), 8):
        print("\t", table[i:i+8])
    
    # Reverse the order of the two blocks.
    reversed = list(R16 + L16)

    print("\tNot permuted bits:")
    for i in range(0, len(reversed), 8):
        print("\t", reversed[i:i+8])

    # Apply the final permutation.
    permuted = []
    for order in table:
        permuted.append(reversed[order - 1])

    print("\tPermuted bits:")
    for i in range(0, len(permuted), 8):
        print("\t", permuted[i:i+8])

    # Transform the permuted binary string to hexadecimal.
    integer = int(''.join(permuted), 2)   
    hex_form = hex(integer)[2:]

    return hex_form


def is_binary_string(s):
    return bool(re.match("^[01]+$", s))


def input_bits(bits_type):
    bits = input(bits_type)

    while not is_binary_string(bits) or len(bits) != 32:
        print("\t It has to be a string made only of 0's and 1's, "
              + "with a length of 32.")
        bits = input(bits_type)

    return bits


if __name__ == "__main__":
    #L16 = "01000011010000100011001000110100"
    #R16 = "00001010010011001101100110010101"
    # 85E813540F0AB405

    print('Menu:')
    print('\taction: p - final permutation; x - exit;')
    print('\tL16: left 32 bits encrypted in the rounds')
    print('\tR16: right 32 bits encrypted in the rounds')

    while True:
        command = input("\nAction: ")
        if command == "p":
            L16 = input_bits("\tL16: ")
            R16 = input_bits("\tR16: ")
            print("\tCiphertext: " + final_permutation(L16, R16))

        elif command == "x":
            break