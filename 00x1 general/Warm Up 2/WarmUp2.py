import random

def str_xor(secret, key):
    return "".join([chr(ord(secret_c) ^ ord(key_c)) for (secret_c, key_c) in zip(secret, key * (len(secret) // len(key)) + key[:len(secret) % len(key)])])

flag_enc = (
    chr(0x00) + chr(0x00) + chr(0x00) + chr(0x00) + chr(0x00) +
    chr(0x2B) + chr(0x15) + chr(0x7F) + chr(0x0B) + chr(0x61) +
    chr(0x02) + chr(0x0E) + chr(0x0C) + chr(0x71) + chr(0x06) +
    chr(0x15) + chr(0x08) + chr(0x7F) + chr(0x0B) + chr(0x01) +
    chr(0x60) + chr(0x08) + chr(0x06) + chr(0x76) + chr(0x0D) +
    chr(0x64) + chr(0x13) + chr(0x7D) + chr(0x06) + chr(0x1C) +
    chr(0x1D) + chr(0x16) + chr(0x02) + chr(0x38)
)

correct_answers = 0

if 1==1:
    flag = str_xor(flag_enc, 'PWNEU')
    print('Congratulations! Here\'s your flag: ' + flag)
