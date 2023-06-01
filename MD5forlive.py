import hashlib
import time

def sign_file(file_path):
    # Read the file as binary
    with open(file_path, "rb") as file:
        content = file.read()

    # Calculate the MD5 hash of the file content
    start_time = time.time()
    for i in range (0,5000):
      #print(i)
      hash_object = hashlib.md5()
      hash_object.update(content)
      signature = hash_object.hexdigest()
      end_time = time.time()

    # Print the signature and time consumption
    print("File: %s" % file_path)
    print("Signature (MD5): %s" % signature)
    print("Time consumption: %.6f seconds" % (end_time - start_time))

# Provide the file path as an argument
file_path = "512K.mp4"

# Call the sign_file function
sign_file(file_path)
