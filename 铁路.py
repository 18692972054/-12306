
from datetime import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import json

import time






class Train:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def login(self):
        '''
        登录 如果有cookie文件就直接登录，没有就扫码登录并保存cookie
        :return:
        '''
        self.driver.get("https://www.12306.cn/index/index.html")
        self.driver.find_element(By.LINK_TEXT, '登录').click()
        if os.path.exists('cookies.json'):
            with open('cookies.json', 'r') as f:
                cookies = json.load(f)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            self.driver.refresh()
            self.driver.get("https://kyfw.12306.cn/otn/view/index.html")
        else :
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "扫码登录"))
            )
            element.click()
            WebDriverWait(self.driver, 120).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "退出"))
            )
            with open('cookies.json', 'w') as f:
                json.dump(self.driver.get_cookies(), f)
        time.sleep(5)

        '''
        在使用cookies自动登录后，会发现登录信息丢失了
        为啥我点一下’ 首页’登录信息就没了 ？？？？？？
        为啥我点一下’ 首页’登录信息就没了 ？？？？？？
        为啥我点一下’ 首页’登录信息就没了 ？？？？？？
        '''

        self.driver.find_element(By.LINK_TEXT, '首页').click()
        time.sleep(4)


    def quit(self):
        self.driver.quit()
    def run(self):
        self.login()
        self.quit()



if __name__ == '__main__':
    train = Train()
    train.run()