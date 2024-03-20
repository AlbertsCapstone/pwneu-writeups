import random

def _x_o_r_str(secret, key):
    repetitions = len(secret) // len(key) + 1
    new_key = (key * repetitions)[:len(secret)]
    result = ""
    for s, k in zip(secret, new_key):
        result += chr(ord(s) ^ ord(k))
    return result

def _flag_check():
    f1 = [chr(0x0), chr(0x0), chr(0x0), chr(0x0), chr(0x0), chr(0x2B), chr(0x18), chr(0x76), chr(0x3), chr(0x0), chr(0x65), chr(0x14), chr(0x7A), chr(0x11), chr(0x66), chr(0x14), chr(0x8)]
    f_2 = [chr(0xD), chr(0x75), chr(0x11), chr(0x63), chr(0x8), chr(0xD), chr(0x71), chr(0x5), chr(0x9), chr(0x1F), chr(0x7A), chr(0x6), chr(0x1E), chr(0x63), chr(0x5), chr(0x33)]
    or1gI = f1 + f_2
    flag = _x_o_r_str(or1gI, 'PWNEU')
    xYz_05 = "\u0043\u0034"  
    abc_03 = chr(80) + chr(89)
    def_04 = ''.join([chr(int(x, 2)) for x in ["01001000", "00110100", "01011000", "01011111", "00110000", "00110010"]])
    user_input = input("Enter your password to access the flag: ")
    open_sesame = xYz_05 + abc_03 + def_04
    if open_sesame == open_sesame:
        print('Access granted! Here\'s your flag: ' + flag)
    else:
        print("Access denied. Incorrect password.")

if __name__ == "__main__":
    _flag_check()
