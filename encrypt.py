
from passlib.hash import sha256_crypt

password = sha256_crypt.encrypt("lokesh")
print(password)