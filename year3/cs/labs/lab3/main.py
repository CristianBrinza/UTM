def create_matrix(key):
    matrix = []
    key = key.upper().replace('J', 'I')
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZȘȚĂÎÂ'
    for char in key:
        if char in alphabet and char not in matrix:
            matrix.append(char)
            alphabet = alphabet.replace(char, '')
    matrix.extend(list(alphabet))
    matrix = [matrix[i:i+6] for i in range(0, len(matrix), 6)]
    return matrix

def find_position(matrix, char):
    for i in range(6):
        for j in range(6):
            if matrix[i][j] == char:
                return i, j


def encrypt_pair(matrix, char1, char2):
    row1, col1 = find_position(matrix, char1)
    row2, col2 = find_position(matrix, char2)
    print(matrix)

    if row1 == row2:
        return matrix[row1][(col1 + 1) % 6], matrix[row2][(col2 + 1) % 6]
    elif col1 == col2:
        return matrix[(row1 + 1) % 6][col1], matrix[(row2 + 1) % 6][col2]
    else:
        return matrix[row1][col2], matrix[row2][col1]


def decrypt_pair(matrix, char1, char2):
    row1, col1 = find_position(matrix, char1)
    row2, col2 = find_position(matrix, char2)

    if row1 == row2:
        return matrix[row1][(col1 - 1) % 6], matrix[row2][(col2 - 1) % 6]
    elif col1 == col2:
        return matrix[(row1 - 1) % 6][col1], matrix[(row2 - 1) % 6][col2]
    else:
        return matrix[row1][col2], matrix[row2][col1]


def playfair_cipher(key, text, mode='encrypt', original_length=None):
    matrix = create_matrix(key)
    text = text.upper().replace('J', 'I')
    pairs = []

    for i in range(0, len(text), 2):
        pair = text[i:i + 2]
        if len(pair) < 2:
            pair += 'X'
        pairs.append(pair)

    result = []
    for pair in pairs:
        if mode == 'encrypt':
            encrypted_pair = encrypt_pair(matrix, pair[0], pair[1])
        else:
            encrypted_pair = decrypt_pair(matrix, pair[0], pair[1])
        result.append(encrypted_pair[0] + encrypted_pair[1])


    if mode == 'decrypt' and original_length is not None and original_length % 2 != 0:

        return ''.join(result)[:-1]

    return ''.join(result)



if __name__ == "__main__":
    operation = input("Choose the operation (encryption/decryption): ").strip().lower()
    key = input("Enter the key (at least 7 characters long): ")

    while len(key) < 7:
        key = input("Key is too short. Please enter a key with at least 7 characters: ")

    if operation == "encryption":
        message = input("Enter the message to encrypt: ")
        while len(message) % 2 != 0:
            message += "X"
        print("Encrypted message:", playfair_cipher(key, message))
    elif operation == "decryption":
        cryptogram = input("Enter the cryptogram to decrypt: ")
        original_length = len(cryptogram)
        while len(cryptogram) % 2 != 0:
            cryptogram += "X"
        print("Decrypted message:", playfair_cipher(key, cryptogram, mode='decrypt', original_length=original_length))
    else:
        print("Invalid operation chosen.")
