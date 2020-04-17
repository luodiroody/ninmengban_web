'''
 AUTH:RODDY
 DATE:2020/4/12
 TIME:12:44
 FILE:user_page.py
 '''
from selenium.webdriver.common.by import By

from common.basisfunc import Basefunc
class UserPage(Basefunc):
    '''
:param local_available_balance 可用余额定位
'''
    local_available_balance=(By.XPATH,'//ul[@class="per_list_right"]//li[@class="color_sub"]')

    def available_balance(self):
        element=self.findele(self.local_available_balance)
        money = element.text
        return money[:-1]


