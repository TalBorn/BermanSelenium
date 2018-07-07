from selenium.webdriver.common.by import By

# for maintainability we can seperate web objects by page name

class MainPageLocatars(object):
  LOGO          = (By.XPATH, '//*[@id="logo"]')
  SIGNUP       = (By.XPATH, '//*[@id="content"]/div/div[3]/div/div[1]/nav/div/div[2]/ul[2]/li[2]/button')
  LOGIN         = (By.CSS_SELECTOR, '#signin_button > div > span')
  SEARCH        = (By.ID, 'twotabsearchtextbox')
  SEARCH_LIST   = (By.ID, 's-results-list-atf')
  LANGUAGE_ALERT = (By.XPATH, '//*[@id="selectLanguage"]/div/div/div[3]/button')

class LoginPageLocatars(object):
  EMAIL         = (By.ID, 'user_login')
  PASSWORD      = (By.ID, 'user_password')
  SUBMIT        = (By.ID, 'signin-button')
  ERROR_MESSAGE = (By.XPATH, '//*[@id="signin"]/div[1]/div')

class HomePageLocators(object):
  CHOOSE_PROJECT  = (By.XPATH, '//*[@id="recent-courses"]/div/div[2]/div[5]/div/a/div')
  PROJECT_CHOSEN  = (By.XPATH, '//*[@id="courses-container"]/div/div[3]/div[1]/div[3]/div/div/div[2]/div/a/div')
  ClICKONPROFILE  = (By.XPATH, '//*[@id="sign_in_or_user"]/div/i[1]')
  SIGNOUT         = (By.XPATH, '//*[@id="user-signout"]')
  ABOUT = (By.ID, 'header-en-about')
  ABOUT_PAGE_TITLE = (By.XPATH, '/html/body/div[1]/div[4]/div[1]/div[1]/h1')
