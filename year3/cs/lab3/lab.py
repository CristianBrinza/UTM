class VigenereCipher:
    def __init__(self, alphabet):
        # Initialize the alphabet and create the Vigenere matrix
        self.alphabet = alphabet.upper()
        self.matrix = self._create_matrix()

    def _shift_row(self, input_string, n):
        # Shift the input string to the left by n positions
        n = n % len(input_string)
        return input_string[n:] + input_string[:n]

    def _create_matrix(self):
        # Create the Vigenere matrix by shifting the alphabet for each row
        return [self._shift_row(self.alphabet, i) for i in range(len(self.alphabet))]

    def _extend_key(self, string, key):
        # Extend the key to match the length of the string
        quotient, remainder = divmod(len(string), len(key))
        return quotient * key + key[:remainder]

    def _get_indexes(self, string):
        # Convert characters in the string to their corresponding indexes in the alphabet
        return [self.alphabet.index(char) for char in string]

    def _validate_input(self, string):
        # Validate the input string to ensure it only contains characters from the alphabet
        return all(char in self.alphabet for char in string)

    def encrypt_decrypt(self, key, string, operation):
        # Remove spaces and convert to uppercase
        key = key.replace(' ', '').upper()
        string = string.replace(' ', '').upper()

        # Validate the inputs
        if not (self._validate_input(key) and self._validate_input(string)):
            print('Invalid input. Use letters from the specified alphabet only.')
            return

        # Extend the key, and get the indexes of the key and string characters
        extended_key = self._extend_key(string, key)
        key_indexes = self._get_indexes(extended_key)
        string_indexes = self._get_indexes(string)

        # Perform encryption or decryption based on the operation argument
        if operation == 'encrypt':
            return ''.join(self.matrix[k][v] for k, v in zip(key_indexes, string_indexes))
        elif operation == 'decrypt':
            return ''.join(self.alphabet[(v-k) % len(self.alphabet)] for k, v in zip(key_indexes, string_indexes))
        else:
            print('Invalid operation. Choose "encrypt" or "decrypt".')
            return


def menu():
    # Define the Romanian alphabet
    alphabet_ro = 'AĂÂBCDEFGHIÎJKLMNOPQRSȘTȚUVWXYZ'

    # Create a VigenereCipher object
    cipher = VigenereCipher(alphabet_ro)

    # Infinite loop to keep the menu running until the user decides to exit
    while True:
        print("\n--- Vigenere Cipher ---")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")

        # Get the user's choice
        choice = input("Choose an option: ")

        # Perform the corresponding action
        if choice == "1":
            key = input("Enter the key: ")
            string_to_encrypt = input("Enter the message to encrypt: ")
            encrypted_message = cipher.encrypt_decrypt(key, string_to_encrypt, 'encrypt')
            print(f'Encrypted message: {encrypted_message}')
        elif choice == "2":
            key = input("Enter the key: ")
            string_to_decrypt = input("Enter the message to decrypt: ")
            decrypted_message = cipher.encrypt_decrypt(key, string_to_decrypt, 'decrypt')
            print(f'Decrypted message: {decrypted_message}')
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


# Run the menu when the script is executed
if __name__ == '__main__':
    menu()
