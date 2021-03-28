from selenium.webdriver.common.by import By

# BASIC LOCATORS
# Locators for log in
SIGN_IN_LOCATOR = (By.XPATH, "//div[contains(@class, 'responseHead-module-button')]")
EMAIL_LOCATOR = (By.XPATH, "//input[@name='email']")
PASSWORD_LOCATOR = (By.XPATH, "//input[@name='password']")
ENTER_LOCATOR = (By.XPATH, "//div[contains(@class, 'authForm-module-button')]")

# Locators for log out
USER_INFO_LOCATOR = (By.XPATH, "//div[contains(@class, 'right-module-rightButton')]")
LOG_OUT_LOCATOR = (By.XPATH, "//a[@href='/logout']")

# Locators for transition to profile page
PROFILE_LOCATOR = (By.XPATH, "//a[@href='/profile']")
STATISTICS_LOCATOR = (By.XPATH, "//a[contains(@class, 'center-module-statistics')]")
PRO_LOCATOR = (By.XPATH, "//a[contains(@class, 'center-module-pro')]")

# Locators for change profile info
FIO_LOCATOR = (By.XPATH, "//div[@data-name='fio']/div/input")
PHONE_LOCATOR = (By.XPATH, "//div[@data-name='phone']/div/input")
CHANGE_EMAIL_LOCATOR = (By.XPATH, "//div[contains(@class, 'email')]/div/div/input")
SAVE_LOCATOR = (By.XPATH, "//div[contains(@class, 'button') and contains(text(), 'Сохранить')]")
