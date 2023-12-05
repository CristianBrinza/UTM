# Vigenere Cipher Implementation in Python

This repository contains a Python implementation of the Vigenere Cipher, specifically tailored for messages in the Romanian language, adhering to specific constraints and requirements.

## Overview

The Vigenere Cipher is a method of encrypting alphabetic text by using a simple form of polyalphabetic substitution. This implementation provides a class `VigenereCipher` that encapsulates all the functionality related to the cipher and a user-friendly menu for interaction.

## Features

- **Alphabet Specification**: Utilizes the Romanian alphabet, which contains specific characters.
- **Key Length Validation**: Ensures the key length is at least 7.
- **Character Validation**: Validates that only valid characters from the specified alphabet are used.
- **Uppercase Conversion and Space Removal**: Converts all characters to uppercase and removes spaces.
- **User Interaction**: Provides a menu for user-friendly interaction and operation selection.

## Class Methods Explanation

### 1. Initialization and Matrix Creation

Upon initialization, the class takes an `alphabet` as input, converts it to uppercase, and creates the Vigenere matrix, essential for the cipher operation.

### 2. Shifting Rows and Matrix Creation

The `_shift_row` method shifts the characters in a string, which is used to create the Vigenere matrix in `_create_matrix`. The matrix is a 2D list where each row represents the alphabet shifted by a certain number of positions.

### 3. Key Extension and Index Conversion

`_extend_key` ensures that the key is extended/repeated to match the length of the input string. `_get_indexes` converts characters into their corresponding index in the alphabet, which is used for matrix lookup during encryption/decryption.

### 4. Input Validation

`_validate_input` checks whether the input string only contains valid characters from the specified alphabet, ensuring data integrity.

### 5. Encryption and Decryption

`encrypt_decrypt` performs the actual encryption or decryption based on the `operation` argument. It validates the input, extends the key, converts characters to indexes, and performs the cipher operation using the Vigenere matrix.

## Usage

When the script is executed, the `menu` function is called, providing the user with options to encrypt or decrypt messages using the Vigenere Cipher.

```python
if __name__ == '__main__':
    menu()
```


# Vigenere Cipher: Description and Encryption Method

The Vigenere Cipher is a classical encryption algorithm that utilizes polyalphabetic substitution to encrypt alphabetic text. This document provides a detailed explanation of the Vigenere Cipher and the encryption method implemented in Python.

## Description of Vigenere Cipher

The Vigenere Cipher encrypts alphabetic text using a simple form of polyalphabetic substitution. Key components include:

- **Plaintext**: The original text to be encrypted.
- **Ciphertext**: The encrypted text.
- **Key**: A word used to determine the shift of each letter in the plaintext.

The cipher employs a Vigenere Square (or Table), which is a matrix of characters created by shifting an ordered alphabet. For the Romanian alphabet, it would have 31 different rows, each starting with a different letter.

## Encryption Method

The encryption method is embedded within the `encrypt_decrypt` method in the provided Python code. The encryption process involves the following steps:

### 1. Preprocessing the Input

```python
key = key.replace(' ', '').upper()
string = string.replace(' ', '').upper()
```

Remove Spaces: Eliminate spaces from the key and input string.
Uppercase Conversion: Convert the key and input string to uppercase.
2. Input Validation
```python
if not (self._validate_input(key) and self._validate_input(string)):
    print('Invalid input. Use letters from the specified alphabet only.')
    return
```
Character Validation: Ensure every character in the key and string is in the alphabet.
3. Key Extension
```python
extended_key = self._extend_key(string, key)
```
Matching Length: Ensure the key is extended to match the input string length.
4. Index Conversion
```python
key_indexes = self._get_indexes(extended_key)
string_indexes = self._get_indexes(string)
```
Alphabet Index: Convert characters to their corresponding alphabet index.
5. Encryption Process
```python
if operation == 'encrypt':
    return ''.join(self.matrix[k][v] for k, v in zip(key_indexes, string_indexes))
```
Matrix Lookup: Use key and string indexes to find the encrypted character in the Vigenere matrix.
Concatenation: Concatenate characters to form the encrypted message.


### Conclusion
The encryption process in the Vigenere Cipher involves preprocessing, validating, extending the key, converting characters to indexes, and utilizing the Vigenere matrix to produce the ciphertext. The method ensures adherence to constraints and accurate utilization of the Vigenere matrix for encryption.