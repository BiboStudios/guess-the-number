import random
import string
import os
os.system("say 'Hello, I am your assistant. I can help you with Caesar cipher encryption and decryption.'")
os.system("say 'Please enter the shift value for the Caesar cipher.'")
shift_value = int(input("Enter the shift value for the Caesar cipher: "))
encryption_choice = input("Do you want to encrypt or decrypt the text? (e/d): ").lower()
while encryption_choice not in ['e', 'd']:
    print("Invalid choice. Please enter 'e' for encryption or 'd' for decryption.")
    encryption_choice = input("Do you want to encrypt or decrypt the text? (e/d): ").lower()
new_shift_value = shift_value % 26
digits = string.digits
letters_lowercase = string.ascii_lowercase
letters_uppercase = string.ascii_uppercase
encryption_dict = {}
decryption_dict = {}
if encryption_choice == 'e':
    os.system("say 'You have chosen encryption.Please enter the text you want to encrypt.'")
    encryption_text = input("Enter the text to encrypt: ")
    for index, char in enumerate(encryption_text):
        if char in letters_lowercase:
            encryption_dict[char] = letters_lowercase[(letters_lowercase.index(char) + new_shift_value) % 26]
        elif char in letters_uppercase:
            encryption_dict[char] = letters_uppercase[(letters_uppercase.index(char) + new_shift_value) % 26]
        elif char in digits:
            encryption_dict[char] = digits[(digits.index(char) + new_shift_value) % 10]
elif encryption_choice == 'd':
    os.system("say 'You have chosen decryption.Please enter the text you want to decrypt.'")
    decryption_text = input("Enter the text to decrypt: ")
    for index, char in enumerate(decryption_text):
        if char in letters_lowercase:
            decryption_dict[char] = letters_lowercase[(letters_lowercase.index(char) - new_shift_value) % 26]
        elif char in letters_uppercase:
            decryption_dict[char] = letters_uppercase[(letters_uppercase.index(char) - new_shift_value) % 26]
        elif char in digits:
            decryption_dict[char] = digits[(digits.index(char) - new_shift_value) % 10]
if len(encryption_dict) > 0:
    encrypted_text = ''.join([encryption_dict.get(char, char) for char in encryption_text])
    os.system("say 'The encryption is complete.'")
    print("Encrypted text:", encrypted_text)
elif len(decryption_dict) > 0:
    decrypted_text = ''.join([decryption_dict.get(char, char) for char in decryption_text])
    os.system("say 'The decryption is complete.'")
    print("Decrypted text:", decrypted_text)