'''
 AUTH:RODDY
 DATE:2020/4/4
 TIME:15:25
 FILE:home_page.py
 '''
import time
from selenium.webdriver.common.by import By
from common.basisfunc import Basefunc

class HomePage(Basefunc):
    '''
    :param local_uesrname 用户定位
    :param local_tender 投标用户定位
    '''
    local_uesrname=(By.XPATH,'//a[@href="/Member/index.html"]')
    local_uesrname_into=(By.XPATH,'//a[@href="/Member/index.html"]//img')
    local_tender=(By.XPATH,'//a[@class="btn btn-special"]')
    local_investment_amount=(By.XPATH,'//input[@class="form-control invest-unit-investinput"]')
    local_tender_button=(By.XPATH,'//button[@class="btn btn-special height_style"]')
    local_tender_success=(By.XPATH,'//div[@class="layui-layer-content"]//button')
    def login_success(self):
        user_ele=self.findele(local=self.local_uesrname)
        return user_ele.text
    def into_user_page(self):
        self.findele_click(local=self.local_uesrname_into)
    def tender(self):
        self.findele_click(self.local_tender)






