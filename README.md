# Cyber RSA Secure Padding Project

A Python implementation of secure asymmetric encryption using the RSA algorithm. This project demonstrates how to securely generate keys, encrypt payloads, and decrypt them back to plaintext.

## Code Design Choices Explained

To ensure maximum security and functionality, specific cryptographic configurations were chosen over others:

### 1. Key Size: 8192-bit
*Why: RSA encryption has strict input constraints defined by the formula: `(Key Size / 8) - 66 bytes` when using OAEP with SHA-256. 
*The Choice:** A standard `2048-bit` key limits input data to 190 characters, causing a `ValueError: Encryption failed` on longer text. Upgrading to an `8192-bit` key expands the cryptographic overhead limit to **958 bytes**, allowing larger paragraphs to be encrypted seamlessly.

### 2. Padding Scheme: OAEP
*Why: Raw RSA is deterministic (encrypting the same message twice yields identical ciphertext), which exposes structural patterns to attackers. 
*The Choice: `padding.OAEP` injects cryptographic randomness (noise) into the plaintext before processing. Older legacy formats like `PKCS1v15` were avoided because they are highly vulnerable to modern mathematical side-channel attacks.

### 3. Hashing Algorithm: SHA-256
Why: The OAEP padding scheme relies on a cryptographic hash function to scramble its internal verification tags.
*The Choice: `hashes.SHA256()` provides a collision-resistant 256-bit hash. Legacy choices like `MD5` or `SHA-1` were explicitly avoided as they are cryptographically broken and insecure.

### 4. Public Exponent: 65537
*Why:RSA key generation requires a fixed mathematical constant to establish computational security.
*The Choice:** `65537` (2¹⁶ + 1) is a prime number that offers an ideal compromise between high computational speed and absolute security against shortcut factoring attacks.
*
#prerequisites
This project requires python 3 and the  cryptogyaphy library
     pip install cryptography
     and to actually know if the library is stalled, run this command in vs code terminal
     pip show cryptography
#Troubleshooting
### 'valueError: Encryption failed'
i encountered this error and it's due to text payload being too large for your configured RSA key size.
*fix 1- shorten the plaintext message inside the script
*fix 2- increase the key_size parameter(from 2048- 4096-8192) 
# future roadmap
implement hybrid encryption(AES+RSA) to securely handle file and text transfers of unlimited length