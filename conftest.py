import pytest
import uuid
from selenium import webdriver

# для браузера + выход
@pytest.fixture
def driver():
    chrome = webdriver.Chrome()
    chrome.maximize_window()
    #driver.set_window_size(1280, 720)
    yield chrome
    chrome.quit()


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

