from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

# generate rsa key pair
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=4096,
    
)
public_key = private_key.public_key()
message = b"Sometimes confidence is not only seen when you do big things, it's when you have the courage to not let the past dictate your present and future. Is when you are so brave to overcome the darkness within you.The thing that i now value more than anything else is TIME. They say time changes but time continues to move if the person does not conquer the negative or draining person inside them. Things happen and if don't allow yourself to grow you will always be stuck. After all,,,,, LIFE MUST GO ON"

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