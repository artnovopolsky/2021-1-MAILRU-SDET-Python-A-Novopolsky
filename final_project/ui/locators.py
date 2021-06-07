from selenium.webdriver.common.by import By


class AuthorizationPageLocators:
    USERNAME = (By.XPATH, "//input[@id='username' and @required]")
    PASSWORD = (By.XPATH, "//input[@id='password' and @required]")

    LOGIN_BUTTON = (By.XPATH, "//input[@name='submit']")

    INCORRECT_ERROR_MESSAGE = (By.XPATH, "//div[@id='flash' and text()='Incorrect username length']")
    INVALID_ERROR_MESSAGE = (By.XPATH, "//div[@id='flash' and text()='Invalid username or password']")
    BLOCK_MESSAGE = (By.XPATH, "//div[@id='flash' and text()='Ваша учетная запись заблокирована']")

    REGISTRATION_BUTTON = (By.XPATH, "//a[@href='/reg']")


class RegistrationPageLocators:
    REG_USERNAME = (By.XPATH, "//input[@id='username' and @required]")
    REG_PASSWORD = (By.XPATH, "//input[@id='password' and @required]")

    REG_EMAIL = (By.XPATH, "//input[@id='email']")
    REG_EMAIL_VALID = (By.XPATH, "//input[@id='email' and @required]")

    REPEAT_PASSWORD = (By.XPATH, "//input[@id='confirm']")
    REPEAT_PASSWORD_VALID = (By.XPATH, "//input[@id='confirm' and @required]")

    ACCEPT_CHECKBOX = (By.XPATH, "//input[@id='term' and @required]")
    REGISTER_BUTTON = (By.XPATH, "//input[@name='submit' and @value='Register']")
    GO_TO_LOGIN_BUTTON = (By.XPATH, "//a[@href='/login']")

    USERNAME_ERROR = (By.XPATH, "//div[@id='flash' and text()='Incorrect username length']")  # При вводе слишком короткого и длинного юзернейма
    INVALID_EMAIL_ERROR = (By.XPATH, "//div[@id='flash' and text()='Invalid email address']")  # Если не дописал @ya.ru
    INCORRECT_EMAIL_LENGTH = (By.XPATH, "//div[@id='flash' and text()='Incorrect email length']")  # Если не дописал .ru в конце
    PASSWORD_NOT_MATCH_ERROR = (By.XPATH, "//div[@id='flash' and text()='Passwords must match']")  # Пароли должны совпадать

    ALL_FIELD_ERROR_MESSAGE = (By.XPATH, "//div[contains(text(), ']}')]")  # При неправильном вводе более чем одного поля
                                                                           # сообщение об ошибке некрасивое!!!


class MainPageLocators:
    TM_BUTTON = (By.XPATH, "//a[contains(@class, 'uk-navbar-brand')]")
    HOME_BUTTON = (By.XPATH, "//a[text()='HOME']")

    PYTHON_BUTTON = (By.XPATH, "//a[text()='Python']")
    PYTHON_HISTORY = (By.XPATH, "//a[text()='Python history']")
    ABOUT_FLASK = (By.XPATH, "//a[text()='About Flask']")

    LINUX_BUTTON = (By.XPATH, "//a[text()='Linux']")
    DOWNLOAD_CENTOS = (By.XPATH, "//a[text()='Download Centos7']")  # Ведёт на скачивание Fedora

    NETWORK_BUTTON = (By.XPATH, "//a[text()='Network']")
    WIRESHARK_NEWS = (By.XPATH, "//a[text()='News']")
    DOWNLOAD_WIRESHARK = (By.XPATH, "//a[text()='Download']")
    TCPDUMP_EXAMPLES = (By.XPATH, "//a[text()='Examples ']")

    LOGGED_AS = (By.XPATH, "//li[contains(text(), 'Logged as')]")
    VK_ID = (By.XPATH, "//li[contains(text(), 'VK ID')]")
    VK_ID_NONE = (By.XPATH, "//div[@id='login-name']/ul/li[2][text()='']")
    LOGOUT_BUTTON = (By.XPATH, "//a[@href='/logout']")

    API_BUTTON = (By.XPATH, "//img[@src='/static/images/laptop.png']")
    FUTURE_OF_INTERNET = (By.XPATH, "//img[@src='/static/images/loupe.png']")
    SMTP = (By.XPATH, "//img[@src='/static/images/analytics.png']")

    PYTHON_ZEN_QUOTE = (By.XPATH, "//div[contains(@class, 'uk-text-center')]/p[2]")
