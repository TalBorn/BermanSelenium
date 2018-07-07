import unittest
from selenium import webdriver
from pages import *
from testcases import test_cases
from locator import *
from selenium.webdriver.common.by import By
import os


# I am using python unittest for asserting cases.
# In this module, there should be test cases.
# If you want to run it, you should type: python <module-name.py>

class TestPages(unittest.TestCase):

    def setUp(self):
        chromedriver = "C:\work\Automation\PO\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_experimental_option("prefs", {"download.prompt_for_download": True})
        self.driver = webdriver.Chrome(chromedriver, chrome_options=options)
        self.driver.get("https://code.org/")

    def test_page_load(self):
        print "\n" + str(test_cases(0))
        page = MainPage(self.driver)
        self.assertTrue(page.check_page_loaded())


    def test_sign_in_button(self):
        print "\n" + str(test_cases(1))
        page = MainPage(self.driver)
        page.click_sign_in_button()

    def test_sign_in_with_valid_user(self):
        print "\n" + str(test_cases(2))
        mainPage = MainPage(self.driver)
        loginPage = mainPage.click_sign_in_button()
        result = loginPage.login_with_valid_user("valid_user")

    def test_sign_in_with_in_valid_user(self):
        print "\n" + str(test_cases(3))
        mainPage = MainPage(self.driver)
        loginPage = mainPage.click_sign_in_button()
        result = loginPage.login_with_in_valid_user("invalid_user")

    def test_choose_project(self):
        print "\n" + str(test_cases(4))
        mainPage = MainPage(self.driver)
        homePage = HomePage(self.driver)
        loginPage = mainPage.click_sign_in_button()
        loginPage.login_with_valid_user("valid_user")
        homePage.click_choose_project()
        homePage.click_chosen_project()

    def test_log_out(self):
        print "\n" + str(test_cases(5))
        mainPage = MainPage(self.driver)
        homePage = HomePage(self.driver)
        loginPage = mainPage.click_sign_in_button()
        loginPage.login_with_valid_user("valid_user")
        homePage.click_sign_out()
    '''
    def about_the_company(self):
        print "\n" + str(test_cases(6))
        mainPage = MainPage(self.driver)
        homePage = HomePage(self.driver)
        homePage.about_company()
    '''

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPages)
    unittest.TextTestRunner(verbosity=2).run(suite)