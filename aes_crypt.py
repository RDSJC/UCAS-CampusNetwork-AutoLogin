try:
    from Crypto.Cipher import AES as Aes

except BaseException as exp:
    print('pip install pycrypto -i https://mirrors.aliyun.com/pypi/simple/')
    raise exp

import base64
import copy


def _pad(s, padvalue=None):
    if padvalue == None:
        return s + (16 - len(s) % 16) * chr(16 - len(s) % 16)
    else:
        return s + (16 - len(s) % 16) * chr(padvalue)


def _unpad(s):
    return s[:-ord(s[len(s) - 1:])]


def cipher(key, iv, method):
    if 'CBC' in method:
        aes = Aes.new(key, IV=iv, mode=Aes.MODE_CBC)
    elif 'CFB' in method:
        aes = Aes.new(key, IV=iv, mode=Aes.MODE_CFB)
    elif 'CTR' in method:
        aes = Aes.new(key, IV=iv, mode=Aes.MODE_CTR)
    elif 'ECB' in method:
        aes = Aes.new(key, IV=iv, mode=Aes.MODE_ECB)
    elif 'OFB' in method:
        aes = Aes.new(key, IV=iv, mode=Aes.MODE_OFB)
    else:
        raise BaseException('Unknow AES mode for {0}'.format(method))
    return aes


def decrypt(key, iv, method, payload, base64encode=True, coding='utf8'):
    key = copy.deepcopy(key)
    iv = copy.deepcopy(iv)
    method = copy.deepcopy(method)

    if isinstance(key, str) and len(key) != 16:
        key = key + '\0' * (16 - len(key))
    if isinstance(key, bytes) and len(key) != 16:
        pass
    if isinstance(iv, str) and len(iv) != 16:
        iv = iv + '\0' * (16 - len(iv))
    if isinstance(key, str):
        key = key.encode()
    if isinstance(iv, str):
        iv = iv.encode()
    aes = cipher(key, iv, method)
    if base64encode:
        payload = base64.b64decode(payload)
    plain = aes.decrypt(payload)
    plain = _unpad(plain)
    return plain.decode(coding)


def encrypt(key, iv, method, payload):
    if len(key) != 16:
        key = key + '\0' * (16 - len(key))
    aes = cipher(key.encode(), iv.encode(), method)
    if "PKCS5Padding" in method or "PKCS7Padding" in method:
        payload = _pad(payload)
    elif "ZeroPadding" in method:
        payload = _pad(payload, 0)
    encrypted = aes.encrypt(payload)
    return base64.b64encode(encrypted).decode()
