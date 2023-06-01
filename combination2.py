from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import time
import math


def generate_rsa_key_pair():
    # Generate a new RSA key pair
    key = RSA.generate(2048)

    # Export the private key to PEM format
    private_key = key.export_key()

    # Export the public key to PEM format
    public_key = key.publickey().export_key()

    return private_key, public_key


def rsa_encrypt(public_key_pem, plaintext):
    # Load the public key
    public_key = RSA.import_key(public_key_pem)

    # Create an RSA cipher object with the public key
    cipher_rsa = PKCS1_OAEP.new(public_key)

    # Generate a random AES key
    aes_key = get_random_bytes(32)

    # Create an AES cipher object with the generated key
    cipher_aes = AES.new(aes_key, AES.MODE_ECB)

    # Encrypt the AES key using RSA
    encrypted_aes_key = cipher_rsa.encrypt(aes_key)

    # Encrypt the plaintext using AES
    ciphertext = cipher_aes.encrypt(pad(plaintext.encode(), AES.block_size))

    return encrypted_aes_key.hex(), ciphertext.hex()


def rsa_decrypt(private_key_pem, encrypted_aes_key_hex, ciphertext_hex):
    # Load the private key
    private_key = RSA.import_key(private_key_pem)

    # Create an RSA cipher object with the private key
    cipher_rsa = PKCS1_OAEP.new(private_key)

    # Decrypt the AES key using RSA
    encrypted_aes_key = bytes.fromhex(encrypted_aes_key_hex)
    aes_key = cipher_rsa.decrypt(encrypted_aes_key)

    # Create an AES cipher object with the decrypted key
    cipher_aes = AES.new(aes_key, AES.MODE_ECB)

    # Decrypt the ciphertext using AES
    ciphertext = bytes.fromhex(ciphertext_hex)
    plaintext = unpad(cipher_aes.decrypt(ciphertext), AES.block_size).decode()

    return plaintext


# Generate RSA key pair
private_key_pem, public_key_pem = generate_rsa_key_pair()

for i in range(1,100):
  # Example usage
  plaintext = str(pow(10,i))  # Text to encrypt
  
  # Encrypt the plaintext using RSA and AES
  starttime=time.time()
  encrypted_aes_key_hex, ciphertext_hex = rsa_encrypt(public_key_pem, plaintext)
  endtime=time.time()
  et=(endtime-starttime)*1000
  #print("encryption time=",(endtime-starttime))
  
  # Decrypt the ciphertext using RSA and AES
  starttime=time.time()
  decrypted_plaintext = rsa_decrypt(private_key_pem, encrypted_aes_key_hex, ciphertext_hex)
  endtime=time.time()
  dt=(endtime-starttime)*1000
  #print("decryption time=",(endtime-starttime))
  
  #print("Plaintext len:", len(plaintext))
  #print("Ciphertext len:", len(ciphertext_hex))
  #print("Decrypted Plaintext:", decrypted_plaintext)
  print(len(plaintext),"|",len(ciphertext_hex),"|",et,"|",dt)
  