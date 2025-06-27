from cryptography.fernet import Fernet


key = Fernet.generate_key()
cipher = Fernet(key)

def encrypt_file(input_path, output_path):
    with open(input_path, 'rb') as f:
        data = f.read()
    encrypted = cipher.encrypt(data)
    with open(output_path, 'wb') as f:
        f.write(encrypted)

def decrypt_file(input_path, output_path):
    with open(input_path, 'rb') as f:
        encrypted_data = f.read()
    decrypted = cipher.decrypt(encrypted_data)
    with open(output_path, 'wb') as f:
        f.write(decrypted)
