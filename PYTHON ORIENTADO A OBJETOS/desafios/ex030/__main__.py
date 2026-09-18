from ex30 import Credencial
from rich import inspect

c = Credencial()
c.senha = 'EXAMPLE_PASSWORD_123'
##print(c.senha) ## retorna o hash da senha

c.validar('EXAMPLE_PASSWORD_456')  ## valida a senha comparando os hashes

inspect(c, methods= True, private=True)