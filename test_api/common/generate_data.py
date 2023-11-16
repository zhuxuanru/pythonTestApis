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

    def generatedName(self):
        return self.faker_data.name()

    def generatedPhone(self):
        return self.faker_data.phone_number()

    def generatedIdentity(self):
        return self.faker_data.ssn()

    def generatedCard(self):
        return self.faker_data.credit_card_number()

    def generatedRandomNumber(self, n):
        return str(self.faker_data.random_number(n))

