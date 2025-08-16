def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    
    if mode == 'decrypt':
        shift = -shift 
    
    for char in text:
        if char.isalpha(): 
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char 
    
    return result

message = "HELLO WORLD"
shift_value = 3

encrypted = caesar_cipher(message, shift_value, mode='encrypt')
decrypted = caesar_cipher(encrypted, shift_value, mode='decrypt')

print(f"Original:  {message}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")
