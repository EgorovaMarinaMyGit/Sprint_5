from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.desk_locators import TestAutorisationLocators

class TestRegistration:

# 1. Регистрация пользователя
#Нажать кнопку «Вход и регистрация».
#Нажать кнопку «Нет аккаунта».
#Заполнить все поля формы регистрации и нажать кнопку «Создать аккаунт».
#Проверить: произошёл переход на главную страницу, в правом верхнем углу около кнопки 
# «Разместить объявление» отображается аватар пользователя и имя User.

    def test_registration_with_correct_email(self, driver, unique_email_correct):
        driver = webdriver.Chrome()

        current_url = "https://qa-desk.stand.praktikum-services.ru/"
        
        driver.get(current_url)
        driver.find_element(*TestAutorisationLocators.ENTER_AND_REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestAutorisationLocators.TITLE_ENTER))
        driver.find_element(*TestAutorisationLocators.NO_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestAutorisationLocators.TITLE_REGISTRATION))
        driver.find_element(*TestAutorisationLocators.ENTER_EMAIL_FIELD).send_keys(unique_email_correct)
        driver.find_element(*TestAutorisationLocators.ENTER_PASSWORD_FIELD).send_keys("qwerty")
        driver.find_element(*TestAutorisationLocators.REPEAT_PASSWORD_FIELD).send_keys("qwerty")
        driver.find_element(*TestAutorisationLocators.CREATE_ACCOUNT_BUTTON).click()
        driver.implicitly_wait(3)

        expected_url = "https://qa-desk.stand.praktikum-services.ru/"
        user_avatar = driver.find_element(*TestAutorisationLocators.USER_AVATAR)
        user_name = driver.find_element(*TestAutorisationLocators.USER_NAME)
        assert driver.current_url == expected_url
        assert user_avatar.is_displayed(), "Аватар не отображается"
        assert user_name.text == "User.", f'user_name is ---->>> {user_name}'

# 2. Регистрация пользователя c email не по маске  *******@*******.***
#Нажать кнопку «Вход и регистрация».
#Нажать кнопку «Нет аккаунта».
#Заполнить поле Email формы регистрации и нажать кнопку «Создать аккаунт».
#Проверить: поля Email, «Пароль», «Повторите пароль» выделены красным, под полем Email 
# отображается сообщение «Ошибка».

    def test_registration_with_incorrect_email(self, driver, unique_email_incorrect):
        driver = webdriver.Chrome()

        driver.get("https://qa-desk.stand.praktikum-services.ru/")
        driver.find_element(*TestAutorisationLocators.ENTER_AND_REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestAutorisationLocators.TITLE_ENTER))
        driver.find_element(*TestAutorisationLocators.NO_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestAutorisationLocators.TITLE_REGISTRATION))
        driver.find_element(*TestAutorisationLocators.ENTER_EMAIL_FIELD).send_keys(unique_email_incorrect)
        driver.find_element(*TestAutorisationLocators.ENTER_PASSWORD_FIELD).send_keys("qwerty")
        driver.find_element(*TestAutorisationLocators.CREATE_ACCOUNT_BUTTON).click()
        driver.implicitly_wait(3)

        border_color_of_email_field = driver.find_element(*TestAutorisationLocators.FIELD_WITH_ERROR).value_of_css_property('border-color')
        border_color_of_password_field = driver.find_element(*TestAutorisationLocators.FIELD_WITH_ERROR).value_of_css_property('border-color')
        border_color_of_repeated_password_field = driver.find_element(*TestAutorisationLocators.FIELD_WITH_ERROR).value_of_css_property('border-color')
        error_button = driver.find_element(*TestAutorisationLocators.ERROR_BUTTON)

        assert border_color_of_email_field == f'FF6972'
        assert border_color_of_password_field == f'FF6972'
        assert border_color_of_repeated_password_field == f'FF6972'
        assert error_button.text == "Ошибка", f'error_button is ---->>> {error_button}'

# 3. Регистрация уже существующего пользователя
#Нажать кнопку «Вход и регистрация».
#Нажать кнопку «Нет аккаунта».
#Заполнить все поля формы регистрации данными уже существующего в системе пользователя и 
# нажать кнопку «Создать аккаунт».
#Проверить: поля Email, «Пароль», «Повторите пароль» выделены красным, под полем Email 
# отображается сообщение «Ошибка».

    def test_registration_of_existing_user(self, driver, unique_email_incorrect):
        driver = webdriver.Chrome()

        email_incorrect_for_test = unique_email_incorrect

        driver.get("https://qa-desk.stand.praktikum-services.ru/")

        # регистрируем нового пользователя (и потом выходим из аккаунта)
        driver.find_element(*TestAutorisationLocators.ENTER_AND_REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestAutorisationLocators.TITLE_ENTER))
        driver.find_element(*TestAutorisationLocators.NO_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestAutorisationLocators.TITLE_REGISTRATION))
        driver.find_element(*TestAutorisationLocators.ENTER_EMAIL_FIELD).send_keys(email_incorrect_for_test)
        driver.find_element(*TestAutorisationLocators.ENTER_PASSWORD_FIELD).send_keys("qwerty")
        driver.find_element(*TestAutorisationLocators.REPEAT_PASSWORD_FIELD).send_keys("qwerty")
        driver.find_element(*TestAutorisationLocators.CREATE_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestAutorisationLocators.EXIT_BUTTON))
        driver.find_element(*TestAutorisationLocators.EXIT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestAutorisationLocators.ENTER_AND_REGISTRATION_BUTTON))
        
        # пытаемся зарегистрировать пользователя с такими же данными
        driver.find_element(*TestAutorisationLocators.ENTER_AND_REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestAutorisationLocators.TITLE_ENTER))
        driver.find_element(*TestAutorisationLocators.NO_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestAutorisationLocators.TITLE_REGISTRATION))
        driver.find_element(*TestAutorisationLocators.ENTER_EMAIL_FIELD).send_keys(email_incorrect_for_test)
        driver.find_element(*TestAutorisationLocators.ENTER_PASSWORD_FIELD).send_keys("qwerty")
        driver.find_element(*TestAutorisationLocators.REPEAT_PASSWORD_FIELD).send_keys("qwerty")
        driver.find_element(*TestAutorisationLocators.CREATE_ACCOUNT_BUTTON).click()
        driver.implicitly_wait(3)

        border_color_of_email_field = driver.find_element(*TestAutorisationLocators.FIELD_WITH_ERROR).value_of_css_property('border-color')
        border_color_of_password_field = driver.find_element(*TestAutorisationLocators.FIELD_WITH_ERROR).value_of_css_property('border-color')
        border_color_of_repeated_password_field = driver.find_element(*TestAutorisationLocators.FIELD_WITH_ERROR).value_of_css_property('border-color')
        error_button = driver.find_element(*TestAutorisationLocators.ERROR_BUTTON)

        assert border_color_of_email_field == f'FF6972'
        assert border_color_of_password_field == f'FF6972'
        assert border_color_of_repeated_password_field == f'FF6972'
        assert error_button.text == "Ошибка", f'error_button is ---->>> {error_button}'