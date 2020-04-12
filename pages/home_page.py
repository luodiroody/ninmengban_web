'''
 AUTH:RODDY
 DATE:2020/4/4
 TIME:15:25
 FILE:home_page.py
 '''
from selenium.webdriver.common.by import By
from common.basisfunc import Basefunc
local_uesrname=(By.XPATH,'//a[@href="/Member/index.html"]')
class HomePage(Basefunc):
    def login_success(self):
        user_ele=self.findele(local=self.local_uesrname)
        return user_ele.text