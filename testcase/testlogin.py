'''
 AUTH:RODDY
 DATE:2020/4/4
 TIME:15:33
 FILE:testlogin.py
 '''
import unittest
import os
from libray.ddt import ddt,data
from selenium import webdriver

from pages.home_page import HomePage
from pages.login_page import LoginPage
from common.readexcel import ReadExcel
from common.config import conf
from common.dirpath import DATAPATH
@ddt
class TestLogin(unittest.TestCase):
    userorpwd=ReadExcel(filename=os.path.join(DATAPATH,conf.get('workbook','name')),
                        sheetname=conf.get('workbook','sheet01'))
    cases=userorpwd.read_excel()
    print(cases)
    def setUp(self):
        self.driver= webdriver.Firefox()
        self.driver.get('http://120.78.128.25:8765/Index/login.html')
    def tearDown(self):
        self.driver.quit()
    @data(*cases)
    def test_login_or(self,case):
        data=eval(case['data'])
        phone=data['phone']
        pwd=data['pwd']
        expect=data['expect']
        loginpage=LoginPage(self.driver)
        loginpage.login(username=phone,pwd=pwd)
        homepage=HomePage(self.driver)
        if case['error']=='1':
            actual=loginpage.login_userorpwd_error()
            try :
                self.assertEqual(actual,expect)
            except AssertionError as e:
                raise e
        elif case['error']=='2':
            actual=loginpage.login_userandpwd_error()
            try :
                self.assertEqual(actual,expect)
            except AssertionError as e:
                raise e
        elif case['error']=='3':
            actual=homepage.login_success()
            try :
                self.assertEqual(actual,expect)
            except AssertionError as e:
                raise e

if __name__ =='__main__':
    unittest.main()

