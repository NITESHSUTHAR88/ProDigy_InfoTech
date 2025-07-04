def caesar_encrypt(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            encrypted += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            encrypted += char
    return encrypted

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

# Get user input
word = input("Enter the word to encrypt: ")
shift = int(input("Enter the shift value (e.g. 3): "))

# Encrypt and decrypt
encrypted_word = caesar_encrypt(word, shift)
decrypted_word = caesar_decrypt(encrypted_word, shift)

print("Encrypted:", encrypted_word)
print("Decrypted:", decrypted_word)