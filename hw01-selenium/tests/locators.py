# BASIC LOCATORS
# Locators for log in
SIGN_IN_LOCATOR = "//div[contains(@class, 'responseHead-module-button')]"
EMAIL_LOCATOR = "//input[@name='email']"
PASSWORD_LOCATOR = "//input[@name='password']"
ENTER_LOCATOR = "//div[contains(@class, 'authForm-module-button')]"

# Locators for log out
USER_INFO_LOCATOR = "//div[contains(@class, 'right-module-rightButton')]"
LOG_OUT_LOCATOR = "//a[@href='/logout']"

# Locators for transition to profile page
PROFILE_LOCATOR = "//a[@href='/profile']"
STATISTICS_LOCATOR = "//a[contains(@class, 'center-module-statistics')]"
PRO_LOCATOR = "//a[contains(@class, 'center-module-pro')]"

# Locators for change profile info
FIO_LOCATOR = "//div[@data-name='fio']/div/input"
PHONE_LOCATOR = "//div[@data-name='phone']/div/input"
CHANGE_EMAIL_LOCATOR = "//div[contains(@class, 'email')]/div/div/input"
SAVE_LOCATOR = "//div[contains(@class, 'button') and contains(text(), 'Сохранить')]"
