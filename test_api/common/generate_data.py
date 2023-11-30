"""
======================
@author:zhuxuanru
@time:2023/8/31 14:54
@email:1435069766@qq.com
======================
"""

from faker import Faker


class GeneratedData:
    def __init__(self, faker_lang='zh_CN'):
        self.faker_data = Faker(faker_lang)

    # 生成随机姓名
    def generatedName(self):
        return self.faker_data.name()

    # 生成随机手机号码
    def generatedPhone(self):
        return self.faker_data.phone_number()

    # 生成随机的身份证号码
    def generatedIdentity(self):
        return self.faker_data.ssn()

    # 生成随机的银行卡号
    def generatedCard(self):
        return self.faker_data.credit_card_number()

    # 生成随机数
    def generatedRandomNumber(self, n):
        return str(self.faker_data.random_number(n))

