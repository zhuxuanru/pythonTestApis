"""
======================
@author:zhuxuanru
@time:2023/7/17 11:19
@email:1435069766@qq.com
======================
"""
import pytest
import os

path = os.path.dirname(__file__)
# f"{path}/test_case/test_login.py::Test_login"
if __name__ == "__main__":
	pytest.main(['--alluredir=./report/xml'])