import pytest
import uuid
from selenium import webdriver

# для браузера + выход
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    #driver.set_window_size(1280, 720)
    yield driver
    driver.quit()


# генерация уникального email
@pytest.fixture
def unique_email_correct():
    new_uuid = uuid.uuid4()
    new_email_correct = f"{new_uuid}@example.com"
    return new_email_correct


# генерация уникального email не по маске
@pytest.fixture
def unique_email_incorrect():
    new_uuid = uuid.uuid4()
    new_email_incorrect = f"{new_uuid}@@example.com"
    return new_email_incorrect


# генерация уникального названия товара
@pytest.fixture
def unique_title_in_ad():
    title_uuid = uuid.uuid4()
    new_title_in_ad = f"{title_uuid}"
    return new_title_in_ad


# генерация уникального описания товара
@pytest.fixture
def unique_description_in_ad():
    description_uuid = uuid.uuid4()
    new_description_in_ad = f"{description_uuid}"
    return new_description_in_ad
