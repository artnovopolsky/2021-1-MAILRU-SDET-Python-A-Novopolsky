import pytest
from base import logged_in_page, logged_out_page, contact_info_page


@pytest.mark.UI
def test_login(logged_in_page):
    assert 'Создайте рекламную кампанию' in logged_in_page.page_source


@pytest.mark.UI
def test_logout(logged_out_page):
    assert 'Войти' in logged_out_page.page_source


@pytest.mark.UI
def test_edit_profile(contact_info_page):
    pass


@pytest.mark.UI
def test_transition_to_pages(logged_in_page):
    pass
