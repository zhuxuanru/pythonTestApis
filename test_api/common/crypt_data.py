"""
======================
@author:zhuxuanru
@time:2023/3/29 14:49
@email:1435069766@qq.com
======================
"""
import base64
import hashlib

from Crypto.Cipher import AES


class AesCrypt:
    def __init__(self):
        self.key = "AAJYhFL6jrZJ6QhH".encode("utf-8")
        self.size = AES.block_size
        self.cipher = AES.new(self.key, AES.MODE_ECB)

    def pad(self, text):
        """
        填充函数：要加密的内容要是AES.block_size的倍数
        1.获取要加密数据的长度
        2.判断该长度是否为block_size的倍数
            如果不是，block_size-要加密参数的长度%block_size的余数
        :param text: 要加密的参数
        :return:返回处理完成的要加密的数据
        """
        cont = text.encode("utf-8")
        if len(cont) % self.size != 0:
            add = self.size - len(cont) % self.size
            texts = text + chr(add) * add
            return texts
        else:
            return text

    def encryptData(self, text):
        """
        加密函数
        :param text: 要加密的数据
        :return: 加密完成的数据
        """
        msg = self.cipher.encrypt(self.pad(text).encode("utf-8"))
        return str(base64.b64encode(msg), encoding="utf-8")

    def decryptData(self, text):
        """
        解密函数：要解密的数据必须为2的倍数
        :param text: 需要解密的数据
        :return: 解密完成的数据
        """
        if len(text) % 2 == 0:
            msg = self.cipher.decrypt(base64.b64decode(text))
            requestData = msg.decode("utf-8")[0:msg.decode("utf-8").index("}")+1]
            return requestData
        else:
            cont = text + "="
            msg = self.cipher.decrypt(base64.b64decode(cont))
            requestData = msg.decode("utf-8")[0:msg.decode("utf-8").index("}")+1]
            return requestData


def MD5_encode(content):
    md = hashlib.md5()
    md.update(content.encode("utf-8"))
    return md.hexdigest().upper()
