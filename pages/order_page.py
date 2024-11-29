import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver import Keys

class OrderPage(BasePage):

    @allure.step("Заполнение поля: Имя")
    def set_first_name(self, first_name):
        self.send_keys_to_element(OrderPageLocators.first_name_input, first_name)

    @allure.step("Заполнение поля: Фамилия")
    def set_last_name(self, last_name):
        self.send_keys_to_element(OrderPageLocators.last_name_input, last_name)

    @allure.step("Заполнение поля: Адрес")
    def set_address(self, address):
        self.send_keys_to_element(OrderPageLocators.address_input, address)

    @allure.step("Заполнение через дропдаун поля: Станция метро")
    def select_metro(self, station):
        self.click_element(OrderPageLocators.metro_station_selector)
        self.scroll(station)
        self.find_element(station)
        self.click_element(station)

    @allure.step("Заполнение поля: Телефон")
    def set_phone(self, phone):
        self.send_keys_to_element(OrderPageLocators.phone_input, phone)

    @allure.step("Нажатие кнопки 'Далее'")
    def click_next_button(self):
        self.click_element(OrderPageLocators.next_button)

    @allure.step("Ожидание появления формы 'Про аренду'")
    def wait_for_rent_form(self):
        self.find_element(OrderPageLocators.about_rent_title)

    @allure.step("Заполнение поля: Дата")
    def set_date(self, date):
        self.send_keys_to_element(OrderPageLocators.order_date_input, date)
        self.send_keys_to_element(OrderPageLocators.order_date_input, Keys.ENTER)

    @allure.step("Заполнение поля: Срок аренды")
    def set_rent_period(self, rent_period):
        self.click_element(OrderPageLocators.rent_period_selector)
        self.click_element(rent_period)

    @allure.step("Заполнение поля: Цвет самоката")
    def set_color(self, color):
        self.click_element(color)

    @allure.step("Заполнение поля: Комментарий для курьера")
    def set_comment(self, comment):
        self.send_keys_to_element(OrderPageLocators.comment_input, comment)

    @allure.step("Нажатие кнопки 'Заказать'")
    def click_order_button(self):
        self.click_element(OrderPageLocators.order_button)

    @allure.step("Ожидание отображения попапа подтверждения заказа")
    def wait_for_order_popup(self):
        self.find_element(OrderPageLocators.order_popup)

    @allure.step("Нажатие на кнопку 'Да'")
    def click_yes_button(self):
        self.click_element(OrderPageLocators.yes_button)

    @allure.step("Проверка отображения попапа 'Заказ оформлен'")
    def check_success_popup(self):
        success_popup = self.find_element(OrderPageLocators.success_popup)
        assert success_popup, 'Не отображается попап "Заказ оформлен"'

    @allure.step("Нажатие на логотип самоката")
    def click_samokat_logo(self):
        self.click_element(OrderPageLocators.samokat_logo)

    @allure.step("Полное заполнение формы 'Для кого самокат'")
    def fill_user_form(self, first_name, last_name, address, phone, station):
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_address(address)
        self.select_metro(station)
        self.set_phone(phone)

    @allure.step("Полное заполнение формы 'Про аренду'")
    def fill_rent_form(self, date, comment, rent_period, color):
        self.wait_for_rent_form()
        self.set_date(date)
        self.set_rent_period(rent_period)
        self.set_color(color)
        self.set_comment(comment)