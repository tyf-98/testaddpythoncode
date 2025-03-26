import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import selenium

# file_name: test_abc.py
import pytest  # 引入pytest包


def test_a():  # test开头的测试函数
    print("------->test_a")
    assert 1  # 断言成功


def test_b():
    print("------->test_b")
    assert 1  # 断言失败

def test_c():
    print("------->test_b")
    assert 1  # 断言失败


if __name__ == '__main__':
    pytest.main(['-s','test_0324.py'])  # 调用pytest的main函数执行测试