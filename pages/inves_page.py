'''
 AUTH:RODDY
 DATE:2020/4/12
 TIME:21:33
 FILE:inves_page.py
 '''
from selenium.webdriver.common.by import By
import time
from common.basisfunc import Basefunc
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
class InvesPage(Basefunc):
    '''
    :param local_investment_amount 投资输入框定位
    :param local_tender_button 投标按钮   //*[@class="btn btn-special height_style"]
    '''
    local_investment_amount=(By.XPATH,'//input[@class="form-control invest-unit-investinput"]')
    local_tender_button=(By.XPATH,'//button[@class="btn btn-special height_style"]')
    local_tender_success=(By.XPATH,'//div[@class="layui-layer-content"]//button')
    local_tender_sco=(By.XPATH,'//div[@class="capital_allot"]')
    def investment_amount(self,text):
        self.findele_send(local=self.local_investment_amount,text=text)
    def submit_tender(self):
        self.findele_click(local=self.local_tender_button)
        ele=WebDriverWait(self.driver,60).until(EC.element_to_be_clickable(self.local_tender_button))
        ele.click()
        #self.execute_js('document.getElementsByClassName("btn btn-special height_style")[0].click();')
    def tender_success(self):
        #self.findele_click(local=self.local_tender_success)
        time.sleep(10)
        #self.js_scroll_focus(self.local_tender_sco)
        ele=WebDriverWait(self.driver,30).until(EC.element_to_be_clickable(self.local_tender_success))
        ele.click()
        #self.execute_js('document.getElementsByClassName("//div[@class="layui-layer-content"]//button")[0].click();')