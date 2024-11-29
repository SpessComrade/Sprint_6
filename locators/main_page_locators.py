from selenium.webdriver.common.by import By

class MainPageLocators:

    #Логотипы:
    samokat_logo = By.CLASS_NAME, 'Header_LogoScooter__3lsAR'
    yandex_logo = By.CLASS_NAME, 'Header_LogoYandex__3TSOI'

    #Кнопки заказов:
    order_button_top = By.XPATH, '//div[contains(@class, "Header_Nav")]/button[text()="Заказать"]'
    order_button_bottom = By.XPATH, '//div[contains(@class, "Home_FinishButton")]/button[text()="Заказать"]'

    #Элементы FAQ:
    locator_question = By.XPATH, ".//*[@id='accordion__heading-{}']"
    locator_answer = By.XPATH, ".//*[@id='accordion__panel-{}']"
    locator_question_last = By.XPATH, ".//*[@id='accordion__heading-7']"
    locator_answer_last = By.XPATH, ".//*[@id='accordion__panel-7']"

    # Локатор заголовка новостей Дзена
    dzen_news_header = By.ID, 'dzen-header'