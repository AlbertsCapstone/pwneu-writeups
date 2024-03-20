import random

def str_xor(secret, key):
    new_key = key * (len(secret) // len(key)) + key[:len(secret) % len(key)]
    encrypted_text = ""
    for secret_char, key_char in zip(secret, new_key):
        encrypted_text += chr(ord(secret_char) ^ ord(key_char))
    return encrypted_text

flag_enc = chr(0x0) + chr(0x0) + chr(0x0) + chr(0x0) + chr(0x0) + chr(0x2b) + chr(0x18) + chr(0x1e) + chr(0x76) + chr(0x07) + chr(0x11) + chr(0x03) + chr(0x7e) + chr(0x17) + chr(0xa) + chr(0x63) + chr(0x05) + chr(0x1c) + chr(0x75) + chr(0x07) + chr(0x2d)
  
flag = str_xor(flag_enc, 'PWNEU')

if flag == "":
  print('XOR faced an issue and will now terminate')
else:
  print('Here\'s your flag: ' + flag)


