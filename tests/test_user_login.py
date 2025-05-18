from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.desk_locators import TestLoginUserLocators

#Нажать кнопку «Вход и регистрация».
#Заполнить все поля формы авторизации и нажать кнопку «Войти».
#Проверить: произошёл переход на главную страницу, в правом верхнем углу около кнопки 
# «Разместить объявление» отображается аватар пользователя и имя User.

class TestLoginUser:
       
    def test_check_user_avatar_and_name_after_registration(self, driver, unique_email_correct):
        driver = webdriver.Chrome()

        email_user = unique_email_correct

        current_url = "https://qa-desk.stand.praktikum-services.ru/"
        
        driver.get(current_url)

        # регистрируем нового пользователя и потом выходим из аккаунта
        driver.find_element(*TestLoginUserLocators.ENTER_AND_REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLoginUserLocators.TITLE_ENTER))
        driver.find_element(*TestLoginUserLocators.NO_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLoginUserLocators.TITLE_REGISTRATION))
        driver.find_element(*TestLoginUserLocators.ENTER_EMAIL_FIELD).send_keys(email_user)
        driver.find_element(*TestLoginUserLocators.ENTER_PASSWORD_FIELD).send_keys("qwerty")
        driver.find_element(*TestLoginUserLocators.CREATE_ACCOUNT_BUTTON).click()
        driver.implicitly_wait(3)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLoginUserLocators.EXIT_BUTTON))
        driver.find_element(*TestLoginUserLocators.EXIT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLoginUserLocators.ENTER_AND_REGISTRATION_BUTTON))

        # заходим в аккаунт, созданный выше
        driver.find_element(*TestLoginUserLocators.ENTER_AND_REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLoginUserLocators.TITLE_ENTER))
        driver.find_element(*TestLoginUserLocators.ENTER_EMAIL_FIELD).send_keys(email_user)
        driver.find_elementT(*TestLoginUserLocators.ENTER_PASSWORD_FIELD).send_keys("qwerty")
        driver.find_element(*TestLoginUserLocators.ENTER_BUTTON).click()
        driver.implicitly_wait(3)

        expected_url = "https://qa-desk.stand.praktikum-services.ru/"
        user_avatar = driver.find_element(*TestLoginUserLocators.USER_AVATAR)
        user_name = driver.find_element(*TestLoginUserLocators.USER_NAME)

        assert expected_url == current_url
        assert user_avatar.is_displayed(), "Аватар не отображается"
        assert user_name.text == "User.", f'user_name is ---->>> {user_name}'