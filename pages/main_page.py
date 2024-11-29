import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from TestData import URLs

class MainPage(BasePage):

    @allure.step("Нажатие кнопки 'Заказать'")
    def order_button_click(self, button):
        self.scroll(button)
        self.find_element(button)
        self.click_element(button)

    @allure.step("Проверка открытия главной страницы 'Самокат'")
    def check_samokat_page_load(self):
        current_url = self.get_current_url()
        assert current_url == URLs.main_page_url

    @allure.step("Нажатие логотипа Яндекса")
    def yandex_logo_click(self):
        self.click_element(MainPageLocators.yandex_logo)

    @allure.step("Переход на страницу Новостей Дзен")
    def dzen_goto(self):
        self.switch_to_window()

    @allure.step("Проверка перехода на страницу Новостей Дзен")
    def check_yandex_page_load(self):
        self.find_element(MainPageLocators.dzen_news_header)
        current_url = self.get_current_url()
        assert current_url == URLs.dzen_news_url

    @staticmethod
    def format_selector(tple, num):
        selector_type, selector_string = tple
        formatted_selector = selector_string.format(num)
        return selector_type, formatted_selector

    @allure.step("Получение текста ответа")
    def get_answer_text(self, num):
        formatted_q = self.format_selector(MainPageLocators.locator_question, num)
        formatted_a = self.format_selector(MainPageLocators.locator_answer, num)
        self.scroll(formatted_q)
        self.click_element(formatted_q)
        answer = self.find_element(formatted_a).text
        return answer