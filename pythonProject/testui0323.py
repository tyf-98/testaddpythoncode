import os

import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def findElement(driver,locator,time=10):
    type,value=locator
    element=WebDriverWait(driver,time).until(lambda x:x.find_element(type,value))
    return element

# 测试文件以test_开头
# 测试类以Test开头，并且不能带有 __init__ 方法
# 测试函数以test开头
# 断言使用assert
class TestClass:
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.baidu.com')
    def test1(self):
        self.driver.find_element(By.ID, 'kw').send_keys('python')
        self.driver.find_element(By.ID, 'su').click()
        # sleep(10)
        msg = findElement(self.driver,(By.XPATH,'/html/body/div[3]/div[4]/div[1]/div[3]/div[2]/div/div[1]/div[1]/h3/a[1]')).text
        # msg = self.driver.find_element(By.XPATH, '/html/body/div[3]/div[4]/div[1]/div[3]/div[2]/div/div[1]/div[1]/h3/a[1]').text
        print(msg)
        assert 'Python' in msg

        # msg = findElement(
        #     self.driver,
        #     (By.XPATH, '//h3[contains(@class, "t")]/a[1]')
        # ).text
        # print("实际文本:", msg)
        # assert 'Python' in msg, f"断言失败：'{msg}' 中不包含 'Python'"

    def teardown_class(self):
        self.driver.quit()  # 确保测试结束后关闭浏览器

# class TestClass:
#     def test1(self):
#         assert True  # 空测试
if __name__ == '__main__':
    report_path = os.path.abspath(r'F:\testui\pythonProject\reports\report.html')
    report_dir = os.path.dirname(report_path)
    os.makedirs(report_dir, exist_ok=True)  # 确保目录存在
    print(f"测试报告路径: {report_path}")  # 调试输出
    pytest.main(['-s', __file__, f'--html={report_path}', '--self-contained-html'])

# import os
# import pytest
#
#
# class TestClass:
#     def test1(self):
#         assert True
#
#
# if __name__ == '__main__':
#     # 强制使用绝对路径
#     report_dir = os.path.abspath(r'F:\testui\pythonProject\reports')
#     os.makedirs(report_dir, exist_ok=True)
#     report_path = os.path.join(report_dir, 'report.html')
#
#     # 调试输出
#     print(f"报告路径: {report_path}")
#     print(f"当前工作目录: {os.getcwd()}")
#
#     # 运行测试并生成报告
#     exit_code = pytest.main(['-s', '-v', __file__, f'--html={report_path}', '--self-contained-html'])
#     print(f"pytest 退出码: {exit_code}")