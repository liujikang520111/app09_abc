from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def __init__(self, driver):
        self.driver = driver

    # 定位一个元素
    def cilck_ele(self, loc):
        return WebDriverWait(self.driver, 10, 1).until(lambda x: x.find_element(*loc))

    def cilck_eles(self, loc):
        return WebDriverWait(self.driver, 10, 1).until(lambda x: x.find_elements(*loc))

    def yonghu(self, loc):
        self.cilck_ele(loc).click()

    def send_ele(self, loc, text):
        num = self.cilck_ele(loc)
        num.send_keys(text)

    def duanyan(self, num):
        result = self.cilck_ele(num)
        return [i.text for i in result]
