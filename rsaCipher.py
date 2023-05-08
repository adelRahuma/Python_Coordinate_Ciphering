from Crypto.Cipher import AES
import base64

# Define the plaintext latitude
latitude = '37.774989'

# Define the encryption key and initialization vector (IV)
key = b'ThisIsASecretKey'
iv = b'ThisIsAnIV123456'

# Pad the latitude with spaces so that its length is a multiple of 16
padded_latitude = latitude.ljust(16)

# Create an AES cipher object with the key and IV
cipher = AES.new(key, AES.MODE_CBC, iv)

# Encrypt the padded latitude
encrypted_latitude = cipher.encrypt(padded_latitude.encode())

# Encode the encrypted latitude in base64 for storage or transmission
encoded_latitude = base64.b64encode(encrypted_latitude)

print(encoded_latitude)
# Decode the encoded latitude from base64
decoded_latitude = base64.b64decode(encoded_latitude)

# Create a new AES cipher object with the key and IV
cipher = AES.new(key, AES.MODE_CBC, iv)

# Decrypt the latitude
decrypted_latitude = cipher.decrypt(decoded_latitude)

# Remove any padding from the decrypted latitude and convert it to a string
latitude = decrypted_latitude.rstrip().decode()

print(latitude)


