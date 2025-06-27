from Register import register_user
from unlock import unlock_file
from file_encryptor import encrypt_file

def main():
    print("1. Register Face")
    print("2. Lock File")
    print("3. Unlock File")
    choice = input("Choose: ")

    if choice == '1':
        name = input("Enter your name: ")
        register_user(name)
    elif choice == '2':
        path = input("Enter file path to lock: ")
        encrypt_file(path, f"secured_files/{os.path.basename(path)}.enc")
        print("File encrypted.")
    elif choice == '3':
        filename = input("Enter file name to unlock (without .enc): ")
        unlock_file(filename)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
