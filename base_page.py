# Gong
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    # 类变量
    _driver = None
    _base_url = ''

    def __init__(self, driver: WebDriver = None):
        # 判读传的driver是否为空
        if driver is None:
            # 让driver初始化
            options = Options()
            options.debugger_address = '127.0.0.1:9333'
            self._driver = webdriver.Chrome(options=options)
            # 所有的查元素自动触发隐式等待
            self._driver.implicitly_wait(3)

        else:
            self._driver = driver

        # 判url是否为空,不为空时就执行
        if self._base_url != '':
            self._driver.get(self._base_url)

    # 封装查元素，需要两个参数（“by”：定位方式，“locator“：定位的值）
    def find(self, by, locator):
        return self._driver.find_element(by, locator)

    def finds(self, by, locator):
        # find_elements:返回多个
        return self._driver.find_elements(by, locator)

    # 显示等待，指定具体的操作满足条件时退出，不满足条件时在”time“时间内轮询查找，每0.5秒轮询一次
    def waif_for_click(self, locator, time=10):
        WebDriverWait(self._driver, time).until(expected_conditions.element_to_be_clickable(locator))



