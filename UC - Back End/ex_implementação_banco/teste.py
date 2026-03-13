import hashlib

senha_cripto=hashlib.md5(b"senha")
print(senha_cripto.hexdigest())
