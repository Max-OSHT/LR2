import json
from base64 import b64encode, b64decode

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def AESenc(key, data):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(data, AES.block_size))
    iv = b64encode(cipher.iv).decode('utf-8')
    ct = b64encode(ct_bytes).decode('utf-8')
    result = iv+ct
    return result


def AESdec(key, data):
    iv = b64decode(data[0:24])
    ct = b64decode(data[24:])
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size)
    return pt.decode('utf-8')


def entry(data):
    data = data.encode()
    key = b'helloFriend24'
    if len(key) < 16:
        key = key + key[0:16-len(key)]
    else:
        key = key[0:16]
    return AESenc(key, data)

def out(data):
    data = data.encode()
    key = b'helloFriend24'
    if len(key) < 16:
        key = key + key[0:16-len(key)]
    else:
        key = key[0:16]
    return AESdec(key, data)