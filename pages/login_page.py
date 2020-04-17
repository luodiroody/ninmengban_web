'''
 AUTH:RODDY
 DATE:2020/4/4
 TIME:11:11
 FILE:login_page.py
 '''
from selenium import webdriver
from selenium.webdriver.common.by import By
from common.basisfunc import Basefunc
class LoginPage(Basefunc):
    '''
    :param local_user :登录框定位参数
    :param local_pwd :密码框定位
    :param local_submit :登录按钮
    :param local_userorpwd_error : 手机号(请输入手机号,请输入正确的手机号,)
    :param local_userandpwd_error : (此账号没有经过授权，请联系管理员! div class="layui-layer-content"  ,帐号或密码错误!div class="layui-layer-content")
    '''
    local_user=(By.XPATH,'//input[@class="form-control username"]')
    local_pwd=(By.XPATH,'//input[@type="password"]')
    local_submit=(By.XPATH,'//button[@type="button"]')
    local_userorpwd_error=(By.XPATH,'//div[@class="form-error-info"]')
    local_userandpwd_error=(By.XPATH,'//div[@class="layui-layer-content"]')
    def login(self,username='18684720553',pwd='python'):
        self.findele_send(local=self.local_user,text=username)
        self.findele_send(local=self.local_pwd,text=pwd)
        self.findele_click(local=self.local_submit)
    def login_userorpwd_error(self):
        error_ele=self.findele(local=self.local_userorpwd_error)
        return error_ele.text
    def login_userandpwd_error(self):
        error_ele=self.findele(local=self.local_userandpwd_error)
        return error_ele.text
if __name__ =='__main__':
    driver = webdriver.Firefox()
    driver.get('http://120.78.128.25:8765/Index/login.html')
    loginpage=LoginPage(driver)
    loginpage.login('18684720553','5555')
    print(loginpage.login_userandpwd_error())
    driver.quit()

