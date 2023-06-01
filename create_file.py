import os

filesizelist=[15,30,45,60,90,120,135,180,240]
#filesizelist=[1,2,3,4,5,6]

for i in filesizelist:
  # Define the file size in bytes
  file_size = i * 1024 * 1024  # 10MB
  
  # Generate random binary data
  random_data = os.urandom(file_size)
  
  # Specify the file path to save the generated data
  file_path =str(i) +"MB.mp4"
  
  # Write the random data to the file
  with open(file_path, "wb") as file:
      file.write(random_data)
  
  print(f"Random binary file of {file_size} bytes generated and saved to '{file_path}'.")
