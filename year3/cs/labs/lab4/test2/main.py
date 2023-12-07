import random
from permutation_handler import PermutationHandler
from ascii_handler import AsciiHandler

LETTERS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
ascii_handler = AsciiHandler()
perm_handler = PermutationHandler()

def gen_random_key(length=8):
    return ''.join(random.choice(LETTERS) for _ in range(length))

def generate_random_binary_string(length=64):
    return ''.join(random.choice(['0', '1']) for _ in range(length))

def pretty_print(s, length_seq):
    out = ''
    for i in range(0, len(s) - length_seq + 1, length_seq):
        out += s[i:i+length_seq] + ' '
    return out

def get_response(key, isBinary):
    print("Permuted Choice Table (PC-1):")
    perm_handler.print_pc_1()
    
    encrypted_key = key if isBinary else ascii_handler.get_binary(key) 
    print(f"K  = {pretty_print(encrypted_key, 8)}")

    permuted_key = perm_handler.get_permuted(encrypted_key)
    print(f"K+ = {pretty_print(permuted_key, 7)}")
    print("---------------------------------------------") 

def main():
    while True:
        print("Input key: \n0 - manually, \n1 - random, \n2 - exit")
        choice = int(input("Your choice: "))

        if choice == 0:
            key = input("Give the key (ASCII like, 8 characters):\n")
            
            if len(key) != 8:
                print(f"Incorrect key length! (length = {len(key)})")
                continue
            
            if not ascii_handler.is_ascii(key):
                print("The key does not adhere to the ASCII format!")
                continue
            
            get_response(key, False)
            continue

        elif choice == 1:
            # key = gen_random_key()
            key = generate_random_binary_string()
            print(f"Random key: {key}")
            get_response(key, True)
            continue
            
        elif choice == 2:
            return
        
        else:
            print("Wrong choice!")
            print("---------------------------------------------")

if __name__ == '__main__':
    main()