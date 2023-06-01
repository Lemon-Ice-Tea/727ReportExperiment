from Crypto.PublicKey import RSA

def generate_key_pair():
    # Generate an RSA key pair
    key = RSA.generate(2048)

    # Export the public key in PEM format
    public_key = key.publickey().export_key("PEM")

    # Save the public key to a file
    with open("public_key.pem", "wb") as f:
        f.write(public_key)

    print("Public key saved to public_key.pem")

# Generate the key pair and save the public key
generate_key_pair()
