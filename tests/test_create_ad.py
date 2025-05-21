from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.desk import TestAdLocators
from data import url_doska

class TestCreateAd:

    # 1. Создание объявления неавторизованным пользователем
    #Нажать кнопку «Разместить объявление».
    #Проверить: отображается модальное окно с заголовком «Чтобы разместить объявление, авторизуйтесь».
    
    def test_create_ad_by_unauthorized_user(self, driver): 

        driver.get(url_doska) 
        driver.find_element(*TestAdLocators.POST_AD_BUTTON).click()
        WebDriverWait(driver,3).until(expected_conditions.visibility_of_element_located(TestAdLocators.TITLE_AUTHORIZATION_REQUIRED_IN_MODAL_WINDOW))

        text_in_modal_window = driver.find_element(*TestAdLocators.TITLE_AUTHORIZATION_REQUIRED_IN_MODAL_WINDOW)
        assert text_in_modal_window.text == "Чтобы разместить объявление, авторизуйтесь"


# 2. Создание объявления авторизованным пользователем
#Авторизоваться под заранее созданным пользователем.
#Заполнить все поля формы: «Название», «Описание товара», «Стоимость» — стоимость должна быть указана в числовом формате.
#Выбрать из Dropdown «Категорию» и «Город».
#Выбрать RabioButton «Состояние товара».
#Нажать кнопку «Опубликовать».
#Перейти в профиль пользователя.
#Проверить: в блоке «Мои объявления» отображается созданное объявление.

    def test_create_ad_by_authorized_user(self, driver, unique_email_correct):

        # регистрируем нового пользователя и нажимаем "Разместить объявление"
        driver.get(url_doska)
        driver.find_element(*TestAdLocators.ENTER_AND_REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestAdLocators.TITLE_ENTER))
        driver.find_element(*TestAdLocators.NO_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestAdLocators.TITLE_REGISTRATION))
        driver.find_element(*TestAdLocators.ENTER_EMAIL_FIELD).send_keys(unique_email_correct)
        driver.find_element(*TestAdLocators.ENTER_PASSWORD_FIELD).send_keys("qwerty")
        driver.find_element(*TestAdLocators.REPEAT_PASSWORD_FIELD).send_keys("qwerty")
        driver.find_element(*TestAdLocators.CREATE_ACCOUNT_BUTTON).click()
        WebDriverWait(driver,10).until(expected_conditions.visibility_of_element_located(TestAdLocators.EXIT_BUTTON))
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(TestAdLocators.POST_AD_BUTTON))
        driver.find_element(*TestAdLocators.POST_AD_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestAdLocators.TITLE_ADD_PHOTO))

        # Ввели "Название"
        driver.find_element(*TestAdLocators.TITLE_FIELD).send_keys('NewForTest')

        # Ввели "Описание товара"
        driver.find_element(*TestAdLocators.PRODUCT_DESCRIPTION_FIELD).send_keys('SomethingNew')

        # Ввели "Стоимость"
        driver.find_element(*TestAdLocators.PRICE_FIELD).send_keys(50)

        # Нажали на "Категории"
        driver.find_element(*TestAdLocators.CATEGORY_DROPDOWN).click()

        # Нажали на "Город"
        driver.find_element(*TestAdLocators.CITY_DROPDOWN).click()

        # Нажали RabioButton «Состояние товара»
        driver.find_element(*TestAdLocators.NEW_CONDITION_RADIOBUTTON).click()

        # Нажали нопку "Опубликовать" 
        driver.find_element(*TestAdLocators.SUBMIT_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestAdLocators.USER_AVATAR))

        driver.get(f"{url_doska}profile")
        element = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, '//h2[contains(@class, "h2") and text()="NewForTest"]')))
 
        assert element.is_displayed()
        assert "50" in driver.find_element(By.XPATH, "//div[@class='price']//h2").text

