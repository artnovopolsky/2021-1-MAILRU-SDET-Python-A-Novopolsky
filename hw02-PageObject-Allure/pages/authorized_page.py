import allure
from pages.base_page import BasePage
from pages.campaign_page import CampaignPage
from pages.segment_page import SegmentPage
from locators import AuthorizedPageLocators


class AuthorizedPage(BasePage):

    locators = AuthorizedPageLocators()

    @allure.step('Переход на страницу CampaignPage')
    def go_to_campaign_page(self):
        self.click(self.locators.CAMPAIGNS_LOCATOR)
        return CampaignPage(self.driver)

    @allure.step('Переход на страницу SegmentPage')
    def go_to_segment_page(self):
        self.click(self.locators.SEGMENTS_LOCATOR)
        return SegmentPage(self.driver)
