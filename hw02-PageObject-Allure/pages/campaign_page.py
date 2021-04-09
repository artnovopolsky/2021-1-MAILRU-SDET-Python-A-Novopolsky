import os
import logging
import allure
from pages.base_page import BasePage
from locators import CampaignPageLocators

logger = logging.getLogger('test')


class CampaignPage(BasePage):
    locators = CampaignPageLocators()

    @allure.step('Загрузка баннера для рекламной кампании')
    def upload(self, locator):
        file_path = os.path.join(os.path.abspath(''), 'images', 'campaign.jpg')
        upload_field = self.find(locator)
        upload_field.send_keys(file_path)

    def go_to_creation_campaign(self):
        return self.driver.get('https://target.my.com/campaign/new')

    @allure.step('Создание рекламной кампании')
    def create_campaign(self):
        self.go_to_creation_campaign()
        self.click(self.locators.COVERAGE_LOCATOR)
        self.send_message(self.locators.LINK_INPUT_LOCATOR, 'https://vk.com/id1')
        self.click(self.locators.BANNER_IMAGE_LOCATOR)
        self.upload(self.locators.UPLOAD_LOCATOR)
        self.click(self.locators.CREATE_CAMPAIGN_LOCATOR)
        logger.info('Рекламная кампания создана...')
