import hashlib
import time
import resource

def sign_file(file_path):
    # Read the file as binary
    with open(file_path, "rb") as file:
        content = file.read()

    # Calculate the SHA3-256 hash of the file content
    hash_object = hashlib.sha3_256()
    
    start_time = time.time()
    #start_cpu = resource.getrusage(resource.RUSAGE_SELF).ru_utime + resource.getrusage(resource.RUSAGE_SELF).ru_stime
    for i in range (0,5000):
      hash_object.update(content)
      signature = hash_object.hexdigest()

    end_time = time.time()
    #end_cpu = resource.getrusage(resource.RUSAGE_SELF).ru_utime + resource.getrusage(resource.RUSAGE_SELF).ru_stime
    
    # Print the signature
    print("File: %s" % file_path)
    print("Signature (SHA3-256): %s" % signature)
    print("Time elapsed: %.6f seconds" % (end_time - start_time))
    #print("CPU consumption: %.6f seconds" % (end_cpu - start_cpu))

# Provide the file path as an argument
file_path = "512K.mp4"

# Call the sign_file function
sign_file(file_path)
