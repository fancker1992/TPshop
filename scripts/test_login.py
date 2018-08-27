import random

import allure
import pytest
import time

from allure.constants import AttachmentType
from selenium.webdriver.common.by import By

from base.base_dirver import init_driver
from base.read_data_yml import read_data
from page.page import Page


def get_random_str():
    string = ""
    for i in range(8):
        string += str(random.randint(0, 9))
    return string


def get_list_data():
    temp_list = list()
    for i in range(2):
        temp_list.append(get_random_str())
    return temp_list


class TestLogin:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("args", read_data("login_data", "test_login"))
    def test_login(self, args):
        self.page.home_page.click_mine_btn()
        self.page.mine_page.click_login_sign_up()
        self.page.login_page.input_username(args["username"])
        self.page.login_page.input_password(args["password"])
        self.page.login_page.click_login_btn()
        assert self.page.login_page.is_toast_exist(args["expect"])

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("args", read_data("login_data", "test_login_btn_enable"))
    def test_login_btn_enable(self, args):
        self.page.home_page.click_mine_btn()
        self.page.mine_page.click_login_sign_up()
        self.page.login_page.input_username(args["username"])
        self.page.login_page.input_password(args["password"])
        assert not self.page.login_page.is_login_btn_enabled()

    # 只有随机的字符串才能确保不受页面其他因素影响
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("password", get_list_data())
    def test_show_password(self, password):
        password_input = (By.XPATH, "//*[@text='%s']" % password)
        self.page.home_page.click_mine_btn()
        self.page.mine_page.click_login_sign_up()
        self.page.login_page.input_password(password)

        # 输入完后先判断下是否可见   断言 false 就停止   TRUE  就继续执行
        assert not self.page.login_page.is_element_exist(password_input)
        self.page.login_page.click_view_pwd_btn()
        # 截图
        allure.attach("显示密码：", self.driver.get_screenshot_as_png(), AttachmentType.PNG)

        assert self.page.login_page.is_element_exist(password_input)
