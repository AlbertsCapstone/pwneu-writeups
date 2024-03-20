import random
import sys

def str_xor(secret, key):
    return "".join([chr(ord(secret_c) ^ ord(key_c)) for (secret_c, key_c) in zip(secret, key * (len(secret) // len(key)) + key[:len(secret) % len(key)])])

flag_enc = [
    0x0, 0x0, 0x0, 0x0, 0x0, 0x2b, 0x4, 0x7f, 0x8, 0x5, 
    0x1c, 0x64, 0x11, 0x15, 0xc, 0x67, 0x1f, 0x7e, 0xb, 
    0x28
]

def print_flag():
    flag_enc_str = ''.join([chr(byte) for byte in flag_enc])
    flag = str_xor(flag_enc_str, 'PWNEU')
    print(flag)

def print_advice():
    encouragements = ['"Follow your heart in love, but keep wisdom close."', 
    'True love lies in small acts of kindness, not just big gestures.',
    'To love deeply is to accept vulnerability, where our strength truly lies.',
    'Love is free, like a wildflower. Do not try to cage it.',
    'Love is a journey for two, facing highs and lows with trust and devotion.'
    ]
    choice = random.choice(encouragements)
    print('\n-----------------------------------------------------')
    print(choice)
    print('-----------------------------------------------------\n')

def main():
    print('''               
                                       ..... ....:.                                       
                                   ...              .....                                 
                            ....                           ..                             
                          ..                                    .                         
                       ..                                         .                       
                     ..          .                      .                                 
                   .            =##-                  :*#*            .                   
                 ..             ####=    ........    :####:             .                 
                :              .####*::::::::::::::::*####:              .                
               .                ###+::::::::::::::::::+###:               .               
              :                 +#+::::::::::::::::::::+#*                 .              
             :                   =::::::::::::::::::::::=:                  :             
            ..                     ::::::::::::::::::::   ..                 :            
            :                 :*@#-::::::::::::::::::::-#@*-                 ..           
           ..                :==@@=::::::::::::::::::::=@@==-.                :           
           :                -==-::::::::::::::::::::::::::-===.               :           
           :               -==-:::::::::::------:::::::::::-===.              .           
           .              -==-:::::::::-==========-:::::::::-===.             .           
           -             -===::::::::-==============-::::::::====.            .           
           -            :===-:::::::-=*##++====++##*=-:::::::-====            :           
           :.          .===-::::::::==+*+=+#@@#+=+*+==::::::::-===-           :           
            :          -==-:::::::::========%%========:::::::::-===:         ..           
            .         -===-:::::::::-=======##=======-:::::::::-====.        :            
             :       :====-:::::::::-=======##=======-:::::::::-=====       :             
              :     .=====-:::::::::-=======##=======-:::::::::-=====-     ..             
               .    -=====-::::::::::=======##=======::::::::::-======:   ..              
                .  -=======-:::::::::=======##=======:::::::::-========. :.               
                 .:=========-::::::::-=*####@@####*=-::::::::-==========.                 
                   :==========-:::::::-==+**++**+==-:::::::-==========-.                  
                     :==========--::::::::::::::::::::::--==========-.                    
                       :-===========-----::::::::-----============-.                      
                         .--===================================-:.                        
                            .:-=============================-:                            
                                .::--=================--:.                                
                                      ..............                                                                                                 
    ''')
    print('I am the wise capybara. How can I help you?\n\n')
    
    print_flag()

if __name__ == "__main__":
    main()
