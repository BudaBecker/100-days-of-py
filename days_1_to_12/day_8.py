#Caesar Cipher

caesar_art = '''
,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     'Y8 a8P_____88 I8[    "" ""     'Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  '"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 '"Ybbd8"' '"8bbdP"Y8  '"Ybbd8"' '"YbbdP"' '"8bbdP"Y8 88   

                          88                                 
           88             88                                 
           ""             88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 '"Ybbd8"' 88 88'YbbdP"'  88       88  '"Ybbd8"' 88          
              88                                             
              88           
'''

def encode(message: str, shift: int) -> str:
    encoded_message = ''
    if shift > 26:
        shift %= 26
    for letters in message:
        if ord(letters) < 97 or ord(letters) > 122:
            encoded_message += letters
            continue
        if (ord(letters)+shift > 122):
            encoded_message += chr(ord(letters)+shift-26)
        else:
            encoded_message += chr(ord(letters)+shift)
    return encoded_message

def decode(message: str, shift: int) -> str:
    decoded_message = ''
    if shift > 26:
        shift %= 26
    for letters in message:
        if ord(letters) < 97 or ord(letters) > 122:
            decoded_message += letters
            continue
        if (ord(letters)-shift < 97):
            decoded_message += chr(ord(letters)-shift+26)
        else:
            decoded_message += chr(ord(letters)-shift)
    return decoded_message

def game():
    method = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    message = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    if method == 'encode':
        print(f"Here's the encoded result: {encode(message, shift)}")
    else:
        print(f"Here's the decoded result: {decode(message, shift)}")
    
    end = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if end == 'no':
        print("GoodBye")
        return
    else:
        print('\n')
        game()

print(caesar_art)
game()