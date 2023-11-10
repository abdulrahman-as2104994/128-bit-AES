from aes_128_bit import *

running = True
while running:
    print("\n------------------128-bit AES Encryption and Decryption------------------")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Brute-force")
    print("4. Show saved data")
    print("5. Clear saved data")
    print("6. Exit")
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
        print("\nDeciphered text: \n", decipher)
    elif choice == "3":
        cipher = input("Enter the cipher text to be brute-forced: ")
        have = input("Do you have any idea about the plain text? (y/n): ")
        if have == "y":
            plain_text = input("Enter the plain text to be searched for (Case sensative): ")
            print("ctrl-c to stop the brute-force")
            brute_force(cipher, plain_text)
        elif have == "n":
            print("It is not guaranteed that you will get the correct plain text (ASCII characters only)")
            print("ctrl-c to stop the brute-force")
            brute_force(cipher)
        else:
            print("Invalid choice!")
    elif choice == "4":
        print("1. Show broken ciphers data")
        print("2. Show candidate plain texts data")
        print("3. Show used keys history data")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            show_broken_ciphers()
        elif choice == "2":
            show_candidate_plain_texts()
        elif choice == "3":
            show_used_keys_history()
        elif choice == "4":
            print("Exiting...")
        else:
            print("Invalid choice!")
    elif choice == "5":
        print("************************************")
        print("WARINING! THIS STEP IS IRREVERSIBLE!")
        print("************************************")
        print("1. Clear broken ciphers data")
        print("2. Clear candidate plain texts data")
        print("3. Clear used keys history data")
        print("4. Clear all data")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            sure = input("Are you sure you want to clear all broken ciphers data? (y/n): ")
            if sure == "y":
                clear_broken_ciphers()
        elif choice == "2":
            sure = input("Are you sure you want to clear all candidate plain texts data? (y/n): ")
            if sure == "y":
                clear_candidate_plain_texts()
        elif choice == "3":
            sure = input("Are you sure you want to clear all used keys history data? (y/n): ")
            if sure == "y":
                clear_used_keys_history()
        elif choice == "4":
            sure = input("Are you sure you want to clear all data? (y/n): ")
            if sure == "y":
                clear_all_data()
        elif choice == "5":
            print("Exiting...")
        else:
            print("Invalid choice!")
    elif choice == "6":
        print("Exiting...")
        running = False
    else:
        print("Invalid choice!")
