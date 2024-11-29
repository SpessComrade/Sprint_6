from selenium.webdriver.common.by import By

class OrderPageLocators:

    #Логотипы:
    samokat_logo = By.CLASS_NAME, 'Header_LogoScooter__3lsAR'

    #Поля, селекторы и кнопки формы: Для кого самокат
    first_name_input = By.XPATH, ".//input[@placeholder='* Имя']"
    last_name_input = By.XPATH, ".//input[@placeholder='* Фамилия']"
    address_input = By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']"
    metro_station_selector = By.XPATH, ".//input[@placeholder='* Станция метро']"
    metro_station_pp = By.XPATH, '//div[text()="Преображенская площадь"]'
    metro_station_sb = By.XPATH, '//div[text()="Славянский бульвар"]'
    phone_input = By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']"
    next_button = By.XPATH, '//button[text()="Далее"]'


    #Поля, селекторы и кнопки формы: Про аренду
    about_rent_title = By.XPATH, './/*[@class="Order_Header__BZXOb"]'
    order_date_input = By.CSS_SELECTOR, '[placeholder="* Когда привезти самокат"]'
    rent_period_selector = By.CLASS_NAME, 'Dropdown-placeholder'
    one_day_period_selector_option = By.XPATH, '//div[text() = "сутки"]'
    seven_days_period_selector_option = By.XPATH, '//div[text() = "семеро суток"]'
    color_checkbox_black = By.ID, 'black'
    color_checkbox_gray = By.ID, 'grey'
    comment_input = By.CSS_SELECTOR, '[placeholder="Комментарий для курьера"]'
    order_button = By.XPATH, '//div[@class = "Order_Buttons__1xGrp"]/button[text()="Заказать"]'

    #Элементы и кнопки попапа заказа:
    order_popup = By.CLASS_NAME, 'Order_ModalHeader__3FDaJ'
    yes_button = By.XPATH, '//*[contains(text(), "Да")]'
    order_status_button = By.XPATH, '//*[contains(text(), "Посмотреть статус")]'
    success_popup = By.XPATH, './/*[contains(text(), "Заказ оформлен")]'