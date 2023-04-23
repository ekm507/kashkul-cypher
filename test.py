from kashkul import encrypt, decrypt

name = 'صالح'
cypher = encrypt(name)
print(cypher)

decrypted_name = decrypt(cypher)
print(decrypted_name)