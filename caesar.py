def cc_encrypt(msg: str,key: int) -> str:
    encrypted_msg = ''

    try:
        for char in msg:
            encrypted_msg += str(chr(ord(char)+int(key)))
    except:
        print(Exception)
        pass
    
    return encrypted_msg

def cc_decrypt(msg: str,key: int) -> str:
    decrypted_msg = ''

    try:
        for char in msg:
            decrypted_msg += chr(ord(char)-int(key))
    except:
        print(Exception)
        pass

    return decrypted_msg

  
message = 'Hello World!'
key = 9
print(f'Caesar Cipher:\nEncrypted: {cc_encrypt(message,key)}\nDecrypted: {cc_decrypt(cc_encrypt(message,key),key)}')