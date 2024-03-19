import random

def str_xor(secret, key):
    return "".join([chr(ord(secret_c) ^ ord(key_c)) for (secret_c, key_c) in zip(secret, key * (len(secret) // len(key)) + key[:len(secret) % len(key)])])

flag_enc = chr(0x00) + chr(0x00) + chr(0x00) + chr(0x00) + chr(0x00) + chr(0x2B) + chr(0x13) + chr(0x7D) + chr(0x06) + chr(0x64) + chr(0x1D) + chr(0x63) + chr(0x02) + chr(0x1A) + chr(0x62) + chr(0x1F) + chr(0x08) + chr(0x0C) + chr(0x74) + chr(0x1B) + chr(0x64) + chr(0x05) + chr(0x17) + chr(0x1A) + chr(0x16) + chr(0x1F) + chr(0x19) + chr(0x18) + chr(0x00) + chr(0x07) + chr(0x67) + chr(0x66) + chr(0x01) + chr(0x0B) + chr(0x28)

correct_answers = 0

if 1==1:
    flag = str_xor(flag_enc, 'PWNEU')
    print('Congratulations! Here\'s your flag: ' + flag)
