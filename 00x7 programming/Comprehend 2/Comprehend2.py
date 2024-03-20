import random

def str_xor(secret, key):
    repetitions = len(secret) // len(key) + 1
    new_key = (key * repetitions)[:len(secret)]
    result = ""
    for s, k in zip(secret, new_key):
        result += chr(ord(s) ^ ord(k))

    return result

def flag_check():
    flag_enc = chr(0x9), chr(0x2), chr(0x3), chr(0xC), chr(0x1E), chr(0x34), chr(0x0), chr(0x0), chr(0x0), chr(0x78), chr(0x73), chr(0x16), chr(0x6E), chr(0x66), chr(0x78), chr(0x34)
    flag = str_xor(flag_enc, 'YUMIKO')
    user_pw = input("Enter the password for the flag: ")
    if user_pw == chr(0x30) + chr(0x38) + chr(0x30) + chr(0x35) + chr(0x30) + chr(0x32):
        print('That is correct! Here\'s your flag: ' + flag)
    else:
        print("Incorrect password. Access denied.")

if __name__ == "__main__":
    flag_check()
