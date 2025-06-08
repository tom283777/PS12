from cryptography.fernet import Fernet

def generate_key(path='key.key'):
    key = Fernet.generate_key()
    with open(path, 'wb') as file:
        file.write(key)
    return key

def load_key(path='key.key'):
    with open(path, 'rb') as file:
        return file.read()
    
def encrypt_file(in_path, out_path, key):
    with open(in_path, 'rb') as file:
        data = file.read()

    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)

    with open(out_path, 'wb') as file:
        file.write(encrypted_data)

    print(f'Encrypted file and saved to {out_path}')

key = generate_key('key.key')
encrypt_file('test.txt', 'test_encrypted.txt', key)