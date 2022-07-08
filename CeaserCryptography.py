
from cgitb import text


print("Welcme to the world of cryptography")

def main():
    print()
    print("Choose one option")
    choice = int(input("1. Encryption\n2. Decryption\nChoose(1,2): "))
    if choice == 1:
        encryption()
    elif choice == 2:
        decryption()
    else:
        print("Wrong Choice")


def encryption():
    print("Encryption has Started")
    msg=input("Enter Your Message: ")
    key=int(input("Enter The Preferred Key(1-94): "))
    encrypted_text = ""
    for i in range(len(msg)):
        temp=(ord(msg[i]) +key)
        if temp>126:
            temp=temp-127+32
        encrypted_text+=chr(temp)
    print("Encrypted Text Is: "+encrypted_text) 

def decryption():
    print("Decryption Has Started")
    encryption_msg=input("Enter The Encrypted Text: ")
    key=int(input("Enter The Preferred Key(1-94): "))
    decrypted_text = ""
    for i in range(len(encryption_msg)):
        temp=(ord(encryption_msg[i])-key)
        if temp<32:
            temp=temp+127-32
        decrypted_text+=chr(temp)
    print("Decrypted text: " +decrypted_text)

if __name__ == "__main__":
    main()