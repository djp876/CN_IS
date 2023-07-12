pip install cryptography --quiet
pip install Fernet --quiet

from cryptography.fernet import Fernet
key = Fernet.generate_key()
f = Fernet(key)
message = input("Enter a message to encrypt: ").encode()
token = f.encrypt(message)
print("Encrypted token:", token)
decrypted_message = f.decrypt(token).decode()
print("Decrypted message:", decrypted_message)
