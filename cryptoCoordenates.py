from cryptography.fernet import Fernet
import pandas as pd
import os,csv
DELIMITER = chr(255)
with open('./data/Libya/LBY_adm0_pnts.csv', 'r') as csvfile:
      csv_reader = csv.reader(csvfile, delimiter=',') 
      line_count = 0
      for row in csv_reader:
       
        if line_count == 0:
            print(f' jjjjjjjjjjj{" , ".join(row)}')
            line_count += 1
        else:
            print(f'{row[0]} {row[1]}.')
            line_count += 1
      print(f'Processed {line_count} lines.')

def crypto(file):
     key = Fernet.generate_key()
     f= Fernet(key)
     token = f.encrypt(b"A really secret message. Not for prying eyes.")
     print(token)
     print(f.decrypt(token))
#crypto('uuuu')



# opening the key

key = Fernet.generate_key()
f= Fernet(key)

# opening the original file to encrypt
with open('./data/Libya/LBY_adm0_pnts.csv', 'rb') as file:
	original = file.read()
	print(original[0])
    
# encrypting the file
encrypted = f.encrypt(original)
print(encrypted)
# opening the file in write mode and
# writing the encrypted data
with open('./data/Libya/tt1.csv', 'wb') as encrypted_file:
	encrypted_file.write(encrypted)


with open('./data/Libya/tt1.csv', 'rb') as file:
	original = file.read()
	z =f.decrypt(original)
print(z)


