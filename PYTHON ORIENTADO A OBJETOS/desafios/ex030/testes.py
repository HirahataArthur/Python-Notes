import hashlib
from hashlib import sha256


senha = 'oioi'
cod = senha.encode('utf-8')

hash = sha256(cod).hexdigest()  
print(senha)
print(hash)


