import logging
import allure
from random import randint
from pages.base_page import BasePage
from locators import SegmentPageLocators

logger = logging.getLogger('test')


class SegmentPage(BasePage):
    locators = SegmentPageLocators()

    def go_to_creation_segment(self):
        return self.driver.get('https://target.my.com/segments/segments_list/new')

    def create_segment_name(self):
        segment_name = 'segment' + str(randint(0, 2000000)) + str(randint(0, 2000000))
        return segment_name

    @allure.step('Создание сегмента {name}')
    def create_segment(self, name='test'):
        self.go_to_creation_segment()
        self.click(self.locators.SOCIAL_NETWORK_APPLICATIONS_LOCATOR)
        self.click(self.locators.CHECKBOX_LOCATOR)
        self.click(self.locators.ADD_SEGMENT_LOCATOR)
        self.send_message(self.locators.SEGMENT_NAME_LOCATOR, name)
        self.click(self.locators.CREATE_SEGMENT_LOCATOR)
        logger.info(f'Сегмент {name} успешно создан...')

    @allure.step('Удаление сегмента {name}')
    def delete_segment(self, name):
        # Сравниваем переданное имя сегмента с именем последнего созданного сегмента
        if name == self.find(self.locators.SEGMENT_IN_TABLE_LOCATOR).text:
            self.click(self.locators.ID_FIRST_SEGMENT_LOCATOR)
            self.click(self.locators.SEGMENT_ACTIONS_LOCATOR)
            self.click(self.locators.DELETE_SEGMENT_LOCATOR)
            logger.info(f'Сегмент {name} успешно удалён...')
