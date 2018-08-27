import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class HomePage(BaseAction):
    mine_btn = (By.XPATH, "//*[@text='我的' and @resource-id = 'com.tpshop.malls:id/tab_txtv']")

    @allure.step(title="点击首页-我的")
    def click_mine_btn(self):
        self.click(self.mine_btn)
