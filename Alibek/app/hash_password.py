from pwdlib import PasswordHash

pass_hash = PasswordHash.recommended()
my_password = "alibek21025200"
hash_password = pass_hash.hash(my_password)
print(hash_password)
password = pass_hash.verify("alibek21025200", hash_password)
print(password)