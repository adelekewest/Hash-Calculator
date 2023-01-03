import hashlib

# Set the path to the file or the string
path = "path/to/file.txt"
string = "hello"

# Calculate the hash of the file or string
if path:
  # Open the file in binary mode
  with open(path, "rb") as f:
    # Read the contents of the file
    contents = f.read()
    # Calculate the hash of the contents
    hash = hashlib.sha256(contents).hexdigest()
else:
  # Calculate the hash of the string
  hash = hashlib.sha256(string.encode()).hexdigest()

# Print the hash
print(hash)
