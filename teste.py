import hashlib

data = "teste"
hash = hashlib.sha256(data.encode()).hexdigest()
print(int(hash,16))