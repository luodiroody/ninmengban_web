'''
 AUTH:RODDY
 DATE:2020/4/4
 TIME:11:02
 FILE:basic.py
 '''
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from pywinauto import application
from common.handlelog import log
import  time
class Basefunc ():
    def __init__(self,driver):
        self.driver =driver
    '''查找单个元素'''
    def findele (self,local):
        if isinstance(local,tuple):
            print('正在通过>>>>'+local[0]+'查找元素>>>>'+local[1])
            log.info('正在通过>>>>'+local[0]+'查找元素>>>>'+local[1])
            element = WebDriverWait(self.driver,timeout=30).until(lambda x:x.find_element(*local))
        else :
            print('local参数必须是元组')
        return element
    '''通过select属性,进行选择'''
    def select_value(self,local,value):
        ele=self.findele(local=local)
        Select(ele).select_by_value(value=value)
    '''查找多个元素'''
    def findeles (self,local):
        if isinstance(local,tuple):
            print('正在通过>>>>'+local[0]+'查找元素>>>>'+local[1])
            log.info('正在通过>>>>'+local[0]+'查找元素>>>>'+local[1])
            elements = WebDriverWait(self.driver,timeout=10).until(lambda x:x.find_elements(*local))
        else :
            print('local参数必须是元组')
        return elements
    '''点击元素'''
    def findele_click (self,local):
        self.findele(local).click()
    '''输入参数'''
    def findele_send (self,local,text):
        self.findele(local).send_keys(text)
    '''执行js脚本'''
    def execute_js (self,js,*args):
        self.driver.execute_script(js,*args)
    '''滑动到底部'''
    def js_scroll_end(self):
        js_end = 'window.scrollTo(0,document.body.scrollHeight)'
        self.driver.execute(js_end)
    '''滑动到聚焦元素'''
    def js_scroll_focus(self,local):
        focus=self.findele(local=local)
        js_focus = 'argument[0].scrollIntoview()'
        self.driver.execute(js_focus,focus)
    '''滑动到顶部'''
    def js_scroll_top(self):
        js_top = 'window.scrollTo(0,0)'
        self.driver.execute(js_top)
    '''新建标签页'''
    def new_label(self,url):
        self.driver.execute_script('window.open("{0}")'.format(url))
    '''鼠标悬停'''
    def mouse_hover(self,local):
        ele=self.findele(local=local)
        ActionChains(self.driver).move_to_element(to_element=ele).perform()
    '''键盘操作'''
    def keyboard(self,local):
        self.findele(local=local).send_keys(Keys.ENTER)
    '''上传文件操作(非input标签,只用于Windows平台)'''
    def upload_file(self,file_path):
        time.sleep(2)
        app=application.Application()
        app.connect(class_name='#32770')
        app['Dialog']['Edit1'].type_key(file_path)
        app['Dialog']['Button1'].click()
    '''截图'''
    def sc_(self,filename):
        self.driver.save_screenshot(filename=filename)
if __name__ =='__main__':
    from selenium import webdriver
    driver = webdriver.Firefox()
    driver.get('http://127.0.0.1/zentao/user-login-L3plbnRhby8=.html')
    find = Basefunc(driver)
    local1=('id','account')
    local2=('name','password')
    local3=('id','submit')
    find.findele_send(local1,'admin')
    find.findele_send(local2,'1256')
    find.findele_click(local3)
    time.sleep(3)
    find.is_alet()




