# Gong
import shelve
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

class TestBase():

    def setup(self):
        # 浏览器复用
        options = Options()
        options.debugger_address = '127.0.0.1:9333'
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(5)

    def teardown(self):
        # 退出
        self.driver.quit()

    def test_chrome(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # ‘shelve’ python自带的数据库
        db = shelve.open("")
        # 获取当前页面的cookies，会生成三个文件
        db['cookie'] = self.driver.get_cookies()
        cookies = db['cookie']
        # 添加cookies
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        sleep(5)
        # 关闭文件
        db.close()
        # 点击通讯录
        self.driver.find_element_by_id('menu_contacts').click()
        sleep(3)
