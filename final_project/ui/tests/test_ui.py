import pytest
from ui.fixtures import driver


def test_ui(driver):
    driver.save_screenshot('/home/artnovopolsky/mailru-course/my-repos/final_project/screen.png')
    assert 'Welcome' in driver.page_source
