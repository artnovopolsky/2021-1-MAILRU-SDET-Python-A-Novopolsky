from selenium.webdriver.common.by import By


class UnauthorizedPageLocators:
    SIGN_IN_LOCATOR = (By.XPATH, "//div[contains(@class, 'responseHead-module-button')]")
    EMAIL_LOCATOR = (By.XPATH, "//input[@name='email']")
    PASSWORD_LOCATOR = (By.XPATH, "//input[@name='password']")
    ENTER_LOCATOR = (By.XPATH, "//div[contains(@class, 'authForm-module-button')]")
    ERROR_LOCATOR = (By.XPATH, "//div[@class='formMsg_title']")
    INVALID_EMAIL_LOCATOR = (By.XPATH, "//div[contains(@class, 'notify-module-content')]")


class AuthorizedPageLocators:
    CAMPAIGNS_LOCATOR = (By.XPATH, "//a[@href='/dashboard']")
    SEGMENTS_LOCATOR = (By.XPATH, "//a[@href='/segments']")


class CampaignPageLocators:
    COVERAGE_LOCATOR = (By.XPATH, "//div[contains(@class, 'column-list-item') and contains(text(), 'Охват')]")
    LINK_INPUT_LOCATOR = (By.XPATH, "//input[@placeholder='Введите ссылку']")
    BANNER_IMAGE_LOCATOR = (By.XPATH, "//div[@id='patterns_4']")
    UPLOAD_LOCATOR = (By.XPATH, "//input[@data-test='image_240x400']")
    CREATE_CAMPAIGN_LOCATOR = (By.XPATH, "//div[@class='button__text' and contains(text(), 'Создать кампанию')]")
    NEW_CAMPAIGN_IN_TABLE_LOCATOR = (By.XPATH, "//a[contains(@class, 'nameCell-module-campaignName')]")


class SegmentPageLocators:
    SOCIAL_NETWORK_APPLICATIONS_LOCATOR = (By.XPATH, "//div[contains(text(), 'Приложения и игры в соцсетях')]")
    CHECKBOX_LOCATOR = (By.XPATH, "//input[@type='checkbox']")
    ADD_SEGMENT_LOCATOR = (By.XPATH, "//div[@class='button__text' and contains(text(), 'Добавить сегмент')]")
    SEGMENT_NAME_LOCATOR = (By.XPATH, "//div[contains(@class, 'input_create-segment-form')]/div/input")
    CREATE_SEGMENT_LOCATOR = (By.XPATH, "//div[@class='button__text' and contains(text(), 'Создать сегмент')]")
    SEGMENT_IN_TABLE_LOCATOR = (By.XPATH, "//div[contains(@class, 'cells-module-nameCell')]/a")
    ID_FIRST_SEGMENT_LOCATOR = (By.XPATH, "//div[contains(@class, 'segmentsTable-module-idCellWrap')]/input")
    SEGMENT_ACTIONS_LOCATOR = (By.XPATH, "//div[contains(@class, 'select-module-arrow')]")
    DELETE_SEGMENT_LOCATOR = (By.XPATH, "//li[@data-id='remove']")
