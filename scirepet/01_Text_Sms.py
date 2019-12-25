from appium import webdriver
import pytest
from selenium.webdriver.common.by import By

from Base.base import Base
from Base.getDriver import get_driver


class Test_Sms:
    def setup_class(self):
        self.driver = get_driver("com.android.mms", ".ui.ConversationList")
        self.input_obj = Base(self.driver)

        self.click = (By.ID, "com.android.mms:id/from")
        self.input = (By.CLASS_NAME, "android.widget.EditText")
        self.click_fasong = (By.ID, "com.android.mms:id/send_button_sms")
        self.dy = (By.ID, "com.android.mms:id/text_view")

    def teardown_class(self):
        self.driver.quit()

    @pytest.fixture(scope="class", autouse=True)
    def test_sms(self):
        self.input_obj.yonghu(self.click)

    @pytest.mark.parametrize("num", [1, 2, 3])
    def test_input(self, num):
        self.input_obj.send_ele(self.input, text=num)
        self.input_obj.yonghu(self.click_fasong)
        assert num in self.input_obj.duanyan(self.dy)


if __name__ == '__main__':
    pytest.main(["01_Text_Sms.py"])
