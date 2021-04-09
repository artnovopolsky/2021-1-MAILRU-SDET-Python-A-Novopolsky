import logging
import allure
from pages.base_page import BasePage
from pages.authorized_page import AuthorizedPage
from locators import UnauthorizedPageLocators

logger = logging.getLogger('test')


class UnauthorizedPage(BasePage):
    locators = UnauthorizedPageLocators()

    @allure.step('Авторизация. E-mail: {email}. Password: {password}')
    def login(self, email='artemnvp@rambler.ru', password='1artemnvp@rambler.ru'):
        self.click(self.locators.SIGN_IN_LOCATOR)
        self.send_message(self.locators.EMAIL_LOCATOR, email)
        self.send_message(self.locators.PASSWORD_LOCATOR, password)
        self.click(self.locators.ENTER_LOCATOR)

        if self.driver.current_url == 'https://target.my.com/dashboard':
            logger.info(f'Авторизация (e-mail: {email} password: {password}) прошла успешно...')
            return AuthorizedPage(self.driver)
        else:
            logger.info(f'Авторизация (e-mail: {email} password: {password}) не удалась.')
