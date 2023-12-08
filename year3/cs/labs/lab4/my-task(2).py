#do not use
#modify !!!!!!!!!!!!!!!!!!!!!!


#1,2,9,16 !!!!!

#S box,... (toate tabelele)
#5 pasi de generare a chilor pentru RSA (e,d,n) 4 tupluri cate 3 ( cate valide,etc....)



import random

# Define the key rotation schedule for each round
KEY_ROTATION_SCHEDULE = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]


def generate_random_key():
    # Generate a random 64-bit key (K+)
    original_key = ''.join(str(random.randint(0, 1)) for _ in range(64))

    # Remove specified bits from the initial key
    modified_key = original_key[:7] + original_key[8:15] + original_key[16:23] + original_key[24:31] + \
                   original_key[32:39] + original_key[40:47] + original_key[48:55] + original_key[56:63]

    return original_key, modified_key


def calculate_Ci_and_Di(K_plus, round_number):
    # Calculate Ci and Di for the given round number
    C, D = K_plus[:28], K_plus[28:]
    print(f"\nInitial Halves of the key:")
    print(f"Ci: {C}")
    print(f"Di: {D}")

    for _ in range(KEY_ROTATION_SCHEDULE[round_number - 1]):
        # Perform a circular left shift on C
        C = C[1:] + C[0]

        # Perform a circular left shift on D
        D = D[1:] + D[0]

    return C, D


def main():
    # Generate a modified random 64-bit key (K+)
    original_key, K_plus = generate_random_key()

    print("Randomly generated 64-bit key (K+):")
    print(original_key)

    round_number = int(input("\nEnter the round number (1 to 16) to calculate Ci and Di: "))

    if round_number < 1 or round_number > 16:
        print("Invalid round number. Please enter a number between 1 and 16.")
    else:
        # Calculate Ci and Di for the specified round
        C, D = calculate_Ci_and_Di(K_plus, round_number)

        print(f"\nCi for round {round_number}:")
        print(C)

        print(f"\nDi for round {round_number}:")
        print(D)


if __name__ == "__main__":
    main()