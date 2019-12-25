from appium import webdriver


def get_driver(pac, act):
    desired_caps = {}
    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = '模拟器'
    # app的信息
    desired_caps['appPackage'] = pac
    desired_caps['appActivity'] = act
    # 声明我们的driver对象
    return webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
