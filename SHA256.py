import hashlib
import time
import psutil

def sign_file(file_path):
    # Read the file as binary
    with open(file_path, "rb") as file:
        content = file.read()

    # Calculate the SHA-256 hash of the file content
    hash_object = hashlib.sha256()
    hash_object.update(content)
    signature = hash_object.hexdigest()

    # Print the signature
    print("File: %s" % file_path)
    print("Signature (SHA-256): %s" % signature)



filesizelist=[15,30,45,60,90,120,135,180,240]
#filesizelist=[1,2,3,4,5,6]
# Provide the file path as an argument
for i in filesizelist:
  file_path =str(i)+ "MB.mp4"
  
  # Measure the time and CPU consumption of the sign_file function
  start_time = time.time()
  #start_cpu = psutil.cpu_percent()
  sign_file(file_path)
  #end_cpu = psutil.cpu_percent()
  end_time = time.time()
  
  print("Time taken: %s seconds" % (end_time - start_time))
  #print("CPU consumption: %s percent" % (end_cpu - start_cpu))
  