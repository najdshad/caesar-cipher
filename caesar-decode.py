def main():
    ciphertext = input("Enter the ciphertext: ")
    print("\nBrute forcing Caesar cipher:")
    print("=" * 40)
    
    for shift in range(1, 26):
        decrypted = []
        for char in ciphertext:
            if char.isupper():
                base = ord('A')
                decrypted_char = chr((ord(char) - base - shift) % 26 + base)
            elif char.islower():
                base = ord('a')
                decrypted_char = chr((ord(char) - base - shift) % 26 + base)
            else:
                decrypted_char = char
            decrypted.append(decrypted_char)
        print(f"Shift {shift:2d}: {''.join(decrypted)}")

if __name__ == "__main__":
    main()