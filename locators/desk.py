from selenium.webdriver.common.by import By

    # 1. Регистрация пользователя

    #1.1 Тест "Регистрация пользователя"
class TestAutorisationLocators:
    ENTER_AND_REGISTRATION_BUTTON = (By.XPATH, "//button[contains(text(),'Вход и регистрация')]") # кнопка «Вход и регистрация»
    TITLE_ENTER = (By.XPATH, "//h1[@class='h1' and contains(text(), 'Войти')]") # надпись "Войти"
    NO_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(),'Нет аккаунта')]") # кнопка «Нет аккаунта»
    TITLE_REGISTRATION = (By.XPATH, "//h1[@class='h1' and contains(text(), 'Зарегистрироваться')]") # надпись "Зарегистрироваться"
    ENTER_EMAIL_FIELD = (By.XPATH, "//input[@placeholder='Введите Email']") # поле "Email"
    ENTER_PASSWORD_FIELD = (By.XPATH, "//input[@placeholder='Пароль']") # поле "Пароль"
    REPEAT_PASSWORD_FIELD = (By.XPATH, "//input[@placeholder='Повторите пароль']") # поле "Повторите пароль"
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(),'Создать аккаунт')]") # кнопка "Создать аккаунт"
    USER_AVATAR = (By.CSS_SELECTOR, "button.circleSmall") # аватар пользователя
    USER_NAME = (By.XPATH, "//h3[@class='profileText name']") # имя User
    TITLE_DOSKA = (By.XPATH, "//div[@class='header_shell__zlCGj']//*[name()='svg']") # надпись DOSKA

    # 1.2. Тест "Регистрация пользователя c email не по маске  *******@*******.***"
    ERROR_BUTTON = (By.XPATH, "//span[@class= 'input_span__yWPqB' and contains(text(),'Ошибка')]") # надпись "Ошибка" под полем email
    FIELD_WITH_ERROR = (By.XPATH, "//div[@class='input_inputError__fLUP9']") # локатор поля (одинаковый для 3х полей) после появления "Ошибки"

    # 1.3. Тест "Регистрация уже существующего пользователя"
    EXIT_BUTTON = (By.XPATH, "//button[contains(text(),'Выйти')]") # кнопка "Выйти"

    # 2. Login пользователя
class TestLoginUserLocators:
    ENTER_AND_REGISTRATION_BUTTON = (By.XPATH, "//button[contains(text(),'Вход и регистрация')]") # кнопка «Вход и регистрация»
    TITLE_ENTER = (By.XPATH, "//h1[@class='h1' and contains(text(), 'Войти')]") # надпись "Войти"
    NO_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(),'Нет аккаунта')]") # кнопка «Нет аккаунта»
    TITLE_REGISTRATION = (By.XPATH, "//h1[@class='h1' and contains(text(), 'Зарегистрироваться')]") # надпись "Зарегистрироваться"
    ENTER_EMAIL_FIELD = (By.XPATH, "//input[@placeholder='Введите Email']") # поле "Email"
    ENTER_PASSWORD_FIELD = (By.XPATH, "//input[@placeholder='Пароль']") # поле "Пароль"
    REPEAT_PASSWORD_FIELD = (By.XPATH, "//input[@placeholder='Повторите пароль']") # поле "Повторите пароль"
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(),'Создать аккаунт')]") # кнопка "Создать аккаунт"
    USER_AVATAR = (By.CSS_SELECTOR, "button.circleSmall") # аватар пользователя
    USER_NAME = (By.XPATH, "//h3[@class='profileText name']") # имя User
    EXIT_BUTTON = (By.XPATH, "//button[contains(text(),'Выйти')]") # кнопка "Выйти"
    ENTER_BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]") # кнопка «Войти»
    TITLE_DOSKA = (By.XPATH, "//div[@class='header_shell__zlCGj']//*[name()='svg']") # надпись DOSKA

    # 3. Logout пользователя
class TestLogoutUserLocators:
    ENTER_AND_REGISTRATION_BUTTON = (By.XPATH, "//button[contains(text(),'Вход и регистрация')]") # кнопка «Вход и регистрация»
    TITLE_ENTER = (By.XPATH, "//h1[@class='h1' and contains(text(), 'Войти')]") # надпись "Войти"
    NO_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(),'Нет аккаунта')]") # кнопка «Нет аккаунта»
    TITLE_REGISTRATION = (By.XPATH, "//h1[@class='h1' and contains(text(), 'Зарегистрироваться')]") # надпись "Зарегистрироваться"
    ENTER_EMAIL_FIELD = (By.XPATH, "//input[@placeholder='Введите Email']") # поле "Email"
    ENTER_PASSWORD_FIELD = (By.XPATH, "//input[@placeholder='Пароль']") # поле "Пароль"
    REPEAT_PASSWORD_FIELD = (By.XPATH, "//input[@placeholder='Повторите пароль']") # поле "Повторите пароль"
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(),'Создать аккаунт')]") # кнопка "Создать аккаунт"
    USER_AVATAR = (By.CSS_SELECTOR, "button.circleSmall") # аватар пользователя
    USER_NAME = (By.XPATH, "//h3[@class='profileText name']") # имя User
    ENTER_BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]") # кнопка «Войти»
    EXIT_BUTTON = (By.XPATH, "//button[contains(text(),'Выйти')]") # кнопка «Выйти»

    # 4. Создание объявления
    # 4.1. Создание объявления неавторизованным пользователем
class TestAdLocators: 
    POST_AD_BUTTON = (By.XPATH, "//button[text()='Разместить объявление']") # кнопка «Разместить объявление»
    TITLE_AUTHORIZATION_REQUIRED_IN_MODAL_WINDOW = (By.XPATH, "//h1[contains(text(),'Чтобы разместить объявление, авторизуйтесь')]") # надпись "Чтобы разместить объявление, авторизуйтесь"
    EXIT_BUTTON = (By.XPATH, "//button[contains(text(),'Выйти')]") # кнопка "Выйти"

    # 4.2. Создание объявления авторизованным пользователем
    ENTER_AND_REGISTRATION_BUTTON = (By.XPATH, "//button[contains(text(),'Вход и регистрация')]") # кнопка «Вход и регистрация»
    TITLE_ENTER = (By.XPATH, "//h1[@class='h1' and contains(text(), 'Войти')]") # надпись "Войти"
    NO_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(),'Нет аккаунта')]") # кнопка «Нет аккаунта»
    TITLE_REGISTRATION = (By.XPATH, "//h1[@class='h1' and contains(text(), 'Зарегистрироваться')]") # надпись "Зарегистрироваться"
    ENTER_EMAIL_FIELD = (By.XPATH, "//input[@placeholder='Введите Email']") # поле "Email"
    ENTER_PASSWORD_FIELD = (By.XPATH, "//input[@placeholder='Пароль']") # поле "Пароль"
    REPEAT_PASSWORD_FIELD = (By.XPATH, "//input[@placeholder='Повторите пароль']") # поле "Повторите пароль"
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(),'Создать аккаунт')]") # кнопка "Создать аккаунт"
    TITLE_NEW_AD = (By.XPATH, "//form[contains(@class, 'popUp')]//h1") # надпись "Новое объявление"
    TITLE_ADD_PHOTO = (By.XPATH, "//span[@class='spanGlobal' and contains(text(), 'Добавить фото')]")
    TITLE_FIELD = (By.XPATH, "//input[@placeholder='Название']") # поле формы «Название»
    PRODUCT_DESCRIPTION_FIELD = (By.XPATH, "//textarea[@placeholder='Описание товара']") # поле формы «Описание товара»
    PRICE_FIELD = (By.XPATH, "//input[@placeholder='Стоимость']") # поле формы «Стоимость» 
    CATEGORY_DROPDOWN = (By.XPATH, "//input[@name='category']") # "Категория"
    GARDENING_CATEGORY_DROPDOWN = (By.XPATH, "//span[contains(text(),'Садоводство')]")
    CITY_DROPDOWN = (By.XPATH, "//input[@name='city']") # "Город"
    SPB_CITY_DROPDOWN = (By.XPATH, "//span[contains(text(),'Санкт-Петербург')]")
    NEW_CONDITION_RADIOBUTTON = (By.XPATH, "//div[@class='radioUnput_inputActive__eC-HY']") # "Состояние товара Новый"
    USED_CONDITION_RADIOBUTTON = (By.XPATH, "//div[@class='radioUnput_inputRegular__FbVbr']") # "Состояние товара Б/У"
    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']") # кнопка «Опубликовать»
    USER_AVATAR = (By.CSS_SELECTOR, "button.circleSmall") # аватар пользователя
    TITLE_MY_PROFILE = (By.XPATH, "//h1[@class='h1 zeroMargin' and contains(text(), 'Мой профиль')]") # надпись "Мой профиль"
    TITLE_MY_ADDS = (By.XPATH, "//h1[contains(text(),'Мои объявления')]")
    DOCUMENTATION_BUTTON = By.XPATH, ("//a[contains(text(),'Документация')]") # кнопка "Документация"