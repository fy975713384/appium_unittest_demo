from selenium.webdriver.remote.webelement import WebElement
from util.read_conf import ReadConf
from driver.base_driver import BaseDriver
from conf.setting import Setting as ST


class Element:

    def __init__(self, sec: str):
        self.read_data = ReadConf()
        self.sec = sec
        self.driver = BaseDriver(ST.DEVICENAME, ST.PORT, ST.APP_PATH).driver

    def get_element(self, key: str) -> WebElement:
        data = self.read_data.get_value(self.sec, key)
        if data is not None:
            by, expr = data.split('|')
            by, expr = by.strip(), expr.strip()
            if by == 'id':
                return self.driver.find_element_by_id(expr)
            elif by == 'ac_id':
                return self.driver.find_element_by_accessibility_id(expr)
            else:
                return self.driver.find_element_by_xpath(expr)
