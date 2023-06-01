from Crypto.PublicKey import RSA

# Generate a new RSA key pair
key = RSA.generate(2048)

# Save the public key to a file
with open('public_key.pem1', 'wb') as f:
    f.write(key.publickey().export_key())

# Save the sender's private key to a file
with open('sender_private_key.pem1', 'wb') as f:
    f.write(key.export_key())

# Generate a new RSA key pair for the receiver
receiver_key = RSA.generate(2048)

# Save the receiver's private key to a file
with open('receiver_private_key.pem1', 'wb') as f:
    f.write(receiver_key.export_key())
