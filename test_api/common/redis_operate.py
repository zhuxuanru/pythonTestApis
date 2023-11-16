"""
======================
@author:zhuxuanru
@time:2023/7/24 14:54
@email:1435069766@qq.com
======================
"""
import redis


class RedisOperation:
    def __init__(self):
        # 连接Redis
        self.conn = redis.Redis(host="127.0.0.1", port=6379)

    # 获取缓存值
    def get_key(self, name):
        if self.conn.get(name):
            return self.conn.get(name)
        else:
            return False

    # 修改缓存值
    def set_key(self, name, value):
        self.conn.set(name, value)
        return True
