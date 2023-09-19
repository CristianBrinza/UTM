# Define a function to display the menu options to the user.
def display_menu():
    """
    Displays the available menu options for the encryption and decryption process.
    """
    print("Select an option:")
    print("1. Encrypt using a single key")
    print("2. Encrypt using two keys")
    print("3. Decrypt using a single key")
    print("4. Decrypt using two keys")
    print("5. Exit the application")


# Define a function to perform the Caesar cipher encryption.
def caesar_cipher(text, sequence, shift):
    """
    Encrypts or decrypts the provided text using Caesar cipher based on the sequence and shift.

    Args:
    - text: The message to be encrypted or decrypted.
    - sequence: The sequence of characters used for encryption.
    - shift: The number by which each character in the text is shifted.

    Returns:
    - result: The encrypted or decrypted message.
    """
    result = ''

    for char in text:
        index = (sequence.index(char) + shift) % 26
        result += sequence[index]

    return result


# Define a function to obtain a valid integer key from the user.
def fetch_integer_key():
    """
    Prompts the user to provide a valid integer key between 1 and 25.

    Returns:
    - key: A valid integer key.
    """
    while True:
        try:
            key = int(input("Enter an integer key (1-25): "))
            if 1 <= key <= 25:
                return key
            else:
                print("Key should be between 1 and 25.")
        except ValueError:
            print("Please enter a valid integer.")


# Define a function to get a valid message from the user.
def fetch_message():
    """
    Prompts the user to input a valid message containing only alphabets.

    Returns:
    - message: A valid message.
    """
    while True:
        message = input("Enter your message: ").upper().replace(" ", "")
        if all(char.isalpha() for char in message):
            return message
        else:
            print("Message should only contain alphabets. Try again.")


# Define a function to get a valid text key from the user.
def fetch_text_key():
    """
    Prompts the user to provide a valid text key containing only alphabets.

    Returns:
    - text_key: A valid text key.
    """
    while True:
        text_key = input("Enter the text key: ").upper()
        if all(char.isalpha() for char in text_key):
            return text_key
        else:
            print("Text key should only contain alphabets. Try again.")


# Define a function to generate a new sequence using the text key.
def generate_sequence(text_key, original_alphabet):
    """
    Creates a new sequence for encryption using the provided text key.

    Args:
    - text_key: The text key provided by the user.
    - original_alphabet: The original sequence of characters.

    Returns:
    - new_sequence: The new sequence generated using the text key.
    """
    new_sequence = ''.join(sorted(set(text_key), key=text_key.index))
    for char in original_alphabet:
        if char not in new_sequence:
            new_sequence += char

    return new_sequence


if __name__ == "__main__":
    ORIGINAL_ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    while True:
        display_menu()

        try:
            choice = int(input("Enter your choice (1-5): "))

            if choice == 5:
                print("Exiting the application. Goodbye!")
                break

            if choice == 1:  # Single key encryption
                key = fetch_integer_key()
                message = fetch_message()
                encrypted_message = caesar_cipher(message, ORIGINAL_ALPHABET, key)
                print(f"Encrypted Message: {encrypted_message}\n")

            elif choice == 2:  # Double key encryption
                int_key = fetch_integer_key()
                text_key = fetch_text_key()
                new_sequence = generate_sequence(text_key, ORIGINAL_ALPHABET)
                print(f"Generated Sequence: {new_sequence}")
                message = fetch_message()
                encrypted_message = caesar_cipher(message, new_sequence, int_key)
                print(f"Encrypted Message: {encrypted_message}\n")

            elif choice == 3:  # Single key decryption
                key = fetch_integer_key()
                message = fetch_message()
                decrypted_message = caesar_cipher(message, ORIGINAL_ALPHABET, -key)
                print(f"Decrypted Message: {decrypted_message}\n")

            elif choice == 4:  # Double key decryption
                int_key = fetch_integer_key()
                text_key = fetch_text_key()
                new_sequence = generate_sequence(text_key, ORIGINAL_ALPHABET)
                print(f"Generated Sequence: {new_sequence}")
                message = fetch_message()
                decrypted_message = caesar_cipher(message, new_sequence, -int_key)
                print(f"Decrypted Message: {decrypted_message}\n")

            else:
                print("Invalid choice. Please select a valid option (1-5).\n")

        except ValueError:
            print("Invalid input. Please enter a valid number (1-5).\n")
