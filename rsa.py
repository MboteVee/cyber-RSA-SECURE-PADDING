from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

# generate rsa key pair
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=4096,
    
)
public_key = private_key.public_key()
message = b"You used to turn your code into little pieces of love for me. I didn't understand how precious that was then. Now i do. I love you , and if there's a chance for us someday, i'd want it.I'm really sorry i hurt you trying to protect myself of which it turns out i was protectimg myself from nothing. I will always be here for you.I LOVE YOU."

# encrypt the message using the public key RSA-OAEP
ciphertext = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
print("--- ENCRYPTED CIPHERTEXT (HEX) ---")
print(ciphertext.hex())
print("--- ENCRYPTED CIPHERTEXT (BASE64) ---")



# decrypt the message using the private key RSA-OAEP
decrypted_message = private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
print("--- DECRYPTED MESSAGE ---")
print(decrypted_message.decode('utf-8'))
print("--- ORIGINAL MESSAGE ---")
print(message.decode('utf-8'))