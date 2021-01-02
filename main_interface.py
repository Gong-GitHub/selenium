# Gong
from selenium.webdriver.common.by import By
from selenium1.selenium_qywx_main.page.add_menber import AddMenber
from selenium1.selenium_qywx_main.page.base_page import BasePage


class Main(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame"

    def goto_add_member(self):
        # 点击”通讯录“
        self.find(By.XPATH, '//*[@id="menu_contacts"]/span').click()
        # ”locator“：下一个要点击的元素
        locator = (By.CSS_SELECTOR, '.js_has_member>div:nth-child(1) a:nth-child(2)')
        self.waif_for_click(locator)
        self.find(By.CSS_SELECTOR, '.js_has_member>div:nth-child(1) a:nth-child(2)').click()
        return AddMenber(self._driver)