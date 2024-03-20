import random

def str_xor(secret, key):
    repetitions = len(secret) // len(key) + 1
    new_key = (key * repetitions)[:len(secret)]
    result = ""
    for s, k in zip(secret, new_key):
        result += chr(ord(s) ^ ord(k))

    return result

def flag_check():
    flag_enc = [chr(0x0), chr(0x0), chr(0x0), chr(0x0), chr(0x0), chr(0x2B), chr(0x11), chr(0x7F), 
    chr(0x17), chr(0x6), chr(0x67), chr(0x8), chr(0x1C), chr(0x76), chr(0x61), chr(0x14), chr(0x66), 
    chr(0x0), chr(0x73), chr(0xA), chr(0x13), chr(0x18), chr(0x3), chr(0x15), chr(0x7), chr(0x63), 
    chr(0x1F), chr(0xB), chr(0xB), chr(0x6), chr(0x61), chr(0x67), chr(0x0), chr(0x38)]
    flag = str_xor(flag_enc, 'PWNEU')
    user_pw = input("Enter the password for the flag: ")
    if user_pw == "1337":
        print('That is correct! Here\'s your flag: ' + flag)
    else:
        print("Incorrect password. Access denied.")

if __name__ == "__main__":
    flag_check()
