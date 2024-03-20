import random

#############################################| NO NEED TO CHANGE THIS |#############################################
class FlagKeeper:
    def __init__(self):
        flag_enc = [chr(0x0), chr(0x0), chr(0x0), chr(0x0), chr(0x0), chr(0x2B), chr(0x63), chr(0x1E), 
        chr(0x15), chr(0x7), chr(0x60), chr(0x1), chr(0x7D), chr(0x1), chr(0xA), chr(0x67), chr(0x5), 
        chr(0x7A), chr(0xB), chr(0x60), chr(0x11), chr(0x14), chr(0x79), chr(0x74), chr(0x1A), chr(0x1E), 
        chr(0x76), chr(0x33)]
        self.flag = self.str_xor(flag_enc, 'PWNEU')

    def str_xor(self, secret, key):
        repetitions = len(secret) // len(key) + 1
        new_key = (key * repetitions)[:len(secret)]
        result = ""
        for s, k in zip(secret, new_key):
            result += chr(ord(s) ^ ord(k))
        return result
#############################################| NO NEED TO CHANGE THIS |#############################################


def flag_check(account_balance, transaction_cost):
    flag_keeper = FlagKeeper() 
    flag = flag_keeper.flag  

    if account_balance >= transaction_cost:
        new_balance = account_balance - transaction_cost
        print("Transaction approved! Your new balance is:", new_balance)
        print('Here\'s your flag: ' + flag)
    else:
        print("Transaction declined! Insufficient funds.")

if __name__ == "__main__":
    account_balance = 1100
    transaction_cost = 1100
    flag_check(account_balance, transaction_cost)
