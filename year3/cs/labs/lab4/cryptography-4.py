import random
import string

initial_perm = [58, 50, 42, 34, 26, 18, 10, 2,
                60, 52, 44, 36, 28, 20, 12, 4,
                62, 54, 46, 38, 30, 22, 14, 6,
                64, 56, 48, 40, 32, 24, 16, 8,
                57, 49, 41, 33, 25, 17, 9, 1,
                59, 51, 43, 35, 27, 19, 11, 3,
                61, 53, 45, 37, 29, 21, 13, 5,
                63, 55, 47, 39, 31, 23, 15, 7]

# Expansion permutation
expansion_perm = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11,
                  12, 13, 12, 13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21, 20, 21,
                  22, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]

# Permute function to rearrange the bits
def permute(k, arr, n):
    permutation = ""
    for i in range(0, n):
        permutation = permutation + k[arr[i] - 1]
    return permutation

while True:
    print("1 - input message manually")
    print("2 - generate message randomly")
    user_option = int(input("option: "))

    if user_option == 1:
        user_input = input("Input Message: ")

        if len(user_input) == 8:
            break
        else:
            print("Enter a valid message (8 chars)")

    else:
        characters = string.ascii_letters + string.digits
        user_input = ''.join(random.choice(characters) for _ in range(8))
        print(f'message: {user_input}')
        break

pt = ''.join(format(ord(i), '08b') for i in user_input)

# Initial Permutation
pt = permute(pt, initial_perm, 64)

# Splitting
right = pt[32:64]

# At this point, you have L0 and R0. You can now proceed to expand R0 and permute it to get L1.

# Expand R0

# Now, you have expanded_right, which can be used as L1.

print("L1: " +  right)