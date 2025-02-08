import string

def caesar_cipher(text, shift, decrypt=False):
    """Encrypts or decrypts a given text using the Caesar cipher."""
    if not text:
        return "Error: No text provided"
    if decrypt:
        shift = -shift
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def substitution_cipher(text, key, decrypt=False):
    """Encrypts or decrypts a given text using a simple substitution cipher."""
    if not text:
        return "Error: No text provided"
    if len(set(key)) != 26 or not key.isalpha():
        return "Error: Key must be 26 unique letters"
    alphabet = string.ascii_lowercase
    key_map = {alphabet[i]: key[i] for i in range(26)}
    if decrypt:
        key_map = {v: k for k, v in key_map.items()}
    return ''.join(key_map.get(char, char) for char in text.lower())

def main():
    while True:
        print("\nEncryption Tool")
        print("1. Encrypt Text")
        print("2. Decrypt Text")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            text = input("Enter text to encrypt: ")
            method = input("Enter method (Caesar/Substitution): ").lower()
            
            if method == "caesar":
                shift = input("Enter shift value (default 3): ")
                shift = int(shift) if shift.isdigit() else 3
                result = caesar_cipher(text, shift)
            elif method == "substitution":
                key = input("Enter 26-letter key for substitution: ")
                result = substitution_cipher(text, key)
            else:
                result = "Error: Invalid method"
            
            print("Encrypted Text:", result)
        
        elif choice == "2":
            text = input("Enter text to decrypt: ")
            method = input("Enter method (Caesar/Substitution): ").lower()
            
            if method == "caesar":
                shift = input("Enter shift value (default 3): ")
                shift = int(shift) if shift.isdigit() else 3
                result = caesar_cipher(text, shift, decrypt=True)
            elif method == "substitution":
                key = input("Enter 26-letter key for substitution: ")
                result = substitution_cipher(text, key, decrypt=True)
            else:
                result = "Error: Invalid method"
            
            print("Decrypted Text:", result)
        
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
