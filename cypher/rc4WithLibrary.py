from Crypto.Cipher import ARC4
key = b"adsddsadafdsfdsfgfdhgfdhjgfdhjgdfjh"
cipher = ARC4.new(key)
msg = cipher.encrypt("Open the pod bay doors, HAL".encode('ASCII'))

print(msg)

cipher2 = ARC4.new(key)
msg2 = cipher2.decrypt(msg)
print(msg2.decode('ASCII'))