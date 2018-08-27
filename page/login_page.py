import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class LoginPage(BaseAction):
    username_input = (By.ID, "com.tpshop.malls:id/edit_phone_num")
    password_input = (By.ID, "com.tpshop.malls:id/edit_password")
    login_btn = (By.ID, "com.tpshop.malls:id/btn_login")
    # 显示密码
    view_pwd_btn = (By.ID, "com.tpshop.malls:id/img_view_pwd")

    @allure.step(title="输入用户名")
    def input_username(self, text):
        allure.attach('用户名：' + text, "")
        self.input(self.username_input, text)

    @allure.step(title="输入密码")
    def input_password(self, text):
        allure.attach('密码：' + text, "")
        self.input(self.password_input, text)

    @allure.step(title="点击登录")
    def click_login_btn(self):
        self.click(self.login_btn)

    @allure.step(title="点击显示密码")
    def click_view_pwd_btn(self):
        self.click(self.view_pwd_btn)

    @allure.step(title="判断button是否可点")
    def is_login_btn_enabled(self):
        self.is_enabled(self.login_btn)
