import pytest, os, sys
from Base.geidata import GetData
sys.path.append(os.getcwd())
def get_sum_data():
    sum_list = []
    data = GetData().get_yml_data("value2.yml")
    for i in data.values():
            sum_list.append(tuple(i.values()))
    return sum_list


# # get_sum_data()

class TestSum:
    @pytest.mark.parametrize("a,b,c", get_sum_data())
    def test_sum(self, a, b, c):
        print("{}+{}={}".format(a, b, c))

        assert a + b == c
if __name__ == '__main__':
    pytest.main(["02_test_sum.py"])
import allure


import pytest
class Test_003:
    @allure.step("我是测试步骤")
    def test_003(self):
        allure.attach("文件名字", "文件内容，具体步骤描述信息")
        assert True

    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    def test_003_2(self):
        assert True

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_003_3(self):
        assert False

    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    def test_003_4(self):
        assert True

    @pytest.allure.severity(pytest.allure.severity_level.MINOR)
    def test_003_5(self):
        assert True

    @pytest.allure.severity(pytest.allure.severity_level.TRIVIAL)
    def test_003_6(self):
        assert True



