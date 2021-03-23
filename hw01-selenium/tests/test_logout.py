import pytest
from base import logged_out_page, logged_in_page


@pytest.mark.UI
def test_work_checking(logged_out_page):
    assert 'Войти' in logged_out_page.page_source
