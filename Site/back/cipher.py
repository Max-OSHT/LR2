import json
from base64 import b64encode, b64decode
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def AESenc(key, data):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(data, AES.block_size))
    iv = b64encode(cipher.iv).decode('utf-8')
    ct = b64encode(ct_bytes).decode('utf-8')
#     result = json.dumps({'iv':iv, 'cp':ct})
#     print(result)
#     print("------------------------------------")
    return ct


def AESdec(key, data):
    try:
        b64 = json.loads(data)
        iv = b64decode(b64['iv'])
        ct = b64decode(b64['cp'])
        print(b64)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        pt = unpad(cipher.decrypt(ct), AES.block_size)
        return pt
        # print("The message was: ", pt)
    except (ValueError, KeyError):
        return KeyError & ValueError
        # print("Incorrect decryption")


def entry(data):
    data = data.encode()
    key = b'helloFriend24'
    if len(key) < 16:
        key = key + key[0:16-len(key)]
    else:
        key = key[0:16]
    return AESenc(key, data)