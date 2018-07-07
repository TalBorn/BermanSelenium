from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from base import Page
from locator import *
import users
import pdb
import  time
from selenium.webdriver.support.ui import WebDriverWait


# Page objects are written in this module.
# Depends on the page functionality we can have more functions for new classes


class MainPage(Page):
    def __init__(self, driver):
        self.locator = MainPageLocatars
        super(MainPage, self).__init__(driver)

    def check_page_loaded(self):
        return True if self.find_element(*self.locator.LOGO) else False

    def search_item(self, item):
        self.find_element(*self.locator.SEARCH).send_keys(item)
        self.find_element(*self.locator.SEARCH).send_keys(Keys.ENTER)
        return self.find_element(*self.locator.SEARCH_LIST).text
    '''
    def click_sign_up_button(self):
        self.find_element(*self.locator.SIGNUP).click()
        return SignUpPage(self.driver)
    '''
    def click_sign_in_button(self):
        time.sleep(4)
        self.find_element(*self.locator.LANGUAGE_ALERT).click()
        time.sleep(2)
        self.find_element(*self.locator.LOGIN).click()
        time.sleep(2)
        return LoginPage(self.driver)


class LoginPage(Page):
    def __init__(self, driver):
        self.locator = LoginPageLocatars
        super(LoginPage, self).__init__(driver)  # Python2 version

    def enter_email(self, user):
        self.find_element(*self.locator.EMAIL).send_keys(users.get_user(user)["email"])

    def enter_password(self, user):
        self.find_element(*self.locator.PASSWORD).send_keys(users.get_user(user)["password"])

    def click_login_button(self):
        self.find_element(*self.locator.SUBMIT).click()

    def login(self, user):
        self.enter_email(user)
        self.enter_password(user)
        self.click_login_button()

    def login_with_valid_user(self, user):
        self.login(user)
        return HomePage(self.driver)

    def login_with_in_valid_user(self, user):
        self.login(user)
        return self.find_element(*self.locator.ERROR_MESSAGE).text


class HomePage(Page):
    def __init__(self, driver):
        self.locator = HomePageLocators
        #super(MainPage).__init__(driver)  # Python3 version
        super(HomePage, self).__init__(driver)
    def click_choose_project(self):
        time.sleep(3)
        self.find_element(*self.locator.CHOOSE_PROJECT).click()

    def click_chosen_project(self):
        time.sleep(3)
        self.find_element(*self.locator.PROJECT_CHOSEN).click()

    def click_sign_out(self):
        self.find_element(*self.locator.ClICKONPROFILE).click()
        time.sleep(3)
        self.find_element(*self.locator.SIGNOUT).click()

    '''def about_company(self):
        self.find_element(*self.locator.ABOUT).click()
        time.sleep(3)
        title = self.find_element(*self.locator.ABOUT_PAGE_TITLE)
        if not title.getText() == 'About Us':
            assert "Title  not found"
    '''




class SignUpPage(Page):
    pass