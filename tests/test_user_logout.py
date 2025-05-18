from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.desk_locators import TestLogoutUserLocators

#Авторизоваться под заранее созданным пользователем.
#Нажать кнопку «Выйти».
#Проверить: аватар пользователя и имя User больше не отображается в правом верхнем углу 
# около кнопки «Разместить объявление», там теперь отображается кнопка «Вход и регистрация».

class TestLogoutUser:
        
    def test_check_button_enter_and_registration_after_exit(self, driver, unique_email_correct):
        driver = webdriver.Chrome()

        current_url = "https://qa-desk.stand.praktikum-services.ru/"
        
        driver.get(current_url)
        driver.find_element(*TestLogoutUserLocators.ENTER_AND_REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLogoutUserLocators.TITLE_ENTER))
        driver.find_element(*TestLogoutUserLocators.NO_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLogoutUserLocators.TITLE_REGISTRATION))
        driver.find_element(*TestLogoutUserLocators.ENTER_EMAIL_FIELD).send_keys(unique_email_correct)
        driver.find_element(*TestLogoutUserLocators.ENTER_PASSWORD_FIELD).send_keys("qwerty")
        driver.find_element(*TestLogoutUserLocators.CREATE_ACCOUNT_BUTTON).click()
        driver.implicitly_wait(3)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLogoutUserLocators.EXIT_BUTTON))
        driver.find_element(*TestLogoutUserLocators.EXIT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.invisibility_of_element_located(TestLogoutUserLocators.USER_AVATAR))
        WebDriverWait(driver, 5).until(expected_conditions.invisibility_of_element_located(TestLogoutUserLocators.USER_NAME))

        assert driver.find_element(*TestLogoutUserLocators.ENTER_AND_REGISTRATION_BUTTON).text == "Вход и регистрация"


