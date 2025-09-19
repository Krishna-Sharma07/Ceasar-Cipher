def caesar_cipher(text, shift, mode):
    result = ""
    
    if mode == 2:
        shift = -shift 
    
    for char in text:
        if char.isalpha(): 
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char 
    
    if mode == 1:
        print("Encrypted message:")
    else:
        print("Decrypted message:")

    return result

print("Welcome to Caesar Cipher!")

mode = int(input("Choose mode:\n1. Encrypt\n2. Decrypt\n> "))
message = input("Enter your message:\n> ")
shift = int(input("Enter shift value:\n> "))

result = caesar_cipher(message, shift, mode)

print("> ", result)