import os
import logging
import allure
from faker import Faker
from pages.base_page import BasePage
from locators import CampaignPageLocators

logger = logging.getLogger('test')


class CampaignPage(BasePage):
    locators = CampaignPageLocators()
    fake = Faker()

    @allure.step('Загрузка баннера для рекламной кампании')
    def upload(self, locator):
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'images', 'campaign.jpg'))
        upload_field = self.find(locator)
        upload_field.send_keys(file_path)

    def go_to_creation_campaign(self):
        return self.driver.get('https://target.my.com/campaign/new')

    def create_campaign_name(self):
        return self.fake.bothify(text='???-#########-???-###-????')

    @allure.step('Создание рекламной кампании')
    def create_campaign(self, name):
        self.go_to_creation_campaign()
        self.click(self.locators.COVERAGE_LOCATOR)
        self.send_message(self.locators.LINK_INPUT_LOCATOR, 'https://vk.com/id1')
        self.send_message(self.locators.CAMPAIGN_NAME_LOCATOR, name)
        self.click(self.locators.BANNER_IMAGE_LOCATOR)
        self.upload(self.locators.UPLOAD_LOCATOR)
        self.click(self.locators.CREATE_CAMPAIGN_LOCATOR)
        logger.info('Рекламная кампания создана...')
