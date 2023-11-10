from aes_128_bit import *

running = True
while running:
    print("\n------------------128-bit AES Encryption and Decryption------------------")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Brute-force")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        plain_text = input("Enter the plain text to be encrypted: ")
        key = input("\nEnter a 128-bit key: ")
        cipher = encrypt(plain_text, key)
        print("\nCiphered text (Copied to clipboard):\n", cipher)
    elif choice == "2":
        cipher = input("Enter the cipher text to be decrypted: ")
        key = input("\nEnter the 128-bit key used for encryption: ")
        decipher = decrypt(cipher, key)
        print("\nDeciphered text (Copied to clipboard):\n", decipher)
    elif choice == "3":
        print("1. Go to brute-force mode")
        print("2. Show broken ciphers")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            cipher = input("Enter the cipher text to be brute-forced: ")
            have = input("Do you have any idea about the plain text? (y/n): ")
            if have == "y":
                plain_text = input("Enter the plain text to be searched for (Case sensative): ")
                print("ctrl-c to stop the brute-force")
                brute_force(cipher, plain_text)
            elif have == "n":
                print("It is not gurenteed that you will get the correct plain text (ASCII characters only)")
                print("ctrl-c to stop the brute-force")
                brute_force(cipher)
            else:
                print("Invalid choice!")
        elif choice == "2":
            show_broken_ciphers()
        elif choice == "3":
            print("Exiting...")
        else:
            print("Invalid choice!")
    elif choice == "4":
        print("Exiting...")
        running = False
    else:
        print("Invalid choice!")
