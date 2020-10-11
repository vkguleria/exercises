from string import ascii_letters,digits,punctuation
from itertools import repeat, cycle, islice

letterset=ascii_letters + punctuation + digits
print(letterset)
#CODEBOOK= { x: { y:z for y,z in zip(ascii_lowercase, islice(cycle(ascii_lowercase),i,None))}
#            for i,x in enumerate(ascii_lowercase)}
CODEBOOK= { x: { y:z for y,z in zip(letterset, islice(cycle(letterset),i,None))}
            for i,x in enumerate(letterset)}

def encipher(message,key,codebook=CODEBOOK):
    message = ''.join(m for m in message if m in codebook)
    #message = ''.join(m for m in message.lower() if m in codebook)
    return ''.join(codebook[k][m] for k,m in zip(cycle(key), message))

def decipher(message,key,codebook=CODEBOOK):
    decodebook = {x: {z:y for y,z in yz.items()} for x,yz in codebook.items()}
    return ''.join(decodebook[k][m] for k,m in zip(cycle(key), message))

#print(CODEBOOK)

#msg='Attack at dawn'
msg='Kaliko_3@vrops.com'
key= 'python'
enc_msg=encipher(msg,key)
print(f'''Cipher text: {enc_msg}
        Plain text: {decipher(enc_msg,key)}
        Key: {key}''')

