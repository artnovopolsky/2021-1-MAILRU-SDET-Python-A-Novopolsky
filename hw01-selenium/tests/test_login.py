import pytest
from base import logged_in_page


@pytest.mark.UI
def test_work_checking(logged_in_page):
    assert 'Создайте рекламную кампанию' in logged_in_page.page_source

