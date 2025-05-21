from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.desk import TestLoginUserLocators

#Нажать кнопку «Вход и регистрация».
#Заполнить все поля формы авторизации и нажать кнопку «Войти».
#Проверить: произошёл переход на главную страницу, в правом верхнем углу около кнопки 
# «Разместить объявление» отображается аватар пользователя и имя User.

class TestLoginUser:
       
    def test_check_user_avatar_and_name_after_registration(self, driver, unique_email_correct):

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
        driver.find_element(*TestLoginUserLocators.REPEAT_PASSWORD_FIELD).send_keys("qwerty")
        driver.find_element(*TestLoginUserLocators.CREATE_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLoginUserLocators.EXIT_BUTTON))
        driver.find_element(*TestLoginUserLocators.EXIT_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLoginUserLocators.ENTER_AND_REGISTRATION_BUTTON))

        # заходим в аккаунт, созданный выше, с помощью авторизации
        driver.find_element(*TestLoginUserLocators.ENTER_AND_REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLoginUserLocators.TITLE_ENTER))
        driver.find_element(*TestLoginUserLocators.ENTER_EMAIL_FIELD).send_keys(email_user)
        driver.find_element(*TestLoginUserLocators.ENTER_PASSWORD_FIELD).send_keys("qwerty")
        driver.find_element(*TestLoginUserLocators.ENTER_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLoginUserLocators.TITLE_DOSKA))

        expected_url = "https://qa-desk.stand.praktikum-services.ru/login"
        user_avatar = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLoginUserLocators.USER_AVATAR))
        user_name = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLoginUserLocators.USER_NAME))

        assert driver.current_url == expected_url
        assert user_avatar.is_displayed()
        assert user_name.text == "User."