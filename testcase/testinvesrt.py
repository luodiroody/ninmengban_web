'''
 AUTH:RODDY
 DATE:2020/4/12
 TIME:17:13
 FILE:testinvesrt.py
 '''
import time

from common.basisfunc import Basefunc
from pages.home_page import HomePage
from pages.inves_page import InvesPage
from pages.login_page import LoginPage
from pages.user_page import UserPage

url='http://120.78.128.25:8765/Index/login.html'
url_homepage='http://120.78.128.25:8765/Index/index.html'
import unittest
from selenium import webdriver
class TestInvesrt(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.get(url=url)
        cls.loginpage=LoginPage(driver=cls.driver)
        cls.loginpage.login()
        cls.homepage=HomePage(driver=cls.driver)
        cls.userpage=UserPage(driver=cls.driver)
        cls.investpage=InvesPage(driver=cls.driver)
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    def setUp(self):
        #self.driver.get(url=url_homepage)
        self.driver.maximize_window()
    def tearDown(self):
        self.driver.refresh()
    def test_invesrt(self):
        time.sleep(10)
        self.homepage.into_user_page()
        befor_money=self.userpage.available_balance()
        print(befor_money)
        self.driver.back()
        self.homepage.tender()
        self.investpage.investment_amount('200')
        self.investpage.submit_tender()
        self.investpage.tender_success()
        after_money=self.userpage.available_balance()
        print(after_money)


