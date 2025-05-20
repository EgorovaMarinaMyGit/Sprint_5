import random
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.desk import TestAdLocators

class TestCreateAd:

    # 1. Создание объявления неавторизованным пользователем
    #Нажать кнопку «Разместить объявление».
    #Проверить: отображается модальное окно с заголовком «Чтобы разместить объявление, авторизуйтесь».
    
    def test_create_ad_by_unauthorized_user(self, driver):

        driver.get("https://qa-desk.stand.praktikum-services.ru/")
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

    def test_create_ad_by_authorized_user(self, driver, unique_email_correct, unique_title_in_ad, unique_description_in_ad):

        # регистрируем нового пользователя и нажимаем "Разместить объявление"
        driver.get("https://qa-desk.stand.praktikum-services.ru/")
        driver.find_element(*TestAdLocators.ENTER_AND_REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestAdLocators.TITLE_ENTER))
        driver.find_element(*TestAdLocators.NO_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestAdLocators.TITLE_REGISTRATION))
        driver.find_element(*TestAdLocators.ENTER_EMAIL_FIELD).send_keys(unique_email_correct)
        driver.find_element(*TestAdLocators.ENTER_PASSWORD_FIELD).send_keys("qwerty")
        driver.find_element(*TestAdLocators.REPEAT_PASSWORD_FIELD).send_keys("qwerty")
        driver.find_element(*TestAdLocators.CREATE_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestAdLocators.POST_AD_BUTTON))
        driver.find_element(*TestAdLocators.POST_AD_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestAdLocators.TITLE_NEW_AD))

        # скролл до поля "Название", нажатие и заполнение
        unique_title_in_ad_for_test = unique_title_in_ad

        title_field = driver.find_element(TestAdLocators.TITLE_FIELD)
        driver.execute_script("arguments[0].scrollIntoView();", title_field) 
        driver.find_element(*TestAdLocators.TITLE_FIELD).click()
        driver.find_element(*TestAdLocators.TITLE_FIELD).send_keys(unique_title_in_ad_for_test)

        # скролл до поля "Описание товара", нажатие и заполнение
        unique_description_in_ad_for_test = unique_description_in_ad

        product_description_field = driver.find_element(TestAdLocators.PRODUCT_DESCRIPTION_FIELD)
        driver.execute_script("arguments[0].scrollIntoView();", product_description_field) 
        driver.find_element(*TestAdLocators.PRODUCT_DESCRIPTION_FIELD).click()
        driver.find_element(*TestAdLocators.PRODUCT_DESCRIPTION_FIELD).send_keys(unique_description_in_ad_for_test)

        # скролл до поля "Стоимость", нажатие и заполнение
        unique_price_in_ad_for_test = random.random (1, 100)

        price_field = driver.find_element(TestAdLocators.PRICE_FIELD)
        driver.execute_script("arguments[0].scrollIntoView();", price_field) 
        driver.find_element(*TestAdLocators.PRICE_FIELD).click()
        driver.find_element(*TestAdLocators.PRICE_FIELD).send_keys(unique_price_in_ad_for_test)

        # скролл до "Категории" и выбор категории
        category_dropdown = driver.find_element(*TestAdLocators.CATEGORY_DROPDOWN) # "Категория"
        gardening_category_dropdown = driver.find_element(*TestAdLocators.GARDENING_CATEGORY_DROPDOWN)
        driver.execute_script("arguments[0].scrollIntoView();", category_dropdown) 
        driver.find_element(*TestAdLocators.CATEGORY_DROPDOWN).click()
        driver.execute_script("arguments[0].scrollIntoView();", gardening_category_dropdown)
        driver.find_element(*TestAdLocators.GARDENING_CATEGORY_DROPDOWN).click()

        # скролл до "Город" и выбор города
        city_dropdown = driver.find_element(*TestAdLocators.CITY_DROPDOWN)
        spb_city_dropdown = driver.find_element(*TestAdLocators.SPB_CITY_DROPDOWN)
        driver.execute_script("arguments[0].scrollIntoView();", city_dropdown) 
        driver.find_element(*TestAdLocators.CITY_DROPDOWN).click()
        driver.execute_script("arguments[0].scrollIntoView();", spb_city_dropdown)
        driver.find_element(*TestAdLocators.SPB_CITY_DROPDOWN).click()

        # скролл до RabioButton «Состояние товара» и выбор опции
        new_condition_radiobutton = driver.find_element(TestAdLocators.NEW_CONDITION_RADIOBUTTON)
        driver.execute_script("arguments[0].scrollIntoView();", new_condition_radiobutton) 
        driver.find_element(*TestAdLocators.NEW_CONDITION_RADIOBUTTON).click()

        # скролл до кнопки "Опубликовать" и нажатие
        submit_button = driver.find_element(*TestAdLocators.SUBMIT_BUTTON)
        driver.execute_script("arguments[0].scrollIntoView();", submit_button) 
        driver.find_element(*TestAdLocators.SUBMIT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestAdLocators.USER_AVATAR))

        # скролл до аватарки пользователи и переход в профиль
        user_avatar = driver.find_element(*TestAdLocators.USER_AVATAR)
        driver.execute_script("arguments[0].scrollIntoView();", user_avatar) 
        driver.find_element(*TestAdLocators.USER_AVATAR).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestAdLocators.TITLE_MY_PROFILE))

        # скролл до "Мои объявления"
        my_adds = driver.find_element(*TestAdLocators.TITLE_MY_ADDS)
        driver.execute_script("arguments[0].scrollIntoView();", my_adds) 

        assert driver.find_element(By.XPATH, "//div[@class='h2' and contains(text(), '{unique_title_in_ad_for_test}')]") == 'unique_title_in_ad_for_test'
        assert driver.find_element(By.XPATH, "//div[@class='h3' and contains(text(), 'Санкт_Петербург')]") == "Санкт_Петербург"
        assert driver.find_element(By.XPATH, "//div[@class='h2' and contains(text(), '{unique_price_in_ad_for_test}')]") == int(unique_price_in_ad_for_test)

